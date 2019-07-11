'''
A solution to the project euler problem #96.

https://projecteuler.net/problem=96
'''
import time

from sudokusolver.grid_solvers import Grid


if (__name__ == '__main__'):
    start = time.time()
    total = 0
    missed = 0
    for x in range(1, 51):
        current_puzzle = Grid(filename='96_grids.txt', grid_number=x)
        current_puzzle.solve()
        if current_puzzle.is_solved():
            total += int(str(current_puzzle.state[0][0][0]) +
                         str(current_puzzle.state[0][1][0]) +
                         str(current_puzzle.state[0][2][0]))
        else:
            missed += 1
            print(x, '\n')
            print(current_puzzle)
    print('Total: {}, Elapsed time: {}'.format(total, time.time() - start))
    print('Missed: ', missed)
