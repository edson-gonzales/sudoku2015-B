import os, sys, webbrowser

sys.path.append("../../")
sys.path.append("../console")
sys.path.append("../interface")
sys.path.append("../algorithms")
sys.path.append("../util")

from read_config_file import ReadConfigFile
from sudokuio import SudokuIO
from sudokuiohtml import SudokuIOHtml
from sudokuiocsv import SudokuIOCsv
from backtracking import Backtracking
from Peter_Norvig import PeterNorvig
from Brute_Force import BruteForce
from string import maketrans
from Sudoku_Generator import SudokuGenerator

class GameOptions():
        
    def __init__(self):
        """Main method of the class."""
        self.file_config = '../../config/config.xml'
        self.grid = None
        self.grid_string = None

    def solve_game(self):
        """Return the game solved using the algorithm chosen and if there is not a
        generated game it's looked for a game in the configuration file but only if the file 
        has valid content.

        string get_active_algorithm --> 'Backtracking'. algorithm set in the configuration file
        return int[9][9] - return the current grid that will be displayed in the UI.
        """ 
        get_algorithms = ReadConfigFile(self.file_config).get_list_of_algorithms()
        get_active_algorithm = get_algorithms[0]
        get_file_path = ReadConfigFile(self.file_config).get_input_file()        
        extension = os.path.splitext(get_file_path)[-1].lower()
        file = SudokuIO(get_file_path)
        if self.grid != None or file.exist_the_file():
            generator = self.get_algorithm_object(get_active_algorithm)
            if extension == '.txt' and generator != None and self.grid == None:
                self.grid = generator.solve(file.read_all())
            elif extension == '.csv' and generator != None and self.grid == None:
                file = SudokuIOCsv(file.file_path)
                self.grid_string = self.convert_grid_to_string(file.read_all_to_grid())
                self.grid = generator.solve(self.grid_string)    
            elif generator != None and self.grid != None:
                self.grid_string = self.convert_grid_to_string(self.grid)
                self.grid = generator.solve(self.grid_string)
            else:
                print('There a problem with the solve algorith or with the sudoku numbers')    
        else:
            print('There is not sudoku game to solve')

        return self.grid
        # # in this section we should include the code to invoke algoritm classes to solve the game and return an string to show it in the UI
    
    def get_algorithm_object(self, get_active_algorithm):
        """ return the algorithm that will be used in the solve operation.

        return generator - return an algorithm that will solve the sudoku game.
        """
        generator = None
        if get_active_algorithm == 'Backtracking':
            generator = Backtracking()
        elif get_active_algorithm == 'Peter Novig\'s':
            generator = PeterNorvig()
        elif get_active_algorithm == 'BruteForce':
            generator = BruteForce()
        else:
            print('There is no a valid algorithm')
        return generator

    def convert_grid_to_string(self, grid):
        """ Method that conver a grid in the following format in order to solve it.
        306508400520000000087000031003010080900863005050090600130000250000000074005206392

        return string - a string with the sudoku game in a line.
        """
        self.grid_string = ''
        for row in range(len(grid)):
            self.grid_string = self.grid_string + ''.join("{0}".format(number) for number in grid[row])
        return self.grid_string

    def generate_game(self):
        """Generate the game using the complexity level chosen.

        list get_level_details --> ['Easy',70,60,'Active']. Level details set in the configuration file
        get_level_details[0] --> level name
        get_level_details[1] --> top limit
        get_level_details[2] --> bottom limit
        get_level_details[3] --> status
        return int[9][9] - return the current grid that will be displayed in the UI.
        """ 
        get_level_active_name = ReadConfigFile(self.file_config).get_list_of_generation_levels_names()
        get_level_details = ReadConfigFile(self.file_config).get_details_of_generation_levels(get_level_active_name[0])
      
        generator = SudokuGenerator()
        self.grid = generator.generate_sudoku(get_level_details[0])
        # in this section we should include the code to invoke generate game class and return an string to show it in the UI
        return self.grid

    def save_game(self):
        """Save the game results in a file.

        string get_file_path --> 'c:\sudoku\sudoku.txt'. File path set in the configuration file
        """
        get_file_path = ReadConfigFile(self.file_config).get_output_file()        
        print get_file_path
        extension = os.path.splitext(get_file_path)[-1].lower()
        print(self.grid)
        if self.grid != None:
            if extension == '.txt':
                output = SudokuIO(get_file_path)
                output.write_sudoku_in_file(self.grid)
                webbrowser.open(get_file_path)
            elif extension == '.html':
                output = SudokuIOHtml(get_file_path)
                output.write_sudoku_in_file(self.grid)
                webbrowser.open(get_file_path)
            else:
                print('Format not supported')
        else:
            print('There is not game to save.')
        # in this section we should include the code to invoke save game class in a file