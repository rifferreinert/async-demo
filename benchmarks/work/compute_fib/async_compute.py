import asyncio

from async_runners.AsyncPool import AsyncPool


async def fib(n):
    if n < 2:
        return 1
    a, b = await asyncio.gather(fib(n-2), fib(n-1))
    return a + b


async def run(compute_size, job_count, thread_count):
    pool = AsyncPool(thread_count)
    pool.start()
    work = [compute_size for _ in range(job_count)]
    result = await pool.map(fib, work)
    pool.stop()
    await pool.join()


def do_job(compute_size, job_count, thread_count):
    asyncio.run(run(compute_size, job_count, thread_count))
