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

    def cross(self, row_key_list, column_key_list):
        """
        Cross product of elements in row_key_list and elements in column_key_list.

        Keyword arguments:
        row_key_list -- Mostly this will be the row values. i.e  1, 2, 3,etc
        column_key_list -- Mostly this will be the column values. i.e A, B ,C, etc
        returns list with the filled keys crossed that will be used as
                coordinates, i.e.  [1A, 2A ].
        """

        return [key + value for key in row_key_list for value in column_key_list]

    def parse_grid(self, grid):
        """
        Converts grid game string into a dictionary of possible values,
        {square: digits}, or return False if a contradiction is detected.

        Keyword arguments:
        grid -- String that contains the sudoku game, i.e:
                3000800000007000051000000000000003600020 .......
        returns a dictionary with all the possible values per square. i.e:
               {'I6': '1379', 'H9': '679', 'I2': '12369' ........
        """

        values = dict((square, self.digits) for square in self.squares)
        for (square, digit) in list(self.create_game_dict(grid).items()):
            if digit in self.digits and not self.assign(values, square,
                    digit):
                return False
        return values

    def create_game_dict(self, grid):
        """
        Convert grid game in string format into a dictionary  of {square: char}
        with '0' for empties.

        Keyword arguments:
        grid -- String that contains the sudoku game, i.e:
                3000800000007000051000000000000003600020 .......
        returns grid dict with filled values ready to play, i.e :
                {'A1': '3', 'A2': '0', 'A3': '0' ........
        """

        chars = [colum for colum in grid if colum in self.digits
                 or colum in '0']
        assert len(chars) == 81
        return dict(list(zip(self.squares, chars)))

    def assign(self, values, square, digit):
        """
        Eliminate the list of "other_values"(possible solutions per square)
        except the sent digit from values[square] and then propagate.

        Keyword arguments:
        values -- Initial dictionary with values, i.e: {'I6': '7', 'H9': '9',...
        square -- String key that correspond to the square position, i.e: I6
        digit -- Selected digit value to eliminate, i.e: 7
        returns updated solution dict(i.e: {'E1': '135678', 'H7': '123679' ...)
                or False if a contradiction is detected.
        """

        other_values = values[square].replace(digit, '')
        if all(self.eliminate(values, square, temp_digit) for temp_digit in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, digit):
        """
        Eliminate 'digit' from values[square]. Propagate when values or places <= 2.

        Keyword arguments:
        values -- Initial dictionary with values, i.e: {'I6': '7', 'H9': '9',...
        square -- String key that correspond to the square position, i.e: I6
        digit -- Selected digit value to eliminate, i.e: 7
        returns updated solution dict(i.e: {'E1': '135678', 'H7': '123679' ...)
                or False if a contradiction is detected.
        """
        if digit not in values[square]:
            return values
        values[square] = values[square].replace(digit, '')
        if len(values[square]) == 0:
            return False
        elif len(values[square]) == 1:
            temp_digit = values[square]
            updated_values = (self.eliminate(values, temp_square, temp_digit) for temp_square in self.peers[square])
            if not all(updated_values):
                return False
        for unit in self.units[square]:
            #Keys for the sent digit.
            digit_places = [square for square in unit if digit in values[square]]
            if len(digit_places) == 0:
                return False
            elif len(digit_places) == 1 and not self.assign(values,
                    digit_places[0], digit):
                return False
        return values

    def search(self, values):
        """
        Using depth-first recursive search and propagation,
        try all possible values in the square before try the next one.

        Keyword arguments:
        values -- dictionary of possible values {square: digits}, i.e:
                {'I6': '1379', 'H9': '679', 'I2': '12369' ........
        returns updated dictionary with final values after search algorithm.
                {'I6': '1', 'H9': '6', 'I2': '2' ........
        """

        if values is False:
            return False
        if all(len(values[square]) == 1 for square in self.squares):
            return values
        (unfilled, square) = min((len(values[square]), square)
                                 for square in self.squares
                                 if len(values[square]) > 1)
        return self.get_true_element_from_sequence(
               self.search(self.assign(values.copy(),square, digit)) for digit in values[square])

    def get_true_element_from_sequence(self, sequence):
        """
        returns the element from the generator sequence that has a value ,
        the dictionary with solved values.

        Keyword arguments:
        sequence -- values dictionary.
        """
        print("SEQ",list(sequence))
        for element in sequence:
            if element:
                return element
        return False

    def solve(self, grid):
        """
        Solve the sudoku , returns False if the sudoku was invalid.

        Keyword arguments:
        grid -- Initial sudoku to solve grid in string format,
                i.e: 3000800000007000051000000000000003600020 .......
        returns the final dictionary with values of the solved sudoku
        after apply the search algorithm recursively , i.e:
                {'I6': '1', 'H9': '6', 'I2': '2' ........
        """
        return self.search(self.parse_grid(grid))