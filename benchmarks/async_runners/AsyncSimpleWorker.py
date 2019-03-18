import asyncio


class CoroutinePool:

    def __init__(self, pool_size, cor: asyncio.coroutine, args):
        self.queue = asyncio.Queue()
        self.pool_size = pool_size
        self.cor = cor
        self.workers = []
        self.args = args

    async def run(self):
        self.__fill_queue()
        self.__run_workers()
        await self.__run_to_completion()

    async def __worker(self):
        while True:
            arg = await self.queue.get()
            await self.cor(*arg)
            self.queue.task_done()

    def __fill_queue(self):
        for arg in self.args:
            self.queue.put_nowait(arg)

    def __run_workers(self):
        for _ in range(self.pool_size):
            self.workers.append(asyncio.create_task(self.__worker()))

    async def __run_to_completion(self):
        await self.queue.join()
