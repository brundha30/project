# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:23:44 2022

@author: LENOVO
"""


from tkinter import*
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

top=Tk()
top.geometry('1000x1000')
top.title("Registration")

frame = Frame(top, width=1000, height=1000)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("register.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img, height=450,width=1000)
label.place(x=250,y=230)

id=IntVar()
name=StringVar()
address=StringVar()
username=StringVar()
password=StringVar()
email=StringVar()
mobile=IntVar()


def database():
    id1=id.get()
    name1=name.get()
    address1=address.get()
    username1=username.get()
    password1=password.get()
    email1=email.get()
    mobile1=mobile.get()
    conn=sqlite3.connect('project.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('INSERT INTO register (Id,Name,Address,Username,Password,Email,Mobile) VALUES(?,?,?,?,?,?,?)',(id1,name1,address1,username1,password1,email1,mobile1))
    conn.commit()
    messagebox.showinfo("Registration form","Successfull")
    sqlite.connect('cache.db',timeout=10)

    

label_0 = Label(top,text="REGISTRATION FORM",width=30,font=("bold",30))
label_0.place(x=80,y=20)

label_1 = Label(top,text="ID",width=20,font=("bold",20))
label_1.place(x=90,y=100)

entry_1=Entry(top,textvar=id,width=30)
entry_1.place(x=380,y=110)

label_2 = Label(top,text="Name",width=20,font=("bold",20))
label_2.place(x=90,y=150)

entry_2=Entry(top,textvar=name,width=30)
entry_2.place(x=380,y=160)

label_3 = Label(top,text="Address",width=20,font=("bold",20))
label_3.place(x=90,y=210)


entry_3=Entry(top,textvar=address,width=30)
entry_3.place(x=380,y=220)



label_4 = Label(top,text="Username",width=20,font=("bold",20))
label_4.place(x=90,y=270)

entry_4=Entry(top,textvar=username,width=30)
entry_4.place(x=380,y=280)

label_5 = Label(top,text="Password",width=20,font=("bold",20))
label_5.place(x=90,y=330)

entry_5=Entry(top,textvar=password,width=30,show="*")
entry_5.place(x=380,y=340)

label_6 = Label(top,text="Email",width=20,font=("bold",20))
label_6.place(x=90,y=390)

entry_6=Entry(top,textvar=email,width=30)
entry_6.place(x=380,y=400)

label_7 = Label(top,text="Mobile",width=20,font=("bold",20))
label_7.place(x=90,y=450)

entry_7=Entry(top,textvar=mobile,width=30)
entry_7.place(x=380,y=460)


button=Button(top,text="Submit",width=20,bg="green",fg="white",bd=5,command=database).place(x=200,y=550)

button=Button(top,text="Home",width=20,bg="blue",fg="white",bd=5,command=database).place(x=470,y=550)



top.mainloop()







