import xml.etree.ElementTree as etree

class ReadConfigFile():
    
    def __init__(self, file_config):
        """The Main function(constructor) -- creates the class attributes.

        string file_config -->('../config/config.xml') 
        """                         
        self.xmld = etree.parse(file_config)             
        self.root = self.xmld.getroot()        

    def get_output_file(self):
        """Return list_output.

        list list_output --> ['c:\sudoku','sudoku.txt']
        """
        list_output = []
        for output in self.root.findall('Output'):
            path = output.find('Path').text
            name = output.find('Name').text                     

        list_output.append(path)
        list_output.append(name)        
        
        return list_output            

    def get_list_of_algorithms(self):
        """Return list_algorithms.

        list list_algorithms -->['backtraking','Bruteforce'] algorithms names read from config file.
        """
        list_algorithms = []
        
        for solve in self.root.findall('./Solve/Algorithm'):                        
            if solve.find('Status').text == 'Active':
                name_alg_active = solve.get('name')               
            else:
                name_alg = solve.get('name')
                list_algorithms.append(name_alg)

        list_algorithms.append(name_alg_active)
        list_algorithms.reverse()
        
        return list_algorithms
    
    def get_list_of_generation_levels_names(self):
        """Return list_levels. 
        
        list list_levels -->['Easy','Hard','etc'] levels names read from config file.
        """
        list_levels = []
        for level in self.root.findall("./Generation/Level"):           
            if level.find('Status').text == 'Active':
                name_level_active = level.get('name')
            else:
                name_level = level.get('name')
                list_levels.append(name_level)                
                
        list_levels.append(name_level_active)
        list_levels.reverse()
        
        return list_levels

    def get_details_of_generation_levels(self, level_name):
        """Return list_details_level.

        string level_name --> ('Easy') level name entry required to filter the XML file.
        list list_details_level --> ['Easy',10,30,'Active'] details of specific level; name, bottom, top limit and status value of an especific level.
        """
        list_details_level = []
        
        for level in self.root.findall("./Generation/Level/[@name='" + level_name + "']"):           
                    bottom_limit = level.find('BottomLimit').text
                    top_limit = level.find('TopLimit').text              
                    status = level.find('Status').text              
                    list_details_level.append(level_name)
                    list_details_level.append(bottom_limit)
                    list_details_level.append(top_limit)
                    list_details_level.append(status)
        
        return list_details_level