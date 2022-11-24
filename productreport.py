# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:27:04 2022

@author: LENOVO
"""


from tkinter import*
import sqlite3
top=Tk()
top.title("Product details")
top.geometry("1000x1000")

def cropreport():
    top.destroy()
    import cropreport
def insecticidereport():
    top.destroy()
    import insecticidereport
def seedreport():
    top.destroy()
    import seedreport
def vegetablereport():
    top.destroy()
    import vegetablereport

def back():
    top.destroy()
    import adminhomepage
    
    
Top = Frame(top, width=1000, height=100, bd=5, relief="raise")
Top.pack(side=TOP)  

label_0 = Label(top,text="PRODUCT DETAILS",width=30,font=("bold",40))
label_0.place(x=230,y=30)


Button(top, text= "CROP REPORT", width=20,bg="white", height=1, bd=5, font=("Arial",19,"bold"),command=cropreport).place(x=500,y=150)

Button(top, text= "INSECTICIDES REPORT", width=20,bg="white", height=1, bd=5, font=("Arial",19,"bold"),command=insecticidereport).place(x=500,y=250)

Button(top, text= "SEEDS REPORT", width=20,bg="white", height=1, bd=5, font=("Arial",19,"bold"),command=seedreport).place(x=500,y=350)

Button(top, text= "VEGETABLE REPORT", width=20,bg="white", height=1, bd=5, font=("Arial",19,"bold"),command=vegetablereport).place(x=500,y=450)

Button(top, text= "BACK", width=13,bg="orange", height=1,fg="black", bd=5, font=("Arial",19,"bold"),command=back).place(x=550,y=600)












top.mainloop()