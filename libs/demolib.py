import ctypes
from pathlib import Path


LIB_PATH = Path(__file__).parent / 'demolib.so'
demolib_c = ctypes.CDLL(str(LIB_PATH))


def force_sleep(amount: int) -> None:
    demolib_c.force_sleep(amount)


if __name__ == '__main__':
    print('In Python, will call force_sleep from the C lib')
    force_sleep(3)
    print('Done calling the C lib')
