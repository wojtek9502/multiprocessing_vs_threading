import multiprocessing
import os

from utils import timer

nums = [8, 7, 8, 5, 8, 8, 5, 4, 8, 7, 7, 8, 8, 7, 8, 8, 8]


def calc(n):
    print("process id: {0}".format(os.getpid()))
    counter = 0
    for _ in range(n * 1_000_000):
        counter += 1
    return counter

@timer
def main():
    pool = multiprocessing.Pool()
    pool.map(calc, nums)


if __name__ == '__main__':
    main()
