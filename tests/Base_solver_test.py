import sys
sys.path.append('../../sudoku2015-B')
import unittest
from src.algorithms.Base_solver import BaseSolver


class BaseSolverTest(unittest.TestCase):

    def test_base_solver_raises_an_exception_when_was_not_implement(self):
        with self.assertRaises(NotImplementedError):
            base_solver = BaseSolver()
            test_string = '30008000000070000510000000000000036000200' \
                      '4000070000000000060130045200000000000800'
            base_solver.solve(test_string)


if __name__ == '__main__':
    unittest.main()