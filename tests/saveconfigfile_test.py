# unittest
import sys
sys.path.append("../src/interface")

import xml.etree.ElementTree as etree
import unittest
from saveconfigfile import SaveSettingInConfigFile

class SaveConfigFileTest(unittest.TestCase):

	def test_newchanges_done_in_outpufile_are_saved_in_config_file(self):
		pass
	def test_newalgorithm_isselected_to_solve_sudoku_is_saved_in_config_file(self):
		pass
	def test_level_easy_settingchanges_are_saved_in_config_file(self):
		pass		
	def test_level_medium_settingchanges_are_saved_in_config_file(self):
		pass
	def test_level_hard_settingchanges_are_saved_in_config_file(self):
		pass
	def test_level_custom_settingchanges_are_saved_in_config_file(self):
		pass

if __name__ == '__main__':
	xmld=etree.parse("D:\python2015\config.xml")		
	root=xmld.getroot()
	unittest.main()