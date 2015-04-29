import sys
sys.path.append('../util')
from Algorithm_helper import get_solve_time
from Peter_Norvig import PeterNorvig
from Backtracking import Backtracking
from Brute_Force import BruteForce


class AlgorithmInterface(object):

    def __init__(self,algorithm):
        self.algorithm = algorithm

    @get_solve_time
    def solve(self, sudoku_game):
        self.algorithm.solve(sudoku_game)

    def change_algorithm(self, new_algorithm):
        self.algorithm = new_algorithm
