from concurrent.futures import ThreadPoolExecutor, wait


THREADS = 4
AMOUNT = 1_000_000
count = 0


def increase() -> None:
    global count

    for _ in range(AMOUNT):
        count += 1


def main() -> None:
    global count

    count = 0
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        wait([executor.submit(increase) for _ in range(THREADS)])
    print('Result after increases:', count)


if __name__ == '__main__':
    print('Starting to check counts')
    main()
