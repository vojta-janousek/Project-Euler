'''
Data Based solution to the #1 Project Euler problem.

https://projecteuler.net/problem=6
'''

import pandas as pd


limit = 100
df = pd.DataFrame(data={
                        'N':[i for i in range(1, limit+1)],
                        'N^2':[i**2 for i in range(1, limit+1)]
                        })
solution = ((df['N'].sum())**2) - (df['N^2'].sum())
print('Solution: ', solution)
