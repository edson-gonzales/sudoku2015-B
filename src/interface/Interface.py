import sys
from Tkinter import *
from settings_game import SettingsGame
from game_options import GameOptions

class Interface(Frame):
    
    def __init__(self, main=None):
        """ Main function, creates a tkinter frame object.
        this will call to initwindow() function, which will create and
        invoke all objects that will be available in the mainwindow.
        """
        Frame.__init__(self, main)
        self.main = main
        self.init_window()

    def init_window(self):        
        """Contain the UI objects (labels, buttons, text areas and so on) to be displayed in the window and
        also here has defined the size of the window.                  
        """
        main.geometry("800x500+100+100")
        main.title("Sudoku Game Interface")
        
        #buttons section
        self.show_buttons()
                
        #canvas area to show the game
        canvas_game_area = Canvas(main, height = 400, width = 400, bg = "white")
        canvas_game_area.place(x = 150, y = 10)
           
        main.mainloop()

    def show_buttons(self):
        """Create the window buttons (settings, generate, solve, save and close) in the UI)."""
        settings_button = Button(self.main, text = "Settings", width = 10, heigh = 2, command = self.settings)
        settings_button.place(x = 10, y = 10)

        # generation button 
        generate_button = Button(self.main,text = "Generate", width = 10, heigh = 2, command = self.generate_game_button)
        generate_button.place(x = 10, y = 60)

        # solve button
        solve_button = Button(self.main, text = "Solve", width = 10, heigh = 2, command = self.solve_game_button)
        solve_button.place(x = 10, y = 120)

        # save button
        save_button = Button(main, text = "Save", width = 10, heigh = 2, command = self.save_game_button)
        save_button.place(x = 10, y = 180)

        # close button
        close_button = Button(main, text = "Close", width = 10, heigh = 2, command = self.quit)
        close_button.place(x = 10, y = 240)

    def settings(self):
        """invoke SettingsGame class to displays Soduko Configuration setting window."""
        settings = SettingsGame(self.main)

    def solve_game_button(self):
        """Invoke to solve_game method from GameOption class."""
        solve_game = GameOptions().solve_game()

    def generate_game_button(self):
        """Invoke to generate_game method from GameOption class."""
        generate_game = GameOptions().generate_game()

    def save_game_button(self):
        """Invoke to save_game method from GameOption class."""
        save_game = GameOptions().save_game()

    def quit(self):
        """Close the application."""
        sys.exit()

if __name__ == '__main__':
    main = Tk()
    current = Interface(main)