import time
import timeit

from ThreadPool import ThreadPool


def task(seconds):
    time.sleep(seconds)
