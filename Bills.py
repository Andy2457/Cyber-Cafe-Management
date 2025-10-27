from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as sql
conn=sql.connect(host ='localhost',user ='root',password ='tiger')
c1=conn.cursor()
win=Tk()
win.title('CCM')
win.geometry("1200x600")
win.config(bg="Peru")
win.resizable(False,False)
l1=tkinter.Label(win,text="CYBER_CAFE MANAGEMENT",fg="black",bg="Peru",font=("The Poster King",50))
l1.grid(row=0, columnspan=3)
c1.execute("use Cyber_Cafe")
c1.execute("select * from Bill")
output=c1.fetchall()
l2=tkinter.Label(win,text="Bills",fg="black",bg="peru",font=("LingLengLang",40)).grid(row=1, columnspan=4)
cols = ('Customer ID', 'Customer Name', 'Membership', 'Discount', 'Time', 'Total')
listBox = ttk.Treeview(win, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=2, column=0, columnspan=2)
for c in output:
    listBox.insert("","end",values=(c[0],c[1],c[2],c[3],c[4],c[5]))
win.mainloop()
