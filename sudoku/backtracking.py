class Backtracking:

	def __init__(self,grid):
		self.grid = grid

	def solve(self,grid):
		if(not find_unassigned_location(grid,row,col)):
			return True
		for number in range(1,9):
			if (isSafe(grid,row,col,number)):
				grid[row][col] = number
				if(solve(grid)):
					return True
				grid[row][col] = 'UNASSIGNED';
	 	return False


	def find_unassigned_location(self,grid,row,col):
	 	for row in range(8):
	 		for col in range(8):
	 			if grid[row][col] == 'UNASSIGNED':
	 				return True
	 	return False

	def used_in_row(self, grid, row, num):
	 	for col in range(8):
	 		if grid[row][col] == num:
	 			return True;
	 	return False

	def used_in_col(self, grid, col, num):
	 	for row in range(8):
	 		if grid[row][col] == num:
	 			return True;
	 	return False

	def used_in_box(self, grid, box_start_row,box_start_col, num):
	 	for row in range(3):
	 		for col in range(3):
	 			if grid[row+box_start_row][col+box_start_col] == num:
	 				return True
	 	return False 

	def is_safe(self, grid, row, col, num):
	 	return not used_in_row(grid,row,col,num) and not used_in_col(grid,row,col,num) and not used_in_box(grid,row-row%3, col-col%3,num)

	def print_grid(self, grid):
	 	for row in range(8):
	 		for col in range(8):
	 			print("%2d" + grid[row][col])
	 			print("\n")



grid = [[3,0,6,5,0,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[0,0,3,0,1,0,0,8,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[1,3,0,0,0,0,2,5,0],[0,0,0,0,0,0,0,7,4],[0,0,5,2,0,6,3,0,0]]
sudoku = Backtracking(grid)
if sudoku.solve(grid) == True:
	sudoku.print_grid(grid)
else:
	print("Don't exist a solution")