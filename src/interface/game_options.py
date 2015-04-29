import os
import sys

sys.path.append("../../")
sys.path.append("../console")
sys.path.append("../interface")
sys.path.append("../algorithms")

from read_config_file import ReadConfigFile
from sudokuio import SudokuIO
from sudokuiohtml import SudokuIOHtml
from backtracking import Backtracking
from Peter_Norvig import PeterNorvig
from Brute_Force import BruteForce
from string import maketrans

class GameOptions():
        
    def __init__(self):
        """Main method of the class."""
        self.file_config = '../../config/config.xml'
        self.grid = None
        self.grid_string = None

    def solve_game(self):
        """Return the game solved using the algorithm chosen.

        string get_active_algorithm --> 'Backtracking'. algorithm set in the configuration file
        """ 
        get_algorithms = ReadConfigFile(self.file_config).get_list_of_algorithms()
        get_active_algorithm = get_algorithms[0]
        

        self.grid = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9]
            ]

        return self.grid
        # if self.grid != None:
        #     if get_active_algorithm == 'Backtracking':
        #         generator = Backtracking()
        #         self.grid_string = self.convert_grid_to_string(self.grid)
        #         self.grid = generator.solve(self.grid_string)
        #     elif get_active_algorithm == 'Peter Novig\'s':
        #         generator = PeterNorvig()
        #         self.grid_string = self.convert_grid_to_string(self.grid)
        #         self.grid = generator.solve(self.grid_string)
        #     elif get_active_algorithm == 'BruteForce':
        #         generator = BruteForce()
        #         self.grid_string = self.convert_grid_to_string(self.grid)
        #         self.grid = generator.solve(self.grid_string)
        # else:
        #     print('There is not sudoku game to solve')
        # # in this section we should include the code to invoke algoritm classes to solve the game and return an string to show it in the UI
    
    def convert_grid_to_string(self, grid):
        self.grid_string = ''
        for row in range(len(grid)):
            self.grid_string = self.grid_string + ''.join("{0}".format(number) for number in grid[row])
       # convert_zero_to_dot = maketrans('0', '.')
        #self.grid_string = str(self.grid_string).translate(convert_zero_to_dot)
        return self.grid_string

    def generate_game(self):
        """Generate the game using the complexity level chosen.

        list get_level_details --> ['Easy',70,60,'Active']. Level details set in the configuration file
        get_level_details[0] --> level name
        get_level_details[1] --> top limit
        get_level_details[2] --> bottom limit
        get_level_details[3] --> status
        """ 
        get_level_active_name = ReadConfigFile(self.file_config).get_list_of_generation_levels_names()
        get_level_details = ReadConfigFile(self.file_config).get_details_of_generation_levels(get_level_active_name[0])
      
        #generator = SudokuGenerator()
        #self.grid = generator.generate_sudoku(get_level_details[0])
        # in this section we should include the code to invoke generate game class and return an string to show it in the UI
                
        
        self.grid = [
                [0,1,6,5,7,8,4,9,2],
                [0,0,0,1,3,4,7,6,8],
                [0,8,7,6,2,9,5,3,1],
                [0,6,3,4,1,5,9,8,7],
                [0,7,4,8,0,3,1,2,5],
                [0,5,1,7,9,0,6,4,3],
                [0,3,8,9,4,0,2,5,6],
                [0,9,2,3,5,1,8,7,4],
                [0,4,5,0,8,6,3,1,9]
                ]
        
        return self.grid

    def save_game(self):
        """Save the game results in a file.

        string get_file_path --> 'c:\sudoku\sudoku.txt'. File path set in the configuration file
        """
        get_file_path = ReadConfigFile(self.file_config).get_output_file()        
        print get_file_path
        extension = os.path.splitext(get_file_path)[-1].lower()
        if self.grid != None:
            if extension == '.txt':
                output = SudokuIO(get_file_path)
                output.write_sudoku_in_file(self.grid)
            elif extension == '.html':
                output = SudokuIOHtml(get_file_path)
                output.write_sudoku_in_file(self.grid)
            else:
                print('Format not supported')
        else:
            print('There is not game to save.')
        # in this section we should include the code to invoke save game class in a file