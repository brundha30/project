# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:04:21 2022

@author: LENOVO
"""


from tkinter import*
import tkinter.ttk as ttk
import sqlite3


top=Tk()
top.geometry('1000x1000')
top.title("Order Details")

#def Back():
     
      

def Displaydata():
    con = sqlite3.connect('project.db')
    cursor=con.execute("SELECT * FROM buyproduct")
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
    insecticidename1.set("")
    costrange1.set("")
    description.set("")
  
    id1.set(selecteditem[0])
    insecticidename1.set(selecteditem[1])
    costrange1.set(selecteditem[2])
    description1.set(selecteditem[3])
    
    
def back():
    top.destroy()
    import adminhomepage

    
Top = Frame(top, width=800, height=90, bd=5, relief="raise")
Top.pack(side=TOP) 

label_0 = Label(top,text="Order Detail",width=30,font=("bold",30))
label_0.place(x=340,y=20)

button=Button(top,text="Back",width=15,bg="orange",fg="white",bd=5,command=back).place(x=600,y=600)


sideViewForm = Frame(top, width=10)
sideViewForm.place(x=230,y=120)
scrollbarx = Scrollbar(sideViewForm, orient=HORIZONTAL)
scrollbary = Scrollbar(sideViewForm, orient=VERTICAL)
tree = ttk.Treeview(sideViewForm,columns=("Product_name","Cost","Customer_name","Address","Mobile","Date","Quantity"),selectmode="extended", height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Product_name', text="Product_name", anchor=W)
tree.heading('Cost', text="Cost", anchor=W)
tree.heading('Customer_name', text="Customer_name", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Mobile', text="Mobile", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('Quantity', text="Quantity", anchor=W)
tree.column('#0', stretch=NO,  width=0)
tree.column('#1', stretch=NO,  width=120)
tree.column('#2', stretch=NO, width=120)
tree.column('#3', stretch=NO,  width=120)
tree.column('#4', stretch=NO,  width=120)
tree.column('#5', stretch=NO, width=120)
tree.column('#6', stretch=NO,  width=120)
tree.pack()
tree.bind('<Double-Button-1>', selectedRow)
Displaydata();


if __name__=='__main__':
    top.mainloop()
