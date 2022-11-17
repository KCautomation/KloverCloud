# Importing necessary Libraries
import pickle
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# save cookie function
def seleniumSaveCookie():
    # creating a webdriver object
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://eks.alpha.klovercloud.io/")  # opening the url
    try:
        pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb"))  # writing in pickle file
        print('Cookie file successfully created.')
    except Exception as e:
        print(e)


# driver
if __name__ == "__main__":
    seleniumSaveCookie()  # call the function


def seleniumLoadCookie():
    # creating a webdriver object
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.codespeedy.com/")  # opening the url
    try:
        cookie = pickle.load(open("cookie.pkl", "rb"))  # loading from pickle file
        for i in cookie:
            driver.add_cookie(i)
        print('Cookies added.')
    except Exception as e:
        print(e)
    time.sleep(3)
    driver.get("https://eks.alpha.klovercloud.io/dashboard")
    time.sleep(5)


# driver
if __name__ == "__main__":
    seleniumLoadCookie()  # call the function
