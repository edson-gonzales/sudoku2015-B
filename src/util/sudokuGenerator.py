import random
import sys
sys.path.append("../algorithms")
from Brute_Force import BruteForce


class SudokuGenerator(object):
	"""Generates a sudoku game depends of the complexity level"""
	def __init__(self, dificult):
		"""
		dificult - string, value to define the sudoku's dificult. Posible values:		
		"""
		self.dificult = dificult
		# EMPTY_SUDOKU - string, is the empty sudoku going to send to 
		self.EMPTY_SUDOKU = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
	
	def generateRandomList(self, number, list):
		"""
		Generates a random list to mask index.

		number - int, number of cels per row to be maintained and not modified.
		list - int, list to modify with zero.
		Return - list numbers
		"""
		index = random.randint(0, len(list) - 1)
		result = [list.pop(index)]
		if(number > 1):
			result.extend(self.generateRandomList(number - 1, list))
		return result

	def get_sudoku_dificult(self):
		dificult_sent = self.dificult
		dificult = 0
		print dificult

		while switch(dificult_sent):
			if case('easy'):
		        dificult = 1
		        break
		    if case('medium'):
		        dificult = 2
		        break
		    if case('hard'):
		        dificult = 3
		        break
		    print "Not allowed dificult"		    
		    break
		return dificult

	def mask(self, sudoku):
		"""
		Iterates within the sudoku to mask required values defined by dificult 

		sudoku - grid of integer, grid already solved to iterate in order to 
		mask sudoku cells with zero value
		Return - grid, sudoku masked
		"""
		for rowNum in range(9):
			row = sudoku[rowNum]
			offset = random.randint(0, 1)
			maskIndices = self.generateRandomList(7 + offset, range(9))
			for index in maskIndices:
				row[index] = 0
		return sudoku

	def generate_sudoku(self):
		"""
		Uses the Brute Force algoritm to solve an empty suudoku.

		Return - grid of integer, sudoku masked.
		"""
		brute_force = BruteForce()
		solution = brute_force.solve(self.EMPTY_SUDOKU)
		return self.mask(solution)

if __name__ == '__main__':
	generator = SudokuGenerator()
	sudoku = generator.generate_sudoku('easy')
	print sudoku

	for x in sudoku:
		pass
	list1 = ['1','2','3']
	string = " ".join(list1)
	print list1
	print string