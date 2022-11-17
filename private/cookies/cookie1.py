import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test1():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://www.google.com")
    driver.get("https://eks.alpha.klovercloud.io/")
    time.sleep(3)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.close()


def test2():
    # driver = selenium.webdriver.Firefox()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print("\n", cookies, "\n")
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.close()
