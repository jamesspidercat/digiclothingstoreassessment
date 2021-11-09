#imports
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#classes
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
    def restock_setup(self):
        #dropdown menu
        self.option_selected = StringVar()
        self.option_selected.set("Select Item To Restock")
        self.optmenu_items = []

        for i in self.clothing_objects:
            self.optmenu_items.append(i.name)
        
        self.optmenu_restock = OptionMenu(self.parent,self.option_selected,*self.optmenu_items)
        #number entry
        self.entry_lbl = Label(self.parent, text='Restock Amount:')
        self.entry_text = StringVar()
        self.entry_restock = Entry(self.parent,textvariable=self.entry_text)
        self.entry_restock.bind('<Return>',self.restock)
        #button
        self.btn_restock = Button(self.parent,text="Restock",command=self.restock)
        #pack
        self.optmenu_restock.pack()
        self.entry_lbl.pack()
        self.entry_restock.pack()
        self.btn_restock.pack()

    def restock(self,event="button"):
        try:#checks if you have entered a number in the textbox, if not displays error
            self.restock_ammount = int(self.entry_text.get())
        except:
            messagebox.showerror('Error','Please Enter A Valid Number')
            return
        temp = False
        if (self.restock_ammount > 0):
            for i in self.clothing_objects:
                if (i.name == self.option_selected.get()):
                    i.stock += self.restock_ammount
                    self.refresh()
                    temp = True
                    break
            if (temp == False):
                messagebox.showerror('Error','Please Select An Item Of Clothing To Restock')
        else:
            messagebox.showerror('Error','Please Enter A Positive Number Above 0')

    def clothing_setup(self):
        self.clothing_list = [['Summer Hoodie',8],['Winter Hoodie',12],['Tracksuit',3]]#you can edit avalible clothing and stock here
        self.clothing_objects = []
        for i in range(len(self.clothing_list)):
            setattr(self,'item'+str(i),Clothing(self.parent,self.clothing_list[i][0],self.clothing_list[i][1]))

    def close(self,event):#on esc press; confirms if you want to leave
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
gui.clothing_setup()
gui.restock_setup()
root.mainloop()
