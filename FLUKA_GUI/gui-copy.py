import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import *
import tkFileDialog
from sf2rconverter.root2tk import plot_3d_2canvas
from sf2rconverter.sf2r_lib import sf2r_manager
import tkTree as tkt
import os
from os import *


def get_contents(node):
  path=os.path.join(*node.full_id())
  for filename in sorted(os.listdir(path)):
    full=os.path.join(path, filename)
    folder=0
    if os.path.isdir(full):
	folder=1
    if (folder== 0 and filename[-4:]==".lis") or folder == 1: #
        node.widget.add_node(name=filename, id=filename, flag=folder)


class GUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        #VARIABLES
        self.filelist=[]
        self.file=" "
        self.folder="."
        self.canvas=[]
        self.TOOLBAR=[]
        ############################## 
        
        self.win = parent
        self.win.geometry("1600x1200")
        self.win.title("GUI-V2")
        #MENU
        self.menu=Menu(self.win)
        self.menu.add_command(label="BUTTON",command=self.EXIT)



        #FRAMES
        self.f1 = Frame(self.win)  # TREE
        self.f1_B = Frame(self.f1)  # buttons
        self.f1_L = Frame(self.f1)  # list

        self.f2 = Frame(self.win)  # opcje w przyszlosci
        self.f2_B = Frame(self.f2)  # buttons
         
        # TREES
        self.tree = tkt.Tree(self.win,'./','./',get_contents_callback=get_contents);        

        # BUTTONS
        self.TREE=[]   # FIND FILE
        self.TREE.append(Button(self.f1_B, text="REFRESH"))
        self.TREE.append(Button(self.f1_B, text="LOAD"))
        self.TREE.append(Button(self.f1_B, text="FOLDER"))

        self.BUTTONS=[]
        self.BUTTONS.append( Button(self.f2_B, text="B 1") )
        self.BUTTONS.append( Button(self.f2_B, text="B 2") )
        self.BUTTONS.append( Button(self.f2_B, text="B 3") )
        self.BUTTONS.append( Button(self.f2_B, text="B 4") )
  
        self.EXIT=Button(self.win,text="EXIT",command=self.EXIT)
        # LABELS
        self.l1=Label(self.win,text="START")

        # LISTBOX
        self.lb1 = Listbox(self.f1_L, height=5)
        #self.lb2 = Listbox(self.win, height=5)

        # SCROOLBARS
        self.sb1 = Scrollbar(self.f1_L, orient=VERTICAL)
        

        ############################################


    
        #PACKING
	for i in self.TREE:
           i.pack(side=LEFT)
	for i in self.BUTTONS:
           i.pack(side=LEFT)

        self.sb1.pack(side=LEFT,fill=Y)
        
        
        self.lb1.pack(side=LEFT)
        
        self.f1_B.pack(side=TOP)
        self.f1_L.pack(side=TOP)
         
        self.f2_B.grid(row=0,column=0)
        self.l1.grid(row=1,column=50,columnspan=10)
        self.tree.grid(row=50,column=1,sticky=NW,columnspan=30,rowspan=30)  
                
        self.f1.grid(row=40,column=1,columnspan=10,sticky= NW,rowspan=20)
        self.f2.grid(row=2, column= 0)
        #self.lb2.grid(row = 1, column = 0)
        self.EXIT.grid(row=70,column=90,sticky=NE) 

        #Configuration
        self.win.configure(menu=self.menu)
       
        self.win.columnconfigure(0, minsize=30)
        self.win.columnconfigure(1, minsize=300)
        self.win.columnconfigure(2, minsize=10)
        self.win.columnconfigure(3, minsize=200)
        self.win.columnconfigure(4, minsize=10)

       
        self.win.rowconfigure(2, minsize=200)
        self.win.rowconfigure(3,minsize =100)
      
        for i in range(160):
            self.win.columnconfigure(i,minsize=10)
        for i in range(120):
            self.win.rowconfigure(i,minsize=10)
 
        self.TREE[0].configure(command=self.REFRESH)
        self.TREE[1].configure(command=self.LOAD)
        self.TREE[2].configure(command=self.FOLDER)    
      
        self.l1.configure(width=35,fg="white",font="halvetica",background="blue")
        self.sb1.configure(command=self.lb1.yview)
        self.lb1.configure(yscrollcommand=self.sb1.set) 
        self.EXIT.configure(fg="red")     
    
        self.TREE[1].pack()

        self.REFRESH()
     ##############################################
      #FUNCTOINS
    def LOAD(self):

       self.file = self.tree.cursor_node().get_label()
       if(self.file[-4:] == ".lis"):
        print self.file
        self.STATUS("PLOTTING")
        MGR = sf2r_manager( False  , True) #DEBUG = False API = True
        plots = MGR.run_path(self.folder,self.file) # tu wywala TH1F'y
        
        if self.canvas:
	   for i in range (3):
               self.canvas[0][i].get_tk_widget().destroy()
               self.TOOLBAR[i].destroy()  
               pass                   

        self.canvas=[]
        self.TOOLBAR=[]
        self.canvas.append(plot_3d_2canvas(plots[0],self.win))

        for i in range(2):
            self.canvas[0][i].get_tk_widget().grid(row=3,column=i*65+1,columnspan=40,rowspan=30,sticky=W)
            self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][i],self.win))
            self.TOOLBAR[i].grid(row=33,column=i*65+1,sticky=NW,columnspan=40,rowspan=5)
        self.canvas[0][2].get_tk_widget().grid(row=31,column=40,columnspan=40,rowspan=30,sticky=W)
        self.TOOLBAR.append(NavigationToolbar2TkAgg(self.canvas[0][2],self.win))
        self.TOOLBAR[2].grid(row=61,column=40,columnspan=40,sticky=NW,rowspan=5)   

         
       self.STATUS("FILE " +self.file+" LOADED") 
      
       #else:
     #	 self.STATUS("FILE NOT SELECTED")	

    def REFRESH(self):

      self.lb1.delete(0, END)
      self.filelist=[f for f in listdir(self.folder) if path.isfile(path.join(self.folder,f)) if f != "gui.py"   if f != "gui.pyc"  ]

      

      for i in self.filelist:
        self.lb1.insert(END,i)


    def FOLDER(self):
      tmp=self.folder
      self.folder=tkFileDialog.askdirectory()
      print self.folder
      if self.folder !="":
      	 self.STATUS("NEW DIRECTORY SELECTED")
      	 self.REFRESH()
      else:
      	self.folder = tmp	

    def STATUS(self,string):
        self.l1.configure(text=string)

    def EXIT(self):
      exit()    
   


if __name__ == "__main__":
    root=Tk()
    GUI(root)
    root.mainloop()   
