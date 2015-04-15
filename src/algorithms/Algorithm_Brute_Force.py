import random


class AlgorithmBruteForce(object):

    def __init__(self):        
        # EMPTY_SUDOKU -- empty grid with dimension 9x9.
        self.EMPTY_SUDOKU = [[0] * 9] * 9
        # DIMENSION -- grid dimension expected, to load the grid from a string.
        self.DIMENSION = 9

    def conflict(self, (row1, col1), (row2, col2)):
        """
        Verifies if there is a conflict with given Columns.

        row1 -- row to verify if there is a conflic
        row2 -- row to verify if there is a conflic
        col1 -- column to verify if there is a conflic
        col2 -- column to verify if there is a conflic
        Return -- boolean value, true = conflic false = no conflict
        """
        is_same_cell = row1 == row2 and col1 == col2
        if row1 == row2:
            return True
        if col1 == col2:
            return True
        if row1 / 3 == row2 / 3 and col1 / 3 == col2 / 3 and not is_same_cell:
            return True
        return False

    def setminus(self, list1, list2):
        """
        Looks for a value in List1 that is not in List2 and returns it.

        list1 -- List of values to be verified
        list2 -- List of not allowed values
        """
        return [x for x in list1 if x not in list2]

    def nextcell(self, (pos_row, pos_col)):
        """
        Finds next cell to fill, and returns 0 if the position in the row
        or column reach the limit of it that is pos 8 in the array and would be
        the pos 9 in the sudoku

        pos_row -- current cell position in the row
        pos_col -- current cell position in the column
        """
        if pos_col == 8:
            if pos_row == 8:
                return (0, 0)
            return (pos_row + 1, 0)
        return (pos_row, pos_col + 1)

    def solve(self, sudoku):
        """ Solves the given sudoku.
        Solves a sudoku verifying the possible candidates per position.
        A solved sudoku is returned, just if sudoku has a valid result.
        If sudoku is not resolvable a grid with all values as zero is returned.

        sudoku -- given sudoku in string format
        Return -- grid populated with values that satisfy each row, column and quadrant
        """

        # loadding the sudoku to a matrix into grid.
        grid = self.load_puzzle(sudoku)
        return self.satisfy((0, 0), grid)

    def load_puzzle(self, puzzle_string):
        """ Converts given string to grid 9x9

        puzzle_string -- the given sudoku in a string format, that will be
        converted to a grid.
        Return int[9][9] -- a grid 9x9
        """
        list_of_numbers = [int(n) for n in puzzle_string]
        grid = [[0] * self.DIMENSION] * self.DIMENSION
        for row in range(self.DIMENSION):
            grid[row] = list_of_numbers[row * self.DIMENSION:(row + 1)
                * self.DIMENSION]
        return grid

    def satisfy(self, pos, sudoku):
        """
        populates the allowed values into cell in the given position 'pos'
        just if values satisfy the values in the row, column and quadrant

        pos -- current cell position, example: (row_pos, col_pos)
        sudoku -- grid to iterate and populate with allowed values
        Return -- grid populated with values that satisfy each row, column and quadrant
        """
        if sudoku[pos[0]][pos[1]] != 0:
            if pos != (8, 8):
                return self.satisfy(self.nextcell(pos), sudoku)
            else:
                return sudoku

        values = self.getAllowedValues(pos, sudoku)
        if values == self.EMPTY_SUDOKU:
            return self.EMPTY_SUDOKU
        new = [row[:] for row in sudoku]
        for value in values:
            new[pos[0]][pos[1]] = value
            filled = self.satisfy(self.nextcell(pos), new)
            if filled != self.EMPTY_SUDOKU:
                return filled
        return self.EMPTY_SUDOKU

    def getAllowedValues(self, pos, sudoku):
        """
        Get allowed values and makes sure there are no conflicts within row,
        column and quadrant, reviewing cells randomly.

        pos -- current cell position, (row_pos, col_pos).
        sudoku -- grid to iterate and verify which values are allowed.
        Return -- int array with alllowed values without conflicts.
        """
        conflicts = set([(row, column) for row in range(9) for column in
                        range(9) if (row, column) != pos
                        and self.conflict(pos, (row, column))])
        notallowed = set([sudoku[row][column] for (row, column) in
                         conflicts if sudoku[row][column] != 0])
        values = self.setminus(range(1, 10), notallowed)
        random.shuffle(values)  
        return values