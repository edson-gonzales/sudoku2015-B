from Tkinter import *
import tkFileDialog 
import ttk
from read_config_file import ReadConfigFile
from save_config_file import SaveConfigFile

class SettingsGame(Frame):

    def __init__(self, parent):
        """ Main function(constructor) -- create the class attributes, and create the tkinter frame instance. """
        main = self.main = Toplevel(parent)
        self.file_config = '../../config/config.xml'        

        self.init_window()

    def init_window(self):
        """Invoke methods to display the objects in the window (labels, buttons, listbox, combobox)."""
        self.main.geometry("600x400+200+200")
        self.main.title("Settings Sudoku Game")
    
        #show UI labels
        self.show_labels()

        #show buttons
        self.show_buttons()

        # fill values in the output entry
        self.fill_values_in_the_output_file_entry()

        # supported files types                
        self.save_output_file()

        #create a listbox to show all the available algorithms 
        self.show_list_algorithms()
        
        #create and fill the combobox
        self.show_level_combobox()

        self.main.mainloop()
    
    def show_buttons(self):
        """Create save and close buttons in the UI."""
        #save button
        save_button = Button(self.main, text = " Save ", width = 10, heigh = 2, command=self.save_settings_config_file)
        save_button.place(x = 100, y = 330)

        #close button
        close_button = Button(self.main, text = " Close ", width = 10, heigh = 2, command = self.quit)
        close_button.place(x = 200, y = 330)
    
    def show_labels(self):
        """Create the labels to be displayed in the UI."""
        #label for output file section
        Label(self.main, text = "Output File Config:").place(x = 15, y= 10)
        Label(self.main, text = "Path: ").place(x = 15, y = 40)
        
        #label for algorithm section
        Label(self.main, text = "Solve Algorithm:").place(x = 15, y = 100)
        Label(self.main, text = "Algorithm: ").place(x = 15, y = 125)
        #label for complexity section
        Label(self.main, text = " Complexity :").place(x = 15, y= 210)
        Label(self.main, text = " Level :").place(x = 15, y= 230)
        #label for level section
        Label(self.main, text = "TopLimit: ").place(x = 15, y = 260)
        Label(self.main, text = "BottonLimit: ").place(x = 15, y = 290)

    def save_output_file(self):        
        """Browse the folder where output file will be created."""
        # define button
        save_as_button=Button(self.main, text='Save File', width = 10, heigh = 2,
                              command=self.ask_save_as_file).place(x=410, y=30)
        
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('text files', '.txt'), ('csv files', '.csv')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'sudoku.txt'        
        options['parent'] = self.main
        options['title'] = 'Choose directory'
         
    def ask_save_as_file(self):
        """Return an open a file in write mode."""
        file_path=tkFileDialog.asksaveasfile(mode='w', **self.file_opt)        

        return file_path
 
    def fill_values_in_the_output_file_entry(self, custom_path=None):
        """Fill Output file path box.

        string get_values_output_file --> ('c:\sudoku\sudoku.txt') it gets the value returned of get_output_file function from "readconfigfile" class. """
        get_values_output_file = ReadConfigFile(self.file_config).get_output_file()
        current_path = StringVar()
        current_file_name=StringVar()
        if custom_path == None:            
            current_path.set(get_values_output_file[0]+'\\'+get_values_output_file[1])        
        else:
            current_path.set(custom_path)

        output_file = Entry(self.main, textvariable = current_path, width = 50).place(x = 100, y = 40)
        
    def show_list_algorithms(self):
        """Show the algorithms read from configuration file in a combolist."""
        
        list_of_algorithms = ReadConfigFile(self.file_config).get_list_of_algorithms()      
        
        algorithms_listbox = Listbox(self.main, heigh = 4)
        
        for index in range(len(list_of_algorithms)):
            algorithms_listbox.insert(index,list_of_algorithms[index])          
        
        algorithms_listbox.selection_set( first = 0 )
        algorithms_listbox.place(x = 100, y = 130)
            
    def show_level_combobox(self):
        """Show the levels read from configuration file in the combobox."""

        lst_values_level = ReadConfigFile(self.file_config).get_list_of_generation_levels_names()       
        levels_combo = ttk.Combobox (self.main, state = 'readonly')
        levels_combo['values'] = (lst_values_level)
        levels_combo.current(0)
        levels_combo.place(x = 100, y = 230)
        
        self.show_details_of_level(lst_values_level[0])

    def show_details_of_level(self, level_name):
        """Show the top, botton values of a specific level.

        string level_name --> ('Easy')
        """
        details_level = ReadConfigFile(self.file_config).get_details_of_generation_levels(level_name)
        top_limit = StringVar()
        botton_limit = StringVar()
        top_limit.set(details_level[1])
        botton_limit.set(details_level[2])
        top_limit = Entry(self.main, textvariable = top_limit).place(x = 100, y = 260)
        botton_limit = Entry(self.main,textvariable = botton_limit).place(x = 100, y = 290)

    def save_settings_config_file(self):
        """Invoke to save_config_file class methods to save the changes made in the UI."""

        # save output file path
        new_file_path = ['c:\updated\sudoku','sudoku.txt'] 
        SaveConfigFile(self.file_config).save_output_file_settings(new_file_path)

        # save algorithm
        alg_name = 'BruteForce'
        SaveConfigFile(self.file_config).save_algorithm_settings(alg_name)

        # save level settings
        list_level_details = ['Hard',10,30]
        SaveConfigFile(self.file_config).save_level_settings(list_level_details)

    def quit(self):
        """ This function closes the window and application."""
        sys.exit()
