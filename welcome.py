#cashier side system
from tkinter import *
from main import start_process,stop_process
from datetime import datetime
from databaseconnect import providelength,next_token
def welcome(id):
    
    def start():
        next_button.config(state="normal")
        absent_button.config(state="normal")
        latesttoken=start_process()
        label3.config(text=f"token no:{latesttoken}",fg="black")
    def nextp():
       data=label3.cget('text')
       token,tokenid=data.split(":")
       tokendata=int(tokenid)
       next_token(tokendata)
       if (providelength()==0):
            label3.config(text="sry no any entry:")
       else:
           latestdata=start_process()
           label3.config(text=f"token no:{latestdata}")
    
    def stop():
        next_button.config(state="disabled")
        absent_button.config(state="disabled")
        stop_process()
    root=Tk(className="Main Page")
    root.geometry('500x500')
    label1=Label(root,text=f"hi {id}",padx=50,pady=50,font=("Arial",16))
    label1.grid(column=0,row=0)
    label_time=Label(root,font=("Arial",14))
    label_time.grid(column=3,row=0)
    def update_time():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        label_time.configure(text=current_time)
        root.after(1000, update_time)
    update_time()
    start_button=Button(root,text="Start",font=("Arial",12),background="Green",padx=20,justify="center",command=lambda:start())
    start_button.grid(column=1,row=1)
    stop_button=Button(root,text="Stop",font=("Arial",12),background="red",padx=20,justify="center",command=lambda:stop())
    stop_button.grid(column=3,row=1)
    next_button=Button(root,text="Next",state="disabled",font=("Arial",12),background="blue",padx=20,justify="center",command=lambda:nextp())
    next_button.grid(column=1,row=2)
    label3=Label(root,fg="red",text="",state="disabled",font=("Arial",16),background="white",padx=100,pady=100)
    label3.grid(column=3,row=4)
    absent_button=Button(root,text="Absent",background="Red",font=("Arial",12))
    absent_button.grid(column=3,row=5)
    return root.mainloop()

