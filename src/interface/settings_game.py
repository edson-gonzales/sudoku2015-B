from Tkinter import *
import tkFileDialog
import os 
import ttk
from read_config_file import ReadConfigFile
from save_config_file import SaveConfigFile

class SettingsGame(Frame):

    def __init__(self, parent):
        """ Main function(constructor) -- create the class attributes, and create the tkinter frame instance. """
        main = self.main = Toplevel(parent)
        self.file_config = '../../config/config.xml'        
        self.value = ''
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
        Label(self.main, text = "bottomLimit: ").place(x = 15, y = 290)

    def save_output_file(self):        
        """Browse the folder where output file will be created."""
        # define button
        save_as_button=Button(self.main, text = 'Save File', width = 10, heigh = 2,
                              command = self.ask_save_as_filename).place(x = 410, y = 30)
        
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('text files', '.txt'), ('html files', '.html')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'sudoku.txt'         
        options['parent'] = self.main
        options['title'] = 'Choose directory'
             
    def ask_save_as_filename(self):
        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code. """
   
        # get filename
        file_created = tkFileDialog.asksaveasfilename(**self.file_opt)        

        #call method to update the output file value
        file_path = os.path.abspath(file_created) # absolute file path        

        self.fill_values_in_the_output_file_entry(file_path)

    def fill_values_in_the_output_file_entry(self, custom_path=None):
        """Fill Output file path box.

        string get_values_output_file --> ('c:\sudoku\sudoku.txt') it gets the value returned of get_output_file function from "readconfigfile" class. """
        get_file_path = ReadConfigFile(self.file_config).get_output_file()
        self.current_path = StringVar()        
        if custom_path == None:            
            self.current_path.set(get_file_path)        
        else:
            self.current_path.set(custom_path)

        output_file = Entry(self.main, textvariable = self.current_path, width = 50).place(x = 100, y = 40)
                
    def show_list_algorithms(self):
        """Show the algorithms read from configuration file in a combolist."""
        
        self.list_of_algorithms = ReadConfigFile(self.file_config).get_list_of_algorithms()      
        
        self.algorithms_listbox = Listbox(self.main, heigh = 4, selectmode = SINGLE)
        
        for index in range(len(self.list_of_algorithms)):
            self.algorithms_listbox.insert(END,self.list_of_algorithms[index])          
        
        self.algorithms_listbox.selection_set( first = 0 )
        self.algorithms_listbox.bind('<<ListboxSelect>>',self._choose_algorithm)
        self.algorithms_listbox.place(x = 100, y = 130)
            
    def _choose_algorithm(self,event):
        
        try:
            firstIndex = self.algorithms_listbox.curselection()[0]
            self.value = self.list_of_algorithms[int(firstIndex)]
        except IndexError:
            self.value = ''

    def show_level_combobox(self):
        """Show the levels read from configuration file in the combobox."""

        lst_values_level = ReadConfigFile(self.file_config).get_list_of_generation_levels_names()
        self.value_of_combo = lst_values_level[0]      
        self.levels_combo = ttk.Combobox (self.main, state = 'readonly')
        self.levels_combo['values'] = (lst_values_level)
        self.levels_combo.current(0)
        self.levels_combo.place(x = 100, y = 230)
        self.levels_combo.bind("<<ComboboxSelected>>", self.newselection)
        
        self.show_details_of_level(lst_values_level[0])


    def show_details_of_level(self, level_name):
        """Show the top, botton values of a specific level.

        string level_name --> ('Easy')
        """
        details_level = ReadConfigFile(self.file_config).get_details_of_generation_levels(level_name)
        self.top_limit = StringVar()
        self.bottom_limit = StringVar()
        self.top_limit.set(details_level[1])
        self.bottom_limit.set(details_level[2])
        top_limit_e = Entry(self.main, textvariable = self.top_limit).place(x = 100, y = 260)
        bottom_limit_e = Entry(self.main, textvariable = self.bottom_limit).place(x = 100, y = 290)

    def save_settings_config_file(self):
        """Invoke to save_config_file class methods to save the changes made in the UI."""

        # save output file path                
        SaveConfigFile(self.file_config).save_output_file_settings(self.current_path.get())

        # save algorithm        
        SaveConfigFile(self.file_config).validate_alg_name(self.value)       

        list_level_details = [self.value_of_combo,self.top_limit.get(),self.bottom_limit.get()]
        SaveConfigFile(self.file_config).save_level_settings(list_level_details)

    def newselection(self, event):
        self.value_of_combo = self.levels_combo.get()
        self.show_details_of_level(self.value_of_combo)


    def quit(self):
        """ This function closes the window."""
        self.main.destroy()
