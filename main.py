import pyautogui as pag
import time
import random

def go(working_time,bot_status):
    time_delayed = 0.0
    bot_status.config(text="Status: BOT IS WORKING")

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
     

