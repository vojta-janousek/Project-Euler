#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 1 13:35:06 2018
Updated on Sat Jan 5 11:57:00 2019

@author: vojta

https://projecteuler.net/problem=91
"""
import time

def isright(x_p, y_p, x_q, y_q):
    '''
    Takes coordinates and returns True if they can generate
    a right triangle.
    '''
    a = (x_p ** 2) + (y_p ** 2)
    b = (x_q ** 2) + (y_q ** 2)
    c = ((x_p - x_q) ** 2) + ((y_p - y_q) ** 2)

    if ((c > a) and (c > b)):
        if ((x_p == 0 and y_q == 0) or (x_q == 0 and y_p == 0)):
            return True
        else:
            return False
    elif ((a > b) and (a > c)):
        if (x_q * (x_q - x_p) == y_q * (y_p - y_q)):
            return True
        else:
            return False
    elif ((b > a) and (b > c)):
        if (x_p * (x_p - x_q) == y_p * (y_q - y_p)):
            return True
        else:
            return False
    else:
        return False

if (__name__ == '__main__'):
    clock_start = time.time()
    count = 0
    for p in ((n, m) for n in range(51) for m in range(51) if not (n == 0 and m == 0)):
        for q in ((x, y) for x in range(51) for y in range(51) if not (x == 0 and y == 0)):
            if (p != q) and isright(p[0], p[1], q[0], q[1]):
                count += 1
    clock_end = time.time()
    print('Count: {}'.format(int(count/2)))
    print('Elapsed time: {} seconds'.format(clock_end-clock_start))
