'''
A sudoku solving script, intended for importing. After importing the Grid class,
a sudoku puzzle can be defined directly, or within a file.

For a direct input, use for example:

direct_puzzle = Grid(state='puzzle_string_representaion')

where puzzle_string_representaion is a 81 characters long string of numbers
on an unsolved sudoku board, row by row. Unknown tiles are denoted by 0.

For a file input, use for example:

file_puzzle = Grid(filename='sudoku_grids.txt', grid_number=1)

where sudoku_grids.txt is a text file with any number of sudoku grids,
starting with 'Grid 1' for example, following its rows (each on a separate
line)

Once the puzzle is defined, it can be displayed using:

print(puzzle)

or solved using:

puzzle.solve()


The algorithm will always try a simple solution first, before resolving to
a guessing game. Each guess is followed by an attempt at a simple solution
until a correct guess is found.

This file setup is made specifically to be used in solving the Project
Euler problem #96.

https://projecteuler.net/problem=96


The entire script assumes perfect use, and does not contain any
try/except clauses catching incorrect use or inputs.
It is not a comprehensive sudoku solver and as such does not contain
any tests and is not anchored on python package index.

'''
import copy


class Grid():
    '''
    A Sudoku puzzle board/grid:

    State is the puzzle's current solution state presented
    in a triple nested array.

    Grid number is the puzzle's position number in the data file containing
    all of the puzzles.
    '''

    original_state = None

    index_array = [
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
        [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
        [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
        [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
        [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
        [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
        [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
    ]

    def __init__(self, state=None, filename=None, grid_number=None):
        self.state = state
        self.filename = filename
        self.grid_number = grid_number

    def __str__(self):
        if (self.state == None) or (len(self.state) == 81):
            self.load_and_transform()

        s = ''
        for row in self.state:
            for tile in row:
                if (len(tile) == 1):
                    s += str(tile[0])
                else:
                    s += 'X'
        puzzle = (
                  ' -----------------------' + '\n' +

                  '| ' + s[0] + ' ' + s[1] + ' ' + s[2] + ' | ' + s[3] + ' ' +
                  s[4] + ' ' + s[5] + ' | ' + s[6] + ' ' + s[7] + ' ' + s[8] +
                  ' |' + '\n' +

                  '| ' + s[9] + ' ' + s[10] + ' ' + s[11] + ' | ' + s[12] +
                  ' ' + s[13] + ' ' + s[14] + ' | ' + s[15] + ' ' + s[16] +
                  ' ' + s[17] + ' |' + '\n' +

                  '| ' + s[18] + ' ' + s[19] + ' ' + s[20] + ' | ' + s[21] +
                  ' ' + s[22] + ' ' + s[23] + ' | ' + s[24] + ' ' + s[25] +
                  ' ' + s[26] + ' |' + '\n' +

                  '|-----------------------|' + '\n' +

                  '| ' + s[27] + ' ' + s[28] + ' ' + s[29] + ' | ' + s[30] +
                  ' ' + s[31] + ' ' + s[32] + ' | ' + s[33] + ' ' + s[34] +
                  ' ' + s[35] + ' |' + '\n' +

                  '| ' + s[36] + ' ' + s[37] + ' ' + s[38] + ' | ' + s[39] +
                  ' ' + s[40] + ' ' + s[41] + ' | ' + s[42] + ' ' + s[43] +
                  ' ' + s[44] + ' |' + '\n' +

                  '| ' + s[45] + ' ' + s[46] + ' ' + s[47] + ' | ' + s[48] +
                  ' ' + s[49] + ' ' + s[50] + ' | ' + s[51] + ' ' + s[52] +
                  ' ' + s[53] + ' |' + '\n' +

                  '|-----------------------|' + '\n' +

                  '| ' + s[54] + ' ' + s[55] + ' ' + s[56] + ' | ' + s[57] +
                  ' ' + s[58] + ' ' + s[59] + ' | ' + s[60] + ' ' + s[61] +
                  ' ' + s[62] + ' |' + '\n' +

                  '| ' + s[63] + ' ' + s[64] + ' ' + s[65] + ' | ' + s[66] +
                  ' ' + s[67] + ' ' + s[68] + ' | ' + s[69] + ' ' + s[70] +
                  ' ' + s[71] + ' |' + '\n' +

                  '| ' + s[72] + ' ' + s[73] + ' ' + s[74] + ' | ' + s[75] +
                  ' ' + s[76] + ' ' + s[77] + ' | ' + s[78] + ' ' + s[79] +
                  ' ' + s[80] + ' |' + '\n' +

                  ' -----------------------'
                 )
        return puzzle

    def grid_number_to_file_index(self):
        '''
        Converts the grid's number to its starting and ending index
        within the data file.
        '''
        start_index = ((self.grid_number - 1) * 10) + 1
        end_index = ((self.grid_number - 1) * 10) + 9

        return start_index, end_index

    def load_from_simple_file(self):
        '''
        Loads a sudoku puzzle from a file containing a single puzzle in 9 rows,
        where an unknown tile is denoted by a 0.
        '''
        file = open(self.filename, 'r')
        self.state = [[tile for tile in row.strip('\n').split(',')]
                      for row in file.readlines()]
        file.close()

    def load_grid_from_multi_file(self):
        '''
        Loads a sudoku puzzle corresponding to the grid number attribute from
        a file appointed by the file name attribute. The puzzle's state format
        is an array holding 9 arrays with strings representing the puzzle rows.
        '''
        start, end = self.grid_number_to_file_index()

        file = open(self.filename, 'r')
        self.state = [[tile for tile in row.strip('\n').split(',')]
                      for row in file.readlines()[start:end+1]]
        file.close()

    def load_grid_from_input(self):
        '''
        Loads a sudoku puzzle from the directly input state attribute.
        The puzzle's new state format is an array holding 9 arrays with strings
        representing the puzzle rows.
        '''
        self.state = [[self.state[i*9:i*9+9]] for i in range(9)]

    def transform(self):
        '''
        Transforms the grid from an array holding 9 arrays with strings
        representing the puzzle rows into a double nested integer array
        representation.
        '''
        for row in range(9):
            new_row = []
            for tile in self.state[row][0]:
                if (tile == '0'):
                    new_row.append([i for i in range(1, 10)])
                else:
                    new_row.append([int(tile)])
            self.state[row] = new_row

    def load_and_transform(self):
        '''
        Calls the respective loading method base on the input type,
        then calls the transform method. Also saves the original state into
        a self.original_state variable in case the state need to be reverted
        after the grid has been solved or modified.
        '''
        if (self.state == None):
            if (self.grid_number == None):
                self.load_from_simple_file()
            else:
                self.load_grid_from_multi_file()

        else:
            self.load_grid_from_input()

        self.transform()
        self.original_state = copy.deepcopy(self.state)

    def return_to_original_state(self):
        '''
        At the end of the self.load_and_transform method, the original state
        of the grid object deepcopy is stored within the self.original_state
        variable.

        Calling this method reverts the current state to the original.
        This does not overwrite the original state.
        '''
        self.state = copy.deepcopy(self.original_state)

    def check_row(self, row):
        '''
        Gets the full list of known numbers in the investigated row,
        then removes these numbers as candidates from the remaining tiles.
        '''
        working_row = self.state[row]
        full_numbers = [tile[0] for tile in working_row if len(tile)==1]

        for tile in working_row:
            if (len(tile) != 1):
                for candidate_number in range(len(tile)-1, -1, -1):
                    if tile[candidate_number] in full_numbers:
                        tile.pop(candidate_number)

        # Checks the occurence of each number as a candidate. If a number only
        # appears once, it is assigned to the tile where it candidated.
        for n in range(1, 10):
            count = 0
            for tile in working_row:
                if n in tile:
                    count += 1
            if (count == 1):
                for i in range(9):
                    if n in working_row[i]:
                        working_row[i] = [n]

        # Replace the old state with the new cleared state
        self.state[row] = working_row

    def check_column(self, column):
        '''
        Gets the full list of known numbers in the investigated column,
        then removes these numbers as candidates from the remaining tiles.
        '''
        working_column = [self.state[row][column] for row in range(9)]
        full_numbers = [tile[0] for tile in working_column if len(tile)==1]

        for tile in working_column:
            if (len(tile) != 1):
                for candidate_number in range(len(tile)-1, -1, -1):
                    if tile[candidate_number] in full_numbers:
                        tile.pop(candidate_number)

        # Checks the occurence of each number as a candidate. If a number only
        # appears once, it it assigned to the tile where it candidated.
        for n in range(1, 10):
            count = 0
            for tile in working_column:
                if n in tile:
                    count += 1
            if (count == 1):
                for i in range(9):
                    if n in working_column[i]:
                        working_column[i] = [n]

        # Replace the old state with the new cleared state
        for row in range(9):
            self.state[row][column] = working_column[row]

    def check_inner_squares(self, square):
        '''
        Gets the full list of known numbers in the investigated inner square,
        then removes these numbers as candidates from the remaining tiles.
        '''
        working_square = [self.state[i_tuple[0]][i_tuple[1]]
                          for i_tuple in self.index_array[square]]
        full_numbers = [tile[0] for tile in working_square if len(tile)==1]

        for tile in working_square:
            tile_length = len(tile)
            if (tile_length != 1):
                for i in range(tile_length-1, -1, -1):
                    if tile[i] in full_numbers:
                        tile.pop(i)

        # Checks the occurence of each number as a candidate. If a number only
        # appears once, it it assigned to the tile where it candidated.
        for n in range(1, 10):
            total = 0
            for tile in working_square:
                if n in tile:
                    total += 1
            if (total == 1):
                for i in range(9):
                    if n in working_square[i]:
                        working_square[i] = [n]

        # Replace the old state with the new cleared state
        for i in range(9):
            row = self.index_array[square][i][0]
            column = self.index_array[square][i][1]

            self.state[row][column] = working_square[i]



    def simple_solution_rounds(self, rounds):
        '''
        Performs an input number of rounds checking to eliminate potential
        number candidates that already appear in the same row, column,
        or inner square.
        '''
        for round in range(rounds):
            for row in range(9):
                self.check_row(row=row)

            for column in range(9):
                self.check_column(column=column)

            for square in range(9):
                self.check_inner_squares(square=square)

    def is_solved(self):
        '''
        Checks whether all tiles have been filled and that all rows, columns
        and inner squares contain each digit exactly once. Returns False if any
        of the checks fail. Returns True if everything checks out.
        '''
        one_to_nine = [i for i in range(1, 10)]

        for row in range(9):
            for column in range(9):
                if (len(self.state[row][column]) != 1):
                    return False

        for row in range(9):
            full_numbers = [tile[0] for tile in self.state[row] if len(tile)==1]
            if (sorted(full_numbers) != one_to_nine):
                return False

        for column in range(9):
            working_column = [self.state[row][column] for row in range(9)]
            full_numbers = [tile[0] for tile in working_column if len(tile)==1]
            if (sorted(full_numbers) != one_to_nine):
                return False

        for square in range(9):
            working_square = [self.state[i_tuple[0]][i_tuple[1]] for i_tuple
                              in self.index_array[square]]
            full_numbers = [tile[0] for tile in working_square if len(tile)==1]
            if (sorted(full_numbers) != one_to_nine):
                return False

        return True

    def guessing_solution(self):
        '''
        Saves current grid state into a placeholder variable, then makes a list
        of all unknown tiles.
        For each unknown tile, goes through the list of its candidates and
        makes a guess followed by a simple solution attempt. Once it goes
        through all candidates with no progress, moves on to another unknown
        tile.
        If ever a simple solution is found, True is returned and the grid state
        is changed to the solved puzzle.
        If there is no solution in all unknown tiles, False is returned.
        '''
        placeholder = copy.deepcopy(self.state)
        available_indexes = []
        for i in range(9):
            for j in range(9):
                if (len(self.state[i][j]) > 1):
                    available_indexes.append((i, j))

        for i_tuple in available_indexes:
            i, j = i_tuple[0], i_tuple[1]
            tile = self.state[i][j]

            for k in range(len(tile)):
                self.state[i][j] = [tile[k]]
                self.simple_solution_rounds(rounds=100)
                if self.is_solved():
                    return True

                self.state = copy.deepcopy(placeholder)

        return False

    def solve(self):
        '''
        Loads and transforms the grid, unless it already has been. Then tries
        to solve the grid using the simple solution.
        If unsuccessful, goes on to try the guessing solution.
        '''
        if (self.state == None) or (len(self.state) == 81):
            self.load_and_transform()

        self.simple_solution_rounds(rounds=100)
        if not self.is_solved():
            self.guessing_solution()
