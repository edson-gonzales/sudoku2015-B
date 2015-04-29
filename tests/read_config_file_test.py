import sys
import os.path
sys.path.append("../src/interface")
import unittest
from read_config_file import ReadConfigFile

class ReadConfigFileTest(unittest.TestCase):

    def setUp(self):
        self.read_config_test = 'readconfigtest.xml'

    def test_default_values_of_config_file(self):

        get_file_path = ReadConfigFile(self.read_config_test).get_output_file()            
        self.assertEqual("D:\games\sudoku\sudoku.txt", get_file_path)

    def test_one_algorithm_should_be_set_as_active(self):           

        get_data = ReadConfigFile(self.read_config_test).get_list_of_algorithms()          
        default_algorithm = "Backtracking"        
        self.assertEqual(default_algorithm, get_data[0])

    def test_one_level_option_should_be_set_as_active(self):    

        get_data = ReadConfigFile(self.read_config_test).get_list_of_generation_levels_names()           
        self.assertEqual("Easy", get_data[0])

    def test_default_active_easy_level_has_top_and_bottom_limit_values(self):

        details_level = ['Easy', '70', '36', 'Active']
    
        get_data = ReadConfigFile(self.read_config_test).get_details_of_generation_levels(details_level[0])            
        self.assertEqual(details_level, get_data)           


if __name__ == '__main__':
    read_config_test = 'readconfigtest.xml'
    unittest.main()