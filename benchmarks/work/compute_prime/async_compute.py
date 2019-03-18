import asyncio
import sys
import os
import logging
import warnings
logging.basicConfig(level=logging.DEBUG)
warnings.resetwarnings()


class AsyncPool:

    def __init__(self,
                 concurrency: int):

        self.concurrency = concurrency
        self.__in_queue = asyncio.Queue()
        self.__results = {}
        self.next_id = 0
        self.__loop = None
        self.__running = False

    async def __run_loop(self):
        pending = {}

        while self.__running or pending:
            while self.__running and len(pending) < self.concurrency:
                try:
                    task_data = self.__in_queue.get_nowait()
                except:
                    break

                tid, func, args, kwargs = task_data
                task = asyncio.create_task(func(*args, **kwargs))
                pending[task] = tid

            if not pending:
                await asyncio.sleep(0.005)
                continue
            done, _ = await asyncio.wait(pending.keys(),
                                         timeout=0.05,
                                         return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                tid = pending.pop(task)

                try:
                    result = task.result()
                except e as Exception:
                    result = e
                self.__results[tid] = result

    def queue_work(self, func, args, kwargs):
        """Add a job to the queue"""
        tid = self.next_id
        self.next_id += 1
        self.__in_queue.put_nowait((tid, func, args, kwargs))
        return tid

    async def results(self, tids):
        """get results of specific tids"""
        results = {}
        waiting = set(tids.copy())
        while len(waiting) > 0:
            ready = waiting & self.__results.keys()
            for tid in ready:
                waiting.remove(tid)
                results[tid] = self.__results[tid]
            await asyncio.sleep(0.005)

        return [results[tid] for tid in tids]

    async def map(self, func, iterable):
        tids = []
        for elem in iterable:
            tids.append(self.queue_work(func, [elem], {}))

        return await self.results(tids)

    async def apply(self, func, args=[], kwargs={}):
        tid = self.queue_work(func, args, kwargs)
        results = await self.results([tid])
        return results[0]

    async def join(self):
        if self.__running:
            raise Exception('Pool is still running')
        await self.__loop

    def stop(self):
        self.__running = False

    def start(self):
        self.__running = True
        self.__loop = asyncio.create_task(self.__run_loop())


async def prime_count(n):
    prime_count = 0
    for i in range(2, n + 1):
        prime = True
        for d in range(2, i):
            if i % d == 0:
                prime = False
                break
        if prime:
            prime_count += 1

    return prime_count


async def run(compute_size, job_count, thread_count):
    pool = AsyncPool(thread_count)

    pool.start()
    work = [compute_size for _ in range(job_count)]
    result = await pool.map(prime_count, work)
    pool.stop()


def do_job(compute_size, job_count, thread_count):
    asyncio.run(run(compute_size, job_count, thread_count))


# do_job(10000, 10, 3000)
