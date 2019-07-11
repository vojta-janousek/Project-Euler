from grid_solvers import Grid


# Direct input
puzzle1 = Grid(state='003020600900305001001806400008102900700000008006708200002609500800203009005010300')
puzzle1.solve()

# File input
puzzle2 = Grid(filename='sudoku_grids.txt', grid_number=1)
puzzle2.solve()

print(str(puzzle1)==str(puzzle2))
