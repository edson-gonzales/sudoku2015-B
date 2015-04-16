import xml.etree.ElementTree as etree
class ReadConfigFile():
    
    def __init__(self, fileconfig): 
            
            
            self.xmld = etree.parse(fileconfig)             
            self.root = self.xmld.getroot()

        

    def get_output_file(self):
        """ 
        Returns the outputfile path, name and extension values from config file
        listoutput: variable to assign all values read from config file
        """
        list_output = []
        for output in self.root.findall('Output'):
            path = output.find('Path').text
            name = output.find('Name').text         
            extension = output.find('Extension').text   


        list_output.append(path)
        list_output.append(name)
        list_output.append(extension)

        
        return list_output

    def list_of_file_types_supported(self):
        """     
        Returns a list with all files types values supported, it will be also get from config file
        listtypes: variable of list type, it will have assigned all supported files, this info is read from config file
        """
        list_types = []
        
        for solve in self.root.findall('./Output/Extension/type'):          
            name_alg = solve.find('type').text
            #print namealg
            #listypes.append(typevalue)
        

    def get_list_of_algorithms(self):
        """
        Returns a list with all availables algorithms from config file, and the first item will always return
        the active algorithm set for the game.
        listalgorithms: variable of list type, it will have assigned all algorithms read from config file
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

        """
        Returns a list with all availables levels names from config file, and the first item will always return
        the active level set for the game. 

        listlevels=variable of list type, it will have assigned all levels names read from config file
        
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

        """
        method: returns a list with the details of each level specified. the details returned are level name, top limit, bottom limit,
        and status.
        levelname -- thi parameter is string type and to return the details of each, the method requires this entry
        listdetailslevel -- variable of list type, it will have assigned the details of each level
        
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
