import allure
import self
import simple_colors
from allure_commons.types import AttachmentType
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from urllib.request import urlopen
from urllib.error import *


def test_company(self):
    # pytest.skip("Skipping test...later I will implement...")
    pageUrl = "https://eks.alpha.klovercloud.io/"
    username = "admin@klovercloud.com"
    password = "Hello@1234"
    Namespace_Name = "test-30"
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
    print("InvalidSessionIdException error", e)

    item = "//span[contains(text(),'test-com-2')]"
    while True:
        if driver.find_element():
            driver.find_element(By.XPATH, item).click()
            break
        else:
            # driver.find_element(By.XPATH, "xpath to goto next page").click()
            print("Namespace Not Found")
            break
