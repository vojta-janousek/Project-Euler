'''
A solution to the project euler problem #96.

https://projecteuler.net/problem=96
'''
import time
import random
import copy


class Grid():
    '''
    A Sudoku puzzle board/grid:

    State is the puzzle's current solution state presented
    in a triple nested array.

    Grid number is the puzzle's position number in the data file containing
    all of the puzzles.
    '''
    def __init__(self, state, grid_number):
        self.state = state
        self.grid_number = grid_number

    def __str__(self):
        representation = ''
        for line in self.state:
            representation += str(line) + '\n'
        return representation

    def grid_number_to_file_index(self):
        '''
        Converts the grid's number to its starting and ending index
        within the data file.
        '''
        start_index = ((self.grid_number - 1) * 10) + 1
        end_index = ((self.grid_number - 1) * 10) + 9

        return start_index, end_index

    def grid_load_and_transform(self):
        '''
        Loads a sudoku puzzle corresponding to the grid number from the file
        and transforms it into a triple nested array representation.
        '''
        file = open('sudoku_grids.txt', 'r')
        data = file.readlines()

        i, j = self.grid_number_to_file_index()
        representation = ''
        for n in range(i, j+1):
            representation += data[n][:-1]

        file.close()
        representation2 = []
        for m in range(9):
            representation2 += [representation[m*9:m*9+9]]

        # for line in representation2:
        #     print(line)

        for string_row in representation2:
            representation_array = []
            for string_number in string_row:
                if (string_number != '0'):
                    representation_array.append([int(string_number)])
                else:
                    representation_array.append([i for i in range(1, 10)])
            self.state.append(representation_array)

    def check_row(self, row):
        '''

        '''
        working_row = self.state[row]
        full_numbers = []
        for tile in working_row:
            if (len(tile) == 1):
                full_numbers.append(tile[0])

        for tile in working_row:
            tile_length = len(tile)
            if (tile_length != 1):
                for i in range(tile_length-1, -1, -1):
                    if tile[i] in full_numbers:
                        tile.pop(i)

        for n in range(1, 10):
            total = 0
            for tile in working_row:
                if n in tile:
                    total += 1
            if (total == 1):
                for i in range(9):
                    if n in working_row[i]:
                        working_row[i] = [n]

        self.state[row] = working_row

    def check_column(self, column):
        '''

        '''
        working_column = []
        for i in range(9):
            working_column.append(self.state[i][column])

        full_numbers = []
        for tile in working_column:
            if (len(tile) == 1):
                full_numbers.append(tile[0])

        for tile in working_column:
            tile_length = len(tile)
            if (tile_length != 1):
                for i in range(tile_length-1, -1, -1):
                    if tile[i] in full_numbers:
                        tile.pop(i)

        for n in range(1, 10):
            total = 0
            for tile in working_column:
                if n in tile:
                    total += 1
            if (total == 1):
                for i in range(9):
                    if n in working_column[i]:
                        working_column[i] = [n]

        for i in range(9):
            self.state[i][column] = working_column[i]

    def check_inner_squares(self, square):
        '''

        '''
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
        working_square = []
        for i_tuple in index_array[square]:
            working_square.append(self.state[i_tuple[0]][i_tuple[1]])

        full_numbers = []
        for tile in working_square:
            if (len(tile) == 1):
                full_numbers.append(tile[0])

        for tile in working_square:
            tile_length = len(tile)
            if (tile_length != 1):
                for i in range(tile_length-1, -1, -1):
                    if tile[i] in full_numbers:
                        tile.pop(i)

        for n in range(1, 10):
            total = 0
            for tile in working_square:
                if n in tile:
                    total += 1
            if (total == 1):
                for i in range(9):
                    if n in working_square[i]:
                        working_square[i] = [n]

        for i in range(9):
            self.state[index_array[square][i][0]][index_array[square][i][1]] = working_square[i]

    def simple_solution_rounds(self, rounds):
        '''

        '''
        for j in range(rounds):
            for i in range(9):
                self.check_row(row=i)

            for i in range(9):
                self.check_column(column=i)

            for i in range(9):
                self.check_inner_squares(square=i)

    def check_for_simple_solution(self):
        '''

        '''
        for i in range(9):
            for j in range(9):
                if (len(self.state[i][j]) != 1):
                    return False

        for row in range(9):
            working_row = self.state[row]
            full_numbers = []
            for tile in working_row:
                if (len(tile) == 1):
                    full_numbers.append(tile[0])
            if (sorted(full_numbers) != [i for i in range(1, 10)]):
                return False

        for column in range(9):
            working_column = []
            for i in range(9):
                working_column.append(self.state[i][column])

            full_numbers = []
            for tile in working_column:
                if (len(tile) == 1):
                    full_numbers.append(tile[0])
            if (sorted(full_numbers) != [i for i in range(1, 10)]):
                return False

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
        for square in range(9):
            working_square = []
            for i_tuple in index_array[square]:
                working_square.append(self.state[i_tuple[0]][i_tuple[1]])

            full_numbers = []
            for tile in working_square:
                if (len(tile) == 1):
                    full_numbers.append(tile[0])

            if (sorted(full_numbers) != [i for i in range(1, 10)]):
                return False


        return int(str(self.state[0][0][0]) + str(self.state[0][1][0]) + str(self.state[0][2][0]))

    def single_guess_simple_solution(self):
        '''

        '''
        placeholder = copy.deepcopy(self.state)
        available_indexes = []
        for i in range(9):
            for j in range(9):
                if (len(self.state[i][j]) > 1):
                    available_indexes.append((i, j))

        # while True:
        #     i, j = random.randint(0, 8), random.randint(0, 8)
        #     tile = self.state[i][j]
        #     if (len(tile) > 1):
        #         break

        for i_tuple in available_indexes:
            i, j = i_tuple[0], i_tuple[1]
            tile = self.state[i][j]

            for k in range(len(tile)):
                self.state[i][j] = [tile[k]]
                self.simple_solution_rounds(rounds=100)
                simple_test = self.check_for_simple_solution()
                if simple_test:
                    return simple_test

                self.state = copy.deepcopy(placeholder)

        return False

        # pick = random.randint(0, len(tile)-1)
        # self.state[i][j] = [tile[pick]]
        #
        # simple_test = self.check_for_simple_solution()
        # if simple_test:
        #     return simple_test
        # else:
        #     self.state = placeholder
        #     return False

    def guess_until_succesful(self):
        '''

        '''
        while True:
            guess = self.single_guess_simple_solution()
            if guess:
                break
        return guess


if (__name__ == '__main__'):
    start = time.time()
    total = 0
    missed = 0
    for x in range(1, 51):
        current_puzzle = Grid(state=[], grid_number=x)
        current_puzzle.grid_load_and_transform()
        current_puzzle.simple_solution_rounds(rounds=100)

        check = current_puzzle.check_for_simple_solution()
        if check:
            total += check
        else:
            guess_check = current_puzzle.single_guess_simple_solution()
            if guess_check:
                total += guess_check
            else:
                missed += 1
                print(x, '\n')
                print(current_puzzle)
            # total += current_puzzle.guess_until_succesful()

    print('Solution: {}, Elapsed time: {}'.format(total, time.time() - start))
    print('Missed: ', missed)
