from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as sql
conn=sql.connect(host ='localhost',user ='root',password ='tiger')
c1=conn.cursor()
c1.execute('create database if not exists Cyber_Cafe')
c1.execute('use Cyber_Cafe')
c1.execute('create table if not exists Add_new_customer(Customer_nameID int(100),Customer_name varchar(20),Address varchar(100),Phone_no varchar(12),Email_ID varchar(40),Membership varchar(50),Discount varchar(10))')
c1.execute('create table if not exists Bill(Customer_nameID int(100),Customer_name varchar(20),Membership varchar(50),Discount varchar(10),Time int(100),Total int(100))')
win=Tk()
win.title('CCM')
win.geometry("900x700")
bg=PhotoImage(file=r"1\images\bg2.png")
labelforimage=tkinter.Label(win,image=bg)
labelforimage.place(x=580,y=10)
win.config(bg="Peru")
win.resizable(False,False)
l1=tkinter.Label(win,text="CYBER_CAFE",fg="black",bg="Peru",font=("The Poster King",50))
l1.place(x=89,y=5)
l2=tkinter.Label(win,text="MANAGEMENT",fg="black",bg="Peru",font=("The Poster King",50))
l2.place(x=80,y=100)
l3=tkinter.Label(win,text="                      BILL",fg="brown",bg="Peru",font=("The Poster King",30))
l3.place(x=100,y=200)
count=0
globalid=0
def find():
    idd=int(customerid.get())
    globalid=idd
    if idd>count:
        messagebox.showinfo("CCM","No Such Customer")
        customerid.set("")
        name.set("")
        membership.set("")
        discount.set("")
    else:
         win.geometry("900x700")
         c1.execute("select * from Add_new_customer")
         result=c1.fetchall()
         for i in result:
             if str(i[0])==str(idd):
                 customerid.set(str(idd))
                 name.set(str(i[1]))
                 membership.set(str(i[5]))
                 discount.set(str(i[6]))
def back():
    win.destroy()
    os.system("python layer2.py")
def reset():
    customerid.set("")
    name.set("")
    membership.set("")
    discount.set("")
    used.set("Select")
    time.set("Select")
    total.set("")
def total1():
    d=(discount.get())
    dis= int(str(d)[:-1])
    a=int(time.get())
    t=a*50-(a*50*(dis/100))
    total.set(str(t))
def save():
    c=customerid.get()
    n=name.get()
    m=membership.get()
    d=discount.get()
    t=time.get()
    to=total.get()
    c1.execute("insert Bill values ("+str(c)+",'"+str(n)+"','"+str(m)+"','"+str(d)+"','"+str(t)+"','"+str(to)+"')")
    conn.commit()
    win.destroy()
    messagebox.showinfo("CCM","Entered Successfully.")
    os.system("python layer2.py")
customerid=StringVar()
name=StringVar()
used=StringVar()
membership=StringVar()
time=StringVar()
discount=StringVar()
total=StringVar()
c1.execute("select * from Add_new_customer")
result=c1.fetchall()


for i in result:
    count+=1
sett=count+1


b1=ttk.Button(win,text="Find",command=find).place(x=600,y=250,width=200,height=40)
l3=tkinter.Label(win,text="Customer ID :",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=250)
l4=tkinter.Label(win,text="Time Consumed:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=300)
l5=tkinter.Label(win,text="Customer Name :",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=350)
l7=tkinter.Label(win,text="Membership:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=400)
l9=tkinter.Label(win,text="Discount :",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=450)
l8=tkinter.Label(win,text="Total :",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=500)
idd=ttk.Entry(win,state="normal",textvariable=customerid).place(x=250,y=250,width=300,height=40)
mem=ttk.Entry(win,textvariable=membership,state="readonly").place(x=250,y=400,width=400,height=40)
tim=ttk.Entry(win,state="normal",textvariable=time).place(x=250,y=300,width=400,height=40)
disc=ttk.Entry(win,textvariable=discount,state="readonly").place(x=250,y=450,width=300,height=40)
tot=ttk.Entry(win,textvariable=total,state="readonly").place(x=250,y=500,width=300,height=40)
nme=ttk.Entry(win,textvariable=name,state="readonly").place(x=250,y=350,width=300,height=40)
b3=ttk.Button(win,text='Calculate',command=total1).place(x=600,y=500,width=200,height=40)
b2=ttk.Button(win,text='BACK',command=back).place(x=450,y=600,width=100,height=40)
b4=ttk.Button(win,text='RESET',command=reset).place(x=150,y=600,width=100,height=40)
b5=ttk.Button(win,text='SAVE',command=save).place(x=300,y=600,width=100,height=40)
win.mainloop()



