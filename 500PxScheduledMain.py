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
import ImageManagement as Im


Spx.upload_photo()
Spx.run_series_of_likes(100)

schedule.every(2).days.at("21:35").do(Spx.run_series_of_likes, numberofturns=130)
schedule.every(2).days.at("21:25").do(Spx.upload_photo)

while True:
    schedule.run_pending()
    time.sleep(1)
