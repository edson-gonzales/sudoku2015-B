from string import maketrans

class Backtracking(object):
	def __init__(self):
		self.UNASSIGNED = 0
		self.DIMENSION = 9

	def find_unassigned_location(self, grid, row, col):
		""" Function that returns the possition of a cell with the value 
		self.UNASSIGNED

		int[9][9] grid -- the grid with the current sudoku values.
		int row -- row number in the grid.
		int col -- column number in the grid.
		return array[2]: position with the UNASSIGNED value or None in the case that
			the grid is already filled.
		"""

	 	for row in range(len(grid)):
	 		position = self.find_unassigned_cell_by_row(grid, row, col)
	 		if position is not None:
	 		 	return position
	 	return None

	def find_unassigned_cell_by_row(self, grid, row, col):
		""" This method return the cell that is unfilled by a row.

		int[9][9] grid -- the grid with the current sudoku game.
		int row -- The current row to check the self.UNASSIGNED position
		int col -- The current col to check the self.UNASSIGNED position
		"""
		for col in range(len(grid[row])):
	 		if grid[row][col] == self.UNASSIGNED:
	 			return [row,col]
	 	return None
		
	def is_used_in_row(self, grid, row, num):
		"""Function that returns a boolean value when the *num* provided is repeated
		in the row.

		int[9][9] grid -- the grid with the current sudoku values.
		int row -- row number in the grid.
		int num -- number to eval in the row.
		return boolean -- return True when is already used in the row or False when
			is not used.	
		"""
	 	for col in range(len(grid[row])):
	 		if grid[row][col] == num:
	 			return True;
	 	return False
	
	def is_used_in_col(self, grid, col, num):
		""" Function that returns a boolean value when the *num* provided is
		repeated in the column.

		int[9][9] grid -- the grid with the current sudoku values.
		int col -- column number in the grid.
		int num -- number to eval in the col.
		return boolean -- return True when is already used in the column or False 
			when is not used.
		"""
	 	for row in range(len(grid)):
	 		if grid[row][col] == num:
	 			return True;
	 	return False
	
	def is_used_in_box(self, grid, box_start_row, box_start_col, num):
		""" Function that returns a boolean value when the *num* provided is 
		repeated in a box 3x3.

		int[9][9] grid -- the grid with the current sudoku values.
		int box_start_row -- row number in the grid where the box 3x3 starts.
		int box_start_col -- column number in the grid where the box 3x3 starts
		int num -- number to eval in the box.
		return boolean -- return True when is already used in the box3x3 or False
			when is not used.
		"""
	 	for row in range(3):
	 		used = self.is_used_in_row_of_box(grid, row, box_start_row, box_start_col, num)
	 		if used:
	 			return True
	 	return False 

	def is_used_in_row_of_box(self, grid, row, box_start_row, box_start_col, num):
		""" This method return a boolean that means if the 'num' number is already 
		used in the row of a box.

		int[9][9] grid -- the grid with the current sudoku values.
		int row -- The current row of the box where to check the number.
		int box_start_row -- row number in the grid where the box 3x3 starts.
		int box_start_col -- column number in the grid where the box 3x3 starts
		int num -- number to eval in the box.
		return boolean -- return True when is already used in the row of a box3x3 or False
			when is not used.
		"""
		for col in range(3):
	 		if grid[row + box_start_row][col + box_start_col] == num:
	 			return True
	 	return False

	def is_safe(self, grid, row, col, num):
		""" Function that eval a number *num* provided whether this is valid or not 
		in the provided *position [row,col]*.

		Keyword arguments
		int[9][9] grid-- the grid with the current sudoku values.
		int row -- row number in the grid.
		int col -- column number in the grid.
		int num -- number to eval in the sudoku grid.
		return boolean -- return True when the number is valid or False in other case
		"""
	 	return  (not self.is_used_in_row(grid,row,num) 
	 			and not self.is_used_in_col(grid, col, num) 
	 			and not self.is_used_in_box(grid, row - row % 3, col - col % 3, num))

	def solve_backtraking(self, grid):
		""" Function that solve a sudoku game with the backtracking algorithm
		int[9][9] grid -- the grid with the current sudoku values.
		return boolean -- return True the Grid was solved and False when there is 
			not solution.
		"""
		row = 0
		col = 0
		position = self.find_unassigned_location(grid, row, col)
		if (position is None):
			return True
		row = position[0]
		col = position[1]
		for number in range(1,10):
			filled = self.fill_cells(grid, row, col, number)
			if filled:
				return True
	 	return False

	def fill_cells(self, grid, row, col, number):
		""" This method fill a cell from the 'grid' in the position [row,col] with
		the 'number' number if the number accomplish the rules in the position and
		call to solve_backtraking in order to fill the remaining cells.

		int[9][9] grid -- the grid with the current sudoku values.
		int row --  the current start row position of the cell.
		int col -- the current start column position of the cell.
		int number -- the current start number to fill in the cell.
		return boolean -- return True the Grid was solved and False when there is 
			not solution.
		"""
		if (self.is_safe(grid, row, col, number)):
			grid[row][col] = number
			if(self.solve_backtraking(grid)):
				return True
			grid[row][col] = self.UNASSIGNED


	def convert_to_grid(self, grid_string):
		""" Function that convert the provided string to a grid 9x9

		string grid_string -- the string to convert
		return int[9][9] -- a grid 9x9
		"""
		convert_dot_to_zero = maketrans('.', '0')
		grid_string = str(grid_string).translate(convert_dot_to_zero)
		list_of_numbers = [int(n) for n in grid_string]
		grid = [[0] * self.DIMENSION] * self.DIMENSION
		for row in range(self.DIMENSION):
			grid[row] = list_of_numbers[row * self.DIMENSION : ( row + 1 ) * self.DIMENSION]
		return grid


	def solve(self, grid_string):
		""" Function that return a grid 9x9 with the sudoku game solved if this can
		be solved or return none in other case.

		string grid_string -- the string that contains the sudoku game in the format 
		"x....xx............xx....x...xxx.......x....xxx..x.x..x.....xxx.......xx........."
		"""
		grid = self.convert_to_grid(grid_string)
	 	if (self.solve_backtraking(grid)):
	 		return grid
	 	else:
	 		return None
