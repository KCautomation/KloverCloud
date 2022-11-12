import time
from telnetlib import EC

import pytest
import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    InvalidSelectorException
from Src.Locators.locators import Locator
from Src.function.go_application.go_to_application_page import go_create_app_page

from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.function.logIn.test_login import test_cluster_login

ss_path = "/Applications/PHP/"


class TestDeploy(EnvironmentSetup):

    def test_deploy(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        ApplicationName = "3-3"
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to Create Application list *********************")
        try:
            Applications_list = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Applications)))
            print("Applications button is clickable")
            Applications_list.click()
            print("Welcome applications list")
            time.sleep(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 50")
        print("Scroll down")
        time.sleep(3)

        # find and click on an application
        try:
            Application_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),"+ApplicationName+")]")))
            print(ApplicationName, "Application is present in the list")
            Application_name.click()
            print("successfully clicked on :", ApplicationName)
            time.sleep(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        # click on deploy
        try:
            To_deploy = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.To_deploy)))
            print("deploy button is clickable")
            To_deploy.click()
            print("successfully clicked on deploy")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # click on deploy button
        try:
            Deploy_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Deploy_button)))
            print("deploy button is clickable")
            Deploy_button.click()
            print("successfully clicked on deploy")
            time.sleep(20)
            # msg validation
            Deployment_Pending_msg = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_msg)))
            if Deployment_Pending_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(Deployment_Pending_msg.text, ['bold', 'underlined']))
                print("\n")
                pass
                # 2nd msg
                Deployment_Pending_time_msg = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_time_msg)))
                if Deployment_Pending_time_msg.is_displayed():
                    print('Shown a message: ',
                          simple_colors.green(Deployment_Pending_time_msg.text, ['bold', 'underlined']))
                    print("\n")
                    pass
                    time.sleep(30)
                    print("Application_build_finished_successfully")

                    Application_Deployed = WebDriverWait(driver, 120).until(
                        EC.presence_of_element_located((By.XPATH, Locator.Application_Deployed)))
                    if Application_Deployed.is_displayed():
                        print('Shown a message: ',
                              simple_colors.green(Application_Deployed.text, ['bold', 'underlined']))
                        print("\n")
                        pass
                        time.sleep(30)
                        print("Application deployed successfully")
                else:
                    assert False

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)


