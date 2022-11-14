import time
from telnetlib import EC
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.Locators.locators import Locator

from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.test_login import test_cluster_login

ss_path = "/Applications/PHP/"


class TestDeploy(EnvironmentSetup):
    def test_deploy(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        # ApplicationName = input("Enter Application Name: ")
        ApplicationName = 'j-23'
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
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'j-23')]")))
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
            # print("successfully clicked on deploy")
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except ElementClickInterceptedException as e:
            print("ElementClickInterceptedException", e)

        # # click on deploy button
        try:
            Deploy_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, Locator.Deploy_button)))
            print("deploy button is hided")
            time.sleep(2)
            action = ActionChains(driver)
            # click the item
            action.click()
            # perform the operation
            action.perform()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        #
        # # click on okay button to start deploy
        # try:
        #     Okay_button = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, Locator.Okay_button)))
        #     print("Okay_button is clickable")
        #     Okay_button.click()
        #     print("successfully clicked on Okay")
        #     time.sleep(2)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        # try:
        #     Deployment_Pending_msg = WebDriverWait(driver, 7).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_msg)))
        #     if Deployment_Pending_msg.is_displayed():
        #         print('Shown a message: ',
        #               simple_colors.green(Deployment_Pending_msg.text, ['bold', 'underlined']))
        #         print("\n")
        #         # time.sleep(2)
        #         pass
        #     else:
        #         pass
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # error msg
        # # try:
        # #     deployment_failed = WebDriverWait(driver, 20).until(
        # #         EC.presence_of_element_located((By.XPATH, Locator.deployment_failed)))
        # #     if deployment_failed.is_displayed():
        # #         print('Shown a message: ',
        # #               simple_colors.green(deployment_failed.text, ['bold', 'underlined']))
        # #         print("\n")
        # #         time.sleep(3)
        # #         return exit()
        # #         # return False
        # #     else:
        # #         pass
        # # except NoSuchElementException as e:
        # #     print("NoSuchElementException error", e)
        # # except TimeoutException as e:
        # #     print("TimeoutException error", e)
        # # except InvalidSessionIdException as e:
        # #     print("InvalidSessionIdException error", e)
        #
        # # 2nd success msg
        #
        # try:
        #     Deployment_Pending_time_msg = WebDriverWait(driver, 15).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_time_msg)))
        #     if Deployment_Pending_time_msg.is_displayed():
        #         print('Shown a message: ',
        #               simple_colors.green(Deployment_Pending_time_msg.text, ['bold', 'underlined']))
        #         print("\n")
        #         # time.sleep(6)
        #         pass
        #         # print("Application_build_finished_successfully")
        #     else:
        #         pass
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # Application deployed successful msg
        # try:
        #     Application_Deployed = WebDriverWait(driver, 30).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Application_Deployed)))
        #     if Application_Deployed.is_displayed():
        #         print('Shown a message: ',
        #               simple_colors.green(Application_Deployed.text, ['bold', 'underlined']))
        #         print("\n")
        #         pass
        #     else:
        #         pass
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # check deployed or not
        #
        # print("**********Application deployed or not by build button visibility***********")
        # time.sleep(120)
        # # close log
        # try:
        #     Live_Pipeline_Logs = WebDriverWait(driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
        #     Live_Pipeline_Logs.click()
        #     time.sleep(4)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
