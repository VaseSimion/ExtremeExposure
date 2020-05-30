import subprocess
import cv2
import pyautogui
import time
import ImageManipulation as Imp
import CommentGenerator as Cmg
import random
import clipboard


old_author = "Johnny Karate"
for i in range(100):
    # open 500px and go to the newest photo
    subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe https://500px.com/upcoming")

    time.sleep(8)
    pyautogui.moveTo(x=159, y=489, duration=2)
    pyautogui.click()
    time.sleep(3)
    try:
        pyautogui.moveTo('Button.png')  # Find where heart appears on the screen and click it.
        time.sleep(random.random())
    except:
        time.sleep(10 + 5*random.random())
        pyautogui.moveTo(x=159, y=489, duration=2)
        pyautogui.click()
        time.sleep(3)

    for j in range(50):
        # like this photo
        try:
            pyautogui.moveTo('Button.png')  # Find where heart appears on the screen and click it.
            time.sleep(random.random())
            pyautogui.click()
        except:
            pyautogui.press('right')  # press the right arrow key
            pyautogui.moveTo(x=159, y=489, duration=3 + 2 * random.random())
            continue

        # write the comment
        if 10*random.random() < 3:
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
                pyautogui.moveTo('comment_box.png')  # Find where heart appears on the screen and click it.
                time.sleep(random.random())
                pyautogui.click()

                pyautogui.typewrite(comment, interval=0.15)

                pyautogui.moveTo('comment_button.png')  # Find where heart appears on the screen and click it.
                time.sleep(random.random())
                pyautogui.click()

                pyautogui.scroll(500)
                time.sleep(random.random())
            else:
                pyautogui.click(x=850, y=950, duration=1)
            old_author = author
        else:
            time.sleep(1 + random.random())
        # changing to next photo
        pyautogui.press('right')   # press the right arrow key
        pyautogui.moveTo(x=159, y=489, duration=3 + 2*random.random())

    pyautogui.hotkey('ctrl', 'w')  # ctrl-w to clsoe window
    cv2.imshow("screenshot", Imp.get_resized_screenshot())
    cv2.waitKey(10000)
    time.sleep(60 + 60*random.random())
    time.sleep(60 + 60*random.random())
    time.sleep(60 + 60*random.random())
    time.sleep(60 + 60*random.random())
# os.remove("screenshot.png")
