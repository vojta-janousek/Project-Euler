'''
A solution to the project euler problem #66

https://projecteuler.net/problem=66
'''
from sympy.solvers.diophantine import diop_DN

print(sorted([(diop_DN(d, 1)[0], d) for d in range(2, 1001)])[-1][1])
