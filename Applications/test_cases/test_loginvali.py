import time
from telnetlib import EC

import pytest
import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from terminal import bold
from webdriver_manager.core import driver
from Src.Locators.locators import Locator

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ss_path = "/Applications/PHP/"


class TestCreatePHP(EnvironmentSetup):
    def test_Laravel_default_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.alpha.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # input email
        try:
            Email_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Locator.Email_box)))
            Email_box.send_keys('admin@klovercloud.com')
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            Password_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.Password_box)))
            Password_box.send_keys('Hello@1234')
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            Toggle_Visibility_Button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.Toggle_Visibility_Button)))
            Toggle_Visibility_Button.click()
            time.sleep(1)

            Toggle_Visibility_Button.click()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            Sign_In_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.Sign_In_button)))
            LogIn_Authentication_Error = WebDriverWait(driver, 80).until(
                EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
            Sign_In_button.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        if WebDriverWait(driver, 80).until(
                EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error))):

            if LogIn_Authentication_Error.is_displayed:
                print('Shown a error message: ',
                      simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
                driver.close()
            else:
                self.driver.implicitly_wait(10)
                time.sleep(20)

        # try:
        #     if WebDriverWait(driver, 80).until(EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
        #         Dashboard_title = driver.title
        #         Accepted_title = "KloverCloud | Dashboard"
        #         self.assertEqual(Dashboard_title, Accepted_title)
        #         print("Welcome to", Dashboard_title)
        #     else:
        #         print("Login Failed")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

        # LogIn_Authentication_Error = WebDriverWait(driver, 80).until(
        #     EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
        # if LogIn_Authentication_Error.is_displayed():
        #     print("\n")
        #     print('Shown a error message: ',
        #           simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
        #     print("\n")
        # if WebDriverWait(driver, 80).until(EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
        #     Dashboard_title = driver.title
        #     Accepted_title = "KloverCloud | Dashboard"
        #     self.assertEqual(Dashboard_title, Accepted_title)

        # try:
        #     if WebDriverWait(driver, 80).until(EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
        #         Dashboard_title = driver.title
        #         Accepted_title = "KloverCloud | Dashboard"
        #         self.assertEqual(Dashboard_title, Accepted_title)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

        # check msg
        # try:
        #     LogIn_Authentication_Error = WebDriverWait(driver, 80).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
        #     if LogIn_Authentication_Error.is_displayed():
        #         print("\n")
        #         print('Shown a error message: ',
        #               simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
        #         print("\n")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

        # try:
        #     Dashboard_title = driver.title
        #     Accepted_title = "KloverCloud | Dashboard"
        #     self.assertEqual(Dashboard_title, Accepted_title)
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

        # try:
        #
        #     LogIn_Authentication_Error = WebDriverWait(driver, 80).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
        #     if LogIn_Authentication_Error.is_displayed():
        #         print("\n")
        #         print('Shown a error message: ',
        #               simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
        #         print("\n")
        #         driver.close()
        #
        #         if WebDriverWait(driver, 80).until(
        #                 EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
        #             print(driver.title)
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

        # # check dashboard page title
        # try:
        #     Dashboard_Page_tile = driver.title
        #     if Dashboard_Page_tile == "kabir":
        #         assert True
        #     else:
        #         assert False
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

        # try:
        #     LogIn_Authentication_Error = WebDriverWait(driver, 80).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
        #     if LogIn_Authentication_Error.is_displayed():
        #         print("\n")
        #         print('Shown a error message: ',
        #               simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
        #         print("\n")
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        #
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # find_username = WebDriverWait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),'Dashboard')]')))
        # assert find_username
        #
        #
        #

        #     else:
        #         print("Password box is not enabled")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        #
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # else:
        #     print('Successfully showed & hided Password')
        #
        # # Click On SignIn button
        # try:
        #     if log.Sign_In_button.is_enabled():
        #         print("Sign In button is clickable")
        #         log.Sign_In_button.click()
        #     elif log.LogIn_Authentication_Error.is_displayed():
        #         print("\n")
        #         print('Shown a error message: ', simple_colors.red(log.LogIn_Authentication_Error().text, ['bold', 'underlined']))
        #         print("\n")
        #         # print(message.text)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        #
        #
        #
        #
