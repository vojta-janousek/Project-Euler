'''
Solves the project euler problem #684.

https://projecteuler.net/problem=684
'''
from time import time


def fibon(limit):
    '''
    Yields a fibonacci sequence up until the limit number.
    '''
    f_0 = 0
    f_1 = 1
    for i in range(limit-1):
        f_0, f_1 = f_1, f_0 + f_1
        yield f_1


def s(n):
    '''
    Returns the smallest number that has a digit sum of n, mod 1 000 000 007.
    '''
    j = n % 9
    i = int((n - j) / 9)
    s = str(j) + (i * '9')

    if (len(s) > 9):
        chopped = int(s[:-9])
        return (999999999 - (chopped * 7))
    else:
        return int(s)


if (__name__ == '__main__'):
    # print(s(76))
    # print(s(85))
    # print(s(88))
    # print(s(91))
    start = time()
    result = 0
    counter = 2
    for term in fibon(90):
        result = (result + s(term)) % 1000000007
        print(counter)
        counter += 1

    print('Result: {}, Elapsed time: {}'.format(
        result % 1000000007,
        time() - start))
