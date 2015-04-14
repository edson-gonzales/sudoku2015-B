# class settings
from Tkinter import *
import ttk
from read_config_file import ReadConfigFile

class SettingsGame(Frame):

	def __init__(self, parent):
		"""
		returns the tkinter frame, and will invoke init_ window() function.

		self.configfile -- will have the config file location where the game will read the Game settings

		"""
		main = self.main = Toplevel(parent)
		self.fileconfig = '../../config/config.xml'		
		self.init_window()

	def init_window(self):
		"""
		shows the objects to be displayed in the window (labels, buttons, listbox, combobox).
		this function will invoke to the following functions:
			--fillvaluesintheOutpufileEntry()
			--ShowListAlgorithms()
			--showlevelcombobox()

		"""
		self.main.geometry("600x400+200+200")
		self.main.title("Settings Sudoku Game")
	
		#definying the UI option to shown up and edit the values of Output file
		Label(self.main, text = "Output File Config:").place(x = 15, y= 10)
		Label(self.main, text = "Path: ").place(x = 15, y = 40)
		
		# fill values in the output entry
		self.fill_values_in_the_output_file_entry()
		
		# for future suported types
		#self.Listofsupportedfilestypes()

		#create a listbox to list all  to list the available algorithms 
		Label(self.main, text = "Solve Algorithm:").place(x = 15, y = 90)
		Label(self.main, text = "Algorithm: ").place(x = 15, y = 115)
		self.show_list_algorithms()

		#Creaate a combo box with levels values
		Label(self.main, text = " Complexity :").place(x = 15, y= 200)
		Label(self.main, text = " Level :").place(x = 15, y= 220)
		
		#create and fill the combobox
		self.show_level_combobox()

		Label(self.main, text = "TopLimit: ").place(x = 15, y = 250)
		Label(self.main, text = "BottonLimit: ").place(x = 15, y = 280)
		
		
		#buttons
		savebutton = Button(self.main, text = " Save ", width = 10, heigh = 2)
		savebutton.place(x = 100, y = 330)

		closebutton = Button(self.main, text = " Close ", width = 10, heigh = 2, command = self.quit)
		closebutton.place(x = 200, y = 330)

		self.main.mainloop()

	def fill_values_in_the_output_file_entry(self):
		"""
		shows the value in output file box.
		getvaluesoutputfile -- the string value get from "readconfigfile" class to get the Output file settings saved in config file.

		"""
		getvaluesoutputfile = ReadConfigFile(self.fileconfig).get_output_file()
		currentpath = StringVar()
		
		currentpath.set(getvaluesoutputfile[0] + '\\' + getvaluesoutputfile[1] + '.' + getvaluesoutputfile[2])
		

		outputf1 = Entry(self.main, textvariable = currentpath, width = 30).place(x = 100, y = 40)
		

	def list_of_supported_files_types(self):
		"""
		function will populate all files formats to be supported in the Game
		"""

		listtypes = ["txt", "csv", "xml"]	
		lsttypes = ttk.Combobox (self.main, state = 'readonly', width = 5)
		lsttypes['values'] = (listtypes)
		lsttypes.current(0)
		lsttypes.place(x = 270, y = 65)


	def show_list_algorithms(self):
		"""
		calls getlistofalgorithms function from "readconfigfile" class to get the list of availables algorithms saved in config file.
		and this info will be populated in a listbox in the UI

		"""
		
		listofalgorithms = ReadConfigFile(self.fileconfig).get_list_of_algorithms()		
		
		lstAlgorithms = Listbox(self.main, heigh = 4)
		
		for index in range(len(listofalgorithms)):
			lstAlgorithms.insert(index,listofalgorithms[index])			
		
		lstAlgorithms.selection_set( first = 0 )
		lstAlgorithms.place(x = 100, y = 120)
			
	def show_level_combobox(self):

		"""
		function calls getlistofgenerationlevelsnames function from "readconfigfile" class to get the list of levels saved in config file.
		and this info will be populated in a combobox in the UI
		
		"""

		listvalueslevel = ReadConfigFile(self.fileconfig).get_list_of_generation_levels_names()		
		lstLevels = ttk.Combobox (self.main, state = 'readonly')
		lstLevels['values'] = (listvalueslevel)
		lstLevels.current(0)
		lstLevels.place(x = 100, y = 220)
		
		self.show_details_of_level(listvalueslevel[0])

	def show_details_of_level(self,levelname):

		"""
		function calls getdetailsofgenerationlevels function from "readconfigfile" class to get the details of specific level type, this info is read from config file.
		and this info will be populated in top and bottom limit boxes in the UI
		
		"""
		detailslevel = ReadConfigFile(self.fileconfig).get_details_of_generation_levels(levelname)
		toplimit = StringVar()
		bottonlimit = StringVar()
		toplimit.set(detailslevel[1])
		bottonlimit.set(detailslevel[2])
		toplimit = Entry(self.main, textvariable = toplimit).place(x = 100, y = 250)
		bottonlimit = Entry(self.main,textvariable = bottonlimit).place(x = 100, y = 280)

	def quit(self):
		"""
		function will close the window and application

		"""
		sys.exit()
