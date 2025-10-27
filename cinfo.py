from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as sql
win=Tk()
win.title('CCM')
win.geometry("900x600")
bg=PhotoImage(file=r"1\images\bg2.png")
labelforimage=tkinter.Label(win,image=bg)
labelforimage.place(x=580,y=10)
bg1=PhotoImage(file=r"1\images\bg1.png")
b1=tkinter.Label(win,image=bg1)
b1.place(x=450,y=250)
win.config(bg="Peru")
win.resizable(False,False)
l1=tkinter.Label(win,text="CYBER_CAFE",fg="black",bg="Peru",font=("The Poster King",50))
l1.place(x=89,y=5)
l2=tkinter.Label(win,text="MANAGEMENT",fg="black",bg="Peru",font=("The Poster King",50))
l2.place(x=80,y=100)
def addc():
    win.destroy()
    os.system("python add.py")
def update():
    win.destroy()
    os.system("python update.py")
def dele():
    win.destroy()
    os.system("python delete.py")
def allc():
    os.system("python all.py")
def ex():
    win.destroy()
    exit()
def back():
    win.destroy()
    os.system("python layer2.py")
myfont=font.Font(family='LingLengLang',size=30)
b1=Button(win,text="LIST OF CUSTOMERS",fg='brown',font=myfont,command=allc)
b1.place(x=10,y=200)
b2=Button(win,text="ADD NEW CUSTOMER",fg='brown',font=myfont,command=addc)
b2.place(x=10,y=270)
b3=Button(win,text="UPDATE CUSTOMER DETAILS",fg='brown',font=myfont,command=update)
b3.place(x=10,y=340)
b3=Button(win,text="DELETE CUSTOMER DETAILS",fg='brown',font=myfont,command=dele)
b3.place(x=10,y=410)
b4=Button(win,text="EXIT",fg='brown',font=myfont,command=ex)
b4.place(x=10,y=500)
b5=Button(win,text='BACK',fg='brown',font=myfont,command=back).place(x=300,y=500)
win.mainloop()
