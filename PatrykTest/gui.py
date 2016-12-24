import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import *
import tkFileDialog
from sf2rconverter.root2tk import plot_3d_2canvas
from sf2rconverter.sf2r_lib import sf2r_manager

from os import *

class GUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        #VARIABLES
        self.filelist=[]
        self.file=" "
        self.folder="."
        ############################## 
        
        self.win = parent
        self.win.geometry("1600x1200")
        self.win.title("GUI-V1")
        #MENU
        self.menu=Menu(self.win)
        self.menu.add_command(label="EXIT",command=self.EXIT)
        #FRAMES
        self.f1 = Frame(self.win)  # TREE
        self.f1_B = Frame(self.f1)  # buttons
        self.f1_L = Frame(self.f1)  # list

        self.f2 = Frame(self.win)  # opcje w przyszlosci
        self.f2_B = Frame(self.f2)  # buttons
         
        self.f3 = Frame(self.win,height=300, width=1500)
        self.f3_1=0 # tak ma byc

        

        # BUTTONSi
        self.b1 = Button(self.win, text="EXIT",bg="red", fg="white")  # EXIT

        self.b2 = Button(self.f1_B, text="REFRESH")  # TREE
        self.b3 = Button(self.f1_B, text="LOAD")
        self.b7 = Button(self.f1_B, text="FOLDER")

        self.b4 = Button(self.f2_B, text="B 1")  # CANVAS
        self.b5 = Button(self.f2_B, text="B 2")
        self.b6 = Button(self.f2_B, text="B 3")
        self.b8= Button(self.f2_B,text="B 4")
        # LABELS
        self.l1=Label(self.win,text="START")

        # LISTBOX
        self.lb1 = Listbox(self.f1_L, height=5)
        #self.lb2 = Listbox(self.win, height=5)

        # SCROOLBARS
        self.sb1 = Scrollbar(self.f1_L, orient=VERTICAL)
        

        ############################################


    
        #PACKING
        self.b2.pack(side=LEFT)
        self.b3.pack(side=LEFT)
        self.b4.pack(side=LEFT)
        self.b5.pack(side=LEFT)
        self.b6.pack(side=LEFT)
        self.b7.pack(side=LEFT) 
        self.b8.pack(side=LEFT)

        self.sb1.pack(side=LEFT,fill=Y)
        
        
        self.lb1.pack(side=LEFT)
        
        self.f1_B.pack(side=TOP)
        self.f1_L.pack(side=TOP)
        self.f2_B.grid(row=0,column=0)

        

        #GRID SETUP
        #self.b1.grid(row=3, column=2)
        self.l1.grid(row=1,column=2)
        self.f1.grid(row=5,column=2)
        self.f2.grid(row=1, column= 0)
        self.f3.grid(row=2,column=0,columnspan=5)
       # self.lb2.grid(row = 1, column = 0)


        #Configuration
        self.win.configure(menu=self.menu)
        self.win.columnconfigure(0, minsize=400)
        self.win.columnconfigure(1, minsize=10)
        self.win.columnconfigure(2, minsize=400)
        self.win.columnconfigure(3, minsize=10)

        self.win.columnconfigure(4, minsize=400)
        self.win.columnconfigure(5, minsize=0)       
        self.win.rowconfigure(0, minsize=0)
        self.win.rowconfigure(1,minsize= 0)
        self.win.rowconfigure(2, minsize=0)
        self.win.rowconfigure(3,minsize =0)
        self.win.rowconfigure(4, minsize=250)
        self.win.rowconfigure(5, minsize=0)
       # self.f1.configure(bg="#000066")
        #self.f2.configure(bg="blue")
       # self.f3.configure(bg="white") 
        #self.f3_1.configure(bg="white")
       # self.f3_2.configure(bg="white")
       # self.f3_3.configure(bg="white")

        self.b2.configure(command=self.REFRESH)
        self.b3.configure(command=self.LOAD)
        self.b7.configure(command=self.FOLDER)    
      
        self.l1.configure(width=35,fg="white",font="halvetica",background="blue")
        self.sb1.configure(command=self.lb1.yview)
        self.lb1.configure(yscrollcommand=self.sb1.set) 
       
   
      

        self.REFRESH()
     ##############################################
      #FUNCTOINS
    def LOAD(self): # na razie zachowuje tylko nazwe pliku
      if self.lb1.curselection():
        MGR = sf2r_manager( False  , True) #DEBUG = False API = True
      	self.file=str( self.filelist  [int(self.lb1.curselection()[0])] )
        plots = MGR.run_path(self.folder,self.file) # tu wywala TH1F'y
  
        canvas=[]
        TOOLBAR=[]
        canvas.append(plot_3d_2canvas(plots[0],self.win))

        for i in range(3):
            canvas[0][i].get_tk_widget().grid(row=2,column=2*i)
            TOOLBAR.append(NavigationToolbar2TkAgg(canvas[0][i],self.win))
            TOOLBAR[i].grid(row=3,column=2*i,sticky=NW)
            
      	self.STATUS("FILE " +self.file+" LOADED") 
      
      else:
      	self.STATUS("FILE NOT SELECTED")	
    def REFRESH(self):
      self.lb1.delete(0, END)
      self.filelist=[f for f in listdir(self.folder) if path.isfile(path.join(self.folder,f)) if f != "gui.py"   if f != "gui.pyc"  ]
      #print self.filelist
      for i in self.filelist:
        self.lb1.insert(END,i)
    def FOLDER(self):
      tmp=self.folder
      self.folder=tkFileDialog.askdirectory()
      print self.folder
      if self.folder !=():
      	 self.STATUS("NEW DIRECTORY SELECTED")
      	 self.REFRESH()
      else:
      	self.folder = tmp	

    def STATUS(self,string):# label print 
        self.l1.configure(text=string)

         #CANVAS PLOT
    def D1(self):
      if self.file==" ":
      	self.STATUS("NO FILE LOADED")
      else:
      	self.canvas.delete("all")
      	self.canvas.create_line(0, 0, 200, 100)#na razie cokolwiek
      	self.STATUS("DETECTOR 1") 

    def D2(self):
      if self.file==" ":
      	self.STATUS("NO FILE LOADED")
      else:
      
        self.canvas.delete("all")
        self.canvas.create_line(0, 400, 200, 120)#na razie cokolwiek
        self.STATUS("DETECTOR 2")

    def SP(self):
      if self.file==" ":
        self.STATUS("NO FILE LOADED")
      else:
        self.canvas.delete("all")
        self.canvas.create_line(23, 0, 200, 400)#na razie cokolwiek
        self.STATUS("SP")
       
    def CANVAS_SET(self):
      if(self.f3_1 ):
	self.f3_1.destroy()
        self.f3_2.destroy()
        self.f3_3.destroy()

      self.f3_1=Frame(self.f3,height=600, width=500)
      self.f3_2=Frame(self.f3,height=600, width=500)
      self.f3_3=Frame(self.f3,height=600, width=500)    
      self.f3_1.pack(side=LEFT)
      self.f3_2.pack(side=LEFT)
      self.f3_3.pack(side=LEFT)

    def EXIT(self):
      exit()    
   


if __name__ == "__main__":
    root=Tk()
    GUI(root)
    root.mainloop()   
