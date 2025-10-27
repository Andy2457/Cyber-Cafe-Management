from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import random
import tkinter.font as font
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
def customerinfo():
    win.destroy()
    os.system("python cinfo.py")
def bill():
    win.destroy()
    os.system("python bill.py")
def bills():
    os.system("python Bills.py")
def ex():
    win.destroy()
    exit()
myfont=font.Font(family='LingLengLang',size=40)
b1=Button(win,text="CUSTOMER INFO",fg='brown',font=myfont,command=customerinfo)
b1.place(x=10,y=200)
b2=Button(win,text="CREATE BILL",fg='brown',font=myfont,command=bill)
b2.place(x=10,y=300)
b2=Button(win,text="BILLS",fg='brown',font=myfont,command=bills)
b2.place(x=10,y=400)
b4=Button(win,text="EXIT",fg='brown',font=myfont,command=ex)
b4.place(x=10,y=500)
win.mainloop()
