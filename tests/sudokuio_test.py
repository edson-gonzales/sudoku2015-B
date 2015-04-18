import sys

sys.path.append("../../sudoku2015-B")

import unittest

from src.console.sudokuio import SudokuIO

class SudokuIOTest(unittest.TestCase):
    
    def test_write_text_in_file(self):
        text = 'test text'
        file_path = './test.txt'
        file_io = SudokuIO(file_path)
        file_io.write(text)
        self.assertEqual(text,file_io.read_all());

if __name__ == '__main__':
    unittest.main()