# from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Value, Process, Lock

import asyncio


class SharedMemory:
    def __init__(self):
        self.shared_count = 0
        self.shared_count_process = Value("i", 0, lock=False)
        self.lock = Lock()

    def increment_thread(self):
        with self.lock:
            self.shared_count += 1

    def increment_process(self):
        for i in range(1000):
            with self.lock:
                self.shared_count_process.value += 1

    async def increment_coroutine(self):
        self.shared_count += 1

    def threads(self):
        self.shared_count = 0
        with ThreadPoolExecutor(max_workers=1000) as executor:
            for _ in range(200000):
                executor.submit(self.increment_thread)
        print(self.shared_count)

    def processes(self):
        self.shared_count_process.value = 0
        ps = []
        for _ in range(200):
            p = Process(target=self.increment_process)
            p.start()
            ps.append(p)
        [p.join() for p in ps]

        print(self.shared_count_process.value)

    def coroutines(self):
        self.shared_count = 0

        async def loop():
            await asyncio.gather(*[self.increment_coroutine() for _ in range(200_000)])

        asyncio.run(loop())
        print(self.shared_count)


if __name__ == "__main__":
    sm = SharedMemory()
    sm.processes()