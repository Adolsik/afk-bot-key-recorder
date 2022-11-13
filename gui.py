import sys
from tkinter import *
import main
import threading
import keyboard


def stop(): 
    root.destroy()

def go():
   t1 = threading.Thread(target=main.go, args=(float(entry_working_time.get()),label_status), daemon=True)
   t1.start()


root = Tk()
root.geometry('470x270')
root.title('Simple AFK BOT')


frame_main = LabelFrame(root, text="Main", padx=10, pady=10)
frame_main.place(x=10, height=200, width=450)

label_working_time = Label(frame_main, text="Enter how long should bot works (in seconds): ")
label_working_time.grid(row=0, column=0, padx=10, pady=10)
entry_working_time = Entry(frame_main)
entry_working_time.grid(row=0, column=1, padx=10, pady=10)

button_start = Button(root, text='Start', padx=30, command=go)
button_start.place(x=155, y=150)

label_status = Label(root, text=f'Status: BOT IS NOT WORKING')
label_status.place(x=110, y=10)

button_quit = Button(root, text="Quit", command=stop, padx=30)
button_quit.place(x=125, y=220, height=30, width=200)

label_quit = Label(root,text="*PRESS F8 TO STOP BOTTING")
label_quit.place(x=270, y=152)

keyboard.add_hotkey('f8', stop)

root.mainloop()
