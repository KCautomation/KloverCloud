import time
from telnetlib import EC

import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains

from src.Locators.locators import Locator
from src.function.go_application.go_to_application_page import go_create_app_page

from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.function.logIn.login_fun import cluster_login

ss_path = "/Applications/PHP/"


class TestCreateAppPHP(EnvironmentSetup):

    def test_Laravel_default_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        ApplicationName = "laravel-26"
        print("****************** Test Cluster Login *********************")
        try:
            cluster_login()
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to Create Application Page *********************")
        try:
            go_create_app_page(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("----Create Python app with PHP Version: 7.3 &  Laravel version : 7.0--------")
        # choose Laravel
        # app = CreateApplicationPage(self.driver)
        try:
            Laravel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Laravel)))
            print("Laravel button is clickable")
            Laravel.click()
            time.sleep(2)
            # if Laravel.is_displayed():
            #     print("Laravel button is displayed")
            #     Laravel.click()
            #     time.sleep(2)
            # else:
            #     print("Laravel is not displayed below")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully chose on Laravel')

        # put application name
        try:
            ApplicationName_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
            print("ApplicationName_box is visible")
            ApplicationName_box.send_keys(ApplicationName)
            time.sleep(2)
            # if ApplicationName_box.is_enabled():
            #     print("ApplicationName_box is enable")
            #     ApplicationName_box.send_keys('test_Laravel_default_01')
            #     time.sleep(2)
            # else:
            #     print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put ApplicationName')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        print("Scroll down")
        time.sleep(2)

        # Click on team box
        try:
            TeamBox_A = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.TeamBox_A)))
            print("TeamBox_A button is clickable")
            TeamBox_A.click()
            time.sleep(2)
            # if TeamBox_A.is_enabled():
            #     print("Team box is Enable")
            #     TeamBox_A.click()
            #     time.sleep(2)
            # else:
            #     print("Team box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        # choose Default from team box
        try:
            Team_Default = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Team_Default)))
            print("Team_Default button is clickable")
            Team_Default.click()
            time.sleep(2)
            # if Team_Default.is_displayed():
            #     print("Team default is selectable")
            #     Team_Default.click()
            #     time.sleep(3)
            # else:
            #     print("Team: Default is displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully chose on Team Default')

        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        #  click next button
        try:
            Next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
            print("Next_button button is clickable")
            Next_button.click()
            time.sleep(2)
            # if Next_button.is_enabled():
            #     print("Next button is enable")
            #     Next_button.click()
            #     time.sleep(2)
            # else:
            #     print("Next button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully click on Next_button')

        # Again click next button
        try:
            Next_button_two = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
            print("Next_button_two button is clickable")
            Next_button_two.click()
            time.sleep(3)
            # if Next_button_two.is_enabled():
            #     print("Next button is enable")
            #     Next_button_two.click()
            #     time.sleep(3)
            # else:
            #     print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Choose_Namespace_one)))
            print("Choose_Namespace_one button is clickable")
            Choose_Namespace_one.click()
            time.sleep(5)
            # if Choose_Namespace_one.is_enabled():
            #     print("Namespace is selected")
            #     Choose_Namespace_one.click()
            #     time.sleep(5)
            # else:
            #     print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1500")
        time.sleep(2)
        print("Scroll down to show Namespaces")
        # click on save button
        try:
            Save_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Save_button_A)))
            print("Save_button button is clickable")
            Save_button.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on Save button')

        # click on Create application button
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

        ss = SS(driver)
        file_name = ss_path + "create_test_Laravel_default_01" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

        time.sleep(30)
        # close log
        try:
            Live_Pipeline_Logs = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
            Live_Pipeline_Logs.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # application created validation
        try:
            if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locator.To_deploy))):
                assert True
                print('deploy SVG is visible, So Application created perfectly')
                time.sleep(2)
                action = ActionChains(driver)
                # click the item
                action.click()
                # perform the operation
                action.perform()
                time.sleep(2)
            else:
                print("Application created Failed")
                time.sleep(2)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except ElementClickInterceptedException as e:
            print("ElementClickInterceptedException", e)
        #
        # try:
        #     if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locator.Deploy_button))):
        #         self.assertTrue('deploy button is invisible, So Application deployed perfectly')
        #         print("deploy button is visible, So Application Created Successfully")
        #         time.sleep(2)
        #     else:
        #         print("Application Deployed Failed")
        #         time.sleep(2)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error :\n", e, "\n")
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException", e)
        # except ElementClickInterceptedException as e:
        #     print("ElementClickInterceptedException", e)

        # deploy application
        print("******************************* Test Try to deploy application******************************")
        # click on deploy
        try:
            To_deploy = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Locator.To_deploy)))
            print("deploy element is visible")
            # To_deploy.click()
            To_deploy.click()
            # print("successfully clicked on deploy")
            time.sleep(2)
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
                EC.element_to_be_clickable((By.XPATH, Locator.Deploy_button)))
            print("deploy button is clickable")
            Deploy_button.click()
            self.driver.implicitly_wait(20)
            print("successfully clicked on deploy")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click on okay button to start deploy
        try:
            Okay_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Okay_button)))
            print("Okay_button is clickable")
            Okay_button.click()
            print("successfully clicked on Okay")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        try:
            Deployment_Pending_msg = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_msg)))
            if Deployment_Pending_msg.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Deployment_Pending_msg.text, ['bold', 'underlined']))
                print("\n")
                # time.sleep(2)
                pass
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # error msg
        # try:
        #     deployment_failed = WebDriverWait(driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.deployment_failed)))
        #     if deployment_failed.is_displayed():
        #         print('Shown a message: ',
        #               simple_colors.green(deployment_failed.text, ['bold', 'underlined']))
        #         print("\n")
        #         time.sleep(3)
        #         return exit()
        #         # return False
        #     else:
        #         pass
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)

        # 2nd success msg

        try:
            Deployment_Pending_time_msg = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_time_msg)))
            if Deployment_Pending_time_msg.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Deployment_Pending_time_msg.text, ['bold', 'underlined']))
                print("\n")
                # time.sleep(6)
                pass
                # print("Application_build_finished_successfully")
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Application deployed successful msg
        try:
            Application_Deployed = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Locator.Application_Deployed)))
            if Application_Deployed.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Application_Deployed.text, ['bold', 'underlined']))
                print("\n")
                pass
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # check deployed or not

        print("**********Application deployed or not by build button visibility***********")
        time.sleep(120)
        # close log
        try:
            Live_Pipeline_Logs = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
            Live_Pipeline_Logs.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # try:
        #     To_deploy = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.To_deploy)))
        #     print("deploy element is visible")
        #     To_deploy.click()
        #     print("successfully clicked on deploy")
        #     time.sleep(2)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error :\n", e, "\n")
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException", e)
        # except ElementClickInterceptedException as e:
        #     print("ElementClickInterceptedException", e)
        #
        # try:
        #     if WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, Locator.Deploy_button))):
        #         assert True
        #         print("deploy button is invisible, So Application deployed perfectly")
        #         time.sleep(2)
        #         action = ActionChains(driver)
        #         # click the item
        #         action.click()
        #         # perform the operation
        #         action.perform()
        #         time.sleep(2)
        #     else:
        #         print("Application Deployed Failed")
        #         time.sleep(2)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error :\n", e, "\n")
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException", e)
        # except ElementClickInterceptedException as e:
        #     print("ElementClickInterceptedException", e)

        file_name = ss_path + "deploy_success_validation_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

        time.sleep(20)
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

    # def test_Laravel_default_02(self):
    #     # pytest.skip("Skipping test...later I will implement...")
    #     driver = self.driver
    #     ApplicationName = "test_Laravel_default_02"
    #     print("****************** Test Cluster Login *********************")
    #     try:
    #         test_cluster_login(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #
    #     print("****************** Go to Create Application Page *********************")
    #     try:
    #         go_create_app_page(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #     print("----Create Python app with PHP Version: 7.3 &  Laravel version : 6.0--------")
    #     # choose Django
    #     # app = CreateApplicationPage(self.driver)
    #     try:
    #         Laravel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Laravel)))
    #         print("Laravel button is clickable")
    #         Laravel.click()
    #         time.sleep(2)
    #         # if Laravel.is_displayed():
    #         #     print("Laravel button is displayed")
    #         #     Laravel.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Laravel is not displayed below")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel')
    #
    #     # put application name
    #     try:
    #         ApplicationName_box = WebDriverWait(driver, 20).until(
    #             EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
    #         print("ApplicationName_box is visible")
    #         ApplicationName_box.send_keys(ApplicationName)
    #         time.sleep(2)
    #         # if ApplicationName_box.is_enabled():
    #         #     print("ApplicationName_box is enable")
    #         #     ApplicationName_box.send_keys('test_Laravel_default_01')
    #         #     time.sleep(2)
    #         # else:
    #         #     print("ApplicationName_box is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully put ApplicationName')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_box = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_box)))
    #         print("Laravel_version_box button is clickable")
    #         Laravel_version_box.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Laravel_version_box')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_6_0 = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_6_0)))
    #         print("Laravel_version 6.0 button is clickable")
    #         Laravel_version_6_0.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel version 6.0')
    #
    #     # scroll down
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
    #     print("Scroll down")
    #     time.sleep(2)
    #
    #     # Click on team box
    #     try:
    #         TeamBox_A = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.TeamBox_A)))
    #         print("TeamBox_A button is clickable")
    #         TeamBox_A.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on TeamBox_A')
    #
    #     # choose Default from team box
    #     try:
    #         Team_Default = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Team_Default)))
    #         print("Team_Default button is clickable")
    #         Team_Default.click()
    #         time.sleep(2)
    #         # if Team_Default.is_displayed():
    #         #     print("Team default is selectable")
    #         #     Team_Default.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Team: Default is displayed")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Team Default')
    #
    #     # scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
    #     time.sleep(2)
    #     print("Scroll down")
    #
    #     #  click next button
    #     try:
    #         Next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button button is clickable")
    #         Next_button.click()
    #         time.sleep(2)
    #         # if Next_button.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Next button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button')
    #
    #     # Again click next button
    #     try:
    #         Next_button_two = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button_two button is clickable")
    #         Next_button_two.click()
    #         time.sleep(3)
    #         # if Next_button_two.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button_two.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Next_button_two is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button_two')
    #
    #     # again scroll below to show Namespaces
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #
    #     # Choose A Namespace for Prod Environment
    #     try:
    #         Choose_Namespace_one = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Choose_Namespace_one)))
    #         print("Choose_Namespace_one button is clickable")
    #         Choose_Namespace_one.click()
    #         time.sleep(5)
    #         # if Choose_Namespace_one.is_enabled():
    #         #     print("Namespace is selected")
    #         #     Choose_Namespace_one.click()
    #         #     time.sleep(5)
    #         # else:
    #         #     print("Namespace is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully Choose Namespace one')
    #
    #     # again scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #     # click on save button
    #     try:
    #         Save_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Save_button_A)))
    #         print("Save_button button is clickable")
    #         Save_button.click()
    #         time.sleep(2)
    #         # if Save_button.is_enabled():
    #         #     print("Save button is enable")
    #         #     Save_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Save button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Save button')
    #
    #     # click on Create application button
    #     try:
    #         Create_Application = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Create_Application)))
    #         print("Create_Application button is clickable")
    #         Create_Application.click()
    #         # check success message
    #         New_Git_Commit_Pushed_msg = WebDriverWait(driver, 50).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.New_Git_Commit_Pushed_msg)))
    #         if New_Git_Commit_Pushed_msg.is_displayed():
    #
    #             print('Shown a message: ',
    #                   simple_colors.green(New_Git_Commit_Pushed_msg.text, ['bold', 'underlined']))
    #             print("\n")
    #             pass
    #             Application_build_finished_successfully_msg = WebDriverWait(driver, 120).until(
    #                 EC.presence_of_element_located((By.XPATH, Locator.Application_build_finished_successfully_msg)))
    #             if Application_build_finished_successfully_msg.is_displayed():
    #                 print('Shown a message: ',
    #                       simple_colors.green(Application_build_finished_successfully_msg.text, ['bold', 'underlined']))
    #                 print("\n")
    #                 pass
    #                 time.sleep(30)
    #                 print("Application_build_finished_successfully")
    #         else:
    #             assert False
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #
    #     ss = SS(driver)
    #     file_name = ss_path + "test_Laravel_default_02_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    #     # close log
    #     try:
    #         Live_Pipeline_Logs = WebDriverWait(driver, 60).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
    #         Live_Pipeline_Logs.click()
    #         time.sleep(5)
    #         pass
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #     file_name = ss_path + "success_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    # def test_Laravel_default_03(self):
    #     # pytest.skip("Skipping test...later I will implement...")
    #     driver = self.driver
    #     ApplicationName = "test_Laravel_default_03"
    #     print("****************** Test Cluster Login *********************")
    #     try:
    #         test_cluster_login(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #
    #     print("****************** Go to Create Application Page *********************")
    #     try:
    #         go_create_app_page(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #     print("----Create Python app with PHP Version: 7.3 &  Laravel version : 5.8--------")
    #     # choose Django
    #     # app = CreateApplicationPage(self.driver)
    #     try:
    #         Laravel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Laravel)))
    #         print("Laravel button is clickable")
    #         Laravel.click()
    #         time.sleep(2)
    #         # if Laravel.is_displayed():
    #         #     print("Laravel button is displayed")
    #         #     Laravel.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Laravel is not displayed below")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel')
    #
    #     # put application name
    #     try:
    #         ApplicationName_box = WebDriverWait(driver, 20).until(
    #             EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
    #         print("ApplicationName_box is visible")
    #         ApplicationName_box.send_keys(ApplicationName)
    #         time.sleep(2)
    #         # if ApplicationName_box.is_enabled():
    #         #     print("ApplicationName_box is enable")
    #         #     ApplicationName_box.send_keys('test_Laravel_default_01')
    #         #     time.sleep(2)
    #         # else:
    #         #     print("ApplicationName_box is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully put ApplicationName')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_box = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_box)))
    #         print("Laravel_version_box button is clickable")
    #         Laravel_version_box.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Laravel_version_box')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_5_8 = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_5_8)))
    #         print("Laravel_version 6.0 button is clickable")
    #         Laravel_version_5_8.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel version 5.8')
    #
    #     # scroll down
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
    #     print("Scroll down")
    #     time.sleep(2)
    #
    #     # Click on team box
    #     try:
    #         TeamBox_A = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.TeamBox_A)))
    #         print("TeamBox_A button is clickable")
    #         TeamBox_A.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on TeamBox_A')
    #
    #     # choose Default from team box
    #     try:
    #         Team_Default = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Team_Default)))
    #         print("Team_Default button is clickable")
    #         Team_Default.click()
    #         time.sleep(2)
    #         # if Team_Default.is_displayed():
    #         #     print("Team default is selectable")
    #         #     Team_Default.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Team: Default is displayed")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Team Default')
    #
    #     # scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
    #     time.sleep(2)
    #     print("Scroll down")
    #
    #     #  click next button
    #     try:
    #         Next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button button is clickable")
    #         Next_button.click()
    #         time.sleep(2)
    #         # if Next_button.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Next button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button')
    #
    #     # Again click next button
    #     try:
    #         Next_button_two = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button_two button is clickable")
    #         Next_button_two.click()
    #         time.sleep(3)
    #         # if Next_button_two.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button_two.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Next_button_two is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button_two')
    #
    #     # again scroll below to show Namespaces
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #
    #     # Choose A Namespace for Prod Environment
    #     try:
    #         Choose_Namespace_one = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Choose_Namespace_one)))
    #         print("Choose_Namespace_one button is clickable")
    #         Choose_Namespace_one.click()
    #         time.sleep(5)
    #         # if Choose_Namespace_one.is_enabled():
    #         #     print("Namespace is selected")
    #         #     Choose_Namespace_one.click()
    #         #     time.sleep(5)
    #         # else:
    #         #     print("Namespace is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully Choose Namespace one')
    #
    #     # again scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #     # click on save button
    #     try:
    #         Save_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Save_button_A)))
    #         print("Save_button button is clickable")
    #         Save_button.click()
    #         time.sleep(2)
    #         # if Save_button.is_enabled():
    #         #     print("Save button is enable")
    #         #     Save_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Save button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Save button')
    #
    #     # click on Create application button
    #     try:
    #         Create_Application = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Create_Application)))
    #         print("Create_Application button is clickable")
    #         Create_Application.click()
    #         # check success message
    #         New_Git_Commit_Pushed_msg = WebDriverWait(driver, 50).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.New_Git_Commit_Pushed_msg)))
    #         if New_Git_Commit_Pushed_msg.is_displayed():
    #
    #             print('Shown a message: ',
    #                   simple_colors.green(New_Git_Commit_Pushed_msg.text, ['bold', 'underlined']))
    #             print("\n")
    #             pass
    #             Application_build_finished_successfully_msg = WebDriverWait(driver, 120).until(
    #                 EC.presence_of_element_located((By.XPATH, Locator.Application_build_finished_successfully_msg)))
    #             if Application_build_finished_successfully_msg.is_displayed():
    #                 print('Shown a message: ',
    #                       simple_colors.green(Application_build_finished_successfully_msg.text, ['bold', 'underlined']))
    #                 print("\n")
    #                 pass
    #                 time.sleep(30)
    #                 print("Application_build_finished_successfully")
    #         else:
    #             assert False
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #
    #     ss = SS(driver)
    #     file_name = ss_path + "test_Laravel_default_03_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    #     # close log
    #     try:
    #         Live_Pipeline_Logs = WebDriverWait(driver, 60).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
    #         Live_Pipeline_Logs.click()
    #         time.sleep(5)
    #         pass
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #     file_name = ss_path + "success_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    # def test_Laravel_default_04(self):
    #     # pytest.skip("Skipping test...later I will implement...")
    #     driver = self.driver
    #     ApplicationName = "test_Laravel_default_04"
    #     print("****************** Test Cluster Login *********************")
    #     try:
    #         test_cluster_login(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #
    #     print("****************** Go to Create Application Page *********************")
    #     try:
    #         go_create_app_page(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #     print("----Create Python app with PHP Version: 7.3 &  Laravel version : 5.7--------")
    #     # choose Django
    #     # app = CreateApplicationPage(self.driver)
    #     try:
    #         Laravel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Laravel)))
    #         print("Laravel button is clickable")
    #         Laravel.click()
    #         time.sleep(2)
    #         # if Laravel.is_displayed():
    #         #     print("Laravel button is displayed")
    #         #     Laravel.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Laravel is not displayed below")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel')
    #
    #     # put application name
    #     try:
    #         ApplicationName_box = WebDriverWait(driver, 20).until(
    #             EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
    #         print("ApplicationName_box is visible")
    #         ApplicationName_box.send_keys(ApplicationName)
    #         time.sleep(2)
    #         # if ApplicationName_box.is_enabled():
    #         #     print("ApplicationName_box is enable")
    #         #     ApplicationName_box.send_keys('test_Laravel_default_01')
    #         #     time.sleep(2)
    #         # else:
    #         #     print("ApplicationName_box is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully put ApplicationName')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_box = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_box)))
    #         print("Laravel_version_box button is clickable")
    #         Laravel_version_box.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Laravel_version_box')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_5_7 = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_5_7)))
    #         print("Laravel_version 6.0 button is clickable")
    #         Laravel_version_5_7.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel version 5.7')
    #
    #     # scroll down
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
    #     print("Scroll down")
    #     time.sleep(2)
    #
    #     # Click on team box
    #     try:
    #         TeamBox_A = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.TeamBox_A)))
    #         print("TeamBox_A button is clickable")
    #         TeamBox_A.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on TeamBox_A')
    #
    #     # choose Default from team box
    #     try:
    #         Team_Default = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Team_Default)))
    #         print("Team_Default button is clickable")
    #         Team_Default.click()
    #         time.sleep(2)
    #         # if Team_Default.is_displayed():
    #         #     print("Team default is selectable")
    #         #     Team_Default.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Team: Default is displayed")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Team Default')
    #
    #     # scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
    #     time.sleep(2)
    #     print("Scroll down")
    #
    #     #  click next button
    #     try:
    #         Next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button button is clickable")
    #         Next_button.click()
    #         time.sleep(2)
    #         # if Next_button.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Next button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button')
    #
    #     # Again click next button
    #     try:
    #         Next_button_two = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button_two button is clickable")
    #         Next_button_two.click()
    #         time.sleep(3)
    #         # if Next_button_two.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button_two.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Next_button_two is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button_two')
    #
    #     # again scroll below to show Namespaces
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #
    #     # Choose A Namespace for Prod Environment
    #     try:
    #         Choose_Namespace_one = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Choose_Namespace_one)))
    #         print("Choose_Namespace_one button is clickable")
    #         Choose_Namespace_one.click()
    #         time.sleep(5)
    #         # if Choose_Namespace_one.is_enabled():
    #         #     print("Namespace is selected")
    #         #     Choose_Namespace_one.click()
    #         #     time.sleep(5)
    #         # else:
    #         #     print("Namespace is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully Choose Namespace one')
    #
    #     # again scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #     # click on save button
    #     try:
    #         Save_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Save_button_A)))
    #         print("Save_button button is clickable")
    #         Save_button.click()
    #         time.sleep(2)
    #         # if Save_button.is_enabled():
    #         #     print("Save button is enable")
    #         #     Save_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Save button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Save button')
    #
    #     # click on Create application button
    #     try:
    #         Create_Application = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Create_Application)))
    #         print("Create_Application button is clickable")
    #         Create_Application.click()
    #         # check success message
    #         New_Git_Commit_Pushed_msg = WebDriverWait(driver, 50).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.New_Git_Commit_Pushed_msg)))
    #         if New_Git_Commit_Pushed_msg.is_displayed():
    #
    #             print('Shown a message: ',
    #                   simple_colors.green(New_Git_Commit_Pushed_msg.text, ['bold', 'underlined']))
    #             print("\n")
    #             pass
    #             Application_build_finished_successfully_msg = WebDriverWait(driver, 120).until(
    #                 EC.presence_of_element_located((By.XPATH, Locator.Application_build_finished_successfully_msg)))
    #             if Application_build_finished_successfully_msg.is_displayed():
    #                 print('Shown a message: ',
    #                       simple_colors.green(Application_build_finished_successfully_msg.text, ['bold', 'underlined']))
    #                 print("\n")
    #                 pass
    #                 time.sleep(30)
    #                 print("Application_build_finished_successfully")
    #         else:
    #             assert False
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #
    #     ss = SS(driver)
    #     file_name = ss_path + "test_Laravel_default_04_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    #     # close log
    #     try:
    #         Live_Pipeline_Logs = WebDriverWait(driver, 60).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
    #         Live_Pipeline_Logs.click()
    #         time.sleep(5)
    #         pass
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #     file_name = ss_path + "success_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    # def test_Laravel_default_05(self):
    #     # pytest.skip("Skipping test...later I will implement...")
    #     driver = self.driver
    #     ApplicationName = "test_Laravel_default_06"
    #     print("****************** Test Cluster Login *********************")
    #     try:
    #         test_cluster_login(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #
    #     print("****************** Go to Create Application Page *********************")
    #     try:
    #         go_create_app_page(self)
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error :\n", e, "\n")
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException", e)
    #     print("----Create Python app with PHP Version: 7.3 &  Laravel version : 7.0--------")
    #     # choose Django
    #     # app = CreateApplicationPage(self.driver)
    #     try:
    #         Laravel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Laravel)))
    #         print("Laravel button is clickable")
    #         Laravel.click()
    #         time.sleep(2)
    #         # if Laravel.is_displayed():
    #         #     print("Laravel button is displayed")
    #         #     Laravel.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Laravel is not displayed below")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel')
    #
    #     # put application name
    #     try:
    #         ApplicationName_box = WebDriverWait(driver, 20).until(
    #             EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
    #         print("ApplicationName_box is visible")
    #         ApplicationName_box.send_keys(ApplicationName)
    #         time.sleep(2)
    #         # if ApplicationName_box.is_enabled():
    #         #     print("ApplicationName_box is enable")
    #         #     ApplicationName_box.send_keys('test_Laravel_default_01')
    #         #     time.sleep(2)
    #         # else:
    #         #     print("ApplicationName_box is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully put ApplicationName')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_box = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_box)))
    #         print("Laravel_version_box button is clickable")
    #         Laravel_version_box.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Laravel_version_box')
    #
    #     # click on laravel version box
    #     try:
    #         Laravel_version_5_6 = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Laravel_version_5_6)))
    #         print("Laravel_version 6.0 button is clickable")
    #         Laravel_version_5_6.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Laravel version 5.6')
    #
    #     # scroll down
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
    #     print("Scroll down")
    #     time.sleep(2)
    #
    #     # Click on team box
    #     try:
    #         TeamBox_A = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.TeamBox_A)))
    #         print("TeamBox_A button is clickable")
    #         TeamBox_A.click()
    #         time.sleep(2)
    #         # if TeamBox_A.is_enabled():
    #         #     print("Team box is Enable")
    #         #     TeamBox_A.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Team box is not Enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on TeamBox_A')
    #
    #     # choose Default from team box
    #     try:
    #         Team_Default = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Team_Default)))
    #         print("Team_Default button is clickable")
    #         Team_Default.click()
    #         time.sleep(2)
    #         # if Team_Default.is_displayed():
    #         #     print("Team default is selectable")
    #         #     Team_Default.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Team: Default is displayed")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully chose on Team Default')
    #
    #     # scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
    #     time.sleep(2)
    #     print("Scroll down")
    #
    #     #  click next button
    #     try:
    #         Next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button button is clickable")
    #         Next_button.click()
    #         time.sleep(2)
    #         # if Next_button.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Next button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button')
    #
    #     # Again click next button
    #     try:
    #         Next_button_two = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Next_button)))
    #         print("Next_button_two button is clickable")
    #         Next_button_two.click()
    #         time.sleep(3)
    #         # if Next_button_two.is_enabled():
    #         #     print("Next button is enable")
    #         #     Next_button_two.click()
    #         #     time.sleep(3)
    #         # else:
    #         #     print("Next_button_two is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully click on Next_button_two')
    #
    #     # again scroll below to show Namespaces
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #
    #     # Choose A Namespace for Prod Environment
    #     try:
    #         Choose_Namespace_one = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Choose_Namespace_one)))
    #         print("Choose_Namespace_one button is clickable")
    #         Choose_Namespace_one.click()
    #         time.sleep(5)
    #         # if Choose_Namespace_one.is_enabled():
    #         #     print("Namespace is selected")
    #         #     Choose_Namespace_one.click()
    #         #     time.sleep(5)
    #         # else:
    #         #     print("Namespace is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully Choose Namespace one')
    #
    #     # again scroll below
    #     driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
    #     time.sleep(2)
    #     print("Scroll down to show Namespaces")
    #     # click on save button
    #     try:
    #         Save_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Save_button_A)))
    #         print("Save_button button is clickable")
    #         Save_button.click()
    #         time.sleep(2)
    #         # if Save_button.is_enabled():
    #         #     print("Save button is enable")
    #         #     Save_button.click()
    #         #     time.sleep(2)
    #         # else:
    #         #     print("Save button is not enable")
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     else:
    #         print('Successfully clicked on Save button')
    #
    #     # click on Create application button
    #     try:
    #         Create_Application = WebDriverWait(driver, 20).until(
    #             EC.element_to_be_clickable((By.XPATH, Locator.Create_Application)))
    #         print("Create_Application button is clickable")
    #         Create_Application.click()
    #         # check success message
    #         New_Git_Commit_Pushed_msg = WebDriverWait(driver, 50).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.New_Git_Commit_Pushed_msg)))
    #         if New_Git_Commit_Pushed_msg.is_displayed():
    #
    #             print('Shown a message: ',
    #                   simple_colors.green(New_Git_Commit_Pushed_msg.text, ['bold', 'underlined']))
    #             print("\n")
    #             pass
    #             Application_build_finished_successfully_msg = WebDriverWait(driver, 120).until(
    #                 EC.presence_of_element_located((By.XPATH, Locator.Application_build_finished_successfully_msg)))
    #             if Application_build_finished_successfully_msg.is_displayed():
    #                 print('Shown a message: ',
    #                       simple_colors.green(Application_build_finished_successfully_msg.text, ['bold', 'underlined']))
    #                 print("\n")
    #                 pass
    #                 time.sleep(30)
    #                 print("Application_build_finished_successfully")
    #         else:
    #             assert False
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #
    #     ss = SS(driver)
    #     file_name = ss_path + "test_Laravel_default_05_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
    #
    #     # close log
    #     try:
    #         Live_Pipeline_Logs = WebDriverWait(driver, 60).until(
    #             EC.presence_of_element_located((By.XPATH, Locator.Live_Pipeline_Logs)))
    #         Live_Pipeline_Logs.click()
    #         time.sleep(5)
    #         pass
    #     except NoSuchElementException as e:
    #         print("NoSuchElementException error", e)
    #     except TimeoutException as e:
    #         print("TimeoutException error", e)
    #     except InvalidSessionIdException as e:
    #         print("InvalidSessionIdException error", e)
    #     file_name = ss_path + "success_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    #     ss.driver.save_screenshot(file_name)
    #     ss.ScreenShot(file_name)
