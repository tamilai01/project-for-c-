import tkinter as tk
from tkinter import *
win=tk.Tk()
win.geometry("500x500")
win.title("Student management system")
def exit():
    win.destroy()
def aboutpage():
    abt=tk.Tk()
    abt.title("About us")
    abt.geometry("300x300")
    """welcome to parent Window
    created on:23-02-2024
    by Tamil"""
    message= """welcome to parent Window
    created on:23-02-2024
    by Tamil"""
    
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()

menubar=tk.Menu(win) 
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="N",  underline=0, accelerator="Alt+N")
filemenu.add_command(label="New",  underline=0, accelerator="Alt+N")
filemenu.add_command(label="New",  underline=0, accelerator="Alt+N")
filemenu.add_command(label="New",  underline=0, accelerator="Alt+N")
filemenu.add_command(label="New",  underline=0, accelerator="Alt+N")



win.mainloop()