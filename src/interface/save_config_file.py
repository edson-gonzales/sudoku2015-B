import xml.etree.ElementTree as etree
import os

class SaveConfigFile():
    
    def __init__(self, config_file):    
        """Main function, it creates the global variables for reading and saving configuration XML file.

        string config_file -->('../config/config.xml'), save methods uses this entry to save the changes in the configuration file 
        """        
        self.config_file = config_file
        self.xmld = etree.parse(self.config_file)     
        self.root = self.xmld.getroot()           

    def save_output_file_settings(self, new_file_path):
        """Save new_file_path in configuration file.

        list new_file_path --> 'd:\custompath\sudoku.txt', it gets the file path from UI."""     
        ext_file = os.path.splitext(new_file_path)[1]
        if ext_file =='.txt' or ext_file == '.html':
            for output in self.root.findall('./Output'):            
                output.find('Path').text = new_file_path            
            self.xmld.write(self.config_file)   
        else:
            return False

    def save_algorithm_settings(self, alg_name):
        """Save alg_name in configuration file

        string alg_name --> 'Backtracking',, it gets the new algorithm name from UI."""       
        if alg_name != '':
            for alg in self.root.findall("./Solve/Algorithm"):
                if alg.get('name') == alg_name:
                    alg.find('Status').text = 'Active'
                else:
                    alg.find('Status').text = 'Inactive'            
        
            self.xmld.write(self.config_file)
        else:
            return False

    def save_level_settings(self, level_det=[]):
        """Save level_det in configuration file.        
        
        list level_details --> ['Easy', 30, 20], it gets the values from UI."""     

        for level in self.root.findall("./Generation/Level"):                   
            if level.get('name') == level_det[0] and self.validate_top_limit_numbers(level_det[1],level_det[2]) == True: 
                level.find('TopLimit').text = str(abs(int(level_det[1])))
                level.find('BottomLimit').text = str(abs(int(level_det[2])))
                level.find('Status').text = 'Active'
            elif level.get('name') == level_det[0] and self.validate_top_limit_numbers(level_det[1],level_det[2]) == False:                 
                level.find('Status').text = 'Active'
            else:
                level.find('Status').text = 'Inactive'          
        
        self.xmld.write(self.config_file)

    def validate_top_limit_numbers(self, top_number, bottom_number):
        """Return True/False.

        string top_number --> -1,1; expected value is positive and major than bottom_number value
        string bottom_number --> -1,1 ; expected value is positive and minor than top_limit value
        """

        if abs(int(top_number)) > abs(int(bottom_number)):
            return True
        else:
            return False



        
