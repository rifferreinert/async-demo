import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin


from async_runners.AsyncPool import AsyncPool
from work.compute_prime.async_compute import do_job as async_prime
from work.compute_prime.threads_compute import do_job as threads_prime
from work.compute_prime.process_compute import do_job as process_prime
from benchmark import Benchmark

benchmarker = Benchmark(3)

funcs = [(async_prime, 'async_prime'),
         (threads_prime, 'threads_prime'),
         (process_prime, 'process_prime')]

for func, name in funcs:
    print(name)
    result = benchmarker.benchmark(
        func,
        1000,
        [1, 100, 1000],
        [1, 4, 50, 100, 1000])
    result = result.pivot(
        index='job_count', columns='worker_count', values='execution_time')
    result.to_csv(f'data/{name}.csv')
