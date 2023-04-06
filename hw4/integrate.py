import math
import time
import multiprocessing
from datetime import datetime
from functools import partial
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_part(f, a, step, period):
    thread_num, start, end = period
    print(f"{thread_num} started at {datetime.fromtimestamp(time.time())}")
    acc = 0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, n_jobs=1, n_iter=1000000, exc=ThreadPoolExecutor):
    blocks_num = n_iter // n_jobs
    step = (b - a) / n_iter
    if exc == ProcessPoolExecutor:
        job = 'Process '
    else:
        job = 'Thread '
    pairs = [[f'{job}{i+1}', blocks_num * i, blocks_num * (i+1)]
             for i in range(0, n_jobs)]
    pairs[-1][-1] += n_iter % n_jobs

    with exc(max_workers=n_jobs) as executor:
        result_list = executor.map(partial(integrate_part, f, a, step), pairs)
        return result_list


if __name__ == "__main__":
    cpu_num = multiprocessing.cpu_count()
    n_jobs_list = [i for i in range(1, cpu_num*2 + 1)]

    # Увеличила количество n_iter, иначе время потока почти 0
    for n_jobs in n_jobs_list:
        time_1 = time.time()
        result = integrate(math.cos, 0, math.pi / 2,
                           n_jobs=n_jobs, exc=ProcessPoolExecutor)
        print(f'\nProcess with n_jobs {n_jobs} '
              f'result: {sum(list(result)):.10f} '
              f'after {(time.time() - time_1):.17f}\n')

        time_1 = time.time()
        result = integrate(math.cos, 0, math.pi / 2,
                           n_jobs=n_jobs, exc=ThreadPoolExecutor)
        print(f'\nThreads with n_jobs {n_jobs} '
              f'result: {sum(list(result)):.10f} '
              f'after {(time.time() - time_1):.17f}\n')
