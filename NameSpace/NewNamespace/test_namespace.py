import unittest

import allure
import pytest
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
from src.Locators.locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from urllib.request import urlopen
from urllib.error import *


@allure.severity(allure.severity_level.CRITICAL)
class NamespaceCreationOrganization(unittest.TestCase):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_company(self):
        pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.alpha.klovercloud.io/"
        username = "admin@klovercloud.com"
        password = "Hello@1234"
        Namespace_Name = "test-27"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(pageUrl)
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

        driver.get(pageUrl)
        driver.implicitly_wait(20)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(
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
            Password_box = WebDriverWait(driver, 20).until(
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
            Toggle_Visibility_Button = WebDriverWait(driver, 20).until(
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
            Sign_In_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]")))
            print("Password_box is inputable")
            Sign_In_button.click()
            driver.implicitly_wait(10)
            time.sleep(7)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')

        # check error message have or not
        try:
            LogIn_Authentication_Error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
            if LogIn_Authentication_Error.is_displayed():
                print("\n")
                print('Shown a error message: ',
                      simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
                print("\n")
                driver.close()
                # return FileExistsError
            else:
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Login validation
        try:
            if WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
                Dashboard_title = driver.title
                Accepted_title = "KloverCloud | Dashboard"
                self.assertEqual(Dashboard_title, Accepted_title)
                print("Successfully logged in && Welcome to", Dashboard_title)
            else:
                print("Login Failed")
                allure.attach(driver.get_screenshot_as_png(), name="test_login", attachment_type=AttachmentType.PNG)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        """ Create Namespace """

        # # Click On Namespace From Side Navigation
        # driver.find_element(By.XPATH, "//span[contains(text(),'Namespace')]").click()
        # driver.implicitly_wait(10)
        # time.sleep(6)
        #
        # # click on create button from header
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]").click()
        # driver.implicitly_wait(10)
        # time.sleep(4)
        #
        # # click namespace
        # driver.find_element(By.CSS_SELECTOR, "button[role='menuitem']").click()
        # driver.implicitly_wait(10)
        # time.sleep(4)
        #
        # # input Namespace name
        # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Namespace Name']").send_keys(Namespace_Name)
        # time.sleep(3)
        #
        # # click create button for create
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "2]/div[1]/div[2]/button[1]").click()
        # time.sleep(20)
        # try:
        #     actual = driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     if self.assertEqual(actual, accepted):
        #         print("Created Successfully")
        #     else:
        #         print("Created failed")
        # except AssertionError as e:
        #     print(e)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_organization(self):
        pageUrl = "https://eks.alpha.klovercloud.io/"
        username = "admin@klovercloud.com"
        password = "Hello@1234"
        Namespace_Name = "test-26"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(2)

        """ Login """

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

        driver.get(pageUrl)
        driver.implicitly_wait(20)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(
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
            Password_box = WebDriverWait(driver, 20).until(
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
            Toggle_Visibility_Button = WebDriverWait(driver, 20).until(
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
            Sign_In_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]")))
            print("Password_box is inputable")
            Sign_In_button.click()
            driver.implicitly_wait(10)
            time.sleep(7)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')

        # check error message have or not
        try:
            LogIn_Authentication_Error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
            if LogIn_Authentication_Error.is_displayed():
                print("\n")
                print('Shown a error message: ',
                      simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
                print("\n")
                driver.close()
                # return FileExistsError
            else:
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Login validation
        try:
            if WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
                Dashboard_title = driver.title
                Accepted_title = "KloverCloud | Dashboard"
                self.assertEqual(Dashboard_title, Accepted_title)
                print("Successfully logged in && Welcome to", Dashboard_title)
            else:
                print("Login Failed")
                allure.attach(driver.get_screenshot_as_png(), name="test_login", attachment_type=AttachmentType.PNG)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        """ Create Namespace """

        # # Click On Namespace From Side Navigation
        # driver.find_element(By.XPATH, "//span[contains(text(),'Namespace')]").click()
        # driver.implicitly_wait(10)
        # time.sleep(6)
        #
        # # clcik on create button from header
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]").click()
        # driver.implicitly_wait(10)
        # time.sleep(4)
        #
        # # click namespace
        # driver.find_element(By.CSS_SELECTOR, "button[role='menuitem']").click()
        # driver.implicitly_wait(10)
        # time.sleep(4)
        #
        # """
        # # Choose cluster
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/img[1]").click()
        # time.sleep(1)
        #
        # """
        # # input Namespace name
        # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Namespace Name']").send_keys(Namespace_Name)
        # time.sleep(3)
        #
        # # driver.execute_script(window.scrollBy(0, 500))
        #
        # # Scroll
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        # print("Scroll down")
        # time.sleep(4)
        #
        # # Choose access organization from Access Group
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[3]/div[1]/button[2]/span[1]/div[1]").click()
        # time.sleep(2)
        #
        # # click search box and choose organization
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]").click()
        # time.sleep(2)
        #
        # # Organization selection
        # # driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/div[1]/mat-option[2]/div[1]").click()
        # driver.find_element(By.XPATH, "//span[contains(text(),'default')]").click()
        # time.sleep(4)
        #
        # # CPU selection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Memory Selection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Persistent Volume seloection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Bandwidth selection
        # driver.find_element(By.XPATH, "//div[contains(text(),'Moderate')]").click()
        # time.sleep(2)
        #
        # # Scroll
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -550")
        # print("Scroll up")
        # time.sleep(4)
        #
        # # click create button for create
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "2]/div[1]/div[2]/button[1]").click()
        # driver.implicitly_wait(10)
        # print("Create Successfully")
        # time.sleep(5)
        #
        # time.sleep(20)
        # try:
        #     actual = driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     if self.assertEqual(actual, accepted):
        #         print("Created Successfully")
        #     else:
        #         print("Created failed")
        # except AssertionError as e:
        #     print(e)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_team(self):
        pageUrl = "https://eks.alpha.klovercloud.io/"
        username = "admin@klovercloud.com"
        password = "Hello@1234"
        Namespace_Name = "test-26"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(2)

        """ Login """

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

        driver.get(pageUrl)
        driver.implicitly_wait(20)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(
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
            Password_box = WebDriverWait(driver, 20).until(
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
            Toggle_Visibility_Button = WebDriverWait(driver, 20).until(
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
            Sign_In_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]")))
            print("Password_box is inputable")
            Sign_In_button.click()
            driver.implicitly_wait(10)
            time.sleep(7)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')

        # check error message have or not
        try:
            LogIn_Authentication_Error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
            if LogIn_Authentication_Error.is_displayed():
                print("\n")
                print('Shown a error message: ',
                      simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
                print("\n")
                driver.close()
                # return FileExistsError
            else:
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Login validation
        try:
            if WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
                Dashboard_title = driver.title
                Accepted_title = "KloverCloud | Dashboard"
                self.assertEqual(Dashboard_title, Accepted_title)
                print("Successfully logged in && Welcome to", Dashboard_title)
            else:
                allure.attach(driver.get_screenshot_as_png(), name="test_login", attachment_type=AttachmentType.PNG)
                print("Login Failed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        """ Create Namespace """
        #
        # # Click On Namespace From Side Navigation
        # driver.find_element(By.XPATH, "//span[contains(text(),'Namespace')]").click()
        # driver.implicitly_wait(10)
        # time.sleep(6)
        #
        # # click on create button from header
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]").click()
        # driver.implicitly_wait(10)
        # time.sleep(4)
        #
        # # click namespace
        # driver.find_element(By.CSS_SELECTOR, "button[role='menuitem']").click()
        # driver.implicitly_wait(10)
        # time.sleep(4)
        #
        # """
        # # Choose cluster
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/img[1]").click()
        # time.sleep(1)
        #
        # """
        # # input Namespace name
        # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Namespace Name']").send_keys(Namespace_Name)
        # time.sleep(3)
        #
        # # Choose Team from Access Group
        # driver.find_element(By.XPATH,
        #                     "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]/span[1]/div[1]").click()
        # time.sleep(2)
        #
        # # click on search button
        # driver.find_element(By.XPATH,
        #                     "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]").click()
        # time.sleep(2)
        #
        # # choose a team
        # driver.find_element(By.XPATH, "//span[contains(text(),'default')]").click()
        # time.sleep(2)
        #
        # # CPU selection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Memory Selection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Persistent Volume seloection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Bandwidth selection
        # driver.find_element(By.XPATH, "//div[contains(text(),'Moderate')]").click()
        # time.sleep(2)
        #
        # # scroll
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -550")
        # print("Scroll down")
        # time.sleep(4)
        # print("Scroll success")
        #
        # # click create button for create
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "2]/div[1]/div[2]/button[1]").click()
        # driver.implicitly_wait(10)
        # time.sleep(5)
        #
        # time.sleep(20)
        # try:
        #     actual = driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     if self.assertEqual(actual, accepted):
        #         print("Created Successfully")
        #     else:
        #         print("Created failed")
        # except AssertionError as e:
        #     print(e)
