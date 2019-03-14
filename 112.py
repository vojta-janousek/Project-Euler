'''
A solution to the Project Euler problem #112.

https://projecteuler.net/problem=112
'''
from time import time

def is_bouncy(n):
    '''
    Returns True if the input number is bouncy and vice versa.
    '''
    if (sorted(str(n)) == list(str(n))):
        return False
    if (sorted(str(n)) == list(str(n))[::-1]):
        return False
    return True

if __name__ == '__main__':
    bouncy_count = 0
    all_count = 100
    start = time()
    while ((bouncy_count / all_count) < 0.99):
        all_count += 1
        if is_bouncy(all_count):
            bouncy_count += 1
    print('Result: {}, Elapsed time: {}'.format(all_count, time() - start))
