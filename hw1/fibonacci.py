import argparse


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


def fibonacci_number(n: int) -> int:
    """ Function returns fibonacci number of n
    
    :param n: number of fibonacci
    :return: number or sum or numbers
    """
    
    if n == 1 or n == 0: 
        return n
    
    return fibonacci_number(n-1) + fibonacci_number(n-2) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number")
    args = parser.parse_args()

    fib = fibonacci(int(args.number))
    with open("hw1/artifacts/easy/fib.txt", "w") as f:
        f.write(str(fib))

