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

