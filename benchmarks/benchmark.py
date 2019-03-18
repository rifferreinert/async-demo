from timeit import timeit
from functools import partial

import pandas as pd


class Benchmark:
    def __init__(self, trials):
        self.trials = trials

    def __time_func(self, func):
        """run function number times and return time taken"""
        return timeit(func, number=self.trials)

    def benchmark(self, func, work_size, job_counts, worker_counts):
        times = []
        for job_count in job_counts:
            for worker_count in worker_counts:
                time = self.__time_func(
                    lambda: func(work_size, job_count, worker_count)
                )
                times.append({'job_count': job_count,
                              'worker_count': worker_count,
                              'execution_time': time})
        return pd.DataFrame(times)
