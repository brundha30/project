# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:53:42 2022

@author: LENOVO
"""


from tkinter import*
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

top=Tk()
top.geometry('900x600')
top.title("Login")

frame = Frame(top, width=1000, height=900)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("user.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img, height=450,width=1000)
label.place(x=300,y=200)

username=StringVar()
password=StringVar()

def login():
    username1=username.get()
    password1=password.get()
    con=sqlite3.connect('project.db')
    cursor=con.execute('SELECT * FROM register where Name="%s" and Password="%s"'%(username1,password1))
    if cursor.fetchone():
        messagebox.showinfo("","Login Successfull")
    else:
        messagebox.showinfo("","Login Unsuccessfull")
    import orderdetail  

label_0=Label(top,text="USER LOGIN",width=13,font=("bold",30))
label_0.place(x=120,y=20)

label_1=Label(top,text="Username",width=20,font=("bold",20))
label_1.place(x=8,y=120)

entry_1=Entry(top,textvar=username,width=20)
entry_1.place(x=300,y=130)

label_2=Label(top,text="Password",width=20,font=("bold",20))
label_2.place(x=8,y=200)

entry_2=Entry(top,textvar=password,width=20,show="*")
entry_2.place(x=300,y=210)

button=Button(top,text="Login",width=20,bg="white",activebackground="black",bd=5,command=login).place(x=180,y=280)
top.mainloop()
