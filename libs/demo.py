import ctypes
from pathlib import Path


LIB_PATH = Path(__file__).parent / 'libdemo.so'
libdemo = ctypes.PyDLL(str(LIB_PATH))


if __name__ == '__main__':
    print('In Python, will call force_sleep from the C lib')
    libdemo.force_sleep(1)
    print('Done calling the C lib')
