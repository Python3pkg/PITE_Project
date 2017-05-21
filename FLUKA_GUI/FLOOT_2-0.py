import ROOT
import matplotlib
import tkinter.messagebox
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter.filedialog
from .sf2rconverter.root2tk import plot_3d_2canvas, plot_2d_2canvas, plot_1d_2canvas
from .sf2rconverter.sf2r_lib import sf2r_manager, plot_1d, plot_2d, plot_3d
from . import tkTree as tkt
import os
from os import *



def get_contents(node):
  path=os.path.join(*node.full_id())
  for filename in sorted(os.listdir(path)):
    full=os.path.join(path, filename)
    folder=0
    if os.path.isdir(full):
	folder=1
    if (folder== 0 and (filename[-4:]==".lis" or filename[-5:]==".root")) or folder == 1: #
        node.widget.add_node(name=filename, id=filename, flag=folder)

class GUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        #VARIABLES
        self.filelist=[]
        self.file=" "
        self.folder="./Test/Data"
        self.canvas=[]
        self.TOOLBAR=[]
        self.number=3
        ############################## 
        
        self.win = parent
        self.win.geometry("1440x730")
        self.win.title("FLOOT - GUI for FLUKA to ROOT converter")
        #MENU
        self.menu=Menu(self.win)
        self.menu.add_command(label="CONVERT",command=self.CONVERT)
        self.menu.add_command(label="PLOT", command=self.PLOT)
        self.menu.add_command(label="CONVERT AND PLOT",command=self.CONVERT_AND_PLOT)
	self.menu.add_command(label="CHANGE DIRECTORY",command=self.FOLDER)
	self.menu.add_command(label="HELP",command=self.HELP)
	self.menu.add_command(label="QUIT",command=self.EXIT)
        self.l1=Label(self.win,text="START")

        # TREES
        self.tree = tkt.Tree(self.win,'./Test/Data','FLUKA_DIR',get_contents_callback=get_contents)

	self.canv_logo = Canvas(self.win,width=500,height=250)
        ############################################
	self.grid()
	self.l1.grid(column=0,row=0, sticky=NE+SW)
	self.tree.grid(column = 0, row = 1, rowspan = 4, sticky=NE+SW)
	self.canv_logo.grid(column=0,row=5,rowspan=2, sticky=N+S)
	self.logo = PhotoImage(file="floot.gif")
	self.canv_logo.image = self.logo
 

	self.canv_logo.create_image(250,129,image=self.logo)
        #Configuration
        self.win.configure(menu=self.menu)     
        self.tree.configure(background='#EEEEEE', relief='sunken',borderwidth=3)
        self.tree.root.expand()
      
	self.tree.focus_set()
     ##############################################
      #FUNCTOINS
    def layouts(self, histo_num):
		if histo_num>0 and histo_num < 7:
			columns=2
		elif histo_num>=7 and histo_num<=9:
			columns=3
		else:
			ERROR="Nie planuje."
			return ERROR
		histo_num=float(histo_num)
		histo_in_row=int(round(histo_num/columns))
		rows=1+(histo_in_row*2)
		row_size=600/histo_in_row
		for r in range(rows):
			if r%2==0:
				self.win.rowconfigure(r, minsize=10)
			else:
				self.win.rowconfigure(r, minsize=row_size)

		self.win.columnconfigure(0,minsize=200)
		column_size=1000/columns		
		for c in range(1,columns+1):
			self.win.columnconfigure(c,minsize =column_size)

		if histo_num>0 and histo_num <=9:
			histo_ID=0
			if histo_num%2 == 0 and histo_num<7:
				tab=list(range(1,rows))
			elif (histo_num%3==1 or histo_num%3==2) and histo_num>=7:
				tab=list(range(1,rows-2))
			elif histo_num%2 != 0 and histo_num<7:
				tab=list(range(1,rows-2))
			print("ROWS %d" %rows)
			for r in tab[0::2]:
				for c in range(1,columns+1):
					self.canvas[0][histo_ID].get_tk_widget().grid(row=r,column=c)
					histo_ID+=1
			histo_ID=0
			for r in tab[1::2]:
				for c in range(1,columns+1):
					self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][histo_ID],self.win))
					self.TOOLBAR[histo_ID].grid(row=r,column=c)
					histo_ID+=1
                        if histo_num==1:
                          self.canvas[0][histo_ID].get_tk_widget().grid(row=rows-2, column=1,columnspan=2,sticky=N+S+W+E)
                          self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][histo_ID],self.win))
                          self.TOOLBAR[histo_ID].grid(row=rows-1,column=1,columnspan=2,sticky=N+S) 

			if histo_num%2 != 0 and histo_num<7 and histo_num>1:
				self.canvas[0][histo_ID].get_tk_widget().grid(row=rows-2, column=1,columnspan=2,sticky=N+S)
				self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][histo_ID],self.win))
				self.TOOLBAR[histo_ID].grid(row=rows-1,column=1,columnspan=2,sticky=N+S)
			elif histo_num%3==1 and histo_num>=7:
				self.canvas[0][histo_ID].grid(row=rows-2,column=2)
				self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][histo_ID],self.win))
				self.TOOLBAR[histo_ID].grid(row=rows-1,columns=2)
			elif histo_num%3==2 and histo_num>=7:
				self.canvas[0][histo_ID].grid(row=rows-2,column=1,columnspan=2,sticky=W)
				self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][histo_ID],self.win))
				self.TOOLBAR[histo_ID].grid(row=rows-1,columns=3,columnspan=2,sticky=W)
				self.canvas[0][histo_ID+1].grid(row=rows-2,column=2,columnspan=2,sticky=E)
				self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][histo_ID+1],self.win))
				self.TOOLBAR[histo_ID+1].grid(row=rows-1,columns=2,columnspan=2,sticky=E)
		else:
			ERROR="Nie planuje."
			return ERROR
		

    def LOAD(self, plot=True): # plot True jezeli chcemy dodatkowo plotowac, inaczej False

       self.file = self.tree.cursor_node().get_label()
       if(self.file[-4:] == ".lis" or self.file[-5:]==".root"):
        self.STATUS("PLOTTING")
        MGR = sf2r_manager( False  , True) #DEBUG = False API = True
        if (self.file[-4:] == ".lis"):
         plots = MGR.run_path(self.folder,self.file) # tu wywala TH1F'y
        else:
         f = ROOT.TFile.Open(self.file)
         keys = f.GetListOfKeys()
         plots=[]
         p=[]
         for el in keys:
          p.append(f.Get(el.GetName()))
         plots.append(p)
        if self.canvas:
	   for i in range (len(self.canvas[0])):
               self.canvas[0][i].get_tk_widget().destroy()
               self.TOOLBAR[i].destroy()  
               pass   

        self.canvas=[]
        self.TOOLBAR=[]
       
        if plot == False:
            self.STATUS("FILE " +self.file+" ONLY CONVERTED") 
            return

        if isinstance(plots[0],plot_1d):
          self.canvas.append(plot_1d_2canvas(plots[0],self.win))
        elif isinstance(plots[0],plot_2d):
          self.canvas.append(plot_2d_2canvas(plots[0],self.win))
        elif isinstance(plots[0],plot_3d):
          self.canvas.append(plot_3d_2canvas(plots[0],self.win))
        else:
          self.canvas.append(plot_3d_2canvas(plots[0],self.win))#TODO!!!!!          
	self.number=len(self.canvas[0])
	self.layouts(self.number)

       self.tree.focus_set()
       self.STATUS("FILE " +self.file+" CONVERTED AND PLOTTED") 
       self.tree.focus_set()

    def FOLDER(self):
      self.tree.delete(0,END)
      folder=tkinter.filedialog.askdirectory()
      if(folder!='' and isinstance(folder,str)):
       self.folder=folder
       self.tree = tkt.Tree(self.win,self.folder,"FLUKA_DIR",get_contents_callback=get_contents)
       self.tree.configure(background='#EEEEEE', relief='sunken',borderwidth=3)
       self.tree.grid(column = 0, row = 1, rowspan = 5, sticky=NE+SW)
       self.tree.root.expand()
       self.STATUS("NEW DIRECTORY SELECTED")

    def STATUS(self,string):
        self.l1.configure(text=string)
	self.tree.focus_set()

    def EXIT(self):
        exit()    

    def CONVERT(self):
        self.LOAD(plot=False)
	self.tree.focus_set()

    def PLOT(self):
        self.LOAD(plot=True)
	self.tree.focus_set()
    def CONVERT_AND_PLOT(self):
        self.LOAD(plot=True)
	self.tree.focus_set()
   
    def HELP(self):
	tkinter.messagebox.showinfo("Help info","Use your arrow keys to choose file\nENTER to confirm your choice\nYou can only convert this file to ROOT format by clicking CONVERT\nOr convert it and plot, by clicking CONVERT AND PLOT")
	self.tree.focus_set()
   


if __name__ == "__main__":
    root=Tk()
    GUI(root)
    root.mainloop()   
