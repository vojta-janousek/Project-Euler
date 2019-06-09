'''
A solution to the project euler problem #66

https://projecteuler.net/problem=66
'''
print('Sum: ', sum([(4 * (n**2)) - (6 * n) + 6 for n in range(3, 1003, 2)]) + 1)
