import pyautogui as pag
import time
import random


def go(working_time):
    time_delayed = 0.0
    # Primary monitor size
    screen_width, screen_high = pag.size()
    while time_delayed <= working_time:
        # Mouse move
        pag.click()
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_high)
        pag.moveTo(x, y, 0.5)

        # Keyboard move
        pag.press(['w', 's', 'a', 'd', 'space'])
        time_delayed += 3
        time.sleep(3)
