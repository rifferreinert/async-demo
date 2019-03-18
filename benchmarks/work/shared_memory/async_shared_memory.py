import asyncio

from CoroutinePool import CoroutinePool

i = 0


async def mutate():
    global i
    tmp = i
    i = tmp + 1


async def main():
    cp = CoroutinePool(3000, mutate, [[] for _ in range(1000000)])
    await cp.run()

asyncio.run(main())
print(i)
