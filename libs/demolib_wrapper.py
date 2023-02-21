import ctypes
from pathlib import Path


LIB_PATH = Path(__file__).parent / 'demolib.so'
demolib_c = ctypes.PyDLL(str(LIB_PATH))


def force_sleep(amount: int) -> None:
    """
    Similar to time.sleep(), but it sleeps in C and doesn't allow the CPython
    interpreter to switch context.

    :param amount: The number of seconds to sleep for.
    """
    demolib_c.force_sleep(amount)


if __name__ == '__main__':
    print('In Python, will call force_sleep from the C lib')
    force_sleep(3)
    print('Done calling the C lib')
