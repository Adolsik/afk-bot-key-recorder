from tkinter import *
import main

root = Tk()
root.geometry('450x130')

root.title('Simple AFK BOT')
label_working_time = Label(root, text="Enter how long should bot works (in minutes): ")
label_working_time.grid(row=0, column=0, padx=10, pady=10)
entry_working_time = Entry(root)
entry_working_time.grid(row=0, column=1, padx=10, pady=10)

button_start = Button(root, text='Start', padx=30, command=lambda: [main.go(float(entry_working_time.get()*60))])
button_start.grid(row=1, column=1, padx=10, pady=10)

#TODO
#label_status = Label(root, text=f'Status: BOT IS NOT WORKING')
#label_status.grid(row=2, column=0, padx=50, pady=10)
root.mainloop()