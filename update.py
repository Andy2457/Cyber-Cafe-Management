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
l3=tkinter.Label(win,text="Update The Data",fg="brown",bg="Peru",font=("The Poster King",30))
l3.place(x=100,y=200)
count=0
globalid=0
def discc():
    m=membership.get()
    if m=="Select":
        messagebox.showinfo("CCM","Please Select Membership First")
    elif m=="Temporary":
        discount.set("2%")
    elif m=="Basic":
        discount.set("5%")
    elif m=="Premium":
        discount.set("10%")
    elif m=="Platinum":
        discount.set("20%")
def reset():
    customerid.set("")
    name.set("")
    address.set("")
    phone.set("")
    email.set("")
    membership.set("Select")
    discount.set("")
def update():
    c=customerid.get()
    n=name.get()
    a=address.get()
    p=phone.get()
    m=membership.get()
    e=email.get()
    d=discount.get()
    if c=="":
        messagebox.showinfo("CCM","Please Generate ID")
    elif n=="":
        messagebox.showinfo("CCM","Please Enter Name")
    elif a=="":
        messagebox.showinfo("CCM","Please Enter Address")
    elif p=="":
        messagebox.showinfo("CCM","Please Enter Mobile Number")
    elif e=="":
        messagebox.showinfo("CCM","Please Select Email Address")
    elif m=="Select":
        messagebox.showinfo("CCM","Please Select Membership")
    elif d=="":
        messagebox.showinfo("CCM","Please Check Discount")
    else:
        if len(p)==10:
            if m=="Temporary":
                d="2%"
            elif m=="Basic":
                d="5%"
            elif m=="Premium":
                d="10%"
            elif m=="Platinum":
                d="20%"
            c1.execute("update Add_new_customer set Customer_name='"+str(n)+"' where Customer_nameID="+str(c))
            c1.execute("update Add_new_customer set address='"+str(a)+"' where Customer_nameID="+str(c))
            c1.execute("update Add_new_customer set Phone_no='"+str(p)+"' where Customer_nameID="+str(c))
            c1.execute("update Add_new_customer set Email_ID='"+str(e)+"' where Customer_nameID="+str(c))
            c1.execute("update Add_new_customer set membership='"+str(m)+"' where Customer_nameID="+str(c))
            c1.execute("update Add_new_customer set discount='"+str(d)+"' where Customer_nameID="+str(c))
            conn.commit()
            win.destroy()
            messagebox.showinfo("CCM","Entered Successfully.")
            os.system("python cinfo.py")
        else:
            messagebox.showinfo("CCM","Please Enter Valid Mobile No.")

def back():
    win.destroy()
    os.system("python cinfo.py")

def find():
    global globalid
    idd=int(customerid.get())
    globalid=idd
    if idd>count:
        messagebox.showinfo("RMS","No Such Customer")
        customerid.set("")
        name.set("")
        address.set("")
        phone.set("")
        email.set("")
        membership.set("Select")
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
idd=ttk.Entry(win,state="readonly:",textvariable=customerid).place(x=220,y=250,width=300,height=40)
nme=ttk.Entry(win,textvariable=name,state="normal").place(x=220,y=300,width=300,height=40)
ad=ttk.Entry(win,textvariable=address,state="normal").place(x=220,y=350,width=300,height=40)
ead=ttk.Entry(win,textvariable=email,state="normal").place(x=220,y=450,width=300,height=40)
mn=ttk.Entry(win,textvariable=phone,state="normal").place(x=220,y=400,width=300,height=40)
mship=ttk.OptionMenu(win,membership,"Select","Temporary","Basic","Premium","Platinum").place(x=220,y=500,width=300,height=40)
disc=ttk.Entry(win,textvariable=discount,state="readonly").place(x=220,y=550,width=300,height=40)
b5=ttk.Button(win,text="Check Discount",command=discc).place(x=600,y=550,width=200,height=40)
b2=ttk.Button(win,text='BACK',command=back).place(x=450,y=600,width=100,height=40)
b3=ttk.Button(win,text='UPDATE',command=update).place(x=300,y=600,width=100,height=40)
b4=ttk.Button(win,text='RESET',command=reset).place(x=150,y=600,width=100,height=40)
win.mainloop()
