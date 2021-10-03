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
        self.parent.title("Image Gallery")
        self.parent.geometry("500x500+0+0")
        #setup images
        self.current_image = 0
        self.image_objects = []
        for entry in os.scandir('images'):
            if entry.path.endswith(".gif")and entry.is_file():
                self.image_objects.append(PhotoImage(file=entry.path))
        
        #---widgets---
        self.topnew = Toplevel()
        self.close_top = Button(self.topnew,text='close',command=self.close_top).pack()
        #
        self.lbl_title = Label(self.parent,text="no")
        self.btn_close = Button(self.parent,text='close',command=lambda: self.close(True))
        self.btn_img_foward = Button(self.parent,text='>>',command=self.img_foward)
        self.btn_img_back = Button(self.parent,text='<<',command=self.img_back,state='disabled')
        self.display_image = Label(self.parent,image=self.image_objects[self.current_image])

        #---pack---
        self.display_image.pack(side='bottom')
        self.btn_close.pack()
        self.lbl_title.pack()
        self.btn_img_foward.pack()
        self.btn_img_back.pack()

        #option menu
        items = ['test1','teshhhhhhhhhhhhhh2','test3']
        self.sv = StringVar()
        self.sv.set(items[0])
        self.options = OptionMenu(self.parent,self.sv,*items)
        self.options.pack()
        self.btn = Button(self.parent,text='',command=self.print_selected)
        self.btn.pack()
        self.lbl = Label(self.parent,text='',font=("Arial", 125))
        #
        self.btn_value = Button(self.parent,text='pass',command=lambda: self.display(1))
        self.btn_value.pack()
        self.parent.bind('<Escape>', self.close)
        self.parent.bind('<Key>',self.displainput)
        self.lbl.pack()
    def displainput(self,event):
        self.lbl.config(text=str(event.keysym))
    def display(self,num):
        self.lbl.config(text=str(num))
    def print_selected(self):
        temp = self.sv.get()
        self.lbl.config(text=temp)
    def close(self,event):
        if (messagebox.askquestion('Exit?',"Are you sure you want to quit") == 'yes'):
            self.parent.destroy()
    def close_top(self):
        self.topnew.destroy()
    def img_foward(self):
        self.current_image += 1
        if self.current_image >= (len(self.image_objects)-1):
            self.btn_img_foward.config(state='disabled')
        self.btn_img_back.config(state='active')
        self.display_image.config(image=self.image_objects[self.current_image])

    def img_back(self):
        self.current_image -= 1
        if self.current_image <= 0:
            self.btn_img_back.config(state='disabled')
        self.btn_img_foward.config(state='active')
        self.display_image.config(image=self.image_objects[self.current_image])
#main stuff
root = Tk()
form = GUI(root)
root.mainloop()