
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
            break

def stop():
    winsound.PlaySound(None, winsound.SND_PURGE)
    
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}"
    alarm(set_alarm_timer)
    
    
    
# Creating GUI

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text= "Enter time in 24 hour format!", fg ="red", bg= "black", font="Arial").place(x=95,y=130)
addTime = Label(clock, text = "Hour      Min", font=60).place(x=155)
setyouralarm = Label(clock,text = "Time to wake up: ", fg = "blue", font = ("Arial",7, "bold")).place(x=65,y=30)


# Initialization

hour = StringVar()
min = StringVar()


hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=150,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 10).place(x=200,y=30)


submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
stop = Button(clock,text = "Stop Alarm",fg="red",width = 10,command = stop).place(x =205,y=70)
close = Button(clock, text="Quit", command= clock.destroy).place(x=350, y=5)
clock.mainloop()