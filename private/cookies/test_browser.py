import pickle
import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test1():
    # pytest.skip("Skipping test...later I will implement...")
    username = "admin@klovercloud.com"
    password = "Hello@1234"
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument('user-data-dir=C:\\Users\\shabr\\Downloads\\chromedriver_win32\\chromeprofile')
    chrome_driver = "C:/Users/shabr/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)  # driver = webdriver.Chrome()
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
    # pytest.skip("Skipping test...later I will implement...")
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument('user-data-dir=C:\\Users\\shabr\\Downloads\\chromedriver_win32\\chromeprofile')
    chrome_driver = "C:/Users/shabr/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

    # Print website title to make sure its connected properly
    driver.get("https://eks.alpha.klovercloud.io/")
    time.sleep(3)
    print(driver.title)

    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys('test')


def test3():
    pytest.skip("Skipping test...later I will implement...")
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument('user-data-dir=C:\\Users\\shabr\\Downloads\\chromedriver_win32\\chromeprofile')
    chrome_driver = "C:/Users/shabr/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

    # Print website title to make sure its connected properly
    driver.get('https://google.com')
    time.sleep(4)
    print(driver.title)

    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys('test')
