# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:07:59 2022

@author: LENOVO
"""


from tkinter import*
import sqlite3
from PIL import ImageTk, Image

top=Tk()
top.title("Admin Homepage")
top.geometry("1000x1000")

frame = Frame(top, width=1000, height=900)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
#img = ImageTk.PhotoImage(Image.open("grains.jpg"))

# Create a Label Widget to display the text or Image
#label = Label(frame, image = img, height=450,width=1000)
#label.place(x=300,y=200)

def addcrop():
    top.destroy()
    import addcrop
def addinsecticide():
    top.destroy()
    import addinsecticide
def addseed():
    top.destroy()
    import addseed
def addvegetable():
    top.destroy()
    import addvegetable
def productreport():
    top.destroy()
    import productreport
def orderdetail():
    top.destroy()
    import buytable 
def logout():
    import project

label_0 = Label(top,text="ADMIN HOME PAGE",width=30,font=("bold",30))
label_0.place(x=10,y=30)




Button(top, text= "ADD CROPS", width=23,bg="white", height=1, bd=5, font=("Arial",15,"bold"),command=addcrop).place(x=190,y=120)

Button(top, text= "ADD INSECTICIDES ", width=23,bg="white", height=1, bd=5, font=("Arial",15,"bold"),command=addinsecticide).place(x=190,y=200)

Button(top, text= "ADD SEEDS", width=23,bg="white", height=1, bd=5, font=("Arial",15,"bold"),command=addseed).place(x=190,y=280)

Button(top, text= "ADD VEGETABLE", width=23,bg="white", height=1, bd=5, font=("Arial",15,"bold"),command=addvegetable).place(x=190,y=360)

Button(top, text= "REPORTS", width=23,bg="white", height=1,fg="black", bd=5, font=("Arial",15,"bold"),command=productreport).place(x=190,y=440)

Button(top, text= "VIEW ORDER DETAILS", width=23,bg="white", height=1,fg="black", bd=5, font=("Arial",15,"bold"),command=orderdetail).place(x=190,y=520)

Button(top, text= "LOGOUT", width=14,bg="orange", height=1,fg="black", bd=5, font=("Arial",15,"bold"),command=logout).place(x=240,y=630)


top.mainloop()