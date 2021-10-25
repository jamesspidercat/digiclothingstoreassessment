import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import *
import os
class GUI:
    def __init__(self,parent):
        #---setup stuff---
        self.parent = parent
        self.parent.title("Clothing Store")
        self.parent.geometry("500x500+0+0")
        self.parent.bind('<Escape>', self.close)
        #---widgets---
        self.lbl_sold = Label(self.parent,text="Sold: 0",anchor="w")
        self.lbl_instock = Label(self.parent,text="In Stock: 0",anchor="e")
        #self.btn_img_foward = Button(self.parent,text='>>')

        #---pack---
        self.lbl_sold.place(relx = 0.0,
                  rely = 0.0,
                  anchor ='nw')
        self.lbl_instock.place(relx = 1.0,
                  rely = 0.0,
                  anchor ='ne')
    #defs
    def print_selected(self):
        temp = self.sv.get()
        self.lbl.config(text=temp)
    def close(self,event):
        if (messagebox.askquestion('Exit?',"Are you sure you want to quit") == 'yes'):
            self.parent.destroy()
#main stuff
root = Tk()
form = GUI(root)
root.mainloop()