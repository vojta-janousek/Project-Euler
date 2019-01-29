'''
Data Based solution to the #1 Project Euler problem.

https://projecteuler.net/problem=1
'''

import numpy as np


limit = 1000
solution = (sum(np.array([x for x in range(1, limit) if (x % 3 == 0)])) +
            sum(np.array([x for x in range(1, limit) if (x % 5 == 0)])) -
            sum(np.array([x for x in range(1, limit) if (x % 15 == 0)])))

print('Solution: ', solution)
