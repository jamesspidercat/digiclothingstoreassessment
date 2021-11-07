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
        self.sold = 0
        #---widgets---
        self.frame = Frame(self.parent,bd=0,height=1)
        self.lbl_sold = Label(self.frame,text="Sold: 0",anchor="w", bg='red')
        self.lbl_instock = Label(self.frame,text="In Stock: 0",anchor="e",bg='green')

        #---pack---
        self.frame.pack(fill=X)
        self.lbl_sold.pack(side='left')
        self.lbl_instock.pack(side='right')
        
    #defs
    def clothing_setup(self,parent):
        self.clothing_list = [['Summer Hoodie',8],['Winter Hoodie',12],['Tracksuit',3]]
        self.clothing_objects = []
        for i in range(len(self.clothing_list)):
            setattr(self,'item'+str(i),Clothing(parent,self.clothing_list[i][0],self.clothing_list[i][1]))

    def close(self,event):#on esc press confirms if you want to leave
        if (messagebox.askquestion('Exit?',"Are you sure you want to quit") == 'yes'):
            self.parent.destroy()

    def refresh(self):#when anything being displayed on the gui needs to update it is done here
        instock = 0
        for i in self.clothing_objects:
            i.refresh()
            instock += i.stock
        self.lbl_instock.config(text='In Stock: '+str(instock))
        self.lbl_sold.config(text='Sold: '+str(self.sold))

class Clothing:
    def __init__(self,parent,name,stock):
        self.name = name
        self.stock = stock
        self.parent = parent
        gui.clothing_objects.append(self)

        #widgits
        self.frame = LabelFrame(self.parent,text=self.name)
        self.lbl = Label(self.frame,text='In Stock: '+str(self.stock),pady=5)
        self.btn = Button(self.frame,text='Sell', command=self.sell,state='active')

        #pack
        self.frame.pack(fill=BOTH,expand='no',padx=5,pady=5,ipady=5)
        self.lbl.pack()
        self.btn.pack()
        gui.refresh()

    def sell(self):
        self.stock -= 1
        gui.sold += 1
        gui.refresh()
    def refresh(self):
        if (self.stock < 1):
            self.btn.config(state='disabled')
            self.lbl.config(fg='red')
        else:
            self.btn.config(state='active')
            self.lbl.config(fg='black')
            
        self.lbl.config(text='In Stock: '+str(self.stock))
#main stuff
root = Tk()
gui = GUI(root)
gui.clothing_setup(root)
root.mainloop()
