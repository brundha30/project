# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:13:20 2022

@author: LENOVO
"""


from tkinter import*
import sqlite3
from PIL import ImageTk, Image
top=Tk()
top.title("Home Page")
top.geometry("1000x1000")
frame = Frame(top, width=1000, height=600)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("14.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img, height=450,width=1000)
label.place(x=50,y=190)

def Adminlogin():
    top.destroy()
    import adminlogin
def Userlogin():
    top.destroy()
    import userlogin
def Userregistration():
    top.destroy()
    import register
    


label_0 = Label(top,text="ONLINE AGRICULTURE MANAGEMENT SYSTEM",width=60,font=("bold",20))
label_0.place(x=230,y=30)


Button(top, text= "Admin Login", width=15, height=1, bd=5, font=("Arial",21,"bold"),command=Adminlogin).place(x=100,y=150)

Button(top, text= "User Login", width=15, height=1, bd=5, font=("Arial",21,"bold"),command=Userlogin).place(x=570,y=150)

Button(top, text= "User Registration", width=15, height=1, bd=5, font=("Arial",21,"bold"),command=Userregistration).place(x=1000,y=150)

top.mainloop()