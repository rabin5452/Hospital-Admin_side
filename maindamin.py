from server import runserver
from tkinter import *
from datetime import datetime
def stop():
    quit()
root=Tk(className="Main Page")
root.geometry('250x250')
start_button=Button(root,text="Start",font=("Arial",12),background="Green",padx=20,justify="center",command=lambda:runserver())
start_button.grid(column=1,row=0)
end_button=Button(root,text="Stop",font=("Arial",12),background="Green",padx=20,justify="center",command=lambda:stop())
end_button.grid(column=2,row=0)
root.mainloop()