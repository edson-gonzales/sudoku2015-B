# unittest
import sys
sys.path.append("../src/interface")
import unittest
from readconfigfile import ReadConfigFile


class ReadConfigFileTest(unittest.TestCase):

	def test_default_values_of_config_file(self):

		getdata=ReadConfigFile(configtest).getoutputfile()	
		defaultvalues=getdata[0]+"\\"+getdata[1]+"."+getdata[2]	
		self.assertEqual("d:\SudokuGame\Sudoku.txt",defaultvalues)

	def test_one_algorithm_should_be_set_as_active(self):	
	
		getdata=ReadConfigFile(configtest).getlistofalgorithms()			
		self.assertEqual("PeterNovings",getdata[0])

	def test_one_level_option_should_be_set_as_active(self):
	
		getdata=ReadConfigFile(configtest).getlistofgenerationlevelsnames()			
		self.assertEqual("Easy",getdata[0])

	def test_every_level_should_have_bottom_and_top_values(self):

		levelname='Easy'
		detailslevel=[levelname,'60','70','Active']
	
		getdata=ReadConfigFile(configtest).getdetailsofgenerationlevels(levelname)			
		self.assertEqual(detailslevel,getdata)
	
	def test_Output_file_type_shoul_be_txt_csv_or_xml_types_only(self):
		pass
        

if __name__ == '__main__':
	configtest='configtest.xml'
	unittest.main()