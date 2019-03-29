import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin


from async_runners.AsyncPool import AsyncPool
from work.compute_fib.async_compute import do_job as async_fib
from work.compute_fib.threads_compute import do_job as threads_fib
from work.compute_fib.process_compute import do_job as process_fib
from benchmark import Benchmark


benchmarker = Benchmark(3)

funcs = [
    (async_fib, 'async_fib'),
    (threads_fib, 'threads_fib'),
    (process_fib, 'process_fib')
]

for func, name in funcs:
    result = benchmarker.benchmark(
        func,
        23,
        [1, 100, 300],
        [1, 4, 100, 1000])
    result = result.pivot(
        index='job_count', columns='worker_count', values='execution_time')
    result.to_csv(f'data/{name}.csv')
