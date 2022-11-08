import pyautogui as pag
import time
import random

status = "BOT IS NOT WORKING"


def go(working_time):
    time_delayed = 0.0
    status = "BOT IS WORKING"

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
    status = "BOTTING IS DONE"

