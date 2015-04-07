#Interface
import sys
from Tkinter import *
from settings import SettingsGame


class Interface(Frame):
	
	def __init__(self,main=None):
		Frame.__init__(self,main)
		self.main=main
		self.InitWindow()

	def InitWindow(self):
		
		main.geometry("800x500+100+100")
		main.title("Sudoku Game Interface")

		# barmenu options
		self.barmenu()

		#buttons sections
		#settings
		settingsbutton=Button(main,text="Settings", width=10,heigh=2,command=self.settings)
		settingsbutton.place(x=10,y=10)

		# generate button
		generatebutton=Button(main,text="Generate", width=10,heigh=2)
		generatebutton.place(x=10,y=60)

		# Solve button
		solvebutton=Button(main,text="Solve", width=10,heigh=2)
		solvebutton.place(x=10,y=120)

		# Solve button
		savebutton=Button(main,text="Save", width=10,heigh=2)
		savebutton.place(x=10,y=180)

		# close button
		closebutton=Button(main,text="Close", width=10,heigh=2, command=self.quit)
		closebutton.place(x=10,y=240)

		#canvas to show the game
		canvas_game_area=Canvas(main,height=400,width=400,bg="white")
		canvas_game_area.place(x=150,y=10)
	
		#label
		labeltime=Label(main,text="Time: (15:25) Min.")
		labeltime.place(x=200,y=430)

		main.mainloop()

	def barmenu(self):
		barmenu=Menu(main)

		#create the first menu options
		mnuopcions=Menu(main)
		mnuopcions.add_command(label="Settings", command=self.settings)
		mnuopcions.add_command(label="New")
		mnuopcions.add_command(label="Exit", command=self.quit)
		#create the secnd menu options
		mnuhelp=Menu(main)
		mnuhelp.add_command(label="Help Game")
		mnuhelp.add_command(label="About Sudoku Game")
		# add mennus to bar Menu
		barmenu.add_cascade(label="Opcions",menu=mnuopcions)
		barmenu.add_cascade(label="Help",menu=mnuhelp)

		main.config(menu=barmenu)


	def settings(self):

		settings=SettingsGame()


	def quit(self):
		sys.exit()


if __name__ == '__main__':
	main=Tk()
	Interface(main)

