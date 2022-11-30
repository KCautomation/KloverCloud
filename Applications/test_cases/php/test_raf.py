import time
from telnetlib import EC

import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys

from src.Locators.locators import Locator
from src.function.deploy_validation.deploy_validation import test_deploy_validation
from src.function.go_application.go_to_application_page import go_create_app_page

from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.function.logIn.login_fun import test_cluster_login
from src.function.deploy_appication.deploy_app import test_deploy
from src.function.delete_app.delete_application import test_delete_app

ss_path = "/Applications/PHP/"


class TestCreateAppPHP(EnvironmentSetup):

    def test_Laravel_default_02(self):
        # pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
        ss = SS(driver)
        ApplicationName = "laravel-0167"
        print("****************** Try to Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to Create Application Page *********************")
        try:
            driver.refresh()
            time.sleep(3)
            go_create_app_page(self)

            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, Locator.Laravel)))
            driver.refresh()
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("***************Create PHP application with PHP Version: 7.3 &  Laravel version : 6.0***************")

        print("----try to choose Laravel from below--------")
        try:
            Laravel = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, Locator.Laravel)))
            # driver.refresh()
            Laravel.click()
            driver.implicitly_wait(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("----Try to put application name--------")
        try:
            ApplicationName_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
            print("ApplicationName_box is visible")
            ApplicationName_box.send_keys(ApplicationName)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        # click on laravel version box
        print("-----------Try to click Laravel version box----------------")
        try:
            Laravel_version_box = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_box)))
            print("Laravel_version_box button is clickable")
            Laravel_version_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on Laravel_version_box')

        # choose laravel version
        print("-----------Try to choose Laravel version 6.0----------------")

        try:
            Laravel_version_6_0 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_6_0)))
            print("Laravel_version 6.0 button is clickable")
            Laravel_version_6_0.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully chose on Laravel version 5.8')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        print("Scroll down")
        time.sleep(2)

        # Click on team box
        print("----try to click Team box--------")
        try:
            TeamBox_A = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.TeamBox_A)))
            print("TeamBox_A button is clickable")
            TeamBox_A.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        print("----try to choose Team as Default--------")
        try:
            Team_Default = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Team_Default)))
            print("Team_Default button is clickable")
            Team_Default.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        print("----try to click 'Next' button-------")
        try:
            Next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
            print("Next_button button is clickable")
            Next_button.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully click on Next_button')

        print("----try to again click 'Next' button-------")
        try:
            Next_button_two = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
            print("Next_button_two button is clickable")
            Next_button_two.click()
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        # again scroll below to show Namespaces
        print("Try Scroll down to show Namespaces")
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        print("----try to Choose A Namespace for Prod Environment--------")
        try:
            Choose_Namespace_one = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Choose_Namespace_one)))
            print("Choose_Namespace_one button is clickable")
            Choose_Namespace_one.click()
            time.sleep(5)

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully Choose Namespace one')

        print("-----Scroll down to show Namespaces-----")
        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1500")
        time.sleep(2)

        # click on save button
        print("----try to click save button--------")
        try:
            Save_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Save_button_A)))
            print("Save_button button is clickable")
            Save_button.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        except TimeoutException as e:
            print("TimeoutException error", e)

        # click on Create application button
        print("----try to click 'Create application' button--------")
        try:
            Create_Application = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Create_Application)))
            print("Create_Application button is clickable")
            Create_Application.click()
            time.sleep(4)
            # check success message
            New_Git_Commit_Pushed_msg = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Locator.New_Git_Commit_Pushed_msg)))
            if New_Git_Commit_Pushed_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(New_Git_Commit_Pushed_msg.text, ['bold', 'underlined']))
                print("\n")
                time.sleep(6)
                Application_build_finished_successfully_msg = WebDriverWait(driver, 80).until(
                    EC.presence_of_element_located((By.XPATH, Locator.Application_build_finished_successfully_msg)))
                if Application_build_finished_successfully_msg.is_displayed():
                    print('Shown a message: ',
                          simple_colors.green(Application_build_finished_successfully_msg.text, ['bold', 'underlined']))
                    print("\n")
                    print("Application_build_finished_successfully")
                    time.sleep(10)
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # time.sleep(80)
        # wait for confirmation
        try:
            wait_ToCreateApplication = WebDriverWait(driver, 800).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_ToCreateApplication)))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(4)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # application created validation
        print("---------------Try to Crated Application Validation--------------------")
        try:
            driver.refresh()
            time.sleep(3)
            check_create_app = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.XPATH, Locator.check_create_app)))
            check_create_app.click()
            time.sleep(2)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # validation
        try:
            Created_status = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.check_app_status)))

            Accepted_status = "Success"
            Actual_status = Created_status.text
            self.assertEqual(Actual_status, Accepted_status)

            print('Application created status is: ',
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
            print("AssertionError", e)

        # deploy application
        print("*******************************Try to Test deploy application******************************")
        try:
            driver.refresh()
            time.sleep(3)
            test_deploy(self)
            time.sleep(3)

            # message check
            driver.refresh()
            time.sleep(3)
            test_deploy_validation(self)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("*******************************Try Test to delete application******************************")
        try:
            driver.refresh()
            time.sleep(3)
            test_delete_app(self, ApplicationName)
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("---------------------- deleted Application validation-----------------------")

        print("Application Delete Successfully")

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
