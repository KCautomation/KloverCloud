import time
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://klovercloud.com/")
driver.maximize_window()
time.sleep(2)

getStart = "GET STARTED"
driver.find_element(By.LINK_TEXT, getStart).click()
time.sleep(5)

Email_box = "#mat-input-0"
driver.find_element(By.CSS_SELECTOR, Email_box).send_keys(10)
time.sleep(2)
# Password_box = "//body[1]/kc-root[1]/app-login[1]/div[1]/div[2]/div[1]/form[1]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # xpath
# driver.find_element(By.XPATH, Password_box).send_keys(10)
# time.sleep(1)
# Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"
# driver.find_element(By.XPATH, Sign_In_button).click()
# time.sleep(5)
# driver.close()
