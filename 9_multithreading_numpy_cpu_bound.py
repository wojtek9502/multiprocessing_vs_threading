import os
import threading

import numpy as np

from utils import timer

ARRAY_ELEMS = 10_000
N_THREADS = 3


def calc(numpy_arr):
    print("process id: {0}".format(os.getpid()))
    for i in range(ARRAY_ELEMS):
        a = np.dot(numpy_arr, numpy_arr)
        return a


@timer
def main():
    threads = []
    origin_array = np.random.rand(ARRAY_ELEMS, ARRAY_ELEMS)
    for i in range(N_THREADS):
        array_copy = np.copy(origin_array)
        thread = threading.Thread(target=calc, args=(array_copy,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
