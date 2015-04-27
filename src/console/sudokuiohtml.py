import sys

sys.path.append("../../sudoku2015-B")

import unittest

from src.console.sudokuio import SudokuIO

class SudokuIOHtml(SudokuIO):
    def __init__(self, file_path):
        super(SudokuIOHtml, self).__init__(file_path)
        self.string_html = self.create_header()

    def create_header(self):
        string_html = '<html>\n<head>\n' \
            '<style>\n.middle_line_row{\nborder-top-style: dotted;\nborder-top-width: 3px;\n' \
            'border-left-color: green;\n}\n.middle_line_col{\nborder-left-style: dotted;\n' \
            'border-left-width: 3px;\nborder-left-color: green;\n}\n</style>\n'\
            '<h2>Sudoku Exported Grid:</h2>\n</head>\n'
        return string_html

    def convert_grid_to_string(self, grid):
        self.string_html = self.string_html + '<body>\n<table border=\"0\">\n'
        for row in range(len(grid)):
            self.string_html = self.fill_rows(grid, row, self.string_html)
        self.string_html = self.string_html + '</table>\n</body>\n</html>\n'
        return self.string_html


    def fill_rows(self, grid, row, string_html):
        if (row % 3 == 0):
            string_html = string_html + '<tr class=\'middle_line_row\'>\n'
        else:
            string_html = string_html + '<tr>\n'
        for col in range (len(grid[row])):
            if (col == len(grid[row])-1):
                string_html = string_html + '<td>' + str(grid[row][col]) + '</td>\n</tr>\n'
            elif (col % 3 == 0) and (col >= 1):
                string_html = string_html + '<td class=\'middle_line_col\'>' + str(grid[row][col]) + '</td>\n'
            else:
                string_html = string_html + '<td>' + str(grid[row][col]) + '</td>\n'
        return string_html
