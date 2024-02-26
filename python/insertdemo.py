from tkinter import*
import mysql.connector
win=Tk()


win.title("Insert into MYSQL DB DEMO ")
win.geometry("500x500")

frameleft=Frame(win,bg="orange",width=500,height=30)
frameleft.pack(side=LEFT)

frameright=Frame(win,bg="green",width=500,height=30)
frameright.pack(side=RIGHT)


lbl_Title_of_Operaton=Label(frametop,text="insert into MYSQL DB DEMO")
lbl_Title_of_Operaton.grid(row=0,column=1)

labelname=Label(frameleft,text="Name")
labelname.grid(row=2,column=1,padx=10,pady=5)


win.mainloop()