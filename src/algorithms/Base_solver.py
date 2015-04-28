import sys
sys.path.append('../../sudoku2015-B')
from src.utils.Algorithm_helper import AlgorithmHelper

class BaseSolver():

    @get_solve_time
    def solve(self, grid_game):
        """
        Generic method that solves a sudoku game.

        Keyword arguments:
        grid_game -- Sudolu game(81 chars) in string format, i.e: 300080000200...
        Returns a list[9][9] that contains the solved game.
        """
        raise NotImplementedError("Solve method was not implemented.")

