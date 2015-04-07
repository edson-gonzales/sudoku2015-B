# unittest
import sys
sys.path.append("../src/interface")
sys.path.append("../src/config")
import unittest
import xml.etree.ElementTree as etree
from readconfigfile import ReadConfigFile


class ReadConfigFileTest(unittest.TestCase):

	def test_default_values_of_config_file(self):
		getdata=ReadConfigFile().getoutputfile(root)	
		defaultvalues=getdata[0]+"\\"+getdata[1]+"."+getdata[2]		
		self.assertEqual("d:\SudokuGame\Sudoku.txt",defaultvalues)

	def test_default_algorith_setting(self):
		pass
	def test_default_level_setting(self):
		pass		
	def test_list_of_supported_file_types(self):
		pass
	def test_list_of_availables_algorithm(self):
		pass
	def test_list_of_available_levels(self):
		pass
	def test_one_default_algorithm_should_be_set_as_active(self):
		pass
	def test_one_level_option_should_be_set_as_active(self):
		pass
	def test_Output_file_type_shoul_be_txt_csv_or_xml_types_only(self):
		pass
        

if __name__ == '__main__':
	xmld=etree.parse("config.xml")		
	root=xmld.getroot()
	unittest.main()