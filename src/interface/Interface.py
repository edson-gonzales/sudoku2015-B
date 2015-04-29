import sys
sys.path.append("../console")

from Tkinter import *
from tkFont import Font
from settings_game import SettingsGame
from game_options import GameOptions
from sudokuio import SudokuIO

class Interface(Frame):
    
    def __init__(self, main=None):
        """ Main function, creates a tkinter frame object.
        this will call to initwindow() function, which will create and
        invoke all objects that will be available in the mainwindow.
        """
        Frame.__init__(self, main)
        self.game_options = GameOptions()
        self.main = main
        self.init_window()

    def init_window(self):        
        """Contain the UI objects (labels, buttons, text areas and so on) to be displayed in the window and
        also here has defined the size of the window.                  
        """
        main.geometry("800x500+100+100")
        main.title("Sudoku Game Interface")
                
        #Show Game in a text area        
        self.game_area = Text(self.main, height=20, width=50)        
        self.game_area.place(x=150,y=10)

        #buttons section
        self.show_buttons()     
        
        main.mainloop()

    def show_buttons(self):
        """Create the window buttons (settings, generate, solve, save and close) in the UI)."""
        settings_button = Button(self.main, text = "Settings", width = 10, heigh = 2, command = self.settings)
        settings_button.place(x = 10, y = 10)

        # generation button 
        generate_button = Button(self.main,text = "Generate", width = 10, heigh = 2, command = lambda:self.generate_game_button(self.game_options))
        generate_button.place(x = 10, y = 60)

        # solve button
        solve_button = Button(self.main, text = "Solve", width = 10, heigh = 2, command = lambda:self.solve_game_button(self.game_options))
        solve_button.place(x = 10, y = 120)

        # save button
        save_button = Button(main, text = "Save", width = 10, heigh = 2, command = lambda:self.save_game_button(self.game_options))
        save_button.place(x = 10, y = 180)

        # close button
        close_button = Button(main, text = "Close", width = 10, heigh = 2, command = self.quit)
        close_button.place(x = 10, y = 240)

    def settings(self):
        """invoke SettingsGame class to displays Soduko Configuration setting window."""
        settings = SettingsGame(self.main)

    def solve_game_button(self, game_options):
        """Invoke to solve_game method from GameOption class.

        GameOptions game_options - this is the class that manege the events for the buttons.
        """
        solve_game = game_options.solve_game()
        grid_string = None
        if solve_game == None:
            grid_string = 'There is not solution for the sudoku game'
        else:
            grid_string = SudokuIO.format_grid_to_string(solve_game)                
        self.set_text(grid_string)

    def generate_game_button(self, game_options):
        """Invoke to generate_game method from GameOption class.

        GameOptions game_options - this is the class that manege the events for the buttons.
        """
        generate_game = game_options.generate_game()
        grid_string = SudokuIO.format_grid_to_string(generate_game)        
        self.set_text(grid_string)

    def save_game_button(self, game_options):
        """Invoke to save_game method from GameOption class.

        GameOptions game_options - this is the class that manege the events for the buttons.
        """
        save_game = game_options.save_game()

    def clear_text( self ):
        """Clear Game text area."""

        self.game_area.delete( 1.0, END )

    def get_text( self ):
        """Return game text area value."""

        text = self.game_area.get( 1.0, END )
        if ( text is not None ):
            text = text.strip()
        if ( text == "" ):
            text = None
        return text

    def set_text( self, value ):
        """Set the new value in game text area."""

        self.clear_text()
        if ( value is not None ):
            self.game_area.insert( END, value.strip() )

    def quit(self):
        """Close the application."""
        sys.exit()

if __name__ == '__main__':
    main = Tk()
    current = Interface(main)