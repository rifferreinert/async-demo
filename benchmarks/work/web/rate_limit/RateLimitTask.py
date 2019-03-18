import asyncio
import functools

from rate_limit.AsyncRateLimit import AsyncRateLimit


async def task(rl):
    await rl.limit()


def get_task(tokens, time_period):
    rl = AsyncRateLimit(tokens, time_period)
    return functools.partial(task, rl)
