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
		listoutput = []
		for output in self.root.findall('Output'):
			path = output.find('Path').text
			name = output.find('Name').text		    
			extension = output.find('Extension').text	


		listoutput.append(path)
		listoutput.append(name)
		listoutput.append(extension)

		
		return listoutput

	def list_of_file_types_supported(self):
		"""		
		Returns a list with all files types values supported, it will be also get from config file
		listtypes: variable of list type, it will have assigned all supported files, this info is read from config file
		"""
		listypes = []
		
		for solve in self.root.findall('./Output/Extension/type'):			
			namealg = solve.find('type').text
			#print namealg
			#listypes.append(typevalue)
		

	def get_list_of_algorithms(self):
		"""
		Returns a list with all availables algorithms from config file, and the first item will always return
		the active algorithm set for the game.
		listalgorithms: variable of list type, it will have assigned all algorithms read from config file
		"""
  		listalgorithms = []
  		
		for solve in self.root.findall('./Solve/Algorithm'):						
			if solve.find('Status').text == 'Active':
				namealgactive = solve.get('name')				
			else:
				namealg = solve.get('name')
				listalgorithms.append(namealg)

		listalgorithms.append(namealgactive)
		listalgorithms.reverse()
		
		return listalgorithms
	
	def get_list_of_generation_levels_names(self):

		"""
		Returns a list with all availables levels names from config file, and the first item will always return
		the active level set for the game. 

		listlevels=variable of list type, it will have assigned all levels names read from config file
		
		"""
		listlevels = []
		for level in self.root.findall("./Generation/Level"):			
			if level.find('Status').text == 'Active':
				namelevelactive = level.get('name')
			else:
				namelevel = level.get('name')
				listlevels.append(namelevel)				

		listlevels.append(namelevelactive)
		listlevels.reverse()
		
		return listlevels

	def get_details_of_generation_levels(self, levelname):

		"""
		method: returns a list with the details of each level specified. the details returned are level name, top limit, bottom limit,
		and status.
		levelname -- thi parameter is string type and to return the details of each, the method requires this entry
		listdetailslevel -- variable of list type, it will have assigned the details of each level
		
		"""

		listdetailslevel = []
		
		for level in self.root.findall("./Generation/Level/[@name='" + levelname + "']"):			
					bottomlimit = level.find('BottomLimit').text
					toplimit = level.find('TopLimit').text				
					status = level.find('Status').text				
					listdetailslevel.append(levelname)
					listdetailslevel.append(bottomlimit)
					listdetailslevel.append(toplimit)
					listdetailslevel.append(status)

		
		return listdetailslevel		
