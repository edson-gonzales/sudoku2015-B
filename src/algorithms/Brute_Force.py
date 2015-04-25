import random


class BruteForce(object):

    def __init__(self):        
        # EMPTY_SUDOKU -- empty grid with dimension 9x9.
        self.EMPTY_SUDOKU = [[0] * 9] * 9
        # DIMENSION -- grid dimension expected, to load the grid from a string.
        self.DIMENSION = 9

    def has_conflict(self, (first_row, first_column), (second_row, second_col)):
        """
        Verifies if there is a conflict with given Columns.

        first_row -- int, first row position
        second_row -- int, second row position
        first_column -- int, first column position
        second_col -- int, second column position
        Return -- boolean value, true = conflict; false = no conflict
        """
        is_same_cell = first_row == second_row and first_column == second_col
        if first_row == second_row:
            return True
        if first_column == second_col:
            return True
        if first_row / 3 == second_row / 3 and first_column / 3 == second_col / 3 and not is_same_cell:
            return True
        return False

    def set_minus(self, fist_list, second_list):
        """
        Looks for value(s) in fist_list that is not in second_list and returns it.

        fist_list -- array, List of values to be verified
        second_list -- array, List of not allowed values
        Return -- Array with values of fist_list not present in second_list
        """
        return [x for x in fist_list if x not in second_list]

    def get_next_cell(self, (row_position, column_position)):
        """
        Finds next cell to fill, and returns 0 if the position in the row
        or column reach the limit of it that is pos 8 in the array and would be
        the pos 9 in the sudoku

        row_position -- int, current cell position in the row
        column_position -- int, current cell position in the column
        """
        if column_position == 8:
            if row_position == 8:
                return (0, 0)
            return (row_position + 1, 0)
        return (row_position, column_position + 1)

    def solve(self, sudoku):
        """ Solves the given sudoku.
        Solves a sudoku verifying the possible candidates per position.
        A solved sudoku is returned, just if sudoku has a valid result.
        If sudoku is not resolvable a grid with all values as zero is returned.

        sudoku -- given sudoku in string format (81 numbers with spaces). Example:
        '530070000600195000098000060800060003400803001700020006060000280000419000000080070'
        Return -- grid populated with values that satisfy each row, column and quadrant
        """

        # loadding the sudoku into a grid.
        grid = self.convert_puzzle_from_string_to_grid(sudoku)
        return self.populate_grid_with_allowed_values((0, 0), grid)

    def convert_puzzle_from_string_to_grid(self, puzzle_string):
        """ Converts given string to grid 9x9

        puzzle_string -- the given sudoku in a string format, that will be
        converted to a grid. Example:
        '530070000600195000098000060800060003400803001700020006060000280000419000000080070'
        Return int[9][9] -- a grid 9x9
        """
        list_of_numbers = [int(n) for n in puzzle_string]
        grid = [[0] * self.DIMENSION] * self.DIMENSION
        for row in range(self.DIMENSION):
            grid[row] = list_of_numbers[row * self.DIMENSION:(row + 1)
                * self.DIMENSION]
        return grid

    def populate_grid_with_allowed_values(self, position, sudoku):
        """
        populates the allowed values into cell in the given position 'position'
        just if values satisfy the values in the row, column and quadrant

        position -- current cell position, example: (row_position, column_position)
        sudoku -- grid to iterate and populate with allowed values
        Return -- grid populated with values that satisfy each row, column and quadrant
        """
        if sudoku[position[0]][position[1]] != 0:
            if position != (8, 8):
                return self.populate_grid_with_allowed_values(self.get_next_cell(position), sudoku)
            else:
                return sudoku

        values = self.get_allowed_values(position, sudoku)
        if values == self.EMPTY_SUDOKU:
            return self.EMPTY_SUDOKU
        new = [row[:] for row in sudoku]
        for value in values:
            new[position[0]][position[1]] = value
            filled = self.populate_grid_with_allowed_values(self.get_next_cell(position), new)
            if filled != self.EMPTY_SUDOKU:
                return filled
        return self.EMPTY_SUDOKU

    def get_allowed_values(self, position, sudoku):
        """
        Get allowed values and makes sure there are no conflicts within row,
        column and quadrant, reviewing cells randomly.

        position -- current cell position, (row_pos, col_pos).
        sudoku -- grid to iterate and verify which values are allowed.
        Return -- int array with alllowed values without conflicts.
        """
        conflicts = set([(row, column) for row in range(9) for column in
                        range(9) if (row, column) != position
                        and self.has_conflict(position, (row, column))])
        notallowed = set([sudoku[row][column] for (row, column) in
                         conflicts if sudoku[row][column] != 0])
        values = self.set_minus(range(1, 10), notallowed)
        random.shuffle(values)  
        return values