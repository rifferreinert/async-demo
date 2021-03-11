from threading import Thread
from time import sleep
from timeit import timeit
from functools import partial


def sleep_print_num(i):
    sleep(2)
    print(i)


def run_race():
    threads = []
    for i in range(1, 6):
        t = Thread(target=partial(sleep_print_num, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


print(timeit(run_race, number=1))
