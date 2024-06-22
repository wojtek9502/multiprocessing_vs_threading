# Python program to understand
# the concept of pool
import multiprocessing
import os

import requests as requests


def scrape(url):
    print("Worker process id for {0}: {1}".format(url, os.getpid()))
    r = requests.get(url)
    return r.content[:10]


if __name__ == "__main__":
    # input list
    urls = [
        'https://www.geeksforgeeks.org/data-structures/',
        'https://www.geeksforgeeks.org/',
        'https://www.geeksforgeeks.org/array-data-structure-guide/?ref=shm',
        'https://www.geeksforgeeks.org/difference-array-range-update-query-o1/?ref=lbp',
        'https://www.geeksforgeeks.org/queries-for-the-product-of-first-n-factorials/?ref=lbp',
    ]

    # creating a pool object
    p = multiprocessing.Pool(processes=3)

    # map list to target function
    result = p.map(scrape, urls)

    print(result)