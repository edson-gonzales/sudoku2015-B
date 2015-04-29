import random
import sys
sys.path.append("../algorithms")
from Brute_Force import BruteForce


class SudokuGenerator(object):
        """Generates a sudoku game depends of the complexity level sent"""
        def __init__(self):
            # EMPTY_SUDOKU - string, is the empty sudoku going to send to
            self.EMPTY_SUDOKU = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
            self.SUDOKU_DIFFICULT_EASY = 3
            self.SUDOKU_DIFFICULT_MEDIUM = 5
            self.SUDOKU_DIFFICULT_HARD = 6
            self.SUDOKU_DIFFICULT_DEFAULT = 5

        def generate_random_list(self, number, list):
            """
            Generates a random list to mask cells and display zero instead of
            cell's solution.

            number - int, number of cells per row to be maintained and not
            modified.
            list - int, list to modify with zero.
            Return - list numbers
            """
            index = random.randint(0, len(list) - 1)
            result = [list.pop(index)]
            if(number > 1):
                result.extend(self.generate_random_list(number - 1, list))

            return result

        def get_minimum_replaced_cells_with_zero(self, difficult):
            """
            Gets the minimum number of cells going to be replaced by Zero in a
            Sudoku grid.
            difficult - string, sudoku's difficult sent (Example: easy, medium,
            and hard)
            Return - returns the minimum cant of cells going to be masked and
            displayed as zero
            """
            minimum_replaced_cells_with_zero = self.SUDOKU_DIFFICULT_DEFAULT

            if difficult == "easy":
                minimum_replaced_cells_with_zero = self.SUDOKU_DIFFICULT_EASY
            elif difficult == "medium":
                minimum_replaced_cells_with_zero = self.SUDOKU_DIFFICULT_MEDIUM
            elif difficult == "hard":
                minimum_replaced_cells_with_zero = self.SUDOKU_DIFFICULT_HARD

            return minimum_replaced_cells_with_zero

        def mask(self, sudoku, difficult):
            """
            Iterates within the sudoku grid to mask required values defined by
            difficult.

            sudoku - grid of integer, grid already solved to iterate in order to
            mask sudoku cells with zero value
            difficult - string, sudoku's difficult sent by
            Return - grid, sudoku masked
            """
            for rowNum in range(9):
                row = sudoku[rowNum]
                offset = random.randint(0, 1)
                maskIndices = self.generate_random_list(self.get_minimum_replaced_cells_with_zero(difficult) + offset, range(9))
                for index in maskIndices:
                    row[index] = 0
            return sudoku

        def generate_sudoku(self, difficult):
            """
            Uses the Brute Force algoritm to solve an empty suudoku, then uses
            that solved Sudoku  to replace some cells on it with zero values
            depending of the difficult sent.
            Return - grid of integer, sudoku masked.
            """
            brute_force = BruteForce()
            solution = brute_force.solve(self.EMPTY_SUDOKU)
            return self.mask(solution, difficult)