from tkinter import*
import tkinter as tk
from databaseconnect import getdata
import tkinter.messagebox as messagebox
from welcome import welcome
from internet import *
def login():
    while is_connected()==True:
        cashier_id=entry_cashierid.get()
        password=entry_cashierpassword.get()
        clearall()
        if cashier_id==cashier_id and password==getdata(cashier_id):
            welcome(cashier_id)
        else:
            messagebox.showwarning("Warning", "Incorrect user or password")
    else:
        messagebox.showwarning("Warning", "No Internet connection ")

def clearall():
    entry_cashierid.delete(first=0,last=10) 
    entry_cashierpassword.delete(first=0,last=10) 
if __name__=="__main__":
    root=Tk(className="Bank")
    root.geometry('500x500')
    lable0=tk.Label(root,text="LOG-IN",font=("Arial",16),justify='center',padx=50,pady=10).grid(column=1,row=0)
    label1=Label(root,text="CashierID",font=("Arial",10),justify='center',padx=50,pady=10).grid(column=0,row=1)
    entry_cashierid=Entry(root,width=25)
    entry_cashierid.grid(column=1,row=1)

    label2=Label(root,text="Password",font=("Arial",10),justify='center',padx=50,pady=10).grid(column=0,row=2)
    entry_cashierpassword=Entry(root,width=25,show="$")
    entry_cashierpassword.grid(column=1,row=2)

    submit_button=Button(root,text="Submit",font=("Arial",12),command=login)
    submit_button.grid(column=1,row=3)
    root.mainloop()
