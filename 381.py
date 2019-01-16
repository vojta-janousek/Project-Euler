'''
Solves the project euler problem #381.

https://projecteuler.net/problem=381
'''
from time import time
from itertools import islice
from sympy.solvers.diophantine import base_solution_linear as bsl


def prime_sieve(limit):
    prime_array = [True] * limit
    prime_array[0] = prime_array[1] = False

    for (i, isprime) in enumerate(prime_array):
        if isprime:
            yield i
            for n in range(i**2, limit, i):
                prime_array[n] = False


def element_calculation(p):
    '''
    element_calculation(p) = s(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.
    '''
    if ((p - 1) % 6 == 0):
        return (bsl((5*p)+1, -6*p, 6*(p-4))[1] + ((7*p)-1)/3) % p
    else:
        return (bsl(p+1, -6*p, (6*p)-24)[1] + ((5*p)-1)/3) % p

if __name__ == '__main__':

    limit = 10 ** 8
    count = 8
    clock_start = time()

    for prime in islice(prime_sieve(limit), 4, None):
        count += int(element_calculation(prime))

    print(count, time() - clock_start)
