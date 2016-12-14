from Tkinter import *
from os import *

class GUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        #VARIABLES
        self.filelist=[]
	self.file=""
        ############################## 
        
        self.win = parent
	self.win.geometry("1024x800")
        self.win.title("GUI-V1")
        #FRAMES
        self.f1 = Frame(self.win)  # TREE
        self.f1_B = Frame(self.f1)  # buttons
        self.f1_L = Frame(self.f1)  # list

        self.f2 = Frame(self.win)  # canvas
        self.f2_B = Frame(self.f2)  # buttons

        # BUTTONS
        self.b1 = Button(self.win, text="EXIT",bg="red", fg="white")  # EXIT

        self.b2 = Button(self.f1_B, text="REFRESH")  # TREE
        self.b3 = Button(self.f1_B, text="LOAD")

        self.b4 = Button(self.f2_B, text="DETECTOR 1")  # CANVAS
        self.b5 = Button(self.f2_B, text="DETECTOR 2")
        self.b6 = Button(self.f2_B, text="SP")

        # LABELS
        

        # LISTBOX
        self.lb1 = Listbox(self.f1_L, height=5)

        # SCROOLBARS
        self.sb1 = Scrollbar(self.f1_L, orient=VERTICAL)

        # canvas
        self.canvas=Canvas(self.f2,width=600,height=600)
        ############################################


    
        #PACKING
        self.b2.pack(side=LEFT)
        self.b3.pack(side=LEFT)
        self.b4.pack(side=LEFT)
        self.b5.pack(side=LEFT)
        self.b6.pack(side=LEFT)


        self.sb1.pack(side=LEFT,fill=Y)
        self.lb1.pack(side=LEFT)

        self.f1_B.pack(side=TOP)
        self.f1_L.pack(side=TOP)
        self.f2_B.pack(side=BOTTOM)

        self.canvas.pack(side=TOP)


        #GRID SETUP
        self.b1.grid(row=25, column=25)
        self.f1.grid(row=0,column=0)
        self.f2.grid(row=1, column= 10)

        #Configuration
        self.b1.configure(command=self.EXIT)
        self.b2.configure(command=self.REFRESH)
        self.b3.configure(command=self.LOAD)  
        self.b4.configure(command=self.D1)
        self.b5.configure(command=self.D2)
        self.b6.configure(command=self.SP)
        
        self.sb1.configure(command=self.lb1.yview)
        self.lb1.configure(yscrollcommand=self.sb1.set)
   
        self.canvas.configure(background='white')

        self.REFRESH()
     ##############################################
      #FUNCTOINS
    def LOAD(self): # na razie zachowuje tylko nazwe pliku
      self.file=str( self.filelist  [int(self.lb1.curselection()[0])] )
      print self.file
    def REFRESH(self):
      self.lb1.delete(0, END)
      self.filelist=[f for f in listdir(".") if path.isfile(path.join(".",f)) if f != "gui.py"   if f != "gui.pyc"  ]
      #print self.filelist
      for i in self.filelist:
        self.lb1.insert(END,i)
               
         #CANVAS PLOT
    def D1(self):
      self.canvas.delete("all")
      self.canvas.create_line(0, 0, 200, 100)#na razie cokolwiek
      
    def D2(self):
      self.canvas.delete("all")
      self.canvas.create_line(0, 400, 200, 120)#na razie cokolwiek
      
    def SP(self):
      self.canvas.delete("all")
      self.canvas.create_line(23, 0, 200, 400)#na razie cokolwiek
      
    def EXIT(self):
      exit()    
   


if __name__ == "__main__":
    root=Tk()
    GUI(root)
    root.mainloop()
