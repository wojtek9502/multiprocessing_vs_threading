import concurrent.futures
import os
from utils import timer

nums = [8, 7, 8, 5, 8, 8, 5, 4, 8, 7, 7, 8, 8, 7, 8, 8, 8]
N_THREADS = 3


def calc(n):
    print("process id: {0}".format(os.getpid()))
    counter = 0
    for _ in range(n * 1_000_000):
        counter += 1
    return counter


@timer
def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(calc, nums)

    for res in results:
        print(res)


if __name__ == '__main__':
    main()
