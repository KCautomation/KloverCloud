import pytest
import time
from telnetlib import EC
import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from src.Locators.locators import Locator
from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.function.logIn.login_fun import test_cluster_login
ss_path = "/Applications/JavaScript/"


class TestCreateJavascript(EnvironmentSetup):

    def test_eJs_default_01(self):
        pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
        ApplicationName = "ejs-03"

        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print(" *********************** Create Express JS Application Based On Team: none *********************")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                CreateNew_H.click()
                print("CreateNew_H button is clickable")
                time.sleep(2)
            else:
                print("CreateNew_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew_H')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                NewApplication_H.click()
                self.driver.implicitly_wait(10)
                time.sleep(5)
                print("NewApplication_H button is clickable")
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')

        print("----------------------Create DotNet app with version 3.1-----------------------------------")

        # click on ExpressJS
        try:
            ExpressJS = self.driver.find_element(By.XPATH, Locator.ExpressJS)
            if ExpressJS.is_enabled():
                ExpressJS.click()
                print("ExpressJS button is enable")
                driver.implicitly_wait(10)
                time.sleep(3)
            else:
                print("ExpressJS button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose ExpressJS')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys(ApplicationName)
                print("ApplicationName_box is enable")
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        print("Scroll down")
        time.sleep(2)

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                print("Next button is enable")
                time.sleep(2)
            else:
                print("Next button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button')

        # Again click next button
        try:
            Next_button_two = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button_two.is_enabled():
                Next_button_two.click()
                print("Next button is enable")
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        print("Scroll down to show Namespaces")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                Choose_Namespace_one.click()
                print("Namespace is selected")
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        print("Scroll down to show Namespaces")
        time.sleep(2)

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                Save_button.click()
                print("Save button is enable")
                time.sleep(2)
            else:
                print("Save button is not enable")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        try:
            Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
            if Create_Application.is_enabled():
                Create_Application.click()
                time.sleep(180)
                print("Create application button is enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "JavaScript_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

        print("******************************* Test Try to deploy application******************************")
        # click on deploy
        try:
            To_deploy = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Locator.To_deploy)))
            print("deploy element is visible")
            # To_deploy.click()
            To_deploy.click()
            time.sleep(2)
            # To_deploy.sendKeys(Keys.ENTER)
            action = ActionChains(driver)
            # click the item
            action.send_keys(Keys.ENTER)
            # perform the operation
            action.perform()

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

        # click on deploy button
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

        print("******************************* Test Try to delete application******************************")
        try:
            application_Settings = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.application_Settings)))
            print("application_Settings is clickable")
            application_Settings.click()
            print("Welcome application_Settings ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # click on Delete button
        try:
            application_Delete = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.application_Delete)))
            print("application_Delete is clickable")
            application_Delete.click()
            print("successfully clicked application_Delete ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # input application name
        try:
            Application_namebox_D = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Application_namebox_D)))
            print("application_Delete is clickable")
            Application_namebox_D.send_keys(ApplicationName)
            print("successfully inputted Application_name ")
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

        # input application name
        try:
            Delete_permanently_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Delete_permanently_button)))
            print("application_Delete is clickable")
            Delete_permanently_button.click()
            print("successfully clicked on Delete_permanently_button ")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # check msg
        try:
            Application_Deleted_Success_msg = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, Locator.Application_Deleted_Success_msg)))
            if Application_Deleted_Success_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(Application_Deleted_Success_msg.text, ['bold', 'underlined']))
                print("\n")
                pass
            else:
                assert False
            time.sleep(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_eJs_default_02(self):
        pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
        ApplicationName = "ejs-04"

        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("********************* Create Express JS Application Based On Team : none********************")

        print("--------------------Go to Create Application  Page----------------------")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                CreateNew_H.click()
                print("CreateNew_H button is clickable")
                time.sleep(2)
            else:
                print("CreateNew_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew_H')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                NewApplication_H.click()
                self.driver.implicitly_wait(10)
                time.sleep(5)
                print("NewApplication_H button is clickable")
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')

        print("--------------------Create Express Js  Application with Version: 4.17.0----------------------")

        # click on ExpressJS
        try:
            ExpressJS = self.driver.find_element(By.XPATH, Locator.ExpressJS)
            if ExpressJS.is_enabled():
                ExpressJS.click()
                print("ExpressJS button is enable")
                driver.implicitly_wait(10)
                time.sleep(3)
            else:
                print("ExpressJS button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose ExpressJS')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys(ApplicationName)
                print("ApplicationName_box is enable")
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # click on Express Js Version box to show all versions
        try:
            Express_Js_Version_box = driver.find_element(By.XPATH, Locator.Express_Js_Version_box)
            if Express_Js_Version_box.is_enabled():
                Express_Js_Version_box.click()
                time.sleep(1)
                print("Express Js Version box is enable")
            else:
                print("Express Js Version box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Express Js Version box & shown all versions')

        # Choose Express version 4.17.1 version 3.0
        try:
            JS_V_4_17_1 = driver.find_element(By.XPATH, Locator.JS_V_4_17_1)
            if JS_V_4_17_1.is_displayed():
                JS_V_4_17_1.click()
                time.sleep(1)
                print("JS_V_4_17_1 is enable")
            else:
                print("JS Version 4.17.1 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose JS Version 4.17.1')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        print("Scroll down")
        time.sleep(2)

        # Click on team box
        try:
            TeamBox_A = self.driver.find_element(By.XPATH, Locator.TeamBox_A)
            if TeamBox_A.is_enabled():
                print("Team box is Enable")
                TeamBox_A.click()
                time.sleep(1)
            else:
                print("Team box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        # Choose Default from team
        try:
            Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
            if Team_Default.is_displayed():
                print("Team default is selectable")
                Team_Default.click()
                time.sleep(2)
            else:
                print("Team box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Team Default')

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                print("Next button is enable")
                time.sleep(2)
            else:
                print("Next button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button')

        # Again click next button
        try:
            Next_button_two = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button_two.is_enabled():
                Next_button_two.click()
                print("Next button is enable")
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        print("Scroll down to show Namespaces")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                Choose_Namespace_one.click()
                print("Namespace is selected")
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        print("Scroll down to show Namespaces")
        time.sleep(2)

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                Save_button.click()
                print("Save button is enable")
                time.sleep(2)
            else:
                print("Save button is not enable")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        try:
            Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
            if Create_Application.is_enabled():
                Create_Application.click()
                time.sleep(180)
                print("Create application button is enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "JavaScript_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

        print("******************************* Test Try to deploy application******************************")
        # click on deploy
        try:
            To_deploy = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Locator.To_deploy)))
            print("deploy element is visible")
            # To_deploy.click()
            To_deploy.click()
            time.sleep(2)
            # To_deploy.sendKeys(Keys.ENTER)
            action = ActionChains(driver)
            # click the item
            action.send_keys(Keys.ENTER)
            # perform the operation
            action.perform()

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

        # click on deploy button
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

        print("******************************* Test Try to delete application******************************")
        try:
            application_Settings = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.application_Settings)))
            print("application_Settings is clickable")
            application_Settings.click()
            print("Welcome application_Settings ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # click on Delete button
        try:
            application_Delete = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.application_Delete)))
            print("application_Delete is clickable")
            application_Delete.click()
            print("successfully clicked application_Delete ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # input application name
        try:
            Application_namebox_D = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Application_namebox_D)))
            print("application_Delete is clickable")
            Application_namebox_D.send_keys(ApplicationName)
            print("successfully inputted Application_name ")
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

        # input application name
        try:
            Delete_permanently_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Delete_permanently_button)))
            print("application_Delete is clickable")
            Delete_permanently_button.click()
            print("successfully clicked on Delete_permanently_button ")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # check msg
        try:
            Application_Deleted_Success_msg = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, Locator.Application_Deleted_Success_msg)))
            if Application_Deleted_Success_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(Application_Deleted_Success_msg.text, ['bold', 'underlined']))
                print("\n")
                pass
            else:
                assert False
            time.sleep(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)