import time
import multiprocessing
import json
from threading import Thread


def fibonacci_number(n: int) -> int:
    """ Function returns fibonacci number of n
    
    :param n: number of fibonacci
    :return: number or sum or numbers
    """
    
    if n == 1 or n == 0: 
        return n
    
    return fibonacci_number(n-1) + fibonacci_number(n-2)


def fibonacci(n: int):
    """ Function print first fibonacci numbers
    Write in terminal 'python fibonacci.py -n <number>'

    :param n: count of fibonacci numbers
    :return: list of fibonacci numbers
    """

    fib = []
    for i in range(n):
        fib.append((fibonacci_number(i)))
    return fib


if __name__ == "__main__":
    number = 45
    time_result = {}

    start = time.time()
    for i in range(10):
        print('sequential', i)
        fib = fibonacci(number)
    time_result['sequential'] = (time.time() - start) / 10

    print('threading')
    start = time.time()
    threads = [Thread(target=fibonacci, args=(number,)) for i in range(10)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    time_result['threading'] = (time.time() - start) / 10

    print('multiprocessing')
    start = time.time()
    processes = [multiprocessing.Process(target=fibonacci,
                                         args=(number,)) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    time_result['multiprocessing'] = (time.time() - start) / 10

    with open("hw4/artifacts/easy/time.json", "w") as f:
        json.dump(time_result, f)

