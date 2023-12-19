import CommentGenerator as Cmg
import random
import time
import pyautogui
import pyperclip
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import ImageManagement as Im


def run_series_of_likes(numberofturns):
    print("******************************************** New run started, runs left:",numberofturns)
    # open 500px and go to the newest photo
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://500px.com/login?r=%2Fupcoming")
    action = ActionChains(driver)
    try:
        # login
        user = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "emailOrUsername"))). \
            send_keys("")
        passfill = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "")
        driver.find_element(By.XPATH, "//*/div[3]/div/form/button").click()

        # wait to be logged in
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "justifiedGrid")))

        old_author = "Johnny Karate"
        likedCounter = 0
        commentCounter = 0
        photosPerTurn = 50
        for i in range(numberofturns):
            try:
                driver.get("https://500px.com/upcoming")
                photos_section = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "justifiedGrid")))
                WebDriverWait(photos_section, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class^='Elements__PhotoCardWrapper-sc-1obh427-7']")))
                time.sleep(2)
                photos = driver.find_elements(By.CSS_SELECTOR, "div[class^='Elements__PhotoCardWrapper-sc-1obh427-7']")
                try:
                    driver.execute_script('arguments[0].scrollIntoView();',photos[6])
                    time.sleep(0.1)
                    action.move_to_element(photos[6]).click().perform()
                except:
                    time.sleep(2)
                    action.move_to_element(photos[6]).click().perform()
            except:
                print("Error code 1")
                time.sleep(3)

            # like
            try:
                heart_box = WebDriverWait(driver, 30).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "StyledLayout__Box-b9gazd-0.Elements__IconWrapper-sc-1t7bwc6-1.laOSpw")))

                heart_color = heart_box.get_attribute('aria-label')

                if heart_color == 'Unlike photo':
                    heart_box.click()
                    likedCounter += 1
                else:
                    WebDriverWait(driver, 30).until(ec.presence_of_element_located(
                            (By.CLASS_NAME, "Elements__PhotoNavigationChevron-sc-1e3xy9t-26.ecpwQD"))).click()
            except:
                print("Error code 2")
                try:
                    driver.get("https://500px.com/upcoming")
                    photos_section = WebDriverWait(driver, 60).until(
                        ec.presence_of_element_located((By.ID, "justifiedGrid")))
                    WebDriverWait(photos_section, 60).until(ec.presence_of_element_located(
                        (By.CSS_SELECTOR, "div[class^='Elements__PhotoCardWrapper-sc-1obh427-7']")))
                    photos = driver.find_elements(By.CSS_SELECTOR,
                                                  "div[class^='Elements__PhotoCardWrapper-sc-1obh427-7']")
                    try:
                        action.move_to_element(photos[6]).click().perform()
                    except:
                        time.sleep(2)
                        action.move_to_element(photos[6]).click().perform()
                except:
                    print("Error code 3")
                    pass

            time.sleep(2 + 2 * random.random())

            for j in range(photosPerTurn):
                # print("******************Run", j)
                # like this photo
                try:
                    # print("In try")
                    heart_box = WebDriverWait(driver, 30).until(
                        ec.presence_of_element_located(
                            (By.CLASS_NAME, "StyledLayout__Box-b9gazd-0.Elements__IconWrapper-sc-1t7bwc6-1.laOSpw")))
                    heart_color = heart_box.get_attribute('aria-label')
                    #print(heart_color)
                    driver.execute_script('arguments[0].scrollIntoView();', heart_box)
                    if heart_color == 'Unlike photo':
                        heart_box.click()
                        likedCounter += 1
                        time.sleep(1)
                    else:
                        action.send_keys(Keys.ARROW_RIGHT).perform()
                        time.sleep(1)
                        continue
                except:
                    print("Error code 4")
                    time.sleep(180)
                    try:
                        driver.close()
                    except:
                        print("Driver was not on")
                    run_series_of_likes(numberofturns-i)
                    i=numberofturns-1
                    break
                # write the comment
                if 10 * random.random() < 3:
                    try:
                        # generate a comment
                        author_box = WebDriverWait(driver, 60).until(
                            ec.presence_of_element_located((By.CLASS_NAME,
                                                            "StyledTypography__Paragraph-sc-1un6cv3-4.jIDtxr")))
                        author = author_box.text.split("\n")[1].split(" ")[0]
                        comment = Cmg.getcomment("fluff", author)
                        print(comment)

                        if author != old_author:

                            # write it
                            comm_box = WebDriverWait(driver, 30).until(
                                ec.presence_of_element_located((By.CLASS_NAME, "Elements__StyledTextarea-sc-48xv3y-12.ipxgRV")))
                            driver.execute_script('arguments[0].scrollIntoView();', comm_box)
                            comm_box.send_keys(comment)
                            time.sleep(2 + 2 * random.random())

                            driver.find_elements(By.CLASS_NAME, "Elements__Button-tze21g-2.dgFUjF")[-1].click()
                            time.sleep(2 + random.random())

                            commentCounter += 1
                        else:
                            print("Same author as before")
                        old_author = author
                    except:
                        print("Error on commenting")
                else:
                    time.sleep(1 + random.random())

                time.sleep(2 + 2 * random.random())
                # move to next photo
                try:
                    #send next picture
                    action.send_keys(Keys.ARROW_RIGHT).perform() # this seems to not work
                except:
                    print("6")
                    time.sleep(1)

            print("Comments given: ", commentCounter)
            print("Likes given: ", likedCounter)
            time.sleep(180 + 180 * random.random())
        driver.close()
    except:
        print("7")
        time.sleep()
        try:
            driver.close()
        except:
            print("Driver was not on")
        run_series_of_likes(numberofturns-i)
        i=numberofturns-1
    print("Session done")


def upload_photo():
    try:
        path = Im.get_image_path("/home/vase/ExtremeExposure/Photos")
        title = "Norway landscape this summer, as seen on @simion.vase"
        caption = Im.generate_image_caption(path)
        
        # open 500px and go to the newest photo
        driver = webdriver.Chrome()
        driver.get("https://500px.com/login?r=%2Fupcoming")
        action = ActionChains(driver)

        # login
        user = WebDriverWait(driver,60).until(ec.presence_of_element_located((By.ID, "emailOrUsername"))). \
            send_keys("sularea.vasile@gmail.com")
        passfill = WebDriverWait(driver,40).until(ec.presence_of_element_located((By.ID, "password"))).send_keys(
            "V15as11E")
        driver.find_element(By.XPATH, "//*/div[3]/div/form/button").click()

        # wait to be logged in
        photos_section = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "justifiedGrid")))

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/nav/div[1]/div[2]/div[3]/button").click()
        upload_button = WebDriverWait(driver, 30).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id=\"root\"]/div[3]/div[2]/div/span/div/span/div/div/div[2]/div[2]/span/div/span/div/div")))
        upload_button.click()
        pyperclip.copy(path)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v', interval=0.3)
        pyautogui.press('Enter')
        time.sleep(10)

        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id=\"editpanel-title\"]")))
        time.sleep(10)
        element.send_keys("a")
        element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        element.send_keys(title)

        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id=\"edit-panel-description\"]")))
        element.send_keys(caption)
        
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "Elements__StyledInput-sc-48xv3y-13.bCsoEX"))).send_keys("Landscape")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "category-option-0"))).click()
        
        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "btn-upload")))
        element.click()
        time.sleep(10)
        os.remove(path)

        driver.close()
        print("photo uploaded",path)
    except:
        try:
            driver.close()
        except:
            print("Driver was not defined")
        upload_photo(path, title, caption)

if __name__ == "__main__":
    time.sleep(10)
