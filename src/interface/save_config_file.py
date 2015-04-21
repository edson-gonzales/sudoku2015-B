import xml.etree.ElementTree as etree

class SaveConfigFile():
    
    def __init__(self, config_file):    
        """ Main function, it creates the global variables for reading and saving configuration XML file."""        
        self.config_file=config_file
        self.xmld=etree.parse(self.config_file)     
        self.root=self.xmld.getroot()           

    def save_output_file_settings(self, new_file_path):
        """ This function saves the changes done in UI related to output file settings.

        list new_file_path -- it gets the values(path and file name ) from UI."""     
        for output in self.root.findall('./Output'):            
            output.find('Path').text = new_file_path[0]
            output.find('Name').text = new_file_path[1]
                    
        self.xmld.write(self.config_file)   
        
    def save_algorithm_settings(self, alg_name):
        """ This function saves the changes done in UI related to algorithm choosen to solve the game."""       
        for alg in self.root.findall("./Solve/Algorithm"):
            if alg.get('name') == alg_name:
                alg.find('Status').text = 'Active'
            else:
                alg.find('Status').text = 'Inactive'            
        
        self.xmld.write(self.config_file)

    def save_level_settings(self, level_details):
        """ This function saves the changes done in UI related to complexity of the game(easy,medium,high or custom).
        
        list level_details -->got the values to save in the config file."""     
        for level in self.root.findall("./Generation/Level"):
            if level.get('name') == level_details[0]:
                level.find('BottomLimit').text = str(level_details[1])
                level.find('TopLimit').text = str(level_details[2])
                level.find('Status').text = 'Active'
            else:
                level.find('Status').text = 'Inactive'          
        
        self.xmld.write(self.config_file)