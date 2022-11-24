# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:46:22 2022

@author: LENOVO
"""


from tkinter import*
import sqlite3
from tkinter import messagebox

top=Tk()
top.geometry('1000x1000')
top.title("Buy Products")

productname=StringVar()
cost=StringVar()
customername=StringVar()
address=StringVar()
mobile=IntVar()
date=StringVar()
quantity=StringVar()


def database():
    productname1=productname.get()
    cost1=cost.get()
    customername1=customername.get()
    address1=address.get()
    quantity1=quantity.get()
    mobile1=mobile.get()
    date1=date.get()
    quantity1=quantity.get()
    conn=sqlite3.connect('project.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('INSERT INTO buyproduct (Product_name,Cost,Customer_name,Address,Mobile,Date,Quantity) VALUES(?,?,?,?,?,?,?)',(productname1,cost1,customername1,address1,mobile1,date1,quantity1))
    conn.commit()
    messagebox.showinfo("Message","Successfull")
    sqlite.connect('cache.db',timeout=10)
    
def home():
    top.destroy()
    import orderdetail
    

label_0 = Label(top,text="BUY PRODUCTS",width=30,font=("bold",30))
label_0.place(x=80,y=20)

label_1 = Label(top,text="Product Name",width=20,font=("bold",20))
label_1.place(x=90,y=100)

entry_1=Entry(top,textvar=productname,width=30)
entry_1.place(x=380,y=110)

label_2 = Label(top,text="Cost",width=20,font=("bold",20))
label_2.place(x=90,y=150)

entry_2=Entry(top,textvar=cost,width=30)
entry_2.place(x=380,y=160)

label_3 = Label(top,text="Customer Name",width=20,font=("bold",20))
label_3.place(x=90,y=270)

entry_3=Entry(top,textvar=customername,width=30)
entry_3.place(x=380,y=280)

label_4 = Label(top,text="Address",width=20,font=("bold",20))
label_4.place(x=90,y=210)


midViewForm = Frame(top, width=10)
midViewForm.place(x=380,y=200)
scrollbarx = Scrollbar(midViewForm, orient=HORIZONTAL)
scrollbary = Scrollbar(midViewForm, orient=VERTICAL)

scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.pack(side=BOTTOM, fill=X)
textarea=Text(midViewForm,width=23,height=3,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
for i in range(20):
    textarea.insert(END,"\n")
textarea.pack(side=BOTTOM,fill=X)



label_5 = Label(top,text="Mobile",width=20,font=("bold",20))
label_5.place(x=90,y=330)

entry_5=Entry(top,textvar=mobile,width=30)
entry_5.place(x=380,y=340)

label_6 = Label(top,text="Date",width=20,font=("bold",20))
label_6.place(x=90,y=390)

entry_6=Entry(top,textvar=date,width=30)
entry_6.place(x=380,y=400)

label_7 = Label(top,text="Quantity",width=20,font=("bold",20))
label_7.place(x=90,y=450)

entry_7=Entry(top,textvar=quantity,width=30)
entry_7.place(x=380,y=460)


button=Button(top,text="Submit",width=20,bg="green",fg="white",bd=5,command=database).place(x=200,y=550)

button=Button(top,text="Home",width=20,bg="blue",fg="white",bd=5,command=home).place(x=470,y=550)



top.mainloop()







