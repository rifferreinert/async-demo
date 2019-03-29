from threading import Thread
from time import sleep
from timeit import timeit
from functools import partial


def sleep_print_num(wait_time, i):
    sleep(wait_time)
    print(i)


def run_two():
    t1 = Thread(target=partial(sleep_print_num, 0.55, 1))
    t1.start()
    t2 = Thread(target=partial(sleep_print_num, 0.5, 2))
    t2.start()
    t1.join()
    t2.join()


print(timeit(run_two, number=1))
