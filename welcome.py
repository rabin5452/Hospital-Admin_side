import tkinter as tk
import mysql.connector
import threading
from datetime import datetime
from databaseconnect import providelength,cursor,cnx,get_minmumtoken,nexttoken,indicate_absent,storeservicetime
services_times=[]
counter=0
tokennum=0
count_timer=True
wakeup_called = False
condition = threading.Condition()
def welcome(id):
    root = tk.Tk()
    root.config(bg="white")
    root.geometry('800x600')
    root.resizable(False,False)
    header_frame = tk.Frame(root, bg='Blue', height=50)
    header_frame.pack(fill=tk.X)
    logo_image = tk.PhotoImage(file='icon.png')
    logout_image = tk.PhotoImage(file='2767155.png')
    resized_logout_image = logout_image.subsample(20)
    resized_logo_image = logo_image.subsample(4)
    logo_label = tk.Label(header_frame, image=resized_logo_image)
    logo_label.pack(side=tk.LEFT, padx=10)
    logout_button = tk.Button(header_frame, text='Logout', image=resized_logout_image,highlightthickness=1,highlightbackground="white",
                            compound=tk.RIGHT, command=root.destroy)
    logout_button.pack(side=tk.RIGHT)
    def sleep_until_wakeup():
        global wakeup_called
        # wait for the wakeup call
        with condition:
            while not wakeup_called:
                condition.wait()

        # when the wakeup call is made, reset the flag and return
        wakeup_called = False
        return

    def wakeup():
        global wakeup_called
    
        # notify the waiting thread
        with condition:
            wakeup_called = True
            condition.notify()
    def providelength_():
        cnx1=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='token'
        )
        cursor1=cnx1.cursor()
        sql = "SELECT count(*) FROM tokendata"
        cursor1.execute(sql)
        data=cursor1.fetchone()[0]
        return data
    def startprocess():
            wakeup()
            global tokennum
            next_button.config(state="normal")
            call_button.config(state="normal")
            if providelength_()>0:
                next_button.config(state="normal")
                call_button.config(state="normal")
                tokenid=get_minmumtoken()
                tokennum=tokenid[1]
                label3.config(text=f"TOKEN NO:{tokenid[1]}")
                label4.config(text=f"Email:{tokenid[0]}")
            else:
                label3.config(text="NO ANY ENTRIES")
                label4.config(text="NO ANY ENTRIES")
                t = threading.Thread(target=sleep_until_wakeup)
                t.start()
    def stop_process():
        global counter,tokennum
        next_button.config(state="disabled")
        call_button.config(state="disabled")
        absent_button.config(state="disabled")
        cancel(counter)
        label3.config(text="Press Start to Start:")

    servicing_time=tk.Label(root,font=("Arial",14))
    servicing_time.place(x=200,y=500)
    def count_time():
        global counter,count_timer
        if count_timer:
            counter =counter+1
            # Calculate hours, minutes, and seconds
            hours = counter // 3600
            minutes = (counter % 3600) // 60
            seconds = counter % 60
            # Format the time as a string with leading zeros
            time_str = f"{hours:02d}-{minutes:02d}-{seconds:02d}"
            servicing_time.config(text=time_str)
            servicing_time.after(1000, count_time) # 1000ms = 1s
    def cancel(counter1):
        global count_timer,counter,tokennum
        count_timer = False
        final_countvalue=counter1
        min_counter=final_countvalue/(60)
        services_times.append(min_counter)
        storeservicetime(min_counter,tokennum)
        counter=0
        count_time()
        servicing_time.configure(text="00-00-00")

    def call():
        absent_button.config(state="normal")
        global counter,count_timer
        count_timer=True
        counter=0
        count_time() 
        
    def next_token():
        global counter,tokennum
        wakeup()
        cancel(counter)
        absent_button.config(state="disabled")
        data=label3.cget('text')
        if data=="NO ANY ENTRIES":
            if providelength_()>0:
                try:
                    tokenid=get_minmumtoken()
                except TypeError:
                    t = threading.Thread(target=sleep_until_wakeup)
                    t.start()
                else:
                    label3.config(text=f"TOKEN NO:{tokenid[1]}")
                    label4.config(text=f"Email:{tokenid[0]}")
                    tokennum=tokenid[1]
                    nexttoken(str(tokennum))
                    t = threading.Thread(target=sleep_until_wakeup)
                    t.start()
            else:
                    t = threading.Thread(target=sleep_until_wakeup)
                    t.start()
        else:
            if providelength_()>0:
                token,tokenid=data.split(":")
                try:
                    tokenid=get_minmumtoken()
                except TypeError:
                    t = threading.Thread(target=sleep_until_wakeup)
                    t.start()
                else:
                    tokennum=tokenid[1]
                    label3.config(text=f"TOKEN NO:{tokenid[1]}")
                    label4.config(text=f"Email:{tokenid[0]}")
                    nexttoken(tokenid[1])
                    t = threading.Thread(target=sleep_until_wakeup)
                    t.start()
            else:
                label3.config(text="NO ANY ENTRIES")
                label4.config(text="NO ANY ENTRIES")
                t = threading.Thread(target=sleep_until_wakeup)
                t.start()
        
    
    def absent_cutomer():
        global counter
        data=label3.cget('text')
        token,tokenid=data.split(":")
        data=label4.cget('text')
        email,emailid=data.split(":")
        services_times.append(0)
        cancel(counter)
        indicate_absent(tokenid,emailid)
        nexttoken(tokenid)
        next_token()




    label_time=tk.Label(header_frame,font=("Arial",14))
    label_time.pack(fill=tk.Y)
    queue_detail_label=tk.Label(root,bd=1,relief="solid",padx=100,pady=200)
    queue_detail_label.place(x=550,y=50)
    def update_data():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            a=providelength_()
            label_time.configure(text=current_time)
            queue_detail_label.configure(text=f"length:{a}")
            root.after(1000, update_data)
    update_data()
    
    start_button=tk.Button(root,text="Start Process",font=("Arial",12),background="Green",padx=20,justify="center",command=lambda:startprocess())
    start_button.place(x=15,y=50)
    stop_button=tk.Button(root,text="Stop Process",font=("Arial",12),background="RED",padx=20,justify="center",command=lambda:stop_process())
    stop_button.place(x=350,y=50)
    
    label3=tk.Label(root,fg="black",text="Press Start Process",state="disabled",font=("Arial",16),background="Skyblue",borderwidth=5,highlightbackground="gray",width=20,height=10)
    label3.place(x=20,y=100)
    label4=tk.Label(root,fg="black",text="email",state="disabled",font=("Arial",16),background="White",borderwidth=5,highlightbackground="gray",width=23,height=10)
    label4.place(x=250,y=100)
    next_button=tk.Button(root,fg="white",text="Next",font=("Arial",12),state="disabled",background="Blue",padx=20,justify="center",command=next_token)
    next_button.place(x=30,y=100)
    call_button=tk.Button(root,fg="black",text="Call",font=("Arial",12),state="disabled",background="Dark blue",padx=20,justify="center",command=lambda:call())
    call_button.place(x=120,y=100)
    absent_button=tk.Button(root,fg="white",text="Absent",font=("Arial",12),state="disabled",background="red",padx=20,justify="center",command=lambda:absent_cutomer())
    absent_button.place(x=200,y=350)
        
    servicingtime=tk.Label(root,text="Servicing Time:",font=("Arial",16))
    servicingtime.place(x=10,y=500)
    # def provide_livelength():
    #         a=providelength()
    #         queue_detail_label.configure(text=f"queuelength:{a}")
    #         root.after(1000, provide_livelength)
    # provide_livelength()
    
    return root.mainloop()


