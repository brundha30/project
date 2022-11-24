# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:56:51 2022

@author: LENOVO
"""

from tkinter import filedialog
from tkinter import*
import tkinter.ttk as ttk
import sqlite3


top=Tk()
top.geometry('1000x1000')
top.title("Vegetable Report")

vegetableid1=IntVar()
vegetablename1=StringVar()
costrange1=StringVar()
description1=StringVar()

global file,blob_data
def upload():
    global file,blob_data
    file = filedialog.askopenfilename()
    fob=open(file,'rb')
    blob_data=fob.read() # Binary data is ready   
    

def Update():
      con = sqlite3.connect('project.db')
      cursor=con.execute('UPDATE addvegetable SET Vegetable_Name = ?,Cost_Range = ?, Description = ?,Photo = ? ''WHERE Vegetable_ID = ?', (str(vegetablename1.get()),str(costrange1.get()),str(description1.get()),int(vegetableid1.get()),blob_data))
      con.commit()

def Delete():
      con = sqlite3.connect('project.db')
      cursor = con.cursor()
      query = "DELETE from addvegetable where Vegetable_ID = ?"
      cursor.execute(query,(int(id1.get()),))
      con.commit()
      
     
#def Back():
     
      

def Displaydata():
    con = sqlite3.connect('project.db')
    cursor=con.execute("SELECT * FROM addvegetable")
    fetch = cursor.fetchall()
    
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    con.close()
    
def selectedRow(event):
    curItem=tree.focus()
    contents=(tree.item(curItem))
    selecteditem=contents['values']
    
    
    vegetableid1.set("")
    vegetablename1.set("")
    costrange1.set("")
    description1.set("")
  
    vegetableid1.set(selecteditem[0])
    vegetablename1.set(selecteditem[1])
    costrange1.set(selecteditem[2])
    description1.set(selecteditem[3])
    
def back():
    top.destroy()
    import productreport      
    
Top = Frame(top, width=800, height=90, bd=5, relief="raise")
Top.pack(side=TOP) 



label_0 = Label(top,text="View Vegetable Report",width=30,font=("bold",30))
label_0.place(x=340,y=20)

label_1 = Label(top,text="Vegetable ID",width=20,font=("bold",20))
label_1.place(x=10,y=110)

entry_1=Entry(top,textvar=vegetableid1,width=30)
entry_1.place(x=290,y=120)

label_2 = Label(top,text="Vegetable Name",width=20,font=("bold",20))
label_2.place(x=10,y=170)

entry_2=Entry(top,textvar=vegetablename1,width=30)
entry_2.place(x=290,y=180)

label_3 = Label(top,text="Cost Range",width=20,font=("bold",20))
label_3.place(x=10,y=230)

entry_3=Entry(top,textvar=costrange1,width=30)
entry_3.place(x=290,y=240)

label_4 = Label(top,text="Description",width=20,font=("bold",20))
label_4.place(x=10,y=290)

entry_4=Entry(top,textvar=description1,width=30)
entry_4.place(x=290,y=300)


label_5 = Label(top,text="Upload Image",width=20,font=("bold",20))
label_5.place(x=10,y=350)



button=Button(top,text="Browse",width=17,bg="white",fg="black",bd=4,font=("arial"),command=upload).place(x=290,y=350)

button=Button(top,text="Update",width=15,bg="green",fg="white",bd=5,command=Update).place(x=90,y=550)

button=Button(top,text="Delete",width=15,bg="red",fg="white",bd=5,command=Delete).place(x=290,y=550)

button=Button(top,text="Back",width=15,bg="orange",fg="white",bd=5,command=back).place(x=490,y=550)


sideViewForm = Frame(top, width=10)
sideViewForm.place(x=700,y=120)
scrollbarx = Scrollbar(sideViewForm, orient=HORIZONTAL)
scrollbary = Scrollbar(sideViewForm, orient=VERTICAL)
tree = ttk.Treeview(sideViewForm,columns=("Vegetable_ID","Vegetable_Name","Cost_Range","Description","Photo"),selectmode="extended", height=17, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Vegetable_ID', text="Vegetable_ID", anchor=W)
tree.heading('Vegetable_Name', text="Vegetable_Name", anchor=W)
tree.heading('Cost_Range', text="Cost_Range", anchor=W)
tree.heading('Description', text="Description", anchor=W)
tree.heading('Photo', text="Photo", anchor=W)
tree.column('#0', stretch=NO,  width=0)
tree.column('#1', stretch=NO,  width=120)
tree.column('#2', stretch=NO, width=120)
tree.column('#3', stretch=NO,  width=120)
tree.pack()
tree.bind('<Double-Button-1>', selectedRow)
Displaydata();


if __name__=='__main__':
    top.mainloop()
