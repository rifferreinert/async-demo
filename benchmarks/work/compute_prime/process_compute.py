from concurrent.futures import ProcessPoolExecutor


def prime_count(n):
    prime_count = 0
    for i in range(2, n + 1):
        prime = True
        for d in range(2, i):
            if i % d == 0:
                prime = False
                break
        if prime:
            prime_count += 1

    return prime_count


def do_job(compute_size, job_count, thread_count):
    work = [compute_size for _ in range(job_count)]
    with ProcessPoolExecutor(max_workers=thread_count) as executor:
        executor.map(prime_count, work)


# do_job(10000, 10, 30)
