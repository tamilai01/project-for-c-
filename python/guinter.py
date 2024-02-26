from tkinter import *
app=Tk()
app.title("Gui simple calculater")
app.geometry("500x500+500+100")
app.config(bg="aqua")
def add():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a+b
   labeloutput.config(text=c)

def sub():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a-b
   labeloutput.config(text=c)

def Multiply():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a*b
   labeloutput.config(text=c)


def mod():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a%b
   labeloutput.config(text=c)


def div():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a/b
   labeloutput.config(text=c)


def expo():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a**b
   labeloutput.config(text=c)
 

def flrdiv():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a//b
   labeloutput.config(text=c)
 

def lessthan():
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a<b
   labeloutput.config(text=c)
 

def greaterthan():

   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a<b
   labeloutput.config(text=c)
 

 
def equalto():
   
   a=int(inputbox1.get())
   b=int(inputbox2.get())
   c=a==b
   labeloutput.config(text=c)




lblTitle=Label(text="Simple calculator", fg="crimson")
lblTitle.grid(row=0,column=2,padx=60,pady=10) 

lblTitle1=Label(app,text="Enter first number", fg="crimson",font="serif")
lblTitle1.grid(row=1,column=1,padx=5,pady=5)


inputbox1=Entry(app,width=5)
inputbox1.grid(row=1,column=2)


lblTitle3=Label(app,text="Enter second number", fg="crimson",font="serif")
lblTitle3.grid(row=2,column=1,padx=5,pady=5)


inputbox2=Entry(app,width=5)
inputbox2.grid(row=2,column=2)



labeloutput=Label(app, text="click")
labeloutput.grid(row=2, column=10,pady=5)



btnadd=Button(app,text="+",command=add,fg="crimson")

btnadd.grid(row=3,column=1,padx=5,pady=5)


btnsub=Button(app,text="-",command=sub,fg="crimson")


btnsub.grid(row=3,column=2,padx=5,pady=5)

btnmultiply=Button(app,text="*",command=Multiply,fg="crimson")
btnmultiply.grid(row=3,column=3,padx=5,pady=5)


btnmod=Button(app,text="%",command=mod,fg="crimson")
btnmod.grid(row=3,column=4,padx=5,pady=5)


btndiv=Button(app,text="/",command=div,fg="crimson")
btndiv.grid(row=3,column=5,padx=5,pady=5)


btnmod=Button(app,text="**",command=expo,fg="crimson")

btnmod.grid(row=3,column=6,padx=5,pady=5)

btnflrdiv=Button(app,text="//",command=flrdiv,fg="crimson")

btnflrdiv.grid(row=3,column=7,padx=5,pady=5)

btnlessthan=Button(app,text="<",command=lessthan,fg="crimson")

btnlessthan.grid(row=3,column=8,padx=5,pady=5)


btnlessthan=Button(app,text=">",command=greaterthan,fg="crimson")

btnlessthan.grid(row=3,column=9,padx=5,pady=5)


btnequalto=Button(app,text="==",command=equalto,fg="crimson")
btnequalto.grid(row=3,column=10,padx=5,pady=5)













# lblTitle4=Label(app,text="-", command=sub, fg="crimson")
# lblTitle4.grid(row=6,column=1,padx=10,pady=10);



    
app.mainloop()