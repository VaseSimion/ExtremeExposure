import subprocess
import cv2
import pyautogui
import time
import ImageManipulation as Imp
import CommentGenerator as Cmg
import random
import clipboard

# open 500px and go to the newest photo
subprocess.call("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe https://500px.com/fresh")
time.sleep(8)
pyautogui.moveTo(x=159, y=489, duration=2)
pyautogui.click()
time.sleep(3)

for i in range(2):
    # like this photo
    pyautogui.moveTo('Button.png')  # Find where heart appears on the screen and click it.
    time.sleep(random.random())
    pyautogui.click()

    # generate a comment
    pyautogui.press('f6')   # press the right arrow key
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    author = Cmg.getauthor(clipboard.paste())
    comment = Cmg.getcomment("fluff", author)
    print(comment)

    # write the comment
    if True:  # 10*random.random() < 4:
        pyautogui.scroll(-400)
        time.sleep(1+random.random())
        pyautogui.moveTo('comment_box.png')  # Find where heart appears on the screen and click it.
        time.sleep(random.random())
        pyautogui.click()

        pyautogui.typewrite(comment, interval=0.2)

        pyautogui.moveTo('comment_button.png')  # Find where heart appears on the screen and click it.
        time.sleep(random.random())
        pyautogui.click()

        pyautogui.scroll(500)
        time.sleep(random.random())

    # changing to next photo
    pyautogui.click(x=200, y=900, duration=1 + random.random())
    pyautogui.press('right')   # press the right arrow key
    pyautogui.moveTo(x=159, y=489, duration=3 + 2*random.random())


pyautogui.hotkey('ctrl', 'w')  # ctrl-w to clsoe window
cv2.imshow("screenshot", Imp.get_resized_screenshot())
cv2.waitKey(10000)
# os.remove("screenshot.png")
