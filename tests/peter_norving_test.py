import sys
sys.path.append("../../sudoku2015-B")

import unittest
from src.algorithms.peter_norving import PeterNorvig

class PeterNorvingTest(unittest.TestCase):

    def setUp(self):
        self.valid_test_game = '300080000000700005100000000000000360002004000070000000000060130045200000000000800'
        self.invalid_test_game = '333380000000700005100000000000000360002004000070000000000060130045200000000000800'
        self.valid_test_game_solved = {'H8': '9', 'I8': '5', 'C1': '1', 'I6': '9', 'G9': '4', \
                                       'H7': '7', 'E1': '9', 'C9': '3', 'B8': '1', 'D9': '9', \
                                       'F4': '3', 'D1': '4', 'H5': '3', 'F5': '9', 'D4': '5', \
                                       'C3': '7', 'D5': '2', 'A2': '5', 'B1': '2', 'D6': '7', \
                                       'F2': '7', 'I5': '7', 'E7': '5', 'G2': '2', 'B9': '5', \
                                       'I9': '2', 'G7': '1', 'A6': '6', 'A8': '2', 'H2': '4', \
                                       'C7': '4', 'C2': '6', 'F7': '2', 'G3': '9', 'D3': '1', \
                                       'E4': '6', 'E2': '3', 'H9': '6', 'C4': '9', 'A5': '8', \
                                       'E8': '7', 'H4': '2', 'C6': '2', 'I2': '1', 'F8': '4', \
                                       'B6': '3', 'I7': '8', 'B4': '7', 'I1': '6', 'E6': '4', \
                                       'F6': '8', 'D7': '3', 'E3': '2', 'B3': '8', 'C5': '5', \
                                       'A4': '1', 'A9': '7', 'G8': '3', 'E5': '1', 'C8': '8', \
                                       'D2': '8', 'H6': '1', 'F1': '5', 'D8': '6', 'I3': '3', \
                                       'A1': '3', 'F3': '6', 'E9': '8', 'F9': '1', 'A7': '9', \
                                       'G4': '8', 'B5': '4', 'H3': '5', 'I4': '4', 'H1': '8', \
                                       'B7': '6', 'G1': '7', 'G6': '5', 'A3': '4', 'B2': '9', 'G5': '6'}
        self.invalid_test_game_length = '333380000000700005100000000000000360002004000070000000000060130045200000000000800123'
        self.invalid_input_data = '!@#!@#$%^&*(700005100000000000000360002004000070000000000060130045200000000000800'
        self.peter_norving_test = PeterNorvig()
        self.expected_length = 81

    def test_a_valid_sudoku_game_is_solved_correctly(self):
        self.assertEqual(self.peter_norving_test.solve(self.valid_test_game), self.valid_test_game_solved)

    def test_invalid_sudoku_game_returns_false(self):
        self.assertFalse(self.peter_norving_test.solve(self.invalid_test_game))

    def test_invalid_input_data_generates_an_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.peter_norving_test.solve(self.peter_norving_test.solve(self.invalid_input_data))

    def test_cross_result_contains_elements_from_both_lists(self):

        list_a = '12'
        list_b = 'AB'
        list_cross = self.peter_norving_test.cross(list_a, list_b)
        self.assertTrue(list_cross[0] == (list_a[0] + list_b[0]))

    def test_all_possible_values_are_generated_for_a_square(self):
        test_game_key = 'D9'
        test_game_values = self.peter_norving_test.parse_grid(self.valid_test_game)
        expected_possible_values = '124789'
        self.assertEqual(test_game_values.get(test_game_key), expected_possible_values)

    def test_values_are_not_generated_for_invalid_sudoku_game(self):
        test_game_values = self.peter_norving_test.parse_grid(self.invalid_test_game)
        self.assertFalse(test_game_values)

    def test_valid_length_game_generates_the_values_dictionarie(self):
        actual_values_legth = len(self.peter_norving_test.grid_values(self.valid_test_game))
        self.assertEqual(actual_values_legth, self.expected_length)

    def test_invalid_length_game_generates_an_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.peter_norving_test.grid_values(self.invalid_test_game_length)

if __name__ == '__main__':
    unittest.main()


