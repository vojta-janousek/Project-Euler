'''
Solves the project euler problem #686.

https://projecteuler.net/problem=686
'''
from time import time


if __name__ == '__main__':
    clock_start = time()
    j, p, count = 0, 1, 0
    while (j < 678910):
        p = int(str(p * 2)[:15])
        count += 1
        if (str(p)[:3] == '123'):
            j += 1

    print('Result: {}, Elapsed time: {}'.format(count, time() - clock_start))
