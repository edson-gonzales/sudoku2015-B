import random
import sys
sys.path.append("../algorithms")
from Brute_Force import BruteForce


class SudokuGenerator(object):
	"""Generates a sudoku game depends of the complexity level sent"""
	def __init__(self):		
		# EMPTY_SUDOKU - string, is the empty sudoku going to send to 
		self.EMPTY_SUDOKU = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
	
	def generate_random_list(self, number, list):
		"""
		Generates a random list to mask cells and display zero instead of cell's 
		solution.

		number - int, number of cells per row to be maintained and not modified.
		list - int, list to modify with zero.
		Return - list numbers
		"""
		index = random.randint(0, len(list) - 1)
		result = [list.pop(index)]
		if(number > 1):
			result.extend(self.generate_random_list(number - 1, list))
		
		return result

	def get_minimum_replaced_cells_with_zero(self, dificult):
		"""
		Gets the minimum number of cells going to be replaced by Zero in a 
		Sudoku grid.

		dificult - string, sudoku's dificult sent
		Return - returns the minimum cant of cells going to be masked and
		displayed as zero
		"""
		minimum_replaced_cells_with_zero = 5
		
		if dificult == "easy":
		    minimum_replaced_cells_with_zero = 3
		elif dificult == "medium":
		    minimum_replaced_cells_with_zero = 5
		elif dificult == "hard":
		    minimum_replaced_cells_with_zero = 6
		
		return minimum_replaced_cells_with_zero

	def mask(self, sudoku, dificult):
		"""
		Iterates within the sudoku grid to mask required values defined by dificult.

		sudoku - grid of integer, grid already solved to iterate in order to 
		mask sudoku cells with zero value
		Return - grid, sudoku masked
		"""
		for rowNum in range(9):
			row = sudoku[rowNum]
			offset = random.randint(0, 1)
			maskIndices = self.generate_random_list(self.get_minimum_populates_cell_per_row(dificult) + offset, range(9))
			#maskIndices = self.generateRandomList(1 + offset, range(9))
			for index in maskIndices:
				row[index] = 0
		return sudoku

	def generate_sudoku(self, dificult):
		"""
		Uses the Brute Force algoritm to solve an empty suudoku, then uses that 
		solved Sudoku  to replace some cells on it with zero values depending of 
		the dificult sent.

		Return - grid of integer, sudoku masked.
		"""
		brute_force = BruteForce()
		solution = brute_force.solve(self.EMPTY_SUDOKU)
		return self.mask(solution, dificult)

