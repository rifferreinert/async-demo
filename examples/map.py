import requests
from timeit import timeit
from time import sleep
from functools import partial
from concurrent.futures import ThreadPoolExecutor


def sleep_print_num(wait_time, i):
    sleep(wait_time)
    print(i)


def run_two():
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(sleep_print_num(0.55, 1))
        executor.submit(sleep_print_num(0.50, 2))


# print(timeit(run_two, number=1))


URL_LIST = [
    "https://facebook.com",
    "https://github.com",
    "https://google.com",
    "https://microsoft.com",
    "https://yahoo.com",
    "https://bing.com",
    "https://apple.com",
    "https://tesla.com",
]


def download(threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        sites = executor.map(requests.get, URL_LIST)


print(timeit(lambda: list(map(requests.get, URL_LIST)), number=1))
print(timeit(lambda: download(1), number=1))
print(timeit(lambda: download(4), number=1))
