import sys
sys.path.append("../../sudoku2015-B")

import unittest
from src.algorithms.peter_norving import PeterNorvig

class PeterNorvingTest(unittest.TestCase):

    def setUp(self):
        self.valid_test_game = '300080000000700005100000000000000360002004000070000000000060130045200000000000800'
        self.invalid_test_game = '333380000000700005100000000000000360002004000070000000000060130045200000000000800'
        self.invalid_test_game_length = '333380000000700005100000000000000360002004000070000000000060130045200000000000800123'
        self.peter_norving_test = PeterNorvig()

    def test_a_valid_sudoku_game_is_solved_correctly(self):
        print(self.peter_norving_test.solve(self.valid_test_game))

    def test_cross_result_contains_elements_from_both_lists(self):

        list_a = '12'
        list_b = 'AB'
        list_cross = self.peter_norving_test.cross(list_a, list_b)
        self.assertTrue(list_cross[0] == (list_a[0] + list_b[0]))

    def test_all_possible_values_are_generated_for_a_square(self):
        test_game_key = 'D9'
        test_game_values = self.peter_norving_test.parse_grid(self.valid_test_game)
        expected_possible_values = '124789'
        self.assertEquals(test_game_values.get(test_game_key), expected_possible_values)

    def test_values_are_not_generated_for_invalid_sudoku_game(self):
        test_game_values = self.peter_norving_test.parse_grid(self.invalid_test_game)
        self.assertFalse(test_game_values)

    def test_valid_length_game_generates_the_values_dictionarie(self):
        actual_values_legth = len(self.peter_norving_test.grid_values(self.valid_test_game))
        expected_length = 81
        self.assertEquals(actual_values_legth, expected_length)

    def test_invalid_length_game_generates_an_assertion_error(self):
        with self.assertRaises(AssertionError):
            self.peter_norving_test.grid_values(self.invalid_test_game_length)

if __name__ == '__main__':
    unittest.main()


