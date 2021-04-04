import pyautogui
import time
from datetime import datetime

while True:

    accept = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
    decline = pyautogui.locateCenterOnScreen('decline.png', confidence=0.7)

    if accept:
        pyautogui.moveTo(accept)
        # click multiple times just to make sure accept button gets clicked
        pyautogui.click(accept)

        print(f'Game Accepted. {datetime.now()}')

        # Discord stuff

        time.sleep(5)
    else:
        print(datetime.now())
        time.sleep(1)
