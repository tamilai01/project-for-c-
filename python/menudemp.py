import tkinter as tk
from tkinter import *
win=tk.Tk()
win.geometry("500x500")
win.title("student management system")
def exit():
    win.destroy()
def close():
    win.destroy()
def aboutpage():
    abt=tk.Tk()
    why=tk.Tk()
    abt.title("About us")
    why.title("why this notepad")
    abt.geometry("300x300")
    """Welcome to parent window
    created on : 23-02-2024
    by Tamil
    """
    why.geometry("300x300")
    message="""Notepad is a text editor, i.e., an app specialized in editing plain text.
      It can edit text files (bearing the ". txt" filename extension)
      and compatible formats, such as batch files, INI files, and log files. 
    """
    message="""Welcome to parent window
    created on : 23-02-2024
    by Tamil
    """
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()

menubar=tk.Menu(win) 
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)

filemenu.add_command(label="New",  underline=0, accelerator="Alt+N")
filemenu.add_command(label="New window",  underline=4, accelerator="Alt+N")
filemenu.add_command(label="Open",  underline=0, accelerator="Alt+O")
filemenu.add_command(label="Save",  underline=0, accelerator="Alt+S")
filemenu.add_command(label="SaveAs",  underline=4, accelerator="")
filemenu.add_separator()
filemenu.add_command(label="PageSetup",  underline=7, accelerator="")
filemenu.add_command(label="Print",  underline=0, accelerator="crlt+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",  underline=1, command=quit, accelerator="")
win.bind("<Control-3>", exit)
filemenu.add_command(label="close",  underline=1, command=quit, accelerator="")
win.bind("<Control-3>", close)


editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu,underline=0)

editmenu.add_command(label="undo",  underline=0, accelerator="ctrl+Z")
editmenu.add_command(label="redo",  underline=4, accelerator="")
editmenu.add_separator()
editmenu.add_command(label="copy",  underline=0, accelerator="ctrl+C")
editmenu.add_command(label="cut",  underline=0, accelerator="ctrl+X")
editmenu.add_command(label="paste",  underline=4, accelerator="ctrl+V")
editmenu.add_command(label="delete",  underline=4, accelerator="del")
editmenu.add_command(label="paste",  underline=4, accelerator="ctrl+V")
editmenu.add_separator()
editmenu.add_command(label="find",  underline=4, accelerator="ctrl+F")
editmenu.add_command(label="findnext",  underline=4, accelerator="ctrl+F3")
editmenu.add_command(label="replace",  underline=4, accelerator="ctrl+H")
editmenu.add_command(label="go to..",  underline=4, accelerator="ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="select all",  underline=4, accelerator="ctrl+A")
editmenu.add_command(label="Time and Date",  underline=4, accelerator="F5")



formatmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu,underline=0)
formatmenu.add_command(label="Word Wrap",  underline=0)
formatmenu.add_command(label="Font..",  underline=4)


viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu,underline=0)
viewmenu.add_command(label="status bar",  underline=0)

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
helpmenu.add_command(label="view help",  underline=0)
helpmenu.add_separator()
helpmenu.add_command(label="about page",  underline=0,command=aboutpage)




win.config(menu=menubar)
win.mainloop()


