import pyautogui
import cv2
import numpy as np
import time

time.sleep(2)
pyautogui.screenshot("forinstatemp.png")
image = cv2.imread("forinstatemp.png", 0)

template = cv2.imread('instaHeart.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

threshold = 0.90
loc = np.where(res >= threshold)
x = 9999
y = 9999
print(loc)
for pt in zip(*loc[::-1]):
    x = pt[0] + w // 2
    y = pt[1] + h // 2

