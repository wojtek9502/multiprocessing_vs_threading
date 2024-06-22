import multiprocessing
import os

import requests

from utils import timer


def scrape(url):
    print("process id for {0}: {1}".format(url, os.getpid()))
    response = requests.get(url)
    return response.content[:10]


@timer
def main():
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
    pool = multiprocessing.Pool(6)
    result = pool.map(scrape, urls)
    print(result)


if __name__ == '__main__':
    main()
