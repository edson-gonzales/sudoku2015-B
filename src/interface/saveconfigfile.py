import xml.etree.ElementTree as etree

class SaveSettingInConfigFile():
	
	def __init__(self,root=None,xmld=None,configfile=None):	
		
		self.root=root
		self.xmld=xmld
		self.file=configfile

		#save the setting of output file in the XML
		self.saveoutputfilesettings()
		#update xml when new alg was selected
		self.savealgorithmssettings()
		#update xml when new level was selected
		self.savelevelsettings()
		# get details of levelgeneration
				

	def saveoutputfilesettings(self):
		outputnewvalues=['d:\updated\sudoku','sudokuName','csv_sudoku']		

		for output in root.findall('./Output'):
			
			output.find('Path').text=outputnewvalues[0]
			output.find('Name').text=outputnewvalues[1]
			output.find('Extension').text=outputnewvalues[2]			
		
		xmld.write(configfile)	
		
	def savealgorithmssettings(self):
		newalg='PeterNovings'
		for alg in root.findall("./Solve/Algorithm"):
			if alg.get('name')==newalg:
				alg.find('Status').text='Active'
			else:
				alg.find('Status').text='Inactive'			
		
		xmld.write(configfile)

	def savelevelsettings(self):
		newlevelvalues=['Custom',10,15]
		for level in root.findall("./Generation/Level"):
			if level.get('name')==newlevelvalues[0]:
				level.find('BottomLimit').text=str(newlevelvalues[1])
				level.find('TopLimit').text=str(newlevelvalues[2])
				level.find('Status').text='Active'
			else:
				level.find('Status').text='Inactive'			
		
		xmld.write(configfile)

#save=SaveSettingInConfigFile("D:\python2015\config.xml")
if __name__ == '__main__':
	configfile="D:\python2015\config.xml"
	xmld=etree.parse(configfile)		
	root=xmld.getroot()
	SaveSettingInConfigFile(root,xmld,configfile)