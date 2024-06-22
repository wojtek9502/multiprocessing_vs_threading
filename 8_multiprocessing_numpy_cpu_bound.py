import multiprocessing
import os

import numpy as np

ARRAY_ELEMS = 100_00


def calc(numpy_arr):
    print("Worker process id for {0}: {1}".format(numpy_arr, os.getpid()))
    for i in range(ARRAY_ELEMS):
        a = np.dot(numpy_arr, numpy_arr)
        return a


if __name__ == '__main__':
    numpy_arrays = [
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS),
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS),
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS),
        np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS)
    ]
    pool = multiprocessing.Pool()
    pool.map(calc, numpy_arrays)
