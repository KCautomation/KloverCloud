import time
import pytest
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Locators.locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException


def go_create_app_page(self):
    driver = self.driver
    print(Fore.CYAN + "-----------------------From Header frame----------------------------------------")
    # click on create button from header
    try:
        CreateNew_H = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.CreateNew_H)))
        print("CreateNew_H button is clickable")
        CreateNew_H.click()
        time.sleep(2)
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)
    else:
        print('Successfully clicked on CreateNew')

    # click on "New Application" button from dropdown
    try:
        NewApplication_H = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locator.NewApplication_H)))
        print("NewApplication_H button is clickable")
        NewApplication_H.click()
        time.sleep(5)
        driver.implicitly_wait(20)
    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    else:
        print('Successfully clicked on NewApplication_H')
    print(Fore.CYAN + "-----------------------Welcome Create Application Page----------------------------------------")