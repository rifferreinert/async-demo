import asyncio
import time


async def sleep_print_num(sleep, i):
    await asyncio.sleep(sleep)
    print(i)


async def print_loop():
    tasks = []
    for i in range(10):
        print('loop')
        # await asyncio.sleep(0.5)
        time.sleep(0.5)
        tasks.append(asyncio.create_task(sleep_print_num(1, i)))

    await asyncio.gather(*tasks)

asyncio.run(print_loop())
