import os

class SudokuIO(object):

    def __init__(self,file_path):
        """ Constructor of the class, curently this define the variables for the open 
        mode w and w+ and the path where the file is located.

        string file_path - this is the current path where the path is located. 
        """
        self.file_path = file_path
        self.WRITE_MODE_TRUNCATE = 'w+'
        self.WRITE_MODE = 'w'

    def write(self, text):
        """ Method that write a text in the file located in the path self.file_path

        string text - this is the text that will be saved in the file.
        """
        try:
            file = open(self.file_path, self.WRITE_MODE_TRUNCATE)
            file.write(text)
            file.close()
        except IOError:
            print('The file' + self.file_path + 'does not exist')

    def read_all(self):
        """ Method that read all content of a text file and return the string value for
        the content.

        return string - return an string with the content of all file.
        """
        try:
            file = open(self.file_path)
            result = file.read()
            file.close()
            return result
        except IOError:
            print('The file' + self.file_path + 'does not exist')

    def delete_content(self):
        """ Method that delete the content of a file or clear the content of the file 
        located in the path self.file_path
        """
        try:
            open(self.file_path, self.WRITE_MODE).close()
        except IOError:
            print('The file' + self.file_path + 'does not exist')

    def delete_file(self):
        """ This method remove the file from the system        
        """
        if self.exist_the_file():
            try:
                os.remove(self.file_path)
            except IOError:
                print('The file' + self.file_path + 'does not exist')

    def exist_the_file(self):
        """ this method returns true or false if the file exist

        return boolean - return true or false if the file exist or not respectively.
        """
        return os.path.exists(self.file_path) and os.path.isfile(self.file_path)


    def format_grid(self, grid):
        """ Method that convert a grid[9][9] in an string with the sudoku format.

        int[9][9] grid - the grid that will be converted in a string.
        return string - return the representation of a grid[9][9] in the sudoku format.
        """

        grid_string = '------------------\n'
        for row in range(len(grid)):
            grid_string = self.fill_rows(grid, row, grid_string)
        return grid_string

    def fill_rows(self, grid, row, grid_string):
        """ Fill the row of a grid in the grid_string variable

        return string - return the current representation of a grid in the sudoku format but by row.
        """
        for col in range (len(grid[row])):
            if (col == len(grid[row])-1):
                grid_string = grid_string + str(grid[row][col]) + '\n'
            elif (col % 3 == 2):
                grid_string = grid_string + str(grid[row][col]) + '|'
            else:
                grid_string = grid_string + str(grid[row][col]) + ' '
        if (row % 3 == 2):
            grid_string = grid_string + '------------------\n'
        return grid_string

    
    def write_sudoku_in_file(self,grid):
        """ Mehod that write a sudoku grid in a txt file located in self.file_path

        int[9][9] grid - the grid 9x9 that will be writed in a txt file.
        """
        grid_string = self.format_grid(grid)
        self.write(grid_string)