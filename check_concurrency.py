import time
from concurrent.futures import ThreadPoolExecutor, wait
from contextlib import contextmanager

from libs.demolib_wrapper import force_sleep


SLEEP_SECS = 3
THREADS = 4


@contextmanager
def timing(what: str):
    start = time.time()
    yield
    elapsed = time.time() - start

    print(elapsed, 'seconds for', what)


def main() -> None:
    with timing(f'sleeping in Python in {THREADS} threads'):
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = [
                executor.submit(time.sleep, SLEEP_SECS)
                for _ in range(THREADS)
            ]
            wait(futures)

    with timing(f'sleeping in C in {THREADS} threads'):
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = [
                executor.submit(force_sleep, SLEEP_SECS)
                for _ in range(THREADS)
            ]
            wait(futures)


if __name__ == '__main__':
    print('Starting to check concurrency')
    main()
