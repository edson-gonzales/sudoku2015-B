# class settings
from Tkinter import *
import ttk

class SettingsGame(Frame):

	def __init__(self):
		main=Tk()
		#Frame.__init__(self,main)
		#self.main=main
		self.initwindow(main)

	def initwindow(self,main):
		
		main.geometry("600x400+200+200")
		main.title("Settings Sudoku Game")
	
		#definying the UI option to shown up and edit the values of Output file
		Label(main,text="Output File Config:").place(x=15,y=10)
		Label(main,text="Path: ").place(x=15,y=35)
		Label(main,text="Name: ").place(x=15,y=65)
		Label(main,text="Ext.: ").place(x=230,y=65)

		outputf1=Entry(main).place(x=100,y=35)
		outputf2=Entry(main).place(x=100,y=65)

		self.Listofsupportedfilestypes(main)

		#create a listbox to list all  to list the available algorithms 
		Label(main,text="Solve Algorithm:").place(x=15,y=90)
		Label(main,text="Algorithm: ").place(x=15,y=115)
		self.ShowListAlgorithms(main)

		#Creaate a combo box with levels values
		Label(main,text=" Complexity :").place(x=15,y=200)
		Label(main,text=" Level :").place(x=15,y=220)
		self.showlevelcombobox(main)
		Label(main,text="TopLimit: ").place(x=15,y=250)
		Label(main,text="BottonLimit: ").place(x=15,y=280)
		toplimit=Entry(main).place(x=100,y=250)
		bottonlimit=Entry(main).place(x=100,y=280)


		#buttons
		savebutton=Button(main,text=" Save ", width=10,heigh=2)
		savebutton.place(x=100,y=330)

		closebutton=Button(main,text=" Close ", width=10,heigh=2,command=self.quit)
		closebutton.place(x=200,y=330)

		main.mainloop()

	def Listofsupportedfilestypes(self,main):

		listtypes=["Txt","csv","xml"]	
		lsttypes = ttk.Combobox (main, state='readonly',value=listtypes,width=5)
		lsttypes.place(x=270,y=65)


	def ShowListAlgorithms(self,main):
		#lstvalues=readfile()
		lstvalues=["Peter","backtracking","Others"]
		
		lstAlgorithms=Listbox(main,heigh=4)
		pos=6
		for index in range(len(lstvalues)):
			lstAlgorithms.insert(index,lstvalues[index])			
			pos=pos+1
		
		lstAlgorithms.place(x=100,y=120)
			
	def showlevelcombobox(self,main):
		
		listvalueslevel=["Easy","Medium","Hard","Custom"]		
		lstLevels = ttk.Combobox (main, state='readonly',value=listvalueslevel)
		lstLevels.place(x=100,y=220)
		
	def quit(self):
		sys.exit()

#if __name__ == '__main__':
#main=Tk()
#SettingsGame(main)
