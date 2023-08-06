from setuptools import setup, Extension, find_packages

def main():
    setup(name="gladie.uwinsock",
          version="0.1.0",
          description="Implementation of Winsock AF_UNIX socket type for Python.",
          author="Noah Tanner",
          author_email="50159154+kevinshome@users.noreply.github.com",
          packages=find_packages(include=["uwinsock"]),
          ext_modules=[Extension("_winsock", ["uwinsock/_winsock/_winsock.c"])])

if __name__ == "__main__":
    main()
