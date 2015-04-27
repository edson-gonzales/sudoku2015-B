import time


class BaseSolver():

    def solve(self, grid_game):
        """
        Generic method that solves a sudoku game.

        Keyword arguments:
        grid_game -- Sudolu game(81 chars) in string format, i.e: 300080000200...
        Returns a list[9][9] that contains the solved game.
        """
        raise NotImplementedError("Solve method was not implemented.")

    def get_solve_time(func):
        """
        Decorator that calculates the solve time.

        Keyword arguments:
        func -- We will get the execution time of this function.
        """
        def wrapper(*arg):
            start_time = time.clock()
            res = func(*arg)
            solved_time = time.clock() - start_time
            print("Solved in: %2.4f sec" % solved_time)
            return res
        return wrapper

