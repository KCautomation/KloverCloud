# Actions builder = new Actions(driver);
# builder.keyDown(Keys.RETURN).keyUp(Keys.RETURN).build().perform();
#
#
#  Robot robot = new Robot();
#     robot.keyPress(KeyEvent.VK_ENTER); //press enter key
#   robot.keyRelease(KeyEvent.VK_ENTER); //release enter key

import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test2():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    # tes = driver.find_element(By.XPATH, "//input[@id='email']")
    action = ActionChains(driver)
    # click the item
    action.send_keys(Keys.ENTER)
    # perform the operation
    action.perform()
    time.sleep(2)
    driver.close()


# def test1():
#     # driver = selenium.webdriver.Firefox()
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.google.com")
#     time.sleep(3)
#
#     # Robot robot = driver.r
#     # robot.keyPress(KeyEvent.VK_ENTER) //press enter key
#     # robot.keyRelease(KeyEvent.VK_ENTER) //release enter key
#
#     Robot = robot(driver)
#     robot.keyPress
#
#     #     action = ActionChains(driver)
#     #     # click the item
#     #     action.click()
#     #     # perform the operation
#     #     action.perform()
#     #     time.sleep(2)
#     # Actions builder = new Actions(driver)
#     # builder.keyDown(Keys.RETURN).keyUp(Keys.RETURN).build().perform()
#
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#     driver.close()
