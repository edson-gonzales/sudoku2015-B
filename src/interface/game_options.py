import os

from read_config_file import ReadConfigFile

class GameOptions():
        
    def __init__(self):
        """Main method of the class."""
        self.file_config = '../../config/config.xml'

    def solve_game(self):
        """Return the game solved using the algorithm chosen.

        string get_active_algorithm --> 'Backtracking'. algorithm set in the configuration file
        """ 
        get_algorithms = ReadConfigFile(self.file_config).get_list_of_algorithms()
        get_active_algorithm = get_algorithms[0]
        print get_active_algorithm
        # in this section we should include the code to invoke algoritm classes to solve the game and return an string to show it in the UI

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
        print get_level_details
        # in this section we should include the code to invoke generate game class and return an string to show it in the UI

    def save_game(self):
        """Save the game results in a file.

        string get_file_path --> 'c:\sudoku\sudoku.txt'. File path set in the configuration file
        """
        get_file_path = ReadConfigFile(self.file_config).get_output_file()        
        print get_file_path
        # in this section we should include the code to invoke save game class in a file