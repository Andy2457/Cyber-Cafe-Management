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
l3=tkinter.Label(win,text="Delete",fg="brown",bg="Peru",font=("The Poster King",30))
l3.place(x=100,y=200)
count=0
globalid=0
def reset():
    customerid.set("")
    name.set("")
    address.set("")
    phone.set("")
    email.set("")
    membership.set("")
    discount.set("")
def back():
    win.destroy()
    os.system("python cinfo.py")

def find():
    idd=int(customerid.get())
    globalid=idd
    if idd>count:
        messagebox.showinfo("CCM","No Such Customer")
        customerid.set("")
        name.set("")
        address.set("")
        phone.set("")
        email.set("")
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
                 address.set(str(i[2]))
                 phone.set(str(i[3]))
                 email.set(str(i[4]))
                 membership.set(str(i[5]))
                 discount.set(str(i[6]))
def dele():
    ans=messagebox.askquestion("RMS","Are You Sure To Delete")
    if ans=="yes":
        idd=customerid.get()
        c1.execute("delete from Add_new_customer where Customer_nameID="+str(idd))
        conn.commit()
        messagebox.showinfo("CCM","Operation Sucessful")
        win.destroy()
        os.system("python cinfo.py")
customerid=StringVar()
name=StringVar()
address=StringVar()
phone=StringVar()
email=StringVar()
membership=StringVar()
discount=StringVar()
c1.execute("select * from Add_new_customer")
result=c1.fetchall()

for i in result:
    count+=1
sett=count+1
b1=ttk.Button(win,text="Find",command=find).place(x=600,y=250,width=200,height=40)
l2=tkinter.Label(win,text="Customer ID :",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=250)
l3=tkinter.Label(win,text="Name:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=300)
l4=tkinter.Label(win,text="Address:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=350)
l5=tkinter.Label(win,text="Phone no.:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=400)
l8=tkinter.Label(win,text="Email Address:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=450)
l6=tkinter.Label(win,text="Membership:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=500)
l7=tkinter.Label(win,text="Discount:",fg="white",bg="peru",font=("Constantia",20,'bold')).place(x=20,y=550)
idd=ttk.Entry(win,state="normal",textvariable=customerid).place(x=220,y=250,width=300,height=40)
nme=ttk.Entry(win,textvariable=name,state="readonly").place(x=220,y=300,width=300,height=40)
ad=ttk.Entry(win,textvariable=address,state="readonly").place(x=220,y=350,width=300,height=40)
ead=ttk.Entry(win,textvariable=email,state="readonly").place(x=220,y=450,width=300,height=40)
mn=ttk.Entry(win,textvariable=phone,state="readonly").place(x=220,y=400,width=300,height=40)
mship=ttk.Entry(win,textvariable=membership,state="readonly").place(x=220,y=500,width=300,height=40)
disc=ttk.Entry(win,textvariable=discount,state="readonly").place(x=220,y=550,width=300,height=40)
b2=ttk.Button(win,text='BACK',command=back).place(x=450,y=600,width=100,height=40)
b3=ttk.Button(win,text='DELETE',command=dele).place(x=300,y=600,width=100,height=40)
b4=ttk.Button(win,text='RESET',command=reset).place(x=150,y=600,width=100,height=40)
win.mainloop()
