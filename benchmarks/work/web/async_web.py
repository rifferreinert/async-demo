from functools import partial

import aiohttp
import asyncio
import os


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
    async with session.get(url) as resp:
        await resp.read()
    return True


async def run(work_size, job_count, worker_count):
    pool = AsyncPool(worker_count)
    pool.start()

    async with aiohttp.ClientSession() as session:
        work = [URL_LIST[i % 8] for i in range(job_count)]
        work = [os.getenv('slowurl') for i in range(job_count)]
        result = await pool.map(partial(get_website, session), work)
    await asyncio.sleep(0.005)
    pool.stop()
    await pool.join()


def do_job(compute_size, job_count, worker_count):
    asyncio.run(run(compute_size, job_count, worker_count))
