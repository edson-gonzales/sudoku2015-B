import sys
import os.path
sys.path.append("../src/interface")
import unittest

from read_config_file import ReadConfigFile
from save_config_file import SaveConfigFile

class ReadConfigFileTest(unittest.TestCase):

    def test_outputfilepath_changed_is_saved_in_config_file(self):

        new_file_path = 'c:\sudokugame\sudoku.txt'
        SaveConfigFile(save_config_test).save_output_file_settings(new_file_path)
        get_file_path = ReadConfigFile(save_config_test).get_output_file()

        self.assertEqual(new_file_path, get_file_path)

    def test_txt_supported_file_type_is_saved_in_config_file(self):
        
        txt_file_type = 'c:\sudokugame\sudoku.txt'
        SaveConfigFile(save_config_test).save_output_file_settings(txt_file_type)
        get_file_path = ReadConfigFile(save_config_test).get_output_file()        
        self.assertEqual('.txt', os.path.splitext(get_file_path)[1])

    def test_html_supported_file_type_is_saved_in_config_file(self):

        html_file_type = 'c:\sudokugame\sudoku.html'
        SaveConfigFile(save_config_test).save_output_file_settings(html_file_type)
        get_file_path = ReadConfigFile(save_config_test).get_output_file()        
        self.assertEqual('.html', os.path.splitext(get_file_path)[1])

    def test_non_supported_file_type_is_not_saved_in_config_file(self):

        other_file_type = 'c:\sudokugame\sudoku.csv'        
        self.assertFalse(SaveConfigFile(save_config_test).save_output_file_settings(other_file_type))
        
    def test_change_BruteForce_algorithm_to_Backtracking_in_config_file(self):

        active_alg = 'Bruteforce'
        SaveConfigFile(save_config_test).validate_alg_name(active_alg)
        change_alg_to = 'Backtracking'
        SaveConfigFile(save_config_test).validate_alg_name(change_alg_to)
        get_active_alg = ReadConfigFile(save_config_test).get_list_of_algorithms()
        self.assertEqual(change_alg_to, get_active_alg[0])

    def test_empty_algoritm_name_is_not_saved_in_config_file(self):

        empty_alg_name = ''
        self.assertFalse(SaveConfigFile(save_config_test).validate_alg_name(empty_alg_name))

    def test_change_from_easy_to_medium_level_in_config_file(self):

        active_level = ['Easy', 70, 60]        
        SaveConfigFile(save_config_test).save_level_settings(active_level)
        change_level_to = ['Medium', 50, 40]
        SaveConfigFile(save_config_test).save_level_settings(change_level_to)
        get_level_name = ReadConfigFile(save_config_test).get_list_of_generation_levels_names()
        self.assertEqual(change_level_to[0], get_level_name[0])
    
    def test_change_top_limit_of_custom_level_in_config_file(self):            
        change_top_limit = ['Custom', 23, 20]
        SaveConfigFile(save_config_test).save_level_settings(change_top_limit)
        get_level = ReadConfigFile(save_config_test).get_details_of_generation_levels(change_top_limit[0])
        self.assertEqual(change_top_limit[1], int(get_level[1]))

    def test_change_bottom_limit_of_custom_level_in_config_file(self):    
        change_bottom_limit = ['Custom', 23, 20]
        SaveConfigFile(save_config_test).save_level_settings(change_bottom_limit)
        get_level = ReadConfigFile(save_config_test).get_details_of_generation_levels(change_bottom_limit[0])
        self.assertEqual(change_bottom_limit[2], int(get_level[2]))

    def test_negative_value_for_top_limit_is_saved_as_positive_in_config_file(self):
        change_top_limit = ['Custom', -23, -20]
        SaveConfigFile(save_config_test).save_level_settings(change_top_limit)
        get_level = ReadConfigFile(save_config_test).get_details_of_generation_levels(change_top_limit[0])
        self.assertEqual(abs(change_top_limit[1]), int(get_level[1]))


if __name__ == '__main__':
    save_config_test = 'saveconfigtest.xml'
    unittest.main()