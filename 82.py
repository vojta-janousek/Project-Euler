'''
A solution to the project euler problem #82.

https://projecteuler.net/problem=82
'''
import time


def minimum_path(row, column):
    '''
    Finds the minimum path for a given tile in the data matrix and returns
    the sum of numbers on this path.
    '''
    # The most simple path - just going straight to the right
    current_minimum = data[row][column] + data[row][column+1]

    row_checked = row + 1
    # Tries every path from current tile to the bottom of the matrix
    # to find the one with the smallest path sum
    while (row_checked <= dimension):
        current_path = data[row][column] + data[row_checked - 1][column + 1]
        for row_index in range(row + 1, row_checked):
            current_path += data[row_index][column]

        if (current_path < current_minimum):
            current_minimum = current_path

        row_checked += 1

    row_checked = row - 1
    # Same, but checks all paths going up from the current tile
    while (row_checked >= 0):
        current_path = data[row][column] + data[row_checked][column + 1]
        for row_index in range(row - 1, row_checked - 1, -1):
            current_path += data[row_index][column]

        if (current_path < current_minimum):
            current_minimum = current_path

        row_checked -= 1

    return current_minimum

def replace_with_minimum(replace_data, column):
    '''
    Outputs the input matrix, with the input column's tiles replaced
    with their minimum path sum
    '''
    array_of_minimums = [minimum_path(row, column) for row in range(dimension)]

    for row in range(dimension):
        replace_data[row][column] = array_of_minimums[row]

    return replace_data

if (__name__ == '__main__'):
    start = time.time()

    # Load the file data into a double nested array acting as matrix
    dimension = 80
    data = [[int(tile) for tile in row.strip('\n').split(',')]
            for row in open('82_matrix.txt', 'r')]

    for row in range(dimension - 2, -1, -1):
        data = replace_with_minimum(data, row)

    smallest_path_sum = sorted([data[row][0] for row in range(dimension)])[0]
    print('Minimum path sum: {}, Elapsed time: {}'.format(smallest_path_sum,
                                                          time.time() - start
                                                          ))
