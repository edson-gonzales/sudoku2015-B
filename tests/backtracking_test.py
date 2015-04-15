import sys

sys.path.append("../../sudoku2015-B")

import unittest


from src.algorithms.backtracking import Backtracking

class BacktrackingTest(unittest.TestCase):

    def test_return_none_for_find_unassigned_location_of_a_3x3_grip_when_all_are_full(self):
        grid = [[1,2,3],[2,3,1],[3,1,2]]
        backtracking = Backtracking()
        self.assertIsNone(backtracking.find_unassigned_location(grid,0,0))  
    def test_return_position_for_find_unassigned_location_of_a_3x3_grip_when_there_is_a_blank(self):
        grid = [[1,2,3],[2,3,0],[3,1,2]]
        backtracking = Backtracking()
        self.assertEqual([1,2],backtracking.find_unassigned_location(grid,0,0)) 
    def test_return_position_for_find_unassigned_location_of_a_3x3_grip_when_there_is_a_blank_at_the_end(self):
        grid = [[1,2,3],[2,3,1],[3,1,0]]
        backtracking = Backtracking()
        self.assertEqual([2,2],backtracking.find_unassigned_location(grid,0,0))
    def test_return_position_for_find_unassigned_location_of_a_3x3_grip_when_there_is_more_than_one_blank(self):
        grid = [[1,2,0],[2,0,1],[3,0,2]]
        backtracking = Backtracking()
        self.assertEqual([0,2],backtracking.find_unassigned_location(grid,0,0))

    def test_return_true_when_a_number_is_used_in_a_row(self):
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
        backtracking = Backtracking()
        self.assertTrue(backtracking.is_used_in_row(grid,0,9))
    def test_return_true_when_a_number_is_used_in_the_last_row(self):
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
        backtracking = Backtracking()
        self.assertTrue(backtracking.is_used_in_row(grid,8,3))
    def test_return_false_when_a_number_is_not_used_in_a_row(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,0,0],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]
        backtracking = Backtracking()
        self.assertFalse(backtracking.is_used_in_row(grid,1,8))
    def test_return_false_when_a_number_is_not_used_in_the_last_row(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,0,0,9]
            ]
        backtracking = Backtracking()
        self.assertFalse(backtracking.is_used_in_row(grid,8,3))

    def test_return_true_when_a_number_is_used_in_a_col(self):
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
        backtracking = Backtracking()
        self.assertTrue(backtracking.is_used_in_col(grid,0,9))
    def test_return_true_when_a_number_is_used_in_the_last_col(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,0],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,0],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]
        backtracking = Backtracking()
        self.assertTrue(backtracking.is_used_in_col(grid,8,3))
    def test_return_false_when_a_number_is_not_used_in_a_col(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,0,0],
            [4,0,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]
        backtracking = Backtracking()
        self.assertFalse(backtracking.is_used_in_col(grid,1,8))
    def test_return_false_when_a_number_is_not_used_in_the_last_col(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,0],
            [1,3,8,9,4,7,2,5,0],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,0,0,9]
            ]
        backtracking = Backtracking()
        self.assertFalse(backtracking.is_used_in_col(grid,8,3))

    def test_return_true_when_a_number_is_used_in_a_box(self):
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
        backtracking = Backtracking()
        self.assertTrue(backtracking.is_used_in_box(grid,6,3,1))
    def test_return_false_when_a_number_is_not_used_in_a_box(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,0,0],
            [4,0,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,0,6,3,1,9]
            ]
        backtracking = Backtracking()
        self.assertFalse(backtracking.is_used_in_box(grid,6,3,8))
    
    def test_return_true_when_a_number_is_valid_in_a_sudoku_grid_position(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,0,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]
        backtracking = Backtracking()
        self.assertTrue(backtracking.is_safe(grid,5,3,7))
    def test_return_false_when_a_number_is_not_valid_in_a_sudoku_grid_position(self):
        grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,0,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]
        backtracking = Backtracking()
        self.assertFalse(backtracking.is_safe(grid,3,7,3))

    def test_return_grid_solved_when_is_solved_a_valid_sudoku_grid(self):
        grid = "3.65.84..52........87....31..3.1..8.9..863..5.5..9.6..13....25......"\
            "..74..52.63.."

        backtracking = Backtracking()
        self.assertEqual([
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ],backtracking.solve(grid))
    def test_return_None_when_cannot_be_solved_a_sudoku_grid(self):
        grid = "3.65.84..52........87....31..3.1..8.9..863..5.5..9.6..13....25......"\
            "..74..52.6392"
        backtracking = Backtracking()
        self.assertIsNone(backtracking.solve(grid))

if __name__ == '__main__':
    unittest.main()