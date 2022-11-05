import pyautogui as pag
import time
import random

time_delayed = 0.0
# Primary monitor size
screen_width, screen_high = pag.size()

while True:
    try:
        bot_working_time = float(input("Enter how long the bot should run (in minutes):")) * 60
        while time_delayed <= bot_working_time:
            # Mouse move
            pag.click()
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_high)
            pag.moveTo(x, y, 0.5)
            # Keyboard move
            pag.press(['w', 's', 'a', 'd', 'space'])
            time_delayed += 3
            # interval
            print("BOT IS WORKING")
            time.sleep(3)
        print("BOT HAS FINISHED HIS WORK")
        break;
    except:
        print("Invalid input")
        time.sleep(1)





