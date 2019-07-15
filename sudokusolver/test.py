'''
Grid unit tests, testing the features intended for use by the documentation.

Files simple_file_example.txt and multi_file_example.txt are required
for the tests.
'''
import unittest

from grid_solvers import Grid


class TestLoading(unittest.TestCase):
    '''
    Tests for proper input loading and different loading methods corresponding
    to the input type.
    '''
    def test_different_input_methods(self):
        '''
        Test that all 3 available methods of loading work and lead
        to the same result.
        '''
        first_half = '00302060090030500100180640000810290070000'
        second_half = '0008006708200002609500800203009005010300'
        state_string = first_half + second_half

        directly_loaded = Grid(state=state_string)
        simple_file_loaded = Grid(filename='simple_file_example.txt')
        multi_file_loaded = Grid(filename='multi_file_example.txt',
                                 grid_number=1)

        directly_loaded.load_and_transform()
        simple_file_loaded.load_and_transform()
        multi_file_loaded.load_and_transform()

        self.assertEqual(directly_loaded.state, simple_file_loaded.state)
        self.assertEqual(directly_loaded.state, multi_file_loaded.state)
        self.assertEqual(simple_file_loaded.state, multi_file_loaded.state)


class TestSolving(unittest.TestCase):
    '''
    Tests the solving algorithm and reverting back to the original state.
    '''
    def test_solution_algorithm(self):
        '''
        Test that an unsolved puzzle does not meet the requirements
        of a solved puzzle.
        Test that a solvable loaded and transformed puzzle is solved
        by the algorithm.
        '''
        puzzle = Grid(filename='simple_file_example.txt')
        puzzle.load_and_transform()
        self.assertFalse(puzzle.is_solved())

        puzzle.solve()
        self.assertTrue(puzzle.is_solved())

    def test_reverse_to_original_after_solving(self):
        '''
        Test that the state of a solved puzzle returned back to its original
        state is equal to its state before it being solved.
        '''
        original_puzzle = Grid(filename='simple_file_example.txt')
        original_puzzle.load_and_transform()

        solved_and_returned_puzzle = Grid(filename='simple_file_example.txt')
        solved_and_returned_puzzle.solve()
        solved_and_returned_puzzle.return_to_original_state()

        self.assertEqual(original_puzzle.state,
                         solved_and_returned_puzzle.state)


if (__name__ == '__main__'):
    unittest.main()
