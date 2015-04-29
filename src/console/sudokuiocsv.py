import sys, csv

sys.path.append("../../")

from src.console.sudokuio import SudokuIO

class SudokuIOCsv(SudokuIO):
	def __init__(self,file_path):
		super(SudokuIOCsv, self).__init__(file_path)
		self.WRITING_MODE = 'wt'
		self.READING_MODE = 'rt'

	def write(self, grid):
		try:
			file = open(file_path,self.WRITING_MODE)
			writer = csv.DictWriter(file)
			for row in range(grid):
				writer.writerow("{0}".format(number) for number in grid[row])
			file.close()
		except IOError:
			file.close()
        	print('The file' + self.file_path + 'does not exist')
	
	def read_all(self):
		try:
			return open(file_path,self.READING_MODE).read()
		except IOError:
			print('The file' + self.file_path + 'does not exist')

	@staticmethod
	def format_grid_to_string(grid):
		