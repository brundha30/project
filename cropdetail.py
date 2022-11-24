# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:19:08 2022

@author: LENOVO
"""


from tkinter import*
import tkinter.ttk as ttk
import sqlite3


top=Tk()
top.geometry('1000x1000')
top.title("Crop Details")

#def Back():
     
      

def Displaydata():
    con = sqlite3.connect('project.db')
    cursor=con.execute("SELECT * FROM addcrop")
    fetch = cursor.fetchall()
    
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    con.close()
    
def selectedRow(event):
    curItem=tree.focus()
    contents=(tree.item(curItem))
    selecteditem=contents['values']
    
    
    id1.set("")
    cropname1.set("")
    costrange1.set("")
    description.set("")
  
    id1.set(selecteditem[0])
    cropname1.set(selecteditem[1])
    costrange1.set(selecteditem[2])
    description1.set(selecteditem[3])
    
def back():
    top.destroy()
    import orderdetail
    
Top = Frame(top, width=800, height=90, bd=5, relief="raise")
Top.pack(side=TOP) 

label_0 = Label(top,text="View Crop Detail",width=30,font=("bold",30))
label_0.place(x=340,y=20)

button=Button(top,text="Back",width=15,bg="orange",fg="white",bd=5,command=back).place(x=600,y=600)


sideViewForm = Frame(top, width=10)
sideViewForm.place(x=400,y=120)
scrollbarx = Scrollbar(sideViewForm, orient=HORIZONTAL)
scrollbary = Scrollbar(sideViewForm, orient=VERTICAL)
tree = ttk.Treeview(sideViewForm,columns=("Id","Crop_Name","Cost_Range","Description"),selectmode="extended", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=W)
tree.heading('Crop_Name', text="Crop_Name", anchor=W)
tree.heading('Cost_Range', text="Cost_Range", anchor=W)
tree.heading('Description', text="Description", anchor=W)
tree.column('#0', stretch=NO,  width=0)
tree.column('#1', stretch=NO,  width=120)
tree.column('#2', stretch=NO, width=120)
tree.column('#3', stretch=NO,  width=120)
tree.pack()
tree.bind('<Double-Button-1>', selectedRow)
Displaydata();


if __name__=='__main__':
    top.mainloop()
