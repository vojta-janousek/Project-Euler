'''
A solution to the project euler problem #62

https://projecteuler.net/problem=62
'''
from time import time


# Lower/Upper limits of cube digit lengths
orders = [(465, 1000), (1000, 2155), (2155, 4642), (4642, 10000)]

def digit_count(n):
    '''Returns a string of consecutive digit counts of cubed n, from 0 to 9. '''
    digit_number_string = ''

    # Counts of digits from 0 to 9 appended as strings
    for i in range(10):
        digit_number_string += str(str(n ** 3).count(str(i)))
    return digit_number_string

def permutations_finder(start, end):
    '''
    Defines a dictionary with keys as the possible cube digit_count of input integers
    from start to end. The values for each key are its occurence within this range.
    Returns a tuple of the maximum occurence count and its corresponding value.
    '''
    dict = {}
    for j in range(start, end):
        dc_j = digit_count(j)
        if dc_j in dict:
            dict[dc_j] += 1
        else:
            dict[dc_j] = 1
    max_count = max(dict, key=dict.get)
    return((max_count, dict[max_count]))

if __name__ == '__main__':
    time_start = time()
    for order in orders:
        pf = permutations_finder(order[0], order[1])
        # Check to see if target number is within the currently observed order of magnitude
        if (pf[1] == 5):
            # Look for an example and break at the lowest one
            for k in range(order[0], order[1]):
                if (digit_count(k) == pf[0]):
                    print('Result: {}, Elapsed time: {}'.format(
                            k ** 3, time() - time_start
                    ))
                    break
