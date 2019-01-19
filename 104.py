'''
A solution to the project euler problem #106.

https://projecteuler.net/problem=104
'''

import time


def ispandigital(s):
    '''
    Returns True if input s is a string representation of a 1-9
    pandigital number. Return False otherwise.
    '''
    if sorted(s) == [str(m) for m in range(1, 10)]:
        return True
    else:
        return False


# Setup for the Fibonacci sequence
f1_head, f1_tail = 1, 1
f2_head, f2_tail = 1, 1
fn_head, fn_tail = 2, 2
n = 3
clock_start = time.time()

while True:
    # The terms of the Fibonacci sequence whose last 9 digits are checked
    # for being pandigital can be continuously cut off.
    #
    # Therefore, by making it a much smaller number each time, it is easier
    # to check first, and only then check the first 9 digits using the full term.
    if ispandigital(str(fn_tail)[-9:]):
        if ispandigital(str(fn_head)[:9]):
            print('Solution: {}, Elapsed time: {}'.format(n, time.time()-clock_start))
            break

    n += 1
    f1_head, f2_head, fn_head = f2_head, fn_head, fn_head + f2_head
    f1_tail, f2_tail, fn_tail = f2_tail, fn_tail, fn_tail + f2_tail

    fn_tail = int(str(fn_tail)[-9:])
    f2_tail = int(str(f2_tail)[-9:])
    f1_tail = int(str(f1_tail)[-9:])
