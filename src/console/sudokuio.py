class SudokuIO(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.WRITE_MODE = 'r+'

    def write(self, text):
        file = open(self.file_path, self.WRITE_MODE)
        file.write(text)
        file.close()

    def read_all(self):
        print("Path: "+self.file_path)
        file = open(self.file_path)
        result = file.read()
        file.close()
        return result
    
    def print_sudoku(self, grid):
        grid_string = '-------------------------\n'
        for row in range(len(grid)):
            size = len(grid[row])
            for col in range (len(grid[row])):
                if (col == len(grid[row])-1):
                    grid_string = grid_string + str(grid[row][col] + '\n')
                elif (col % 3 == 2):
                    grid_string = grid_string + str(grid[row][col] + '|')
                else:
                    grid_string = grid_string + str(grid[row][col] + ' ')
            if (row % 3 == 2):
                grid_string = grid_string + '--------------------------\n'
        grid_string = grid_string + '\n'
        print(grid_string)