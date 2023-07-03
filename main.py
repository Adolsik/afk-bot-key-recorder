from tkinter import messagebox
import pyautogui as pag
import time
import random
import keyboard
import os


def go_unl(bot_status):
    time_delayed = 0.0
    bot_status.config(text="Status: ON")

    # Primary monitor size
    screen_width, screen_high = pag.size()

    while True:
        time.sleep(3)

        # Mouse move
        pag.click()
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_high)
        pag.moveTo(x, y, 0.5)

        # Keyboard move
        pag.press(['w', 's', 'a', 'd', 'space'])

        time_delayed += 3


def go(working_time, bot_status):
    time_delayed = 0.0
    bot_status.config(text="Status: ON")

    # Primary monitor size
    screen_width, screen_high = pag.size()

    while time_delayed <= working_time:
        time.sleep(3)

        # Mouse move
        pag.click()
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_high)
        pag.moveTo(x, y, 0.5)

        # Keyboard move
        pag.press(['w', 's', 'a', 'd', 'space'])

        time_delayed += 3
    bot_status.config(text="Status: BOT HAS FINISHED HIS WORK")


def record(save_directory, filename, bot_status, button_start):
    try:
        bot_status.config(text="Status: ON")

        recording = keyboard.record(until='f10')

        path = save_directory + f"\{filename}.txt"
        f = open(path, 'w')
        for rec in recording:
            if rec == recording[-1]:
                f.write(f'{str(rec)}')
            else:
                f.write(f'{str(rec)},')
        f.close()

        button_start['state'] = 'normal'
        bot_status.config(text="Status: OFF")
        messagebox.showinfo('Done', 'Record saved successfully',)
    except:
        button_start['state'] = 'normal'
        bot_status.config(text="Status: OFF")
        messagebox.showerror('Error', 'Something went wrong. Try again.')


def play(file, loop, speed, bot_status, button_start):
    try:
        bot_status.config(text="Status: ON")

        list_keyboard_event = []
        f = open(file, 'r')
        recording = f.read()
        record_list = recording.split(sep=',')
        for rec in record_list:
            sliced = slice(rec.find('(') + 2, rec.find(')'), 1)
            list_keyboard_event.append(keyboard.KeyboardEvent(rec[sliced].strip(), rec[rec.find('(')+1],))

        if loop:
            while True:
                keyboard.play(list_keyboard_event, speed_factor=speed)
                time.sleep(1)
        else:
            keyboard.play(list_keyboard_event, speed_factor=speed)

        button_start['state'] = 'normal'
        bot_status.config(text="Status: OFF")
        messagebox.showinfo('Done', 'Action has ended', )
    except:
        button_start['state'] = 'normal'
        bot_status.config(text="Status: OFF")
        messagebox.showerror('Error', 'Something went wrong. Try again.')

