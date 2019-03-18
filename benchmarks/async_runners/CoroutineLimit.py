import asyncio


class CoroutineLimit:

    def __init__(self, limit, cor: asyncio.coroutine, args):
        self.queue = asyncio.Queue()
        self.sem = asyncio.Semaphore(limit)
        self.cor = cor
        self.tasks = []
        self.args = args

    async def run(self):
        self.fill_queue_task = asyncio.create_task(
            self.__fill_queue())
        task_loop = asyncio.create_task(self.run_task_loop())
        await self.__run_to_completion()
        task_loop.cancel()

    async def run_task_loop(self):
        def wrap(f):
            async def wrapped(*args):
                try:
                    await f(*args)
                finally:
                    self.sem.release()
                    self.queue.task_done()
            return wrapped

        while True:
            arg = await self.queue.get()
            await self.sem.acquire()
            asyncio.create_task(wrap(self.cor)(*arg))

    async def __fill_queue(self):
        self.fill_queue_tasks = []
        for arg in self.args:
            await self.queue.put(arg)

    async def __run_to_completion(self):
        await self.fill_queue_task
        await self.queue.join()
