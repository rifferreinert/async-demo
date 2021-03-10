from threading import Thread
from time import sleep
from timeit import timeit
from functools import partial


def sleep_print_num(i):
    sleep(1)
    print(i)


def run_race():
    t1 = Thread(target=partial(sleep_print_num, 1))
    t1.start()

    t2 = Thread(target=partial(sleep_print_num, 2))
    t2.start()

    t3 = Thread(target=partial(sleep_print_num, 3))
    t3.start()

    t4 = Thread(target=partial(sleep_print_num, 4))
    t4.start()

    t5 = Thread(target=partial(sleep_print_num, 5))
    t5.start()

    t6 = Thread(target=partial(sleep_print_num, 6))
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()


print(timeit(run_race, number=1))
