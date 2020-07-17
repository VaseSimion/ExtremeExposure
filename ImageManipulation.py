import cv2
import pyautogui
import numpy as np


def get_resized_screenshot():
    desired_size = 224
    pyautogui.screenshot("screenshot.png")
    image = cv2.imread("screenshot.png")
    image = image[120:760, 440:1440]

    old_size = image.shape[:2]  # old_size is in (height, width) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # new_size should be in (width, height) format
    image = cv2.resize(image, (new_size[1], new_size[0]))
    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    color = [0, 0, 0]
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return image


def resize_picture_to_square(picture, size):
    desired_size = size
    image = picture

    old_size = image.shape[:2]  # old_size is in (height, width) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # new_size should be in (width, height) format
    image = cv2.resize(image, (new_size[1], new_size[0]))
    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    color = [0, 0, 0]
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return image

def decode(predictions):
    predictions = [float(round(x, 1)) for x in predictions]
    if predictions.index(max(predictions)) == 0:
        return "Animal"
    elif predictions.index(max(predictions)) == 1:
        return "Cityscape"
    elif predictions.index(max(predictions)) == 2:
        return "Flower"
    elif predictions.index(max(predictions)) == 3:
        return "Landscape"
    elif predictions.index(max(predictions)) == 4:
        return "Portrait"
    elif predictions.index(max(predictions)) == 5:
        return "Unknown"
    else:
        return "Somehting went wrong"


def isHeartRed():
    pyautogui.screenshot("forinstatemp.png")
    image = cv2.imread("forinstatemp.png", 0)

    template = cv2.imread('instaHeart.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.99

    if max_val > threshold:
        print("heart is not red")
        return False
    else:
        print("Heart is red")
        return True

def returnCommentBoxCoordinates():
    pyautogui.screenshot("forinstatemp.png")
    image = cv2.imread("forinstatemp.png", 0)

    template = cv2.imread('instaComment.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.95
    if max_val > threshold:
        x = max_loc[0] + w // 2
        y = max_loc[1] + h // 2


    if x != 9999:
        #print("Found the box")
        return [True, x, y]
    else:
        #print("No box")
        return [False, x, y]

def returnPostBoxCoordinates():
    pyautogui.screenshot("forinstatemp.png")
    image = cv2.imread("forinstatemp.png", 0)

    template = cv2.imread('instaPost.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.95
    if max_val > threshold:
        x = max_loc[0] + w // 2
        y = max_loc[1] + h // 2

    if x != 9999:
        #print("Found the box")
        return [True, x, y]
    else:
        #print("No box")
        return [False, x, y]