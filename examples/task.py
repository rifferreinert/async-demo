import asyncio
from timeit import timeit

async def sleep_print_num(sleep, i):
    await asyncio.sleep(sleep)
    print(i)


async def print_loop():
    tasks = []
    task1 = asyncio.create_task(sleep_print_num(0.55, 1))
    task2 = asyncio.create_task(sleep_print_num(0.5, 2))

    await task1
    await task2

print(timeit(lambda: asyncio.run(print_loop()), number=1))
