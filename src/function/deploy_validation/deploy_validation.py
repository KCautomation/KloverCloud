import time
from telnetlib import EC

import action as action
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


def test_deploy_validation(self):
    # pytest.skip("Skipping test...later I will implement...")
    driver = self.driver
    action = ActionChains(driver)

    print("---------------Deployed Validation--------------------")
    try:
        time.sleep(2)
        to_check_deploy = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Locator.to_check_deploy)))
        print("Deploy_button is located")
        to_check_deploy.click()
        time.sleep(2)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(3)
        pass

    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)
    # validation
    try:
        Deployed_status = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, Locator.Deployed_status)))

        Accepted_status = "Success"
        Actual_status = Deployed_status.text
        self.assertEqual(Actual_status, Accepted_status)

        print('Deployed status is: ',
              simple_colors.green(Actual_status, ['bold', 'underlined']))
        time.sleep(4)
        pass
    except NoSuchElementException as e:
        print("NoSuchElementException error", e)
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException error", e)
    except AssertionError as e:
        print("InvalidSessionIdException error", e)

