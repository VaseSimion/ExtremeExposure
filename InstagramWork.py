import subprocess
import cv2
import pyautogui
import time
import ImageManipulation as Imp
import CommentGenerator as Cmg
import random
import clipboard
#import tensorflow as tf
import numpy as np

file = ["https://www.instagram.com/explore/tags/travel/", "https://www.instagram.com/explore/tags/backpacking/",
        "https://www.instagram.com/explore/tags/photography/", "https://www.instagram.com/explore/tags/model/"]

#model = tf.keras.models.load_model("ModelLocal.h5")
old_author = "Johnny Karate"
for i in range(20):
    #open a page out of the file tags list and open a picture
    subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe " + random.choice(file))
    time.sleep(8)

    pyautogui.moveTo(x=500, y=489, duration=2)
    pyautogui.scroll(int(-500*random.random()) - 500)
    time.sleep(1 + random.random())
    pyautogui.scroll(int(-500*random.random()) - 500)
    time.sleep(1 + random.random())
    pyautogui.scroll(int(-500*random.random()) - 500)
    time.sleep(1 + random.random())
    pyautogui.click()
    time.sleep(3)

    if not Imp.isHeartRed():  # this means there is no empty heart on the screen
        pass
    else:
        pyautogui.moveTo(x=500, y=589, duration=0.5)
        pyautogui.click()
        time.sleep(3)

    for iterable in range(12):
        if Imp.isHeartRed():
            continue

        pyautogui.doubleClick(x=800, y=570, duration=2)
        time.sleep(1)
        if Imp.isHeartRed() and random.random() < 0.3:

            [present, x_box, y_box] = Imp.returnCommentBoxCoordinates()
            if present:
                pyautogui.moveTo(x=x_box, y=y_box, duration=0.5)
                time.sleep(random.random())
                pyautogui.click()

                comment = Cmg.getcomment("", "")
                pyautogui.typewrite(comment, interval=0.15)

                [present, x_post, y_post] = Imp.returnPostBoxCoordinates()
                pyautogui.moveTo(x=x_post, y=y_post, duration=0.3)
                time.sleep(1 + random.random())
                pyautogui.click()
            else:
                print("WTF?")

        pyautogui.moveTo(x=1450, y=580, duration=2)
        pyautogui.click()

        time.sleep(2 + 2*random.random())
    # close the page and wait before the next start of likes
    #pyautogui.hotkey('ctrl', 'w')  # ctrl-w to clsoe window
    cv2.imshow("screenshot", Imp.get_resized_screenshot())
    cv2.waitKey(100)
    time.sleep(60 + 60*random.random())
    time.sleep(60 + 60*random.random())
    time.sleep(60 + 60*random.random())
    time.sleep(60 + 60*random.random())
# os.remove("screenshot.png")
