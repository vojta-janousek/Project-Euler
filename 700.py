'''
Solves the project euler problem #700.

https://projecteuler.net/problem=700
'''
from time import time


def get_sum(modulo, coin):
    '''
    The distance between two Eulercoins is given by the value of the previous
    smallest coin, hence an Euclidian algorithm is used to find their sum.
    '''
    total, y_2 = 0, 1

    while (y_2 != 0):
        (x_1, y_1) = divmod(modulo, coin)
        (x_2, y_2) = divmod(coin, y_1)

        for i in range(x_2, 0, -1):
            total += y_2 + (i * y_1)

        modulo = y_1
        coin = y_2

    return total


if (__name__ == '__main__'):
    start = time()
    print('Result: {}, Elapsed time: {} seconds.'.format(
                                get_sum(4503599627370517, 1504170715041707),
                                time() - start
                                ))
