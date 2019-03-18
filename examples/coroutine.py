import asyncio
import random
from timeit import timeit


async def say_hello():
    print('hello')

asyncio.run(say_hello())


async def print_num(i):
    print(i)


async def sleep_print_num(sleep, i):
    await asyncio.sleep(sleep)
    print(i)


async def run_two():
    await asyncio.gather(sleep_print_num(0.501, 1), sleep_print_num(0.5, 2))
