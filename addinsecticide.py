# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:45:34 2022

@author: LENOVO
"""

from tkinter import filedialog
from tkinter import*
import sqlite3
from tkinter import messagebox

top=Tk()
top.geometry('1000x1000')
top.title("Add Insecticide")

insecticide_id=IntVar()
insecticide_name=StringVar()
cost_range=StringVar()
description=StringVar()

global file,blob_data
def upload():
    global file,blob_data
    file = filedialog.askopenfilename()
    fob=open(file,'rb')
    blob_data=fob.read() # Binary data is ready   

def database():
    insecticideid1=insecticide_id.get()
    insecticidename1=insecticide_name.get()
    costrange1=cost_range.get()
    description1=description.get()
    conn=sqlite3.connect('project.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('INSERT INTO addinsecticide (Insecticide_ID,Insecticide_Name,Cost_Range,Description,Photo) VALUES(?,?,?,?,?)',(insecticideid1,insecticidename1,costrange1,description1,blob_data))
    conn.commit()
    messagebox.showinfo("Message","Data inserted Successfully")
    sqlite.connect('cache.db',timeout=10)
def back():
    top.destroy()
    import adminhomepage


label_0 = Label(top,text="ADD INSECTICIDES",width=30,font=("bold",30))
label_0.place(x=70,y=20)

label_1 = Label(top,text="Insecticide ID",width=20,font=("bold",20))
label_1.place(x=90,y=110)

entry_1=Entry(top,textvar=insecticide_id,width=30)
entry_1.place(x=380,y=120)

label_2 = Label(top,text="Insecticide Name",width=20,font=("bold",20))
label_2.place(x=90,y=170)

entry_2=Entry(top,textvar=insecticide_name,width=30)
entry_2.place(x=380,y=180)

label_3 = Label(top,text="Cost Range",width=20,font=("bold",20))
label_3.place(x=90,y=230)

entry_3=Entry(top,textvar=cost_range,width=30)
entry_3.place(x=380,y=240)

label_4 = Label(top,text="Description",width=20,font=("bold",20))
label_4.place(x=90,y=290)

entry_4=Entry(top,textvar=description,width=30)
entry_4.place(x=380,y=300)


label_5 = Label(top,text="Upload Image",width=20,font=("bold",20))
label_5.place(x=90,y=350)



button=Button(top,text="Browse",width=17,bg="white",fg="black",bd=4,font=("arial"),command=upload).place(x=380,y=350)

button=Button(top,text="Submit",width=20,bg="green",fg="white",bd=5,command=database).place(x=200,y=550)

button=Button(top,text="Back",width=20,bg="orange",fg="white",bd=5,command=back).place(x=470,y=550)


top.mainloop()
