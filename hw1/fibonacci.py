import argparse


def fibonacci(n: int):
    """ Function print first fibonacci numbers
    Write in terminal 'python fibonacci.py -n <number>'
    
    :param n: count of fibonacci numbers
    """

    for i in range(n):
        print(fibonacci_number(i))


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

    fibonacci(int(args.number))