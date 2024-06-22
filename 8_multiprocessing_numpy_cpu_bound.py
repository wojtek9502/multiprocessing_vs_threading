import multiprocessing
import os

import numpy as np

from utils import timer

ARRAY_ELEMS = 10_000


def calc(numpy_arr):
    print("process id: {0} ".format(os.getpid()))
    for i in range(ARRAY_ELEMS):
        a = np.dot(numpy_arr, numpy_arr)
        return a

@timer
def main():
    numpy_arrays = [
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS),
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS),
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS)
    ]
    pool = multiprocessing.Pool()
    pool.map(calc, numpy_arrays)


if __name__ == '__main__':
    main()
