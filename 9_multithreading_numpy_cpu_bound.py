import multiprocessing
import os
import threading

import numpy as np

ARRAY_ELEMS = 100_00
N_THREADS = 6


def calc(numpy_arr):
    print("Worker process id for {0}: {1}".format(numpy_arr, os.getpid()))
    for i in range(ARRAY_ELEMS):
        a = np.dot(numpy_arr, numpy_arr)
        return a


if __name__ == '__main__':
    arrays = []
    threads = []
    origin_array = np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS)
    for i in range(N_THREADS):
        array_copy = np.copy(origin_array)
        thread = threading.Thread(target=calc, args=(array_copy,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
