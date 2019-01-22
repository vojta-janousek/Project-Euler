'''
A solution to the project euler problem #73.

https://projecteuler.net/problem=73
'''

from math import ceil
from time import time

from fractions import Fraction


def fractions_in_range(d):
    '''
    Returns a list of all reduced proper fractions with the input denominator d
    (before reduction) between 1/3 and 1/2 in the form of a
    (numerator, denominator) tuple.
    '''
    fraction_list = []
    n = ceil(d / 3)
    while ((n / d) < 0.5):
        reduced_proper = Fraction(n, d)
        fraction_list.append((reduced_proper.numerator, reduced_proper.denominator))
        n += 1
    return fraction_list


if (__name__ == '__main__'):
    limit = 12001
    final_list = []
    start = time()

    for i in range(2, limit):
        for fract in fractions_in_range(i):
            final_list.append(fract)

    print('# of fractions in range: {}, Elapsed time: {}'.format(
                    len(set(final_list))-1, time()-start))
