import time
from telnetlib import EC

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


class TestDeploy(EnvironmentSetup):

    def test_deploy(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        action = ActionChains(driver)
        # ApplicationName = input("Enter Application Name: ")
        ApplicationName = 'test-j-002'
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to Application list *********************")
        try:
            Applications_list = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Applications)))
            print("Applications button is clickable")
            Applications_list.click()
            self.driver.implicitly_wait(30)
            print("Welcome to applications list")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
        print("Scroll down")
        time.sleep(3)

        # click on an application
        try:
            Application_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'test-j-002')]")))
            if Application_name.is_displayed:
                print(ApplicationName, "Application is present in the list")
                Application_name.click()
                self.driver.implicitly_wait(25)
                print("successfully clicked on :", ApplicationName)
                time.sleep(7)
            else:
                return exit()

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("******************************* Test Try to deploy application******************************")
        # click on deploy
        try:
            To_deploy = WebDriverWait(driver, 30).until(
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
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("---------------Deployed Validation--------------------")
        try:
            # time.sleep(60)
            driver.refresh()
            time.sleep(2)

            to_check_deploy = WebDriverWait(driver, 5).until(
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
            Deployed_status = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Deployed_status)))

            Accepted_status = "Success"
            Actual_status = Deployed_status.text
            self.assertEqual(Actual_status, Accepted_status)

            print('Deployed status is: ',
                  simple_colors.green(Actual_status, ['bold', 'underlined']))
            time.sleep(2)
            pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        except AssertionError as e:
            print("InvalidSessionIdException error", e)

