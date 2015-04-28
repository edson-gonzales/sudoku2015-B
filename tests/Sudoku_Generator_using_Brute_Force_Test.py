import unittest
import sys
sys.path.append("../src/algorithms")
sys.path.append("../src/util")

from Sudoku_Generator import SudokuGenerator


class TestBruteForceAlgorithm(unittest.TestCase):
    generator = SudokuGenerator()

    def test_easy_sudoku_can_be_generated(self):
        difficult = "easy"
        sudoku = self.generator.generate_sudoku(difficult)
        self.assertIsNotNone(sudoku)

    def test_medium_sudoku_can_be_generated(self):
        difficult = "medium"
        sudoku = self.generator.generate_sudoku(difficult)
        self.assertIsNotNone(sudoku)

    def test_hard_sudoku_can_be_generated(self):
        difficult = "hard"
        sudoku = self.generator.generate_sudoku(difficult)
        self.assertIsNotNone(sudoku)

    def test_default_sudoku_is_generated_when_invalid_input_for_difficult(self):
        difficult = "invalid_difficult"
        sudoku = self.generator.generate_sudoku(difficult)
        self.assertIsNotNone(sudoku)


if __name__ == '__main__':
    unittest.main()