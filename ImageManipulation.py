import cv2
import pyautogui


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
