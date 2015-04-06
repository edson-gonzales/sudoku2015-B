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

    ##
    # Cross product of elements in A and elements in B.
    # @param A: Mostly this will be the row values.
    # @param B: Mostly this will be the colum values.
    # @return Array[]: Returns the grid with the filled coordinates.
    def cross(self, A, B):
        return [a+b for a in A for b in B]

    ##
    # Convert grid to a dict of possible values, {square: digits}, or
    # return False if a contradiction is detected.
    # @param grid:  Dict with initial values.
    # @return dict: Grid with all the possible values.
    def parse_grid(self, grid):
        values = dict((s, self.digits) for s in self.squares)
        for s,d in self.grid_values(grid).items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values
    ##
    # Convert grid into a dict of {square: char} with '0' or '.' for empties.
    # @param grid: skeleton grid
    # @return dict: grid dict with the values.
    def grid_values(self, grid):
        chars = [c for c in grid if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    ##
    # Eliminate all the other values (except d) from values[s] and propagate.
    # Return values, except return False if a contradiction is detected.
    # @param values: initial dict
    # @param s: square
    # @param d: digit
    # @return dict: return cleaned values.
    def assign(self, values, s, d):
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False
    ##
    # Eliminate d from values[s]; propagate when values or places <= 2.
    # Return values, except return False if a contradiction is detected.
    # @param values: initial dic
    # @param s: square
    # @param d: digit
    # @return dict: return cleaned values.
    def eliminate(self, values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    ## Using depth-first search and propagation, try all possible values.
    # @param values: updates possible values dict.
    # @return dict: updates possible values dict after search algorithm.
    def search(self, values):
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.squares):
            return values
        n,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d))
                    for d in values[s])
    ##
    # Return some element of seq that is true.
    # @param seq: values dict.
    # @return boolean: return the element that is true.
    def some(self, seq):
        for e in seq:
            if e: return e
        return False
    ##
    # Solve the sudoku , returns False if the sudoku was invalid.
    # @param grid: initial grid to solve.
    def solve(self, grid): return self.search(self.parse_grid(grid))


if __name__ == '__main__':
    hard1 = "3...8.......7....51..............36...2..4....7...........6.13..452...........8.."
    peter = PerterNorvig()
    solved = peter.solve(hard1)
    print(solved)