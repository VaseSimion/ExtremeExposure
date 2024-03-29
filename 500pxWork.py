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
import Shutterstock as Sht

# model = tf.keras.models.load_model("ModelLocal.h5")
old_author = "Johnny Karate"
likedCounter = 0
commentCounter = 0
photosPerTurn = 50
turns = 100

Sht.shutterstock_make_view()

for i in range(turns):
    # open 500px and go to the newest photo
    subprocess.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe https://500px.com/upcoming")

    time.sleep(8)
    pyautogui.moveTo(x=159, y=489, duration=2)
    pyautogui.click()
    time.sleep(3)
    try:
        pyautogui.moveTo('UnselectedButton.png')  # Find where heart appears on the screen and click it.
        time.sleep(random.random())
        pyautogui.click()
        time.sleep(3)
    except:
        time.sleep(10 + 5*random.random())
        pyautogui.moveTo(x=159, y=489, duration=2)
        pyautogui.click()
        time.sleep(3)

    for j in range(photosPerTurn):
        # like this photo
        try:
            pyautogui.moveTo('Button.png')  # Find where heart appears on the screen and click it.
            time.sleep(random.random())
            pyautogui.click()
            likedCounter += 1
        except:
            try:
                pyautogui.moveTo('UnselectedButton.png')  # Find where heart appears on the screen and click it.
                time.sleep(random.random())
                pyautogui.click()
                likedCounter += 1
            except:
                pyautogui.press('right')  # press the right arrow key
                pyautogui.moveTo(x=159, y=489, duration=3 + 2 * random.random())
                continue

        # write the comment
        if 10*random.random() < 3:
            try:
                # generate a comment
                pyautogui.press('f6')  # press the right arrow key
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.5)
                author = Cmg.getauthor(clipboard.paste())
                comment = Cmg.getcomment("fluff", author)
                print(comment)

                if author != old_author:
                    # write it
                    pyautogui.scroll(-400)
                    time.sleep(1+random.random())
                    pyautogui.moveTo('comment_box.png')  # Find where comment appears on the screen and click it.
                    time.sleep(random.random())
                    pyautogui.click()

                    pyautogui.typewrite(comment, interval=0.15)

                    pyautogui.moveTo('comment_button.png')  # Find where heart appears on the screen and click it.
                    time.sleep(random.random())
                    pyautogui.click()

                    pyautogui.scroll(500)
                    commentCounter += 1
                    time.sleep(random.random())
                else:
                    pyautogui.click(x=850, y=950, duration=1)
                    pyautogui.scroll(600)
                old_author = author
            except:
                pyautogui.scroll(600)
                pyautogui.click(x=850, y=950, duration=1)
                print("Error with the comment")
        else:
            time.sleep(1 + random.random())

        # changing to next photo
        pyautogui.press('right')   # press the right arrow key
        pyautogui.moveTo(x=159, y=489, duration=3 + 2*random.random())

    pyautogui.hotkey('ctrl', 'w')  # ctrl-w to clsoe window
    #cv2.imshow("screenshot", Imp.get_resized_screenshot())
    cv2.waitKey(10000)
    print("Comments given: ", commentCounter)
    print("Likes given: ", likedCounter)

    if random.random() < 0.5:
        Sht.shutterstock_make_view()
    if random.random() < 0.5:
        Sht.shutterstock_make_view()
    time.sleep(60 + 60*random.random())
    if random.random() < 0.5:
        Sht.shutterstock_make_view()
    if random.random() < 0.5:
        Sht.shutterstock_make_view()
    time.sleep(60 + 60*random.random())
    if random.random() < 0.5:
        Sht.shutterstock_make_view()
    if random.random() < 0.5:
        Sht.shutterstock_make_view()
    time.sleep(60 + 60*random.random())


    #time.sleep(60 + 60*random.random())
# os.remove("screenshot.png")
