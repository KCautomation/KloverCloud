import unittest

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
from utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.CRITICAL)
class TestNamespaceCreation(unittest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_company(self):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test-30"

        time.sleep(2)
        # try block to read URL
        try:
            html = urlopen(self.baseURL)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print(Fore.LIGHTRED_EX + "HTTP error", e)

        except URLError as e:
            print(Fore.LIGHTRED_EX + "Opps ! Page not found!", e)

        else:
            print(Fore.YELLOW + 'Yeah ! URL found ')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(self.baseURL)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='mat-input-0']")))
            print("Email_box is inputable")
            Email_box.send_keys(self.username)
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
            Password_box.send_keys(self.password)
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
                EC.presence_of_element_located((By.XPATH, "//body[1]/kc-toastr[1]/div[1]/div[1]")))
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
                    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Dashboard')]"))):
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

        print("**********************************Create Namespace With Company******************************")

        # click on create button from header
        print("Try to click on CreateNew button from Header")
        try:
            CreateNew_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]")))
            CreateNew_button.click()
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click namespace
        print("Try to click on Namespace button from frame")
        try:
            Namespace_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[role='menuitem']")))
            Namespace_button.click()
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # input Namespace name
        print("Try to input Namespace Name")
        try:
            NamespaceName_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Namespace Name']")))
            NamespaceName_box.send_keys(Namespace_Name)
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click create button for create
        print("Try to click on Create Button")
        try:
            Create_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")))
            Create_button.click()
            time.sleep(5)
            WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-vpc-list/div/div[2]/div[2]/button[1]/span/div")))
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("******************Create Namespace Validation**********************")
        try:
            actual = driver.current_url
            accepted = "https://eks.alpha.klovercloud.io/namespace"
            if self.assertEqual(actual, accepted):
                print("Created Successfully")
            else:
                print("Created failed")
                assert False
        except AssertionError as e:
            print(e)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_organization(self):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test-30"

        time.sleep(2)
        # try block to read URL
        try:
            html = urlopen(self.baseURL)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print(Fore.LIGHTRED_EX + "HTTP error", e)

        except URLError as e:
            print(Fore.LIGHTRED_EX + "Opps ! Page not found!", e)

        else:
            print(Fore.YELLOW + 'Yeah ! URL found ')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(self.baseURL)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='mat-input-0']")))
            print("Email_box is inputable")
            Email_box.send_keys(self.username)
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
            Password_box.send_keys(self.password)
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
                EC.presence_of_element_located((By.XPATH, "//body[1]/kc-toastr[1]/div[1]/div[1]")))
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
                    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Dashboard')]"))):
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

        print("**********************************Create Namespace With Company******************************")

        # click on create button from header
        print("Try to click on CreateNew button from Header")
        try:
            CreateNew_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]")))
            CreateNew_button.click()
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click namespace
        print("Try to click on Namespace button from frame")
        try:
            Namespace_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[role='menuitem']")))
            Namespace_button.click()
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # input Namespace name
        print("Try to input Namespace Name")
        try:
            NamespaceName_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Namespace Name']")))
            NamespaceName_box.send_keys(Namespace_Name)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("Scroll down")
        time.sleep(2)

        # Choose access organization from Access Group
        print("Try to Choose Organization as access group")
        try:
            Organization = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]/span[1]/div[1]")))
            Organization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click search box and choose organization
        print("Try to click search box")
        try:
            Organization = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]")))
            Organization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Organization selection
        print("Try to choose Organization")
        try:
            Choose_Organization = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'default')]")))
            Choose_Organization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 730")
        print("Scroll down")
        time.sleep(2)

        # CPU selection
        print("Try to update CPU by input CPU box")
        try:
            CPU_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")))
            CPU_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Memory Selection
        print("Try to update CPU by input Memory box")
        try:
            Memory_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")))
            Memory_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Persistent Volume selection
        print("Try to update Volume by input box")
        try:
            Volume_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]")))
            Volume_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Bandwidth selection
        print("Try to update Bandwidth by input box")
        try:
            Bandwidth_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Moderate')]")))
            Bandwidth_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -730")
        print("Scroll up")
        time.sleep(2)

        # click create button for create
        print("Try to click on Create Button")
        try:
            Create_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")))
            Create_button.click()
            time.sleep(5)
            WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-vpc-list/div/div[2]/div[2]/button[1]/span/div")))
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("******************Create Namespace Validation**********************")
        try:
            actual = driver.current_url
            accepted = "https://eks.alpha.klovercloud.io/namespace"
            if self.assertEqual(actual, accepted):
                print("Created Successfully")
            else:
                print("Created failed")
                assert False
        except AssertionError as e:
            print(e)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_team(self):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test-30"

        # try block to read URL
        try:
            html = urlopen(self.baseURL)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print(Fore.LIGHTRED_EX + "HTTP error", e)

        except URLError as e:
            print(Fore.LIGHTRED_EX + "Opps ! Page not found!", e)

        else:
            print(Fore.YELLOW + 'Yeah ! URL found ')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(self.baseURL)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='mat-input-0']")))
            print("Email_box is inputable")
            Email_box.send_keys(self.username)
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
            Password_box.send_keys(self.password)
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
                EC.presence_of_element_located((By.XPATH, "//body[1]/kc-toastr[1]/div[1]/div[1]")))
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
                    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Dashboard')]"))):
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

        print("**********************************Create Namespace With Team******************************")

        # click on create button from header
        print("Try to click on CreateNew button from Header")
        try:
            CreateNew_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]")))
            CreateNew_button.click()
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click namespace
        print("Try to click on Namespace button from frame")
        try:
            Namespace_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[role='menuitem']")))
            Namespace_button.click()
            driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # input Namespace name
        print("Try to input Namespace Name")
        try:
            NamespaceName_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Namespace Name']")))
            NamespaceName_box.send_keys(Namespace_Name)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("Scroll down")
        time.sleep(2)

        # Choose Team from Access Group
        print("Try to Choose Team as access group")
        try:
            Team = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]/span[1]/div[1]")))
            Team.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click search box and choose organization
        print("Try to click search box")
        try:
            Search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]")))
            Search_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Organization selection
        print("Try to choose a team from dropdown")
        try:
            Choose_Team = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'default')]")))
            Choose_Team.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 730")
        print("Scroll down")
        time.sleep(2)

        # CPU selection
        print("Try to update CPU by input CPU box")
        try:
            CPU_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")))
            CPU_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Memory Selection
        print("Try to update CPU by input Memory box")
        try:
            Memory_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")))
            Memory_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Persistent Volume selection
        print("Try to update Volume by input box")
        try:
            Volume_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]")))
            Volume_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Bandwidth selection
        print("Try to update Bandwidth by input box")
        try:
            Bandwidth_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Moderate')]")))
            Bandwidth_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -730")
        print("Scroll up")
        time.sleep(2)

        # click create button for create
        print("Try to click on Create Button")
        try:
            Create_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]")))
            Create_button.click()
            time.sleep(5)
            WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-vpc-list/div/div[2]/div[2]/button[1]/span/div")))
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("******************Create Namespace Validation**********************")
        try:
            actual = driver.current_url
            accepted = "https://eks.alpha.klovercloud.io/namespace"
            if self.assertEqual(actual, accepted):
                print("Created Successfully")
            else:
                print("Created failed")
                assert False
        except AssertionError as e:
            print(e)
