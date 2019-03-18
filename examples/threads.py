from threading import Thread
from time import sleep
from functools import partial


def sleep_print_num(wait_time, i):
    sleep(wait_time)
    print(i)


def print_loop():
    threads = []
    for i in range(10):
        print('loop')
        sleep(0.5)
        t = Thread(target=partial(sleep_print_num, 1, i))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


print_loop()
