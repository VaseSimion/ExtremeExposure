import subprocess
import time
import pyautogui
import random


def shutterstock_make_view():
    try:
        page_number = random.randint(1, 2)
        subprocess.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe https://www.shutterstock.com/da/g/Vase+Simion")
        time.sleep(5)
        if page_number == 1:
            pyautogui.scroll(-400 - (560*random.randint(0, 10)))
        elif page_number == 2:
            pyautogui.moveTo(x=1828, y=628, duration=1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.scroll(-400 - 480*random.randint(0, 10))
        pyautogui.click(x=32 + 1800*random.random(), y=115 + 850 * random.random(), duration=1)
        time.sleep(3)
        pyautogui.moveTo('Download.PNG')  # Find where heart appears on the screen and click it.
        pyautogui.click()
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'w')  # ctrl-w to close window
        pyautogui.click(x=1900, y=1000, duration=5)
        pyautogui.moveTo(x=500, y=500, duration=1)
    except:
        print("Something went bad")
        pyautogui.hotkey('ctrl', 'w')  # ctrl-w to close window