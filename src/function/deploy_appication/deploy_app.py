import time
from telnetlib import EC
import pytest

import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.Locators.locators import Locator

from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.login_fun import test_cluster_login

ss_path = "/Applications/PHP/"


# class TestDeploy(EnvironmentSetup):

def test_deploy(self):
    # pytest.skip("Skipping test...later I will implement...")
    driver = self.driver
    action = ActionChains(driver)
    print("******************************* Test Try to deploy application******************************")
    # click on deploy
    try:
        To_deploy = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, Locator.To_deploy)))
        print("deploy element is visible")
        # To_deploy.click()
        To_deploy.click()
        time.sleep(2)
        print("successfully clicked on deploy")
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)
    except ElementClickInterceptedException as e:
        print("ElementClickInterceptedException", e)

    # click on deploy button
    try:
        Deploy_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locator.Deploy_button)))
        print("deploy button is hided")
        Deploy_button.click()
        time.sleep(2)
    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    # click on okay button
    try:
        Okay_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locator.Okay_button)))
        print("deploy button is hided")
        Okay_button.click()
        time.sleep(4)
    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    # check message
    try:
        Deployment_Pending_msg = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_msg)))
        if Deployment_Pending_msg.is_displayed():
            print('Shown a message: ',
                  simple_colors.green(Deployment_Pending_msg.text, ['bold', 'underlined']))
            pass
        else:
            pass
        time.sleep(4)
    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    try:
        deployment_failed = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locator.deployment_failed)))
        if deployment_failed.is_displayed():
            print('Shown a message: ',
                  simple_colors.green(deployment_failed.text, ['bold', 'underlined']))
            pass
        else:
            pass

    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    try:
        Deployment_Pending_time_msg = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_time_msg)))
        if Deployment_Pending_time_msg.is_displayed():
            print('Shown a message: ',
                  simple_colors.green(Deployment_Pending_time_msg.text, ['bold', 'underlined']))
            time.sleep(4)
            pass
        else:
            pass

    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    try:
        Application_Deployed = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Locator.Application_Deployed)))
        if Application_Deployed.is_displayed():
            print('Shown a message: ',
                  simple_colors.green(Application_Deployed.text, ['bold', 'underlined']))
            pass
        else:
            # WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH, Locator.deployed_validation)))
            # WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, Locator.deployed_validation)))
            time.sleep(2)
            pass

    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    try:
        deployed_validation = WebDriverWait(driver, 800).until(
            EC.presence_of_element_located((By.XPATH, Locator.deployed_validation)))
        if deployed_validation.is_displayed():
            time.sleep(2)
            pass
    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)

    time.sleep(3)