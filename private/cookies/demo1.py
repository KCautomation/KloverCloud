import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test1():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    time.sleep(3)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.close()


def test2():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.close()
