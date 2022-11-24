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

ss_path = "/Applications/GoLang/"


class TestCreateGolangAppNone(EnvironmentSetup):

    def test_golang_none_01(self):
        pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
        ApplicationName = "golang-01"

        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print(" ************************ Create GoLang Application based on Team: None ************************")

        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                CreateNew_H.click()
                self.driver.implicitly_wait(5)
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

        print("\n----------------Create golang application with team: None go echo version 4.1.15------------------\n")

        # Choose GoLang
        try:
            GoLang = self.driver.find_element(By.XPATH, Locator.GoLang)
            if GoLang.is_enabled():
                GoLang.click()
                self.driver.implicitly_wait(10)
                time.sleep(5)
                print("GoLang button is clickable")
                time.sleep(2)
            else:
                print("GoLang button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on GoLang')

        # Put Application Name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys(ApplicationName)
                self.driver.implicitly_wait(10)
                time.sleep(2)
                print("ApplicationName_box is enable")
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted application name')

        # Click On Team box
        # try:
        #     TeamBox_A = driver.find_element(By.XPATH, Locator.TeamBox_A)
        #     if TeamBox_A.is_enabled():
        #         TeamBox_A.click()
        #         time.sleep(1)
        #         print("TeamBox_A is enable")
        #     else:
        #         print("TeamBox_A is not enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on TeamBox')
        #
        # # Choose Default from team
        # try:
        #     Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
        #     if Team_Default.is_displayed():
        #         Team_Default.click()
        #         time.sleep(2)
        #         print("Team_Default is displayed")
        #     else:
        #         print("Team_Default is not displayed")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully chose on Team_Default')

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                self.driver.implicitly_wait(10)
                print("Next_button is enable")
                time.sleep(2)
            else:
                print("Next_button is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Next_button')

        #  again click next button
        try:
            Next_button_two = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button_two.is_enabled():
                Next_button_two.click()
                self.driver.implicitly_wait(10)
                print("Next_button is enable")
                time.sleep(2)
            else:
                print("Next_button is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Next_button')

        # scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        print("Scroll down to show Namespaces")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                Choose_Namespace_one.click()
                print("Choose_Namespace_one is selected")
                time.sleep(5)
            else:
                print("Choose_Namespace_one is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Choose_Namespace_one')

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
            print('Successfully clicked on Save_button')

        # take action's screenshot
        ss = SS(driver)
        file_name = ss_path + "GoLang_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

        # click on Create application button
        try:
            Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
            if Create_Application.is_enabled():
                Create_Application.click()
                print("Create application button is enable")
                time.sleep(180)
            else:
                print("Create application button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Create application')

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

    def test_golang_none_02(self):
        pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
        ApplicationName = "java-01"

        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print(" ************************ Create GoLang Application based on Team: none ************************")

    # *****************Create golang application with go echo version 4.1.14*************************

        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                CreateNew_H.click()
                self.driver.implicitly_wait(5)
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

        print("\n----------------Create golang application with go echo version 4.1.15------------------\n")
        # Choose GoLang
        try:
            GoLang = self.driver.find_element(By.XPATH, Locator.GoLang)
            if GoLang.is_enabled():
                GoLang.click()
                self.driver.implicitly_wait(10)
                time.sleep(5)
                print("GoLang button is clickable")
                time.sleep(2)
            else:
                print("GoLang button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on GoLang')

        # Put Application Name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys(ApplicationName)
                self.driver.implicitly_wait(10)
                time.sleep(2)
                print("ApplicationName_box is enable")
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted application name')

        # click on go echo box to show all versions
        try:
            Goecho_box = driver.find_element(By.XPATH, Locator.Goecho_box)
            if Goecho_box.is_enabled():
                Goecho_box.click()
                time.sleep(1)
                print("Goecho_box is enable")
            else:
                print("Goecho_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Goecho_box')

        # Choose go eco version 4.1.14
        try:
            Goecho_V_4_1_14 = driver.find_element(By.XPATH, Locator.Goecho_V_4_1_14)
            if Goecho_V_4_1_14.is_enabled():
                Goecho_V_4_1_14.click()
                time.sleep(1)
                print("Goecho_V_4_1_14 is enable")
            else:
                print("Goecho_V_4_1_14 is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Go echo_V_4_1_14')

        # # Click On Team box
        # try:
        #     TeamBox_A = driver.find_element(By.XPATH, Locator.TeamBox_A)
        #     if TeamBox_A.is_enabled():
        #         TeamBox_A.click()
        #         time.sleep(1)
        #         print("TeamBox_A is enable")
        #     else:
        #         print("TeamBox_A is not enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on TeamBox')
        #
        # # Choose Default from team
        # try:
        #     Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
        #     if Team_Default.is_displayed():
        #         Team_Default.click()
        #         time.sleep(2)
        #         print("Team_Default is displayed")
        #     else:
        #         print("Team_Default is not displayed")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully chose on Team_Default')

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                self.driver.implicitly_wait(10)
                print("Next_button is enable")
                time.sleep(2)
            else:
                print("Next_button is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Next_button')

        #  again click next button
        try:
            Next_button_two = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button_two.is_enabled():
                Next_button_two.click()
                self.driver.implicitly_wait(10)
                print("Next_button is enable")
                time.sleep(2)
            else:
                print("Next_button is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Next_button')

        # scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        print("Scroll down to show Namespaces")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                Choose_Namespace_one.click()
                print("Choose_Namespace_one is selected")
                time.sleep(5)
            else:
                print("Choose_Namespace_one is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Choose_Namespace_one')

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
            print('Successfully clicked on Save_button')

        # take action's screenshot
        ss = SS(driver)
        file_name = ss_path + "GoLang_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

        # click on Create application button
        try:
            Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
            if Create_Application.is_enabled():
                Create_Application.click()
                print("Create application button is enable")
                time.sleep(180)
            else:
                print("Create application button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Create application')

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
