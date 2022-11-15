import pickle
import time

import robot
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys, ActionChains


def test1():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    action = ActionChains(driver)
    # click the item
    # # action.send_keys(Keys.PAGE_DOWN)
    # action.perform()
    # time.sleep(2)
    # scroll to element
    action.scroll_to_element(driver.find_element(By.XPATH, "//a[contains(text(),'Cookies')]"))
    action.perform()
    time.sleep(2)

    # perform the operation
    action.send_keys(Keys.PAGE_UP)
    action.perform()
    time.sleep(2)

    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))



    driver.close()
