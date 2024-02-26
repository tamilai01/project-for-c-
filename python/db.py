from tkinter import *
import mysql.connector

app=Tk()
app.title("STUDENT MARK LIST")
app.geometry("800x440+300+200")
app.config(bg="lightgreen")
def mydbconnection():
    con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_tamil"
    )
    return con

# print(con)
# print("connceted to database through outside of def at",con)


def insertvalues():
    Name = inputa.get()
    Tamil = inputb.get()
    English = inputc.get()
    Mathematics = inputd.get()
    Science = inpute.get()
    Socialscience = inputf.get()
    e_con= mydbconnection()
    result=e_con.cursor()
    statement="insert into StdMarkdetail(Name,Tamil,English,Mathematics,Science,Socialscience)values(%s,%s,%s,%s,%s,%s);"
    valuepass=(Name,Tamil,English,Mathematics,Science,Socialscience)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row inserted")


def updatevalues():
    Name = inputa.get()
    Tamil = inputb.get()
    e_con= mydbconnection()
    result=e_con.cursor()
    statement="update StdMarkdetail set name=(%s) where sno= (%s);"
    valuepass=(Name,Tamil)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row updated")

def deletevalues():
    Name = inputa.get()
    e_con= mydbconnection()
    result=e_con.cursor()
    statement="delete from StdMarkdetail where sno= (%s);"
    valuepass=(Name,)
    result.execute(statement,valuepass)
    e_con.commit()

    print(result.rowcount,"row deleted")

lbltitle=Label(app,text="Student Name")
lbltitle.grid(row=1, column=1, padx=100 , pady=20)



inputa=Entry(app, width=20)
inputa.grid(row=1, column=2)

lbltitle=Label(app,text="Tamil")
lbltitle.grid(row=2, column=1, padx=100 , pady=20)


inputb=Entry(app, width=20)
inputb.grid(row=2, column=2)



lbltitle=Label(app,text="English")
lbltitle.grid(row=3, column=1, padx=100 , pady=20)


inputc=Entry(app, width=20)
inputc.grid(row=3, column=2)


lbltitle=Label(app,text="Mathematics")
lbltitle.grid(row=4, column=1, padx=100 , pady=20)


inputd=Entry(app, width=20)
inputd.grid(row=4, column=2)



lbltitle=Label(app,text="Science")
lbltitle.grid(row=5, column=1, padx=100 , pady=20)


inpute=Entry(app, width=20)
inpute.grid(row=5, column=2)


lbltitle=Label(app,text="Socialscince")
lbltitle.grid(row=6, column=1, padx=100 , pady=10)


inputf=Entry(app, width=20)
inputf.grid(row=6, column=2)

btnAdd=Button(app,text="Insert",command=insertvalues)
btnAdd.grid(row=8,column=3)


btnAdd=Button(app,text="Update",command=updatevalues)
btnAdd.grid(row=8,column=4)

btnAdd=Button(app,text="Delete",command=deletevalues)
btnAdd.grid(row=8,column=5)

btnAdd=Button(app,text="Reset")
btnAdd.grid(row=8,column=6)





app.mainloop()









