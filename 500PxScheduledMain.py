import schedule
import Selenium500px as Spx
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time


# open 500px and go to the newest photo
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://500px.com/login?r=%2Fupcoming")
action = ActionChains(driver)

# login
user = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "emailOrUsername"))).\
    send_keys("NAME")
passfill = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "password"))).send_keys("PASS")
driver.find_element(By.XPATH, "//*/div[3]/div/form/button").click()

# wait to be logged in
photos_section = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.ID, "justifiedGrid")))

path = 'photo path'
title = "Photo taken in Norway this summer. For more pictures follow @simion.vase"
description = "Photo taken in a trip to Lofoten this summer"

#Spx.upload_photo(driver, path, title, description)
schedule.every(2).days.at("21:00").do(Spx.run_series_of_likes, driver=driver)
Spx.run_series_of_likes(driver)
while True:
    schedule.run_pending()
    time.sleep(1)
