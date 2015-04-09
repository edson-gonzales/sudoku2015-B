import xml.etree.ElementTree as etree

class ReadConfigFile():
	
	def __init__(self):	
		
		xmld=etree.parse("D:\python2015\config.xml")		
		self.root=xmld.getroot()

		#get the outputfile configuration
		self.getoutputfile()
		#get the list of available algorithms
		self.getlistofalgorithms()
		#get the list of available levels
		self.getlistofgenerationlevelsnames()
		# get details of levelgeneration
		self.getdetailsofgenerationlevels("Hard")
		

	def getoutputfile(self):
		
		listoutput=[]
		for output in self.root.findall('Output'):
			path = output.find('Path').text
			name = output.find('Name').text		    
			extension = output.find('Extension').text	


		listoutput.append(path)
		listoutput.append(name)
		listoutput.append(extension)

		#print(listoutput)
		return listoutput

	def listoffiletypessupported(self):
		listypes=[]
		num=1
		for solve in self.root.findall('./Output/Extension/type'):			
			namealg = solve.find('type').text
			#print namealg
			#listypes.append(typevalue)
		
		#print listypes

	def getlistofalgorithms(self):

  		listoutput=[]
  		finallist=[]
		for solve in self.root.findall('./Solve/Algorithm'):						
			if solve.find('Status').text=='Active':
				namealgactive = solve.get('name')				
			else:
				namealg = solve.get('name')
				listoutput.append(namealg)

		listoutput.append(namealgactive)
		listoutput.reverse()
		
		#print (listoutput)
		return listoutput
	
	def getlistofgenerationlevelsnames(self):
		listoutput=[]
		for level in self.root.findall("./Generation/Level"):			
			if level.find('Status').text=='Active':
				namelevelactive = level.get('name')
			else:
				namelevel = level.get('name')
				listoutput.append(namelevel)				

		listoutput.append(namelevelactive)
		listoutput.reverse()
		#print(listoutput)
		return listoutput

	def getdetailsofgenerationlevels(self,levelname):
		listoutput=[]
		
		for level in self.root.findall("./Generation/Level/[@name='"+levelname+"']"):			
					bottomlimit = level.find('BottomLimit').text
					toplimit = level.find('TopLimit').text				
					status = level.find('Status').text				
					listoutput.append(levelname)
					listoutput.append(bottomlimit)
					listoutput.append(toplimit)
					listoutput.append(status)

		#print(listoutput)
		return listoutput		
ReadConfigFile()