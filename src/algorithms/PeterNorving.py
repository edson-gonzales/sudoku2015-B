class PerterNorvig():

    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)
        self.unitlist = ([self.cross(self.rows, c) for c in self.cols] +
                [self.cross(r, self.cols) for r in self.rows] +
                [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        self.units = dict((s, [u for u in self.unitlist if s in u])
                         for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                         for s in self.squares)

    def cross(self, key_list, value_list):
        """
        Cross product of elements in key_list and elements in value_list.
        Returns the grid with the filled coordinates.

        Keyword arguments:
        key_list -- Mostly this will be the row values.
        value_list -- Mostly this will be the colum values.
        """
        return [key+value for key in key_list for value in value_list]

    def parse_grid(self, grid):
        """
        Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected.
        return dict: Grid with all the possible values.

        Keyword arguments:
        param grid -- Dict with initial values.
        """
        values = dict((s, self.digits) for s in self.squares)
        for s,d in self.grid_values(grid).items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def grid_values(self, grid):
        """
        Convert grid into a dict of {square: char} with '0' or '.' for empties.
        return dict: grid dict with the values.

        Keyword arguments:
        grid -- skeleton grid
        """
        chars = [c for c in grid if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, square, digit):
        """
        Eliminate all the other values (except the sent digit) from values[square] and propagate.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        values -- initial dict
        square -- square position
        digit --  selected digits
        """
        other_values = values[square].replace(digit, '')
        if all(self.eliminate(values, square, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, digit):
        """
        Eliminate digit from values[square]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        values -- initial dic
        square -- square position
        digit -- digit values
        """
        if digit not in values[square]:
            return values
        values[square] = values[square].replace(digit, '')
        if len(values[square]) == 0:
            return False
        elif len(values[square]) == 1:
            d2 = values[square]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[square]):
                return False
        for u in self.units[square]:
            dplaces = [square for square in u if digit in values[square]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], digit):
                    return False
        return values

    def search(self, values):
        """
        Using depth-first search and propagation, try all possible values.
        return dict: updates possible values dict after search algorithm.

        Keyword arguments:
        values -- updates possible values dict.
        """
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.squares):
            return values
        n,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d))
                    for d in values[s])

    def some(self, seq):
        """
        Return boolean: return the element that is true.

        Keyword arguments:
        seq -- values dict.
        """
        for e in seq:
            if e: return e
        return False

    def solve(self, grid):
        """
        Solve the sudoku , returns False if the sudoku was invalid.

        Keyword arguments:
        grid -- initial grid to solve.
        """
        return self.search(self.parse_grid(grid))