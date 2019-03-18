from concurrent.futures import ThreadPoolExecutor


def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)


def do_job(compute_size, job_count, thread_count):
    work = [compute_size for _ in range(job_count)]
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(fib, work)
