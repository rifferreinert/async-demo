from concurrent.futures import ProcessPoolExecutor

import requests
import os

URL_LIST = ['https://facebook.com',
            'https://github.com',
            'https://google.com',
            'https://microsoft.com',
            'https://yahoo.com',
            'https://bing.com',
            'https://apple.com',
            'https://tesla.com']


def get_website(url):
    requests.get(url)


def do_job(work_size, job_count, process_count):
    work = [URL_LIST[i % 8] for i in range(job_count)]
    work = ['http://localhost:8080' for i in range(job_count)]
    work = [os.getenv('slowurl') for i in range(job_count)]

    with ProcessPoolExecutor(max_workers=process_count) as executor:
        results = executor.map(get_website, work)
