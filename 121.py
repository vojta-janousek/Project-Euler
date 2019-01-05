#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:27:16 2018

@author: vojta

https://projecteuler.net/problem=121
"""
import time
from math import factorial, floor

number_of_turns = 15
denominator = factorial(number_of_turns+1)
nominator = 0

# [branch probability's nominator, blue discs picked, red discs picked]
tree = [[1, 0, 1], [1, 1, 0]]

def expand_tree(tree_before, round_number):
    '''
    Populates a new tree with the two children of all branches of the input tree
    and returns the new one. Trees are in an array form.
    '''
    tree_after = []
    for branch in tree_before:
        tree_after.append([branch[0]*round_number, branch[1], branch[2]+1])
        tree_after.append([branch[0], branch[1]+1, branch[2]])
    return tree_after

if (__name__ == '__main__'):
    clock_start = time.time()
    # Populating the tree array
    for i in range(2, number_of_turns+1):
        tree = expand_tree(tree, i)
    # Adding up the probabilities of positive outcomes
    for branch in tree:
        if (branch[1] > branch[2]):
            nominator += branch[0]
    clock_end = time.time()      
    print('Nominator: {}, Denominator: {}, Game Prize: {}'.format(nominator, 
          denominator, floor(denominator / nominator)))
    print('Elapsed time: {} seconds'.format(clock_end-clock_start))
        
