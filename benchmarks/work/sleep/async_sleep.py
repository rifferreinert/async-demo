import timeit
import asyncio

from CoroutinePool import CoroutinePool


async def task(seconds):
    await asyncio.sleep(seconds)
