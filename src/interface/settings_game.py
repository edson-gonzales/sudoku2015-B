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
        self.file_config = '../../config/config.xml'        
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
        save_button = Button(self.main, text = " Save ", width = 10, heigh = 2)
        save_button.place(x = 100, y = 330)

        close_button = Button(self.main, text = " Close ", width = 10, heigh = 2, command = self.quit)
        close_button.place(x = 200, y = 330)

        self.main.mainloop()

    def fill_values_in_the_output_file_entry(self):
        """
        shows the value in output file box.
        getvaluesoutputfile -- the string value get from "readconfigfile" class to get the Output file settings saved in config file.

        """
        get_values_output_file = ReadConfigFile(self.file_config).get_output_file()
        current_path = StringVar()
        
        current_path.set(get_values_output_file[0] + '\\' + get_values_output_file[1] + '.' + get_values_output_file[2])
        

        outputf1 = Entry(self.main, textvariable = current_path, width = 30).place(x = 100, y = 40)
        

    def list_of_supported_files_types(self):
        """
        function will populate all files formats to be supported in the Game
        """

        list_types = ["txt", "csv", "xml"]  
        list_types = ttk.Combobox (self.main, state = 'readonly', width = 5)
        list_types['values'] = (list_types)
        list_types.current(0)
        list_types.place(x = 270, y = 65)


    def show_list_algorithms(self):
        """
        calls getlistofalgorithms function from "readconfigfile" class to get the list of availables algorithms saved in config file.
        and this info will be populated in a listbox in the UI

        """
        
        list_of_algorithms = ReadConfigFile(self.file_config).get_list_of_algorithms()      
        
        lst_algorithms = Listbox(self.main, heigh = 4)
        
        for index in range(len(list_of_algorithms)):
            lst_algorithms.insert(index,list_of_algorithms[index])          
        
        lst_algorithms.selection_set( first = 0 )
        lst_algorithms.place(x = 100, y = 120)
            
    def show_level_combobox(self):

        """
        function calls getlistofgenerationlevelsnames function from "readconfigfile" class to get the list of levels saved in config file.
        and this info will be populated in a combobox in the UI
        
        """

        lst_values_level = ReadConfigFile(self.file_config).get_list_of_generation_levels_names()       
        lst_levels = ttk.Combobox (self.main, state = 'readonly')
        lst_levels['values'] = (lst_values_level)
        lst_levels.current(0)
        lst_levels.place(x = 100, y = 220)
        
        self.show_details_of_level(lst_values_level[0])

    def show_details_of_level(self, level_name):

        """
        function calls getdetailsofgenerationlevels function from "readconfigfile" class to get the details of specific level type, this info is read from config file.
        and this info will be populated in top and bottom limit boxes in the UI
        
        """
        details_level = ReadConfigFile(self.file_config).get_details_of_generation_levels(level_name)
        top_limit = StringVar()
        botton_limit = StringVar()
        top_limit.set(details_level[1])
        botton_limit.set(details_level[2])
        top_limit = Entry(self.main, textvariable = top_limit).place(x = 100, y = 250)
        botton_limit = Entry(self.main,textvariable = botton_limit).place(x = 100, y = 280)

    def quit(self):
        """
        function will close the window and application

        """
        sys.exit()
