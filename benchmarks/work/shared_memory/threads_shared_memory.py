import time

from ThreadPool import ThreadPool

i = 0


def mutate():
    global i
    tmp = i
    i = tmp + 1


def main():
    tp = ThreadPool(3000, mutate, [[] for _ in range(1000000)])
    tp.run()


main()
print(i)
