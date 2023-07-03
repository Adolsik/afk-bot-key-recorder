import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import main
import threading
import keyboard
import os


def stop():
    root.destroy()
    # todo


keyboard.add_hotkey('f8', stop)
default_dir: str = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
path_to_play = StringVar

def toggle_menu():
    def collapse_toggle_menu():
        options_frame.destroy()
        toggle_btn.config(text='☰', command=toggle_menu)

    window_height = root.winfo_height()
    options_frame = Frame(root, bg='#158aff')

    main_btn = Button(options_frame, text='Main', bd=0, font=('Bold', '20'), bg='#158aff', fg='white',
                      activebackground='#158aff', activeforeground='white', command=main_menu)
    main_btn.place(x=5, y=20)

    recorder_btn = Button(options_frame, text='Record', bd=0, font=('Bold', '20'), bg='#158aff', fg='white',
                          activebackground='#158aff', activeforeground='white', command=recording_menu)
    recorder_btn.place(x=5, y=80)

    play_btn = Button(options_frame, text='Play', bd=0, font=('Bold', '20'), bg='#158aff', fg='white',
                      activebackground='#158aff', activeforeground='white', command=play_menu )
    play_btn.place(x=5, y=140)

    options_frame.place(x=0, y=50, height=window_height, width=120)
    toggle_btn.config(text='X', command=collapse_toggle_menu)


def main_menu():
    def go_unl():
        task = threading.Thread(target=main.go_unl, args=(label_status,), daemon=True)
        task.start()

    def go():
        task1 = threading.Thread(target=main.go, args=(float(entry_working_time.get()), label_status), daemon=True)
        task1.start()

    keyboard.add_hotkey('f5', go_unl)

    frame_main = LabelFrame(root, text="Main", padx=10, pady=10)
    frame_main.place(x=140, y=60, height=200, width=450)

    label_working_time = Label(frame_main, text="Enter how long should bot works (in seconds): ")
    label_working_time.grid(row=0, column=0, padx=10, pady=10)
    entry_working_time = Entry(frame_main)
    entry_working_time.grid(row=0, column=1, padx=10, pady=10)

    button_start = Button(frame_main, text='Start', padx=30, command=go)
    button_start.place(x=130, y=135)

    label_status = Label(frame_main, text=f'Status: OFF')
    label_status.place(x=10, y=140)

    button_quit = Button(root, text="Quit", command=stop, padx=30)
    button_quit.place(x=255, y=280, height=30, width=200)

    label_rec_info = Label(frame_main, text=f'*Press F5 to start without limited time', font=('italic', '8'))
    label_rec_info.place(x=12, y=30)

    label_quit = Label(frame_main, text="*PRESS F8 TO STOP BOTTING")
    label_quit.place(x=240, y=137)


def recording_menu():

    def record():
        button_start['state'] = 'disabled'
        task2 = threading.Thread(target=main.record, args=(default_dir, entry_filename.get(), label_status, button_start, ),
                                 daemon=True)
        task2.start()

    def open_file_dialog():
        global default_dir
        default_dir = filedialog.askdirectory(initialdir='/', title='Select save directory')
        label_rec_info.config(text=f'File saving path: {default_dir}')

    keyboard.add_hotkey('f9', record)

    frame_main = LabelFrame(root, text="Record", padx=10, pady=10)
    frame_main.place(x=140, y=60, height=200, width=450)

    label_start_rec = Label(frame_main, text=f'Press F9 to start recording or click the button bellow',
                            font=('Bold', 10))
    label_start_rec.place(x=7, y=10)

    label_rec_info = Label(frame_main, text=f'File saving path: {default_dir} ', font=('italic', '8'))
    label_rec_info.place(x=7, y=30)

    button_path = Button(frame_main, text='Change path', padx=30, command=open_file_dialog)
    button_path.place(x=5, y=55)

    label_filename = Label(frame_main, text='File name: ', font=('italic','9'))
    label_filename.place(x=210, y=60)

    entry_filename = Entry(frame_main,  )
    entry_filename.place(x=280, y=60)

    label_status = Label(frame_main, text=f'Status: OFF')
    label_status.place(x=10, y=140)

    button_start = Button(frame_main, text='Record', padx=30, command=record)
    button_start.place(x=130, y=135)

    label_quit = Label(frame_main, text="*PRESS F10 TO STOP RECORDING")
    label_quit.place(x=250, y=137)


def play_menu():
    loop = BooleanVar()

    def open_file_dialog():
        global path_to_play
        path = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('txt files', '*.txt'),))
        label_path_info.config(text=f'Path: {path}')
        path_to_play = path

    def play():
        button_start['state'] = 'disabled'
        task3 = threading.Thread(target=main.play(path_to_play, loop.get(), speed_factor_slider.get(), label_status,
                                                  button_start), args=(), daemon=True)
        task3.start()

    keyboard.add_hotkey('f6', play)

    frame_main = LabelFrame(root, text="Play", padx=10, pady=10)
    frame_main.place(x=140, y=60, height=200, width=450)

    label_path_info = Label(frame_main, text=f'Selected file: None ', font=('italic', '9'))
    label_path_info.place(x=125, y=12)

    label_status = Label(frame_main, text=f'Status: OFF')
    label_status.place(x=0, y=140)

    button_path = Button(frame_main, text='Select file', padx=30, command=open_file_dialog)
    button_path.place(x=0, y=10)

    speed_factor_slider = Scale(frame_main, from_=1, to=10, orient=HORIZONTAL)
    speed_factor_slider.place(x=120, y=43)

    label_speed_factor = Label(frame_main, text='Playing speed: ', font=('italic', '10'))
    label_speed_factor.place(x=0, y=60)

    loop_checkbutton = Checkbutton(frame_main, text='Loop', onvalue='True', offvalue='False', variable=loop)
    loop_checkbutton.deselect()
    loop_checkbutton.place(x=250, y=60)

    button_start = Button(frame_main, text='Play', padx=30, command=play)
    button_start.place(x=130, y=135)

    label_quit = Label(frame_main, text="F6 TO START/ CLICK QUIT TO EXIT LOOP", font=('Arial', '8'))
    label_quit.place(x=228, y=138)


root = Tk()
root.geometry('630x320')
root.title('Simple AFK BOT')

# Toggle menu
menu_frame = Frame(root, bg='#158aff', highlightbackground='white', highlightthickness=1)
menu_frame.pack(side=TOP, fill=tkinter.X)
menu_frame.pack_propagate(False)
menu_frame.configure(height=50)

toggle_btn = Button(menu_frame, text='☰', bg='#158aff', fg='white', font=('Bold', 20), bd=0,
                    activebackground='#158aff', activeforeground='white', command=toggle_menu)
toggle_btn.pack(side=tkinter.LEFT)

title_label = Label(menu_frame, text='AFK BOT', bg='#158aff', fg='white', font=('Bold', 20))
title_label.pack(side=tkinter.LEFT)

main_menu()

root.mainloop()
