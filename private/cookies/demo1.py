import pickle
from http import cookies
from telnetlib import EC

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

cookies_path = "C:\\Users\\shabr\\PycharmProjects\\KloverCloud\\private\\cookies\\cookies.pkl"


def test1():
    username = "admin@klovercloud.com"
    password = "Hello@1234"
    driver = selenium.webdriver.Firefox()
    # chromedriver.TARGET_VERSION = 90
    # chrome.install()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://eks.alpha.klovercloud.io/")

    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys(username)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,
                        "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]").click()
    time.sleep(7)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.close()


def test2():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://eks.alpha.klovercloud.io/")
    time.sleep(10)
    cookies = pickle.load(open(cookies_path, "rb"))
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):  # Checks if the instance expiry a float
            cookie['expiry'] = int(cookie['expiry'])  # it converts expiry cookie to a int
        driver.add_cookie(cookie)
        print(driver.get_cookies())
        driver.get("https://eks.alpha.klovercloud.io/dashboard/")
        time.sleep(4)

    driver.close()
