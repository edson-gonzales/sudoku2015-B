
class Backtracking(object):
	def __init__(self,grid):
		self.grid = grid
		self.UNASSIGNED = 0
	##
	# Function that returns the possition of a cell with the value self.UNASSIGNED
	# @param grid[9][9]: the grid with the current sudoku values.
	# @param row: row number in the grid.
	# @param col: column number in the grid.
	# @return array[2]: position with the UNASSIGNED value or None in the case that the grid is already filled.
	def find_unassigned_location(self,grid,row,col):
	 	for row in range(len(grid)):
	 		for col in range(len(grid[row])):
	 			if grid[row][col] == self.UNASSIGNED:
	 				return [row,col]
	 	return None
	##
	# Function that returns a boolean value when the *num* provided is repeated in the row.
	# @param grid[9][9]: the grid with the current sudoku values.
	# @param row: row number in the grid.
	# @param num: number to eval in the row.
	# @return boolean: return True when is already used in the row or False when is not used.
	def used_in_row(self, grid, row, num):
	 	for col in range(len(grid[row])):
	 		if grid[row][col] == num:
	 			return True;
	 	return False
	
	##
	# Function that returns a boolean value when the *num* provided is repeated in the column.
	# @param grid[9][9]: the grid with the current sudoku values.
	# @param col: column number in the grid.
	# @param num: number to eval in the col.
	# @return boolean: return True when is already used in the column or False when is not used.
	def used_in_col(self, grid, col, num):
	 	for row in range(len(grid)):
	 		if grid[row][col] == num:
	 			return True;
	 	return False
	
	##
	# Function that returns a boolean value when the *num* provided is repeated in a box 3x3.
	# @param grid[9][9]: the grid with the current sudoku values.
	# @param box_start_row: row number in the grid where the box 3x3 starts.
	# @param box_start_col: column number in the grid where the box 3x3 starts
	# @param num: number to eval in the box.
	# @return boolean: return True when is already used in the box3x3 or False when is not used.
	def used_in_box(self, grid, box_start_row,box_start_col, num):
	 	for row in range(3):
	 		for col in range(3):
	 			if grid[row+box_start_row][col+box_start_col] == num:
	 				return True
	 	return False 

	##
	# Function that eval a number *num* provided whether this is valid or not in the provided *position [row,col]*.
	# @param grid[9][9]: the grid with the current sudoku values.
	# @param row: row number in the grid.
	# @param col: column number in the grid.
	# @param num: number to eval in the sudoku grid.
	# @return boolean: return True when the number is valid or False in other case
	def is_safe(self, grid, row, col, num):
	 	return not self.used_in_row(grid,row,num) and not self.used_in_col(grid,col,num) and not self.used_in_box(grid,row-row%3, col-col%3,num)


	##
	# Function that print the sudoku grid.
	# @param grid[9][9]: the grid with the current sudoku values.
	def print_grid(self, grid):
	 	for row in range(len(grid)):
	 		print(''.join(str(x) for x in grid[row]))

	##
	# Function that solve a sudoku game with the backtracking algorithm
	# @param grid[9][9]: the grid with the current sudoku values.
	# @return boolean: return True the Grid was solved and False when there is not solution.
	def solve(self,grid):
		row = 0
		col = 0
		position = self.find_unassigned_location(grid,row,col)
		if (position is None):
			return True
		row = position[0]
		col = position[1]
		for number in range(1,10):
			# print the numbers by empty cell print("("+str(row)+","+str(col)+") number"+str(number))
			if (self.is_safe(grid,row,col,number)):
				grid[row][col] = number
				if(self.solve(grid)):
					return True
				grid[row][col] = self.UNASSIGNED;
	 	return False