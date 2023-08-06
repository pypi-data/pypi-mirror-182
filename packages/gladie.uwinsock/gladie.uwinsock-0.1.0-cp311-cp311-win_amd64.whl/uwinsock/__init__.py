import _winsock
from .fakesocket import socket, AF_UNIX, SOCK_STREAM

def create_socket():
    fd = _winsock.create_socket()
    sock = socket(AF_UNIX, SOCK_STREAM, 0, fileno=fd)
    return sock