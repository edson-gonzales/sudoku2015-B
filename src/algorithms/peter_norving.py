class PeterNorvig:

    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.colums = self.digits
        self.squares = self.cross(self.rows, self.colums)
        self.unitlist = [self.cross(self.rows, colum) for colum in
                         self.colums] + [self.cross(row, self.colums)
                for row in self.rows] + [self.cross(row_square,
                colum_square) for row_square in ('ABC', 'DEF', 'GHI')
                for colum_square in ('123', '456', '789')]
        self.units = dict((square, [unit for unit in self.unitlist
                          if square in unit]) for square in
                          self.squares)
        self.peers = dict((square, set(sum(self.units[square], []))
                          - set([square])) for square in self.squares)

    def cross(self, key_list, value_list):
        """
        Cross product of elements in key_list and elements in value_list.

        Keyword arguments:
        key_list -- Mostly this will be the row values. i.e  1, 2, 3,etc
        value_list -- Mostly this will be the colum values. i.e A, B ,C, etc
        Returns the grid with the filled coordinates crossed, i.e.  [1A, 2A ].
        """

        return [key + value for key in key_list for value in value_list]

    def parse_grid(self, grid):
        """
        Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected.

        Keyword arguments:
        param grid -- Dict with initial values.
        return a dictionary with all the possible values per square.
        """

        values = dict((square, self.digits) for square in self.squares)
        for (square, digit) in self.grid_values(grid).items():
            if digit in self.digits and not self.assign(values, square,
                    digit):
                return False
        return values

    def grid_values(self, grid):
        """
        Convert grid game into a dict of {square: char} with '0' for empties.

        Keyword arguments:
        grid -- grid skeleton
        return grid dict with the filled values ready to play.
        """

        chars = [colum for colum in grid if colum in self.digits
                 or colum in '0']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, square, digit):
        """
        Eliminate all the other values (except the sent digit)
        from values[square] and then propagate.

        Keyword arguments:
        values -- initial dict with values
        square -- square positions
        digit --  selected digit
        return updated values, except return False if a contradiction is detected.
        """

        other_values = values[square].replace(digit, '')
        if all(self.eliminate(values, square, temp_digit)
               for temp_digit in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, digit):
        """
        Eliminate digit from values[square]; propagate when values or places <= 2.

        Keyword arguments:
        values -- initial dic
        square -- square positions
        digit -- digit values
        return updated values, except return False if a contradiction is detected.
        """

        if digit not in values[square]:
            return values
        values[square] = values[square].replace(digit, '')
        if len(values[square]) == 0:
            return False
        elif len(values[square]) == 1:
            temp_digit = values[square]
            if not all(self.eliminate(values, temp_square, temp_digit)
                       for temp_square in self.peers[square]):
                return False
        for unit in self.units[square]:
            dplaces = [square for square in unit if digit
                       in values[square]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1 and not self.assign(values,
                    dplaces[0], digit):
                return False
        return values

    def search(self, values):
        """
        Using depth-first search and propagation, try all possible values.

        Keyword arguments:
        values -- updates possible values dict.
        return updated dict with possible values after search algorithm.
        """

        if values is False:
            return False
        if all(len(values[square]) == 1 for square in self.squares):
            return values
        (unfilled, square) = min((len(values[square]), square)
                                 for square in self.squares
                                 if len(values[square]) > 1)

        return self.get_true_element(self.search(self.assign(values.copy(),
                square, digit)) for digit in values[square])

    def get_true_element(self, sequence):
        """
        return the element that is true.

        Keyword arguments:
        seq -- values dict.
        """

        for element in sequence:
            if element:
                return element
        return False

    def solve(self, grid):
        """
        Solve the sudoku , returns False if the sudoku was invalid.

        Keyword arguments:
        grid -- initial grid to solve.
        """

        return self.search(self.parse_grid(grid))