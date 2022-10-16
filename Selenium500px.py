import CommentGenerator as Cmg
import random
import time
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def run_series_of_likes(driver):
    old_author = "Johnny Karate"
    likedCounter = 0
    commentCounter = 0
    photosPerTurn = 50
    numberofturns = 70
    for i in range(numberofturns):
        driver.get("https://500px.com/upcoming")
        try:
            photos_section = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "justifiedGrid")))
            first_photo = WebDriverWait(photos_section, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "StyledLayout__Box-b9gazd-0.jhVwFU")))
            first_photo.click()
        except:
            pass
        time.sleep(3)

        # like
        heart = driver.find_element(By.XPATH,'//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/*[name()="svg"]')
        heart_color = heart.get_attribute('innerHTML').split("\"")[heart.get_attribute('innerHTML').split("\"").index(" fill=") + 1]

        if heart_color == "#222222":
            heart = driver.find_element(By.XPATH,
                                        "//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div")
            heart.click()
            likedCounter += 1
        else:
            buttons = driver.find_elements(By.XPATH,
                                           "//*[@id=\"copyrightTooltipContainer\"]/div[1]/div/div[3]/div/div/div")
            buttons[-1].click()

        time.sleep(2 + 2*random.random())

        for j in range(photosPerTurn):

            # like this photo
            try:
                heart = driver.find_element(By.XPATH,
                                            '//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/*[name()="svg"]')
                heart_color = heart.get_attribute('innerHTML').split("\"")[
                    heart.get_attribute('innerHTML').split("\"").index(" fill=") + 1]

                if heart_color == "#222222": # #c22b3f for red
                    heart = driver.find_element(By.XPATH,
                                                "//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div")
                    heart.click()
                    likedCounter += 1
                else:
                    buttons = driver.find_elements(By.XPATH,
                                                   "//*[@id=\"copyrightTooltipContainer\"]/div[1]/div/div[3]/div/div/div")
                    buttons[-1].click()
                    continue
            except:
                buttons = driver.find_elements(By.XPATH,
                                               "//*[@id=\"copyrightTooltipContainer\"]/div[1]/div/div[3]/div/div/div")
                buttons[-1].click()
                continue

            # write the comment
            if 10*random.random() < 3:
                try:
                    # generate a comment
                    author_box = driver.find_element(By.XPATH, "//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/p/span/a")
                    author = author_box.text.split('\n')[0]
                    comment = Cmg.getcomment("fluff", author)
                    print(comment)

                    if author != old_author:

                        # write it
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//*[@id=\"create-comment\"]"))).send_keys(comment)
                        time.sleep(2+2*random.random())

                        driver.find_element(By.XPATH, "//*[@id=\"create-button\"]/button[2]").click()
                        time.sleep(2 + random.random())

                        commentCounter += 1
                    else:
                        pass
                    old_author = author
                except:
                    print("Error with the comment")
            else:
                time.sleep(1 + random.random())

            #move to next photo
            try:
                buttons = driver.find_elements(By.XPATH,
                                         "//*[@id=\"copyrightTooltipContainer\"]/div[1]/div/div[3]/div/div/div")
                buttons[-1].click()
            except:
                time.sleep(1)
            time.sleep(3 + 2*random.random())

        print("Comments given: ", commentCounter)
        print("Likes given: ", likedCounter)
        time.sleep(180 + 180*random.random())


def upload_photo(driver, path, title, caption):
    driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/nav/div[1]/div[2]/div[3]/button").click()
    upload_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/div[3]/div[2]/div/span/div/span/div/div/div[2]/div[2]/span/div/span/div/div")))
    upload_button.click()
    time.sleep(1)
    pyautogui.write(path)
    pyautogui.press('Enter')
    time.sleep(10)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"editpanel-title\"]")))
    element.send_keys("a")
    element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    element.send_keys(title)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"edit-panel-description\"]")))
    element.send_keys(caption)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-upload")))
    element.click()

