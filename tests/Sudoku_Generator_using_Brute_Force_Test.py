import unittest, sys
sys.path.append("../src/util")

from Brute_Force import BruteForce

class TestBruteForceAlgorithm(unittest.TestCase):    
	generator = SudokuGenerator()

    def test_easy_sudoku_can_be_generated(self):
    	dificult = "easy"
    	sudoku = generator.generate_sudoku(dificult)
    	self.assertNotNone(sudoku)

	def test_medium_sudoku_can_be_generated(self):
    	dificult = "medium"
    	sudoku = generator.generate_sudoku(dificult)
    	self.assertNotNone(sudoku)

    def test_hard_sudoku_can_be_generated(self):
    	dificult = "hard"
    	sudoku = generator.generate_sudoku(dificult)
    	self.assertNotNone(sudoku)

if __name__ == '__main__':
    unittest.main()