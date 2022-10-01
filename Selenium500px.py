import CommentGenerator as Cmg
import random
import time
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


white_heart = "iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAg5JREFUWIXtlyGyo0AURd+fGktWgGoZ0zgw4IiBDSQqMbABImMS+Q02hoqKIhtoNsAGYAVsoJMF3DHDr5mqTLqh+TURHMut16ceTffjAwDojfnxvwVUzIKmzIKmzIKmvL3gzyHhqqrodrtRVVVERGTbNoVhSNvtlmzb/ivbdR1dLheqqoq6riMiojAMabfbkeu6+otCkyzLwBhDlmUQQqCuaxRFAd/34TgOhBBfWSEEHMeB7/soigJ1XUMI8VVjv9/rLgstwSzLwDlH0zRPnx+PRzDGUJYlyrIEYwx5nj/NNk0Dzrm2pFKwrmswxlDX9ctcL8kYQ1EUL7NCCK2aAPABvB4W0jQlIqLz+azcLqfTiYiIDoeDMpumKS0WC/r8/DTbg5zzf74uE/I8h+M4ypzymHk8HuR5nrIjQ/E8j+73uzKnFLQsi9q2nUTqT9q2JcuylDmloOu63yaodR6q9oDuVzyEITW1zsEkSRAEAaSUxnJSSgRBgCRJtPJaglJKRFGEOI6NJKWUiOMYURRp19G+6kwlx8gNEjSRHCs3WHCMpIncKMF+Uc450jRVZtfrNXzfH713RwkCelOJagrSYbQg8FpyCjnAUBB4LjmVHKAxbuleW5vNhlarFQGgqqroer3Scrk0La0/8qvoOzlV53om6WBPP1RM0rnfTCr4Hbz9f/EsaMosaMosaMrbC/4CUS8GbK3muvMAAAAASUVORK5CYII="
white_selectedheart = "iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAABBBJREFUWIXVmT1v4lgUhl8uhsFmoiiQ3ezsyKQKjFajxUjThGokoKRNWmhT+2eElta0+Q2RpWkSNyNhjaJIIdXYyibR8iGUwRAw3C2QWbL4g69B2bdCvgefx/fec3zusY9SSrGEmsYQjY6JdneITn+E3oDCHI1vxRAfQgEfwkGCbdaPaJhBhPMv4wa+RQA7/RH0Vh93bRO9wWghR6EAwfttBvxOEOEgWS/gs0lx+/czvjf7C0E5aT8SxMEvb/CG8a0OqLcGuH7oTZZvXWKID3/8FgK/E1ge8Oq+t7ZZc9J+JIiP70KO446AXzUDj0/mTwOb1t4Wg08xznbMdrduEg4AHp9MfNUM27EZwKv73kbhLD0+mbi6781cfwGotwY/fc+56XuzD701eHGNsX48mxTXD7NPMC1VVXF5eQlVVQEA0WgUgiAgk8lgd3f3hW29Xocsy1BVFY1GAwAgCAKy2Szi8bijj+uHHn7dYiYpaBIkXhErSRIURcHh4SFSqRQ4joOmaZBlGd1uF4VCAYIgTB6kUqmAZVlkMhnEYjEYhoFqtQpFUZBOp1EoFBx9TUe2j1JKO/0Rvtz+cIVTVRWiKILn+Znxs7MzyLI8cVqpVJDP55HP52dsdV3H6ekpUqmUK+Tng7cIB8l4ifWW88zVajUoiuIIBwDHx8cTMAA4OjpCNpu1teV5HsViEeVyGel02nG59VYfH/ZCY8C7tnPUnp+fI5lMuu6baUgAjnCWBEFAMpnExcWF433v2iY+7AFM0xi6vvhrtZqnQztIL8ViMciy7DjeG4zQNIYgjY57zut2u0gkEnM7nleJRAKGYZ+cLTU6Jki7O3Q1YlkWmqatkw0AoGkaWJZ1tWl3hyCdvntdF4/Hoev6OtkAjKPZa193+iOQ3sC9jMrlclAUBbVabW1wVmbI5XKudr0BBfGq8+LxOJLJJCRJ8twz88gwDEiSNFdmMEfUvpr5r4rFIliWRalUWgnSMAyUSiWwLItisTjXfwhDvMtujuMgiiIopUtDWnCUUoiiCI6zr/+mxRAfSCjgDbgq5DJwABAK+EAWOWEtA7ksHACEgwRkm13svGpB1uv1ybvXTeVyGYZhLAwHANusHyQaZrwtHSBvbm5cISVJgq7rODk5WRgOAKJhBiTC+REKzL/MlniehyiKqFartpBeJZqXQgGCCOcfp5n324vPohvkqnDTTHMVrF6aLkIppSvDAf8WrHOX/PNCAlgZbqbkB8aHpi+3P1ZqcVhFxSpwDPHh88Hb2UMTMD52fvuru/TN16E/f2df9GtehC+/E8B+JLhxKEv7keBMM2kmv3x8F8Le1nJRvYr2thjbJpJtAvwU4zYK6dY8+v+23yy96gampVfdAp7Wq22i22lTnyH+ASLNVyHNRpXRAAAAAElFTkSuQmCC"
red_heart = "iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAeJJREFUWIXt1zFIAlEYB/C/cYNwdzg4KAgNKioO4mJLTra45VBbga0h1ZaSo4JtKe0JtdUQTS462ZKLOURItBk6OIgKDoINoVldvnfvvcjh/vPH9353x3vvO9NkMplgibPy3wBSDCBvDCBvDCBvlh4o6Snulqvo3JXQLVcBAGaHHdZIGKv7cUiq8qV21Grj7eoG3UoVo1YbAGDdCMOxswVLKEi9ponmJhn3B2imczPY90iqAn8hM1u4c1vC6+k5xv2BZr0tFoXzOPHjoZiBTwcn6Fbuic08mSQAoJnOEWttseisngvYq9XR2DsiNmJJ4OKM+LmJm6R1eS0MxNKbCOw91IVgNHvXHok1ROB4MBSC0ez9yyaaDxEoKbIQDGtvItCyRn9m6Q1NbyLQsbstBMPam/wGQ0FYI+tCQPOxbUapbhSqu9iTTUH2urhR08heF5zJBFUtFVBSFQSKeSFI2etCoJinuuYAHdOMCKReHKBz3OJBsuAAhnmQBcmKAxgHVklV4M2mqA5aSZHhL2SZcADHRC373B9vZQFSUmQEinmYHXbWZfhG/kXIKU72uXmW4P8n0UKKwgGUEzVNhs8vaMQPAUAYDhAIBD7HJ9YNoRWhwL/I0v8XG0DeGEDeGEDeLD3wHYkdjlITLcNWAAAAAElFTkSuQmCC"


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
        heart = driver.find_element(By.XPATH, "//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div")
        if heart.screenshot_as_base64 == white_heart or heart.screenshot_as_base64 == white_selectedheart:
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
                                            "//*[@id=\"open-modal\"]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div")
                if heart.screenshot_as_base64 == white_heart or heart.screenshot_as_base64 == white_selectedheart:
                    heart.click()
                    likedCounter += 1
                    time.sleep(2 + 2 * random.random())
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

