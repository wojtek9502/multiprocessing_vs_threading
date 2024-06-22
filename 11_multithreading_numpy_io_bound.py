import concurrent.futures
import os

import requests

ARRAY_ELEMS = 100_00
N_THREADS = 6


def calc(url):
    print("Worker process id for {0}: {1}".format(url, os.getpid()))
    response = requests.get(url)
    return response.content[:10]


if __name__ == '__main__':
    urls = [
        'https://realpython.com/',
        'https://realpython.com/learning-paths/',
        'https://realpython.com/search?kind=article&kind=course&order=newest',
        'https://realpython.com/quizzes/',
        'https://realpython.com/tutorials/all/',
        'https://realpython.com/community/',
        'https://realpython.com/office-hours/',
        'https://realpython.com/podcasts/rpp/',
        'https://realpython.com/products/books/',
        'https://realpython.com/courses/rounding-numbers-python/',
        'https://realpython.com/ruff-python/',
        'https://realpython.com/python-mappings/',
        'https://realpython.com/courses/listing-all-files-directory/',
        'https://realpython.com/python-news-may-2024/',
        'https://realpython.com/python-string-formatting/'

    ]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(calc, urls)

    for res in results:
        print(res)
