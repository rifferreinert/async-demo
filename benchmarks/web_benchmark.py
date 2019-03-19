import logging


import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin


from async_runners.AsyncPool import AsyncPool
from work.web.async_web import do_job as async_web
from work.web.async_web_requests import do_job as async_web_requests
from work.web.threads_web import do_job as threads_web
from work.web.process_web import do_job as process_web
from benchmark import Benchmark

logging.basicConfig(level=logging.DEBUG)

benchmarker = Benchmark(3)

funcs = [
    (async_web_requests, 'async_web_requests'),
    (async_web, 'async_web'),
    (threads_web, 'threads_web'),
    (process_web, 'process_web')
]

for func, name in funcs:
    print(name)
    result = benchmarker.benchmark(
        func,
        13,
        [1, 10, 50],
        [1, 3, 10, 30, 50, 100])
    result = result.pivot(
        index='job_count', columns='worker_count', values='execution_time')
    result.to_csv(f'data/{name}.csv')
