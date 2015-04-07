import xml.etree.ElementTree as etree

class ReadConfigFile():
	
	def __init__(self):	
		
		xmld=etree.parse("D:\python2015\config.xml")		
		root=xmld.getroot()
		#ReadConfigFile(root)
	
		#self.root=root

		#get the outputfile configuration
		self.getoutputfile(root)
		#get the list of available algorithms
		self.getlistofalgorithms(root)
		#get the list of available levels
		self.getlistofgenerationlevelsnames(root)
		# get details of levelgeneration
		self.getdetailsofgenerationlevels(root,"Hard")
		

	def getoutputfile(self,root):
		listoutput=[]
		for output in root.findall('Output'):
			path = output.find('Path').text
			name = output.find('Name').text		    
			extension = output.find('Extension').text	


		listoutput.append(path)
		listoutput.append(name)
		listoutput.append(extension)

		print(listoutput)
		#return listoutput

		#self.listoffiletypessupported(root)

	def listoffiletypessupported(self,root):
		listypes=[]
		num=1
		for solve in root.findall('./Output/Extension/type'):			
			namealg = solve.find('type').text
			#print namealg
			#listypes.append(typevalue)
		
		#print listypes

	def getlistofalgorithms(self,root):

  		listoutput=[]
		for solve in root.findall('./Solve/Algorithm'):			
			namealg = solve.get('name')
			listoutput.append(namealg)				

		#print(listoutput)
		return listoutput
	
	def getlistofgenerationlevelsnames(self,root):
		listoutput=[]
		for level in root.findall("./Generation/Level"):			
			namelevel = level.get('name')
			listoutput.append(namelevel)				

		#print(listoutput)
		return listoutput

	def getdetailsofgenerationlevels(self,root,levelname):
		listoutput=[]
		
		for level in root.findall("./Generation/Level/[@name='"+levelname+"']"):			
					bottomlimit = level.find('BottomLimit').text
					toplimit = level.find('TopLimit').text				
					status = level.find('Status').text				
					listoutput.append(levelname)
					listoutput.append(bottomlimit)
					listoutput.append(toplimit)
					listoutput.append(status)

		#print(listoutput)
		return listoutput		


#if __name__ == '__main__':

	#xmld=etree.parse("D:\python2015\config.xml")		
	#root=xmld.getroot()
#	ReadConfigFile()
read=ReadConfigFile()