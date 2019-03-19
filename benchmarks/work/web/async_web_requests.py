from functools import partial

import requests
import asyncio

from async_runners.AsyncPool import AsyncPool

URL_LIST = ['https://facebook.com',
            'https://github.com',
            'https://google.com',
            'https://microsoft.com',
            'https://yahoo.com',
            'https://bing.com',
            'https://apple.com',
            'https://tesla.com']


async def get_website(session, url):
    return session.get(url)


async def run(work_size, job_count, worker_count):
    pool = AsyncPool(worker_count)
    pool.start()
    work = [URL_LIST[i % 8] for i in range(job_count)]
    session = requests.session()
    result = await pool.map(partial(get_website, session), work)
    pool.stop()
    await pool.join()


def do_job(compute_size, job_count, worker_count):
    asyncio.run(run(compute_size, job_count, worker_count))
