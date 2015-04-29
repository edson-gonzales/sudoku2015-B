import sys

sys.path.append("../src/console")

import unittest

from sudokuiocsv import SudokuIOCsv

class SudokuIOCsvTest(unittest.TestCase):
	def test_write_sudoku_in_file(self):
		file_path = './test.txt'
     	file_io = SudokuIOCsv(file_path)
     	grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]
        file_io.write_sudoku_in_file(grid)
        grid_string = SudokuIO.format_grid_to_string(grid)
        self.assertEqual(grid_string,file_io.read_all())
        file_io.delete_content()

	def test_write_a_3x3_game(self):
		file_path = './test.txt'
        grid = [
            [1,2,3],
            [2,1,3],
            [3,2,1]
            ]
        file_io = SudokuIOCsv(file_path)
        file_io.write_sudoku_in_file(grid)
        grid_string = SudokuIO.format_grid_to_string(grid)
        self.assertEqual(grid_string,file_io.read_all())
        file_io.delete_content()