import io
import os
import selectors
import socket
import _winsock
from enum import IntEnum

_socket = _winsock._socket
AF_UNIX = _socket.AF_UNIX
SOCK_STREAM = _socket.SOCK_STREAM
try:
    import errno
except ImportError:
    errno = None
EAGAIN = getattr(errno, 'EAGAIN', 11)
EWOULDBLOCK = getattr(errno, 'EWOULDBLOCK', 11)
_blocking_errnos = { EAGAIN, EWOULDBLOCK }

IntEnum._convert_(
        'AddressFamily',
        __name__,
        lambda C: C.isupper() and C.startswith('AF_'))

IntEnum._convert_(
        'SocketKind',
        __name__,
        lambda C: C.isupper() and C.startswith('SOCK_'))

class _GiveupOnSendfile(Exception): pass

class SocketIO(io.RawIOBase):

    """Raw I/O implementation for stream sockets.

    This class supports the makefile() method on sockets.  It provides
    the raw I/O interface on top of a socket object.
    """

    # One might wonder why not let FileIO do the job instead.  There are two
    # main reasons why FileIO is not adapted:
    # - it wouldn't work under Windows (where you can't used read() and
    #   write() on a socket handle)
    # - it wouldn't work with socket timeouts (FileIO would ignore the
    #   timeout and consider the socket non-blocking)

    # XXX More docs

    def __init__(self, sock, mode):
        if mode not in ("r", "w", "rw", "rb", "wb", "rwb"):
            raise ValueError("invalid mode: %r" % mode)
        io.RawIOBase.__init__(self)
        self._sock = sock
        if "b" not in mode:
            mode += "b"
        self._mode = mode
        self._reading = "r" in mode
        self._writing = "w" in mode
        self._timeout_occurred = False

    def readinto(self, b):
        """Read up to len(b) bytes into the writable buffer *b* and return
        the number of bytes read.  If the socket is non-blocking and no bytes
        are available, None is returned.

        If *b* is non-empty, a 0 return value indicates that the connection
        was shutdown at the other end.
        """
        self._checkClosed()
        self._checkReadable()
        if self._timeout_occurred:
            raise OSError("cannot read from timed out object")
        while True:
            try:
                return self._sock.recv_into(b)
            except _socket.timeout:
                self._timeout_occurred = True
                raise
            except _socket.error as e:
                if e.errno in _blocking_errnos:
                    return None
                raise

    def write(self, b):
        """Write the given bytes or bytearray object *b* to the socket
        and return the number of bytes written.  This can be less than
        len(b) if not all data could be written.  If the socket is
        non-blocking and no bytes could be written None is returned.
        """
        self._checkClosed()
        self._checkWritable()
        try:
            return self._sock.send(b)
        except _socket.error as e:
            # XXX what about EINTR?
            if e.errno in _blocking_errnos:
                return None
            raise

    def readable(self):
        """True if the SocketIO is open for reading.
        """
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return self._reading

    def writable(self):
        """True if the SocketIO is open for writing.
        """
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return self._writing

    def seekable(self):
        """True if the SocketIO is open for seeking.
        """
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return super().seekable()

    def fileno(self):
        """Return the file descriptor of the underlying socket.
        """
        self._checkClosed()
        return self._sock.fileno()

    @property
    def name(self):
        if not self.closed:
            return self.fileno()
        else:
            return -1

    @property
    def mode(self):
        return self._mode

    def close(self):
        """Close the SocketIO object.  This doesn't close the underlying
        socket, except if all references to it have disappeared.
        """
        if self.closed:
            return
        io.RawIOBase.close(self)
        self._sock._decref_socketios()
        self._sock = None

def _intenum_converter(value, enum_klass):
    """Convert a numeric family value to an IntEnum member.

    If it's not a known member, return the numeric value itself.
    """
    try:
        return enum_klass(value)
    except ValueError:
        return value

class socket(_winsock._socket.socket):

    """A subclass of _socket.socket adding the makefile() method."""

    __slots__ = ["__weakref__", "_io_refs", "_closed"]

    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        # For user code address family and type values are IntEnum members, but
        # for the underlying _socket.socket they're just integers. The
        # constructor of _socket.socket converts the given argument to an
        # integer automatically.
        if fileno is None:
            if family == -1:
                family = _socket.AF_INET
            if type == -1:
                type = _socket.SOCK_STREAM
            if proto == -1:
                proto = 0
        _socket.socket.__init__(self, family, type, proto, fileno)
        self._io_refs = 0
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if not self._closed:
            self.close()

    def __repr__(self):
        """Wrap __repr__() to reveal the real class name and socket
        address(es).
        """
        closed = getattr(self, '_closed', False)
        s = "<%s.%s%s fd=%i, family=%s, type=%s, proto=%i" \
            % (self.__class__.__module__,
               self.__class__.__qualname__,
               " [closed]" if closed else "",
               self.fileno(),
               self.family,
               self.type,
               self.proto)
        if not closed:
            try:
                laddr = self.getsockname()
                if laddr:
                    s += ", laddr=%s" % str(laddr)
            except _socket.error:
                pass
            try:
                raddr = self.getpeername()
                if raddr:
                    s += ", raddr=%s" % str(raddr)
            except _socket.error:
                pass
        s += '>'
        return s

    def __getstate__(self):
        raise TypeError(f"cannot pickle {self.__class__.__name__!r} object")

    def dup(self):
        """dup() -> socket object

        Duplicate the socket. Return a new socket object connected to the same
        system resource. The new socket is non-inheritable.
        """
        fd = _socket.dup(self.fileno())
        sock = self.__class__(self.family, self.type, self.proto, fileno=fd)
        sock.settimeout(self.gettimeout())
        return sock

    def accept(self):
        """accept() -> (socket object, address info)

        Wait for an incoming connection.  Return a new socket
        representing the connection, and the address of the client.
        For IP sockets, the address info is a pair (hostaddr, port).
        """
        fd, addr = self._accept()
        sock = socket(self.family, self.type, self.proto, fileno=fd)
        # Issue #7995: if no default timeout is set and the listening
        # socket had a (non-zero) timeout, force the new socket in blocking
        # mode to override platform-specific socket flags inheritance.
        if _socket.getdefaulttimeout() is None and self.gettimeout():
            sock.setblocking(True)
        return sock, addr

    def makefile(self, mode="r", buffering=None, *,
                 encoding=None, errors=None, newline=None):
        """makefile(...) -> an I/O stream connected to the socket

        The arguments are as for io.open() after the filename, except the only
        supported mode values are 'r' (default), 'w' and 'b'.
        """
        # XXX refactor to share code?
        if not set(mode) <= {"r", "w", "b"}:
            raise ValueError("invalid mode %r (only r, w, b allowed)" % (mode,))
        writing = "w" in mode
        reading = "r" in mode or not writing
        assert reading or writing
        binary = "b" in mode
        rawmode = ""
        if reading:
            rawmode += "r"
        if writing:
            rawmode += "w"
        raw = SocketIO(self, rawmode)
        self._io_refs += 1
        if buffering is None:
            buffering = -1
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering == 0:
            if not binary:
                raise ValueError("unbuffered streams must be binary")
            return raw
        if reading and writing:
            buffer = io.BufferedRWPair(raw, raw, buffering)
        elif reading:
            buffer = io.BufferedReader(raw, buffering)
        else:
            assert writing
            buffer = io.BufferedWriter(raw, buffering)
        if binary:
            return buffer
        encoding = io.text_encoding(encoding)
        text = io.TextIOWrapper(buffer, encoding, errors, newline)
        text.mode = mode
        return text

    if hasattr(os, 'sendfile'):

        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            self._check_sendfile_params(file, offset, count)
            sockno = self.fileno()
            try:
                fileno = file.fileno()
            except (AttributeError, io.UnsupportedOperation) as err:
                raise _GiveupOnSendfile(err)  # not a regular file
            try:
                fsize = os.fstat(fileno).st_size
            except OSError as err:
                raise _GiveupOnSendfile(err)  # not a regular file
            if not fsize:
                return 0  # empty file
            # Truncate to 1GiB to avoid OverflowError, see bpo-38319.
            blocksize = min(count or fsize, 2 ** 30)
            timeout = self.gettimeout()
            if timeout == 0:
                raise ValueError("non-blocking sockets are not supported")
            # poll/select have the advantage of not requiring any
            # extra file descriptor, contrarily to epoll/kqueue
            # (also, they require a single syscall).
            if hasattr(selectors, 'PollSelector'):
                selector = selectors.PollSelector()
            else:
                selector = selectors.SelectSelector()
            selector.register(sockno, selectors.EVENT_WRITE)

            total_sent = 0
            # localize variable access to minimize overhead
            selector_select = selector.select
            os_sendfile = os.sendfile
            try:
                while True:
                    if timeout and not selector_select(timeout):
                        raise TimeoutError('timed out')
                    if count:
                        blocksize = count - total_sent
                        if blocksize <= 0:
                            break
                    try:
                        sent = os_sendfile(sockno, fileno, offset, blocksize)
                    except BlockingIOError:
                        if not timeout:
                            # Block until the socket is ready to send some
                            # data; avoids hogging CPU resources.
                            selector_select()
                        continue
                    except OSError as err:
                        if total_sent == 0:
                            # We can get here for different reasons, the main
                            # one being 'file' is not a regular mmap(2)-like
                            # file, in which case we'll fall back on using
                            # plain send().
                            raise _GiveupOnSendfile(err)
                        raise err from None
                    else:
                        if sent == 0:
                            break  # EOF
                        offset += sent
                        total_sent += sent
                return total_sent
            finally:
                if total_sent > 0 and hasattr(file, 'seek'):
                    file.seek(offset)
    else:
        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            raise _GiveupOnSendfile(
                "os.sendfile() not available on this platform")

    def _sendfile_use_send(self, file, offset=0, count=None):
        self._check_sendfile_params(file, offset, count)
        if self.gettimeout() == 0:
            raise ValueError("non-blocking sockets are not supported")
        if offset:
            file.seek(offset)
        blocksize = min(count, 8192) if count else 8192
        total_sent = 0
        # localize variable access to minimize overhead
        file_read = file.read
        sock_send = self.send
        try:
            while True:
                if count:
                    blocksize = min(count - total_sent, blocksize)
                    if blocksize <= 0:
                        break
                data = memoryview(file_read(blocksize))
                if not data:
                    break  # EOF
                while True:
                    try:
                        sent = sock_send(data)
                    except BlockingIOError:
                        continue
                    else:
                        total_sent += sent
                        if sent < len(data):
                            data = data[sent:]
                        else:
                            break
            return total_sent
        finally:
            if total_sent > 0 and hasattr(file, 'seek'):
                file.seek(offset + total_sent)

    def _check_sendfile_params(self, file, offset, count):
        if 'b' not in getattr(file, 'mode', 'b'):
            raise ValueError("file should be opened in binary mode")
        if not self.type & _socket.SOCK_STREAM:
            raise ValueError("only SOCK_STREAM type sockets are supported")
        if count is not None:
            if not isinstance(count, int):
                raise TypeError(
                    "count must be a positive integer (got {!r})".format(count))
            if count <= 0:
                raise ValueError(
                    "count must be a positive integer (got {!r})".format(count))

    def sendfile(self, file, offset=0, count=None):
        """sendfile(file[, offset[, count]]) -> sent

        Send a file until EOF is reached by using high-performance
        os.sendfile() and return the total number of bytes which
        were sent.
        *file* must be a regular file object opened in binary mode.
        If os.sendfile() is not available (e.g. Windows) or file is
        not a regular file socket.send() will be used instead.
        *offset* tells from where to start reading the file.
        If specified, *count* is the total number of bytes to transmit
        as opposed to sending the file until EOF is reached.
        File position is updated on return or also in case of error in
        which case file.tell() can be used to figure out the number of
        bytes which were sent.
        The socket must be of SOCK_STREAM type.
        Non-blocking sockets are not supported.
        """
        try:
            return self._sendfile_use_sendfile(file, offset, count)
        except _GiveupOnSendfile:
            return self._sendfile_use_send(file, offset, count)

    def _decref_socketios(self):
        if self._io_refs > 0:
            self._io_refs -= 1
        if self._closed:
            self.close()

    def _real_close(self, _ss=_socket.socket):
        # This function should not reference any globals. See issue #808164.
        _ss.close(self)

    def close(self):
        # This function should not reference any globals. See issue #808164.
        self._closed = True
        if self._io_refs <= 0:
            self._real_close()

    def detach(self):
        """detach() -> file descriptor

        Close the socket object without closing the underlying file descriptor.
        The object cannot be used after this call, but the file descriptor
        can be reused for other purposes.  The file descriptor is returned.
        """
        self._closed = True
        return super().detach()

    @property
    def family(self):
        """Read-only access to the address family for this socket.
        """
        return _intenum_converter(super().family, AddressFamily)

    @property
    def type(self):
        """Read-only access to the socket type.
        """
        return _intenum_converter(super().type, SocketKind)

    if os.name == 'nt':
        def get_inheritable(self):
            return os.get_handle_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_handle_inheritable(self.fileno(), inheritable)
    else:
        def get_inheritable(self):
            return os.get_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_inheritable(self.fileno(), inheritable)
    get_inheritable.__doc__ = "Get the inheritable flag of the socket"
    set_inheritable.__doc__ = "Set the inheritable flag of the socket"