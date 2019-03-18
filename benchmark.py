from bokeh.plotting import figure, output_file, show
from timeit import timeit
import asyncio

import pandas as pd

from CoroutinePool import CoroutinePool
from ThreadPool import ThreadPool
from CoroutineLimit import CoroutineLimit

from sleep.async_sleep import task as async_sleep_task
from sleep.threads_sleep import task as threads_sleep_task
from rate_limit.RateLimitTask import get_task as get_rate_limit_task


def benchmarkCoroutinePool(task, args, workers, number):
    async def run():
        cp = CoroutinePool(workers, task, args)
        await cp.run()

    return timeit(lambda: asyncio.run(run()), number=5)


def benchmarkCoroutineLimit(task, args, limit, number):
    async def run():
        cp = CoroutineLimit(limit, task, args)
        await cp.run()

    return timeit(lambda: asyncio.run(run()), number=5)


def benchmarkThreadPool(task, args, workers, number):
    tp = ThreadPool(workers, task, args)
    return timeit(tp.run, number=number)


def benchmarkOverInputs(benchmark, task, args, workers_test, number):
    times = []
    for workers in workers_test:
        times.append(benchmark(task, args, workers, number))
    return pd.DataFrame({'workers': workers_test, 'times': times})


workers_test = range(20, 2000, 100)
args = [[0.1] for _ in range(10000)]


def benchmark_async_rate_limit(
    workers_range,
    tasks_per_second_range,
    total_tasks
):
    for tasks_per_second in tasks_per_second_range:
        task = get_rate_limit_task(tasks_per_second, 1)
        times = benchmarkOverInputs(benchmarkCoroutinePool,
                                    task,
                                    [[] for _ in range(total_tasks)],
                                    workers_range,
                                    5)
        print(f'{tasks_per_second} per second limit')
        print(times)


benchmark_async_rate_limit([1000], [1000, 10000], 100000)


def benchmark_async_sleep():
    times = benchmarkOverInputs(benchmarkCoroutinePool,
                                async_sleep_task,
                                args,
                                workers_test,
                                5)
    return times


def benchmark_async_limit_sleep():
    times = benchmarkOverInputs(benchmarkCoroutineLimit,
                                async_sleep_task,
                                args,
                                workers_test,
                                5)
    return times


def benchmark_threads_sleep():
    times = benchmarkOverInputs(benchmarkThreadPool,
                                threads_sleep_task,
                                args,
                                workers_test,
                                5)
    return times


# df = benchmark_async_sleep()
# df.to_csv('async_pool_sleep.csv')

# df = benchmark_async_limit_sleep()
# df.to_csv('async_limit_sleep.csv')

# df = benchmark_threads_sleep()
# df.to_csv('threads_pool_sleep.csv')
