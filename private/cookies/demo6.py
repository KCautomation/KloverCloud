import pickle
import time
from telnetlib import EC
import allure
import pytest
from unittest import TestCase
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import simple_colors
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from urllib.request import urlopen
from urllib.error import *
from nose.tools import *


class TestMethod:

    def test_cookies(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.alpha.klovercloud.io/"
        username = "admin@klovercloud.com"
        password = "Hello@1234"
        # driver = selenium.webdriver.Firefox()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(pageUrl)
        time.sleep(2)
        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print(Fore.LIGHTRED_EX + "HTTP error", e)

        except URLError as e:
            print(Fore.LIGHTRED_EX + "Opps ! Page not found!", e)

        else:
            print(Fore.YELLOW + 'Yeah ! URL found ')

        self.driver.implicitly_wait(20)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='mat-input-0']")))
            print("Email_box is inputable")
            Email_box.send_keys(username)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put email in Email_box')

        # put password
        try:
            Password_box = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='mat-input-1']")))
            print("Password_box is inputable")
            Password_box.send_keys(password)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put password in Password_box')

        # click on Toggle_Visibility_Button
        try:
            Toggle_Visibility_Button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[4]/button")))
            print("Toggle_Visibility_Button is clickable")
            Toggle_Visibility_Button.click()
            time.sleep(1)
            Toggle_Visibility_Button.click()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')
        # Click on Sign In button

        try:
            Sign_In_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]")))
            print("Password_box is inputable")
            Sign_In_button.click()
            self.driver.implicitly_wait(10)
            time.sleep(7)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

        driver.close()

    def test2(self):
        # driver = selenium.webdriver.Firefox()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.codespeedy.com/")  # opening the url
        driver.maximize_window()
        time.sleep(4)
        try:
            cookie = pickle.load(open("cookie.pkl", "rb"))  # loading from pickle file
            for i in cookie:
                driver.add_cookie(i)
            print('Cookies added.')
        except Exception as e:
            print(e)
