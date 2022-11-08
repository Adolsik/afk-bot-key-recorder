from tkinter import *
import main
import threading
import time

def stop(event=None): 
    root.destroy()

def go():
   t1 = threading.Thread(target=main.go, args=(float(entry_working_time.get()),))
   t1.start()

root = Tk()
root.geometry('520x160')

root.title('Simple AFK BOT')
label_working_time = Label(root, text="Enter how long should bot works (in seconds): ")
label_working_time.grid(row=0, column=0, padx=10, pady=10)
entry_working_time = Entry(root)
entry_working_time.grid(row=0, column=1, padx=10, pady=10)

button_start = Button(root, text='Start', padx=30, command=go)
button_start.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

label_status = Label(root, text=f'Status: {main.status}')
label_status.grid(row=1, column=0, padx=50, pady=10)

button_quit = Button(root, text="Quit", command=root.destroy, padx=30)
button_quit.grid(row=3, column=1, padx=50, pady=10)

label_quit = Label(root,text="Press F8 to stop the bot")
label_quit.grid(row=3, column=0, padx=20, pady=10)

root.bind('<F8>',stop)

root.mainloop()
