import unittest, sys
sys.path.append("../src/algorithms")

from Brute_Force import BruteForce

class TestBruteForceAlgorithm(unittest.TestCase):
    solver = BruteForce()
    sudoku_to_solve = '530070000600195000098000060800060003400803001700020006060000280000419000000080070'
    sudoku_solved = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    sudoku_emty = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def test_sudoku_solution_is_correct_one(self):
      self.assertEquals(self.sudoku_solved, self.solver.solve(self.sudoku_to_solve))

    def test_sudoku_solution_is_not_empty(self):
      self.assertIsNotNone(self.solver.solve(self.sudoku_to_solve))

    def test_sudoku_solution_is_a_matrix_of_numbers(self):
      sudoku_solved = [['A', 'A', 'A', 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 'B', 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]

      self.assertNotEqual(sudoku_solved, self.solver.solve(self.sudoku_to_solve))

    def test_sudoku_is_solved_when_given_sudoku_has_zero_in_each_cell(self):
      self.assertNotEqual(self.sudoku_emty, self.solver.solve(self.sudoku_to_solve))

    def test_sudoku_returns_empty_grid_when_given_sudoku_is_not_resolvable(self):
      sudoku_with_more_rows = '5300700006001999500009800006080006000340080300170002000606000028000041900000008007'
      self.assertEqual(self.sudoku_emty, self.solver.solve(sudoku_with_more_rows))

    def test_easy_sudoku_is_solved_correctly(self):      
      sudoku_easy_to_solve = '534678912600195000098000060800060003426853001700020006060000280000419000000086179'
      self.assertEqual(self.sudoku_solved, self.solver.solve(sudoku_easy_to_solve))

if __name__ == '__main__':
    unittest.main()