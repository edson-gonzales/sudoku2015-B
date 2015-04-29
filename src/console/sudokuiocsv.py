import sys, csv

sys.path.append("../../src/console")

from sudokuio import SudokuIO

class SudokuIOCsv(SudokuIO):
    def __init__(self, file_path):
        """ Creator method that set the permissions for writing and reading

        """
        super(SudokuIOCsv, self).__init__(file_path)
        self.WRITING_MODE = 'wt'
        self.READING_MODE = 'rt'

    def write(self, grid):
        """ Method that write in an csv file located in file_path

        int[9][9] grid - the grid that will be writed in the file
        """
        try:
            file = open(self.file_path,self.WRITING_MODE)
            writer = csv.writer(file)
            for row in range(len(grid)):
                row_array = ["{0}".format(number) for number in grid[row]]
                writer.writerow(row_array)
            file.close()
        except IOError:
            file.close()
            print('The file' + self.file_path + 'does not exist')
    
    def read_all(self):
        """ method that read a csv file located in file_path

        return string - return a grid from a csv file
        """
        try:
            return open(self.file_path,self.READING_MODE).read()
        except IOError:
            print('The file' + self.file_path + 'does not exist')

    def read_all_to_grid(self):
        """ return the read data from a csv file in a grid format.

        return int[9][9] - return the data readed from csv file in grid format.
        """
        csv_content = read_all()
        csv_content = csv_content[0:len(csv_content)-2]
        grid = csv_content.split('\r\n')
        for row in range(len(grid)):
            grid[row] = [int(n) for n in grid[row].split(',')]
        return grid

    @staticmethod
    def format_grid_to_string(grid):
        """method that return the grid in string format bug with rows by line.

        return string - return the representation of a grid in string format.
        """
        for row in range(len(grid)):
            grid[row] = ','.join("{0}".format(number) for number in grid[row])
        string_grid = '\r\n'.join(grid)+'\r\n'
        return string_grid

