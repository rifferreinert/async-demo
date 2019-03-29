import asyncio
import time
from timeit import timeit


async def say_hello():
    print('hello')

asyncio.run(say_hello())


async def sleep_print_num(sleep, i):
    time.sleep(sleep)
    print(i)


async def run_two():
    await asyncio.gather(sleep_print_num(0.55, 1), sleep_print_num(0.5, 2))


async def sleep_print_num_async(sleep, i):
    await asyncio.sleep(sleep)
    print(i)


async def run_two_async():
    await asyncio.gather(sleep_print_num_async(0.55, 1), sleep_print_num_async(0.5, 2))


print(timeit(lambda: asyncio.run(run_two_async()), number=1))
