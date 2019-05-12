'''
A solution to the project euler problem #80.

https://projecteuler.net/problem=80
'''

from math import sqrt
from time import time


def digit_sum(m):
    '''Returns the sum of digits of number m. Input m is in string form. '''
    count = 0
    for num in m:
        count += int(num)
    return count

def sqrt_by_subtraction(a, b):
    '''
    A single iterations of an iterative algorithm where the digits of b represent
    the decimal digits of a square root. Input and output are the iterated
    variables a, b before and after a single iteration, respectively.
    '''
    if (a > b):
        return a-b, b+10
    return a*100, int(str(b)[:-1] + '05')

def sqrt_digits(n):
    '''
    Goes through all iterations of the algorithm until the first 100 digits
    of the square root are known, then returns their sum.
    '''
    a = n * 5
    b = 5
    while (b < 10**106):
        a, b = sqrt_by_subtraction(a, b)
    return digit_sum(str(b)[:100])

if __name__ == '__main__':
    answer = 0
    start = time()
    for number in range(2, 100):
        # To disregard perfect squares
        if (sqrt(number) != int(sqrt(number))):
            answer += sqrt_digits(number)
    print('Result: {}, Elapsed time: {}'.format(answer, time()-start))
