from tkinter.ttk import *
import tkinter
from tkinter import *
import os
import mysql.connector as mycon
from tkinter import messagebox
import hashlib
import winsound
from PIL import ImageTk, Image
count=1
chance=2
cn = mycon.connect(host='localhost',user='root',passwd="tiger")
cur = cn.cursor()
cur.execute("create database if not exists Cyber_cafe")
cur.execute("use Cyber_cafe")
cur.execute("create table if not exists login (user_id varchar(2000),password varchar(2000))")
cur.execute("insert into login values ('Andy2457',md5('tiger'))")
cur.execute("create table if not exists loginhistory (user_id varchar(2000),Details varchar(2000))")
cn.commit()
cur.execute("select*from login")
c=cur.fetchone()
def login():
    global count
    global chance
    global c,cp,u
    u=userr.get()
    p=pasw.get()
    result = hashlib.md5(p.encode())
    cp=result.hexdigest()
    if u=="":
        messagebox.showinfo("CCM","Please Enter User ID")
    elif p=="":
        messagebox.showinfo("CCM","Please Enter Password")
    elif u==c[0] and cp==c[1]:
        winsound.PlaySound(r'1\sound\loginsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
        messagebox.showinfo("CCM","|  Login Sucessful  |")
        win.destroy()
        os.system("python layer2.py")
    else:
        messagebox.showinfo("CCM","Please Enter Correct UserID and Password")
def qui():
    win.destroy()
    exit()
win=Tk()
win.title('CCB')
win.geometry("380x270+300+200")
bg=PhotoImage(file=r"1\images\bg.png")
labelforimage=tkinter.Label(win,image=bg)
labelforimage.pack()
win.resizable(False,False)
l1=tkinter.Label(win,text="CYBER_CAFE MANAGEMENT",fg="brown",bg="white",font=("The Poster King",20))
l1.place(x=60,y=5)
user=PhotoImage(file=r"1\images\logo1.png")
userr=StringVar()
pasw=StringVar()
l2=tkinter.Label(win,image=user)
l2.place(x=90,y=40)
l3=tkinter.Label(win,text="User ID",fg="blue",bg="white",font=("Cambria",12))
l3.place(x=60,y=160)
l4=tkinter.Label(win,text="Password",fg="blue",bg="white",font=("Cambria",12))
l4.place(x=50,y=190)
e1=tkinter.Entry(win,textvariable=userr,fg="white",bg="black")
e1.place(x=150,y=162)
e2=tkinter.Entry(win,textvariable=pasw,show="•",fg="white",bg="black")
e2.place(x=150,y=192)
ex=PhotoImage(file=r"1\images\exet.png")
b2=ttk.Button(win,image=ex,command=qui)
b2.place(x=340,y=180)
log=PhotoImage(file=r"1\images\log.png")
b3=ttk.Button(win,image=log,command=login)
b3.place(x=155,y=220)
win.mainloop()

    

