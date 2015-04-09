# class settings
from Tkinter import *
import ttk
from readconfigfile import ReadConfigFile

class SettingsGame(Frame):

	def __init__(self):
		main=Tk()
		#Frame.__init__(self,main)
		self.main=main
		self.initwindow()

	def initwindow(self):
		#main = self.main
		self.main.geometry("600x400+200+200")
		self.main.title("Settings Sudoku Game")
	
		#definying the UI option to shown up and edit the values of Output file
		Label(self.main,text="Output File Config:").place(x=15,y=10)
		Label(self.main,text="Path: ").place(x=15,y=40)
		#Label(main,text="Name: ").place(x=15,y=65)
		#Label(main,text="Ext.: ").place(x=230,y=65)
		
		# fill values in the output entry
		self.fillvaluesintheentries()
		
		# for future suported types
		#self.Listofsupportedfilestypes()

		#create a listbox to list all  to list the available algorithms 
		Label(self.main,text="Solve Algorithm:").place(x=15,y=90)
		Label(self.main,text="Algorithm: ").place(x=15,y=115)
		self.ShowListAlgorithms()

		#Creaate a combo box with levels values
		Label(self.main,text=" Complexity :").place(x=15,y=200)
		Label(self.main,text=" Level :").place(x=15,y=220)
		
		#create and fill the combobox
		self.showlevelcombobox()

		Label(self.main,text="TopLimit: ").place(x=15,y=250)
		Label(self.main,text="BottonLimit: ").place(x=15,y=280)
		
		
		#buttons
		savebutton=Button(self.main,text=" Save ", width=10,heigh=2)
		savebutton.place(x=100,y=330)

		closebutton=Button(self.main,text=" Close ", width=10,heigh=2,command=self.quit)
		closebutton.place(x=200,y=330)

		self.main.mainloop()

	def fillvaluesintheentries(self):
		getvaluesoutputfile=ReadConfigFile().getoutputfile()
		currentpath=StringVar()
		#currentname=StringVar()
		currentpath.set(getvaluesoutputfile[0]+'\\'+getvaluesoutputfile[1]+'.'+getvaluesoutputfile[2])
		#currentname.set("name.txt")

		outputf1=Entry(self.main,textvariable=currentpath, width=30).place(x=100,y=40)
		#outputf2=Entry(self.main,textvariable=currentname).place(x=100,y=65)

	def Listofsupportedfilestypes(self):

		listtypes=["txt","csv","xml"]	
		lsttypes = ttk.Combobox (self.main, state='readonly',width=5)
		lsttypes['values']=(listtypes)
		lsttypes.current(0)
		lsttypes.place(x=270,y=65)


	def ShowListAlgorithms(self):
		
		listofalgorithms=ReadConfigFile().getlistofalgorithms()		
		
		lstAlgorithms=Listbox(self.main,heigh=4)
		pos=6
		for index in range(len(listofalgorithms)):
			lstAlgorithms.insert(index,listofalgorithms[index])			
			pos=pos+1
		
		lstAlgorithms.selection_set( first = 0 )
		lstAlgorithms.place(x=100,y=120)
			
	def showlevelcombobox(self):

		listvalueslevel=ReadConfigFile().getlistofgenerationlevelsnames()		
		lstLevels = ttk.Combobox (self.main, state='readonly')
		lstLevels['values']=(listvalueslevel)
		lstLevels.current(0)
		lstLevels.place(x=100,y=220)
		
		self.showdetailsoflevel(listvalueslevel[0])

	def showdetailsoflevel(self,levelname):
		detailslevel=ReadConfigFile().getdetailsofgenerationlevels(levelname)
		toplimit=StringVar()
		bottonlimit=StringVar()
		toplimit.set(detailslevel[1])
		bottonlimit.set(detailslevel[2])
		toplimit=Entry(self.main,textvariable=toplimit).place(x=100,y=250)
		bottonlimit=Entry(self.main,textvariable=bottonlimit).place(x=100,y=280)

	def quit(self):
		sys.exit()

SettingsGame()