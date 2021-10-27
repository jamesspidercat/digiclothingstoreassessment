import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import *
class GUI:
    def __init__(self,parent):
        #---setup stuff---
        self.parent = parent
        self.parent.title("Clothing Store")
        self.parent.geometry("500x500+0+0")
        self.parent.bind('<Escape>', self.close)
        #---widgets---
        self.frame = Frame(self.parent,bd=0,height=1)
        self.lbl_sold = Label(self.frame,text="Sold: 0",anchor="w", bg='red')
        self.lbl_instock = Label(self.frame,text="In Stock: 0",anchor="e",bg='green')

        #---pack---
        self.frame.pack(fill=X)
        self.lbl_sold.pack(side='left')
        self.lbl_instock.pack(side='right')

        test = Clothing(parent,'test',4)
    #defs
    def close(self,event):
        if (messagebox.askquestion('Exit?',"Are you sure you want to quit") == 'yes'):
            self.parent.destroy()
class Clothing:
    def __init__(self,parent,name,stock):
        self.name = name
        self.stock = stock
        self.parent = parent
        self.frame = LabelFrame(self.parent,text=self.name)
        self.lbl = Label(self.frame,text='test',bg='blue')
        #pack
        self.frame.pack(fill=BOTH,expand='yes',padx=5)
        self.lbl.pack()
#main stuff
root = Tk()
form = GUI(root)
root.mainloop()