import sys
sys.path.append("../src/interface")
import unittest
from read_config_file import ReadConfigFile

class ReadConfigFileTest(unittest.TestCase):

    def test_default_values_of_config_file(self):
        get_data = ReadConfigFile(config_test).get_output_file()    
        default_values = get_data[0] + "\\" + get_data[1] + "." + get_data[2]   
        self.assertEqual("d:\SudokuGame\Sudoku.txt", default_values)

    def test_one_algorithm_should_be_set_as_active(self):           
        get_data = ReadConfigFile(config_test).get_list_of_algorithms()          
        default_algorithm="Peter Novig"+ "\'"+"s"        
        self.assertEqual(default_algorithm, get_data[0])

    def test_one_level_option_should_be_set_as_active(self):    
        get_data = ReadConfigFile(config_test).get_list_of_generation_levels_names()           
        self.assertEqual("Easy", get_data[0])

    def test_every_level_should_have_bottom_and_top_values(self):
        level_name = 'Easy'
        details_level = [level_name, '60', '70', 'Active']
    
        get_data = ReadConfigFile(config_test).get_details_of_generation_levels(level_name)            
        self.assertEqual(details_level, get_data)           

if __name__ == '__main__':
    config_test='configtest.xml'
    unittest.main()