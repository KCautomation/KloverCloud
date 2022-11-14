import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from src import Locator

from src import LogInPage
from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *

ss_path = "/Applications/PHP/"


class TestCreatePHP(EnvironmentSetup):
    def test_Laravel_none_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # page object
        log = LogInPage(driver)  # LogIn page

        # input email
        try:
            if log.Email_box.is_enabled():
                print("Email box is enabled")
                log.Email_box.send_keys('admin@klovercloud.com')
                time.sleep(1)
            else:
                print("Email box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            if log.Password_box.is_enabled():
                print("Password box is enabled")
                log.Password_box.send_keys('Hello@1234')
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            if log.Toggle_Visibility_Button.is_enabled():
                print("Toggle Visibility Button box is enabled")
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            if log.Sign_In_button.is_enabled():
                print("Sign In button is clickable")
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(7)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        print("****************** Create PHP Laravel Application based on Team: none *********************")
        # click on create button from header

        print("-----------------------Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                print("CreateNew_H button is enable")
                CreateNew_H.click()
                time.sleep(2)
            else:
                print("CreateNew_H In button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                print("NewApplication_H button is enable")
                NewApplication_H.click()
                self.driver.implicitly_wait(30)
                driver.refresh()
                time.sleep(1)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with PHP Version: 7.3 &  Laravel version : 7.0--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Laravel = self.driver.find_element(By.XPATH, Locator.Laravel)
            if Laravel.is_displayed():
                print("Laravel button is displayed")
                Laravel.click()
                time.sleep(2)
            else:
                print("Laravel is not displayed below")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Laravel')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_Laravel_none_01')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')
        #
        # # scroll down
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        # print("Scroll down")
        # time.sleep(2)
        #
        # # Click on team box
        # try:
        #     TeamBox_A = self.driver.find_element(By.XPATH, Locator.TeamBox_A)
        #     if TeamBox_A.is_enabled():
        #         print("Team box is Enable")
        #         TeamBox_A.click()
        #         time.sleep(2)
        #     else:
        #         print("Team box is not Enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on TeamBox_A')
        #
        # # choose Default from team box
        # try:
        #     Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
        #     if Team_Default.is_displayed():
        #         print("Team default is selectable")
        #         Team_Default.click()
        #         time.sleep(3)
        #     else:
        #         print("Team: Default is displayed")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully chose on Team Default')
        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                print("Next button is enable")
                Next_button.click()
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
                print("Next button is enable")
                Next_button_two.click()
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                print("Namespace is selected")
                Choose_Namespace_one.click()
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                print("Save button is enable")
                Save_button.click()
                time.sleep(2)
            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         print("Create application button is enable")
        #         Create_Application.click()
        #         time.sleep(180)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "test_Laravel_none_01_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_Laravel_none_02(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # page object
        log = LogInPage(driver)  # LogIn page

        # input email
        try:
            if log.Email_box.is_enabled():
                print("Email box is enabled")
                log.Email_box.send_keys('admin@klovercloud.com')
                time.sleep(1)
            else:
                print("Email box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            if log.Password_box.is_enabled():
                print("Password box is enabled")
                log.Password_box.send_keys('Hello@1234')
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            if log.Toggle_Visibility_Button.is_enabled():
                print("Toggle Visibility Button box is enabled")
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            if log.Sign_In_button.is_enabled():
                print("Sign In button is clickable")
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(7)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        print("****************** Create PHP Laravel Application based on Team: none *********************")
        # click on create button from header

        print("-----------------------Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                print("CreateNew_H button is enable")
                CreateNew_H.click()
                time.sleep(2)
            else:
                print("CreateNew_H In button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                print("NewApplication_H button is enable")
                NewApplication_H.click()
                self.driver.implicitly_wait(30)
                driver.refresh()
                time.sleep(1)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with PHP Version: 7.3 &  Laravel version : 6.0--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Laravel = self.driver.find_element(By.XPATH, Locator.Laravel)
            if Laravel.is_displayed():
                print("Laravel button is displayed")
                Laravel.click()
                time.sleep(2)
            else:
                print("Laravel is not displayed below")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Laravel')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_Laravel_none_02')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # click on Laravel version box
        try:
            Laravel_version_box = driver.find_element(By.XPATH, Locator.Laravel_version_box)
            if Laravel_version_box.is_enabled():
                print("Laravel_version_box is enabled")
                Laravel_version_box.click()
                time.sleep(2)
            else:
                print("Laravel_version_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Laravel_version_box')

        # choose Laravel version 6.0
        try:
            Laravel_version_6_0 = driver.find_element(By.XPATH, Locator.Laravel_version_6_0)
            if Laravel_version_6_0.is_displayed():
                print("Laravel_version 6.0 is displayed")
                Laravel_version_6_0.click()
                time.sleep(2)
            else:
                print("Laravel Version 6.0 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully choose Laravel Version 6.0')

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
                time.sleep(2)
            else:
                print("Team box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        # choose Default from team box
        try:
            Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
            if Team_Default.is_displayed():
                print("Team default is selectable")
                Team_Default.click()
                time.sleep(3)
            else:
                print("Team: Default is displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Team Default')

        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                print("Next button is enable")
                Next_button.click()
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
                print("Next button is enable")
                Next_button_two.click()
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                print("Namespace is selected")
                Choose_Namespace_one.click()
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                print("Save button is enable")
                Save_button.click()
                time.sleep(2)
            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         print("Create application button is enable")
        #         Create_Application.click()
        #         time.sleep(180)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "test_Laravel_none_02_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_Laravel_none_03(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # page object
        log = LogInPage(driver)  # LogIn page

        # input email
        try:
            if log.Email_box.is_enabled():
                print("Email box is enabled")
                log.Email_box.send_keys('admin@klovercloud.com')
                time.sleep(1)
            else:
                print("Email box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            if log.Password_box.is_enabled():
                print("Password box is enabled")
                log.Password_box.send_keys('Hello@1234')
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            if log.Toggle_Visibility_Button.is_enabled():
                print("Toggle Visibility Button box is enabled")
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            if log.Sign_In_button.is_enabled():
                print("Sign In button is clickable")
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(7)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        print("****************** Create PHP Laravel Application based on Team: none *********************")
        # click on create button from header

        print("-----------------------Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                print("CreateNew_H button is enable")
                CreateNew_H.click()
                time.sleep(2)
            else:
                print("CreateNew_H In button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                print("NewApplication_H button is enable")
                NewApplication_H.click()
                self.driver.implicitly_wait(30)
                driver.refresh()
                time.sleep(1)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with PHP Version: 7.3 &  Laravel version : 5.8--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Laravel = self.driver.find_element(By.XPATH, Locator.Laravel)
            if Laravel.is_displayed():
                print("Laravel button is displayed")
                Laravel.click()
                time.sleep(2)
            else:
                print("Laravel is not displayed below")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Laravel')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_Laravel_none_03')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # click on Laravel version box
        try:
            Laravel_version_box = driver.find_element(By.XPATH, Locator.Laravel_version_box)
            if Laravel_version_box.is_enabled():
                print("Laravel_version_box is enabled")
                Laravel_version_box.click()
                time.sleep(2)
            else:
                print("Laravel_version_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Laravel_version_box')

        # choose Laravel version 6.0
        try:
            Laravel_version_5_8 = driver.find_element(By.XPATH, Locator.Laravel_version_5_8)
            if Laravel_version_5_8.is_displayed():
                print("Laravel_version 5.8 is displayed")
                Laravel_version_5_8.click()
                time.sleep(2)
            else:
                print("Laravel Version 5.8 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully choose Laravel Version 5.8')

        # # scroll down
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        # print("Scroll down")
        # time.sleep(2)
        #
        # # Click on team box
        # try:
        #     TeamBox_A = self.driver.find_element(By.XPATH, Locator.TeamBox_A)
        #     if TeamBox_A.is_enabled():
        #         print("Team box is Enable")
        #         TeamBox_A.click()
        #         time.sleep(2)
        #     else:
        #         print("Team box is not Enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on TeamBox_A')
        #
        # # choose Default from team box
        # try:
        #     Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
        #     if Team_Default.is_displayed():
        #         print("Team default is selectable")
        #         Team_Default.click()
        #         time.sleep(3)
        #     else:
        #         print("Team: Default is displayed")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully chose on Team Default')

        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                print("Next button is enable")
                Next_button.click()
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
                print("Next button is enable")
                Next_button_two.click()
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                print("Namespace is selected")
                Choose_Namespace_one.click()
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                print("Save button is enable")
                Save_button.click()
                time.sleep(2)
            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         print("Create application button is enable")
        #         Create_Application.click()
        #         time.sleep(180)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "test_Laravel_none_03_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_Laravel_none_04(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # page object
        log = LogInPage(driver)  # LogIn page

        # input email
        try:
            if log.Email_box.is_enabled():
                print("Email box is enabled")
                log.Email_box.send_keys('admin@klovercloud.com')
                time.sleep(1)
            else:
                print("Email box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            if log.Password_box.is_enabled():
                print("Password box is enabled")
                log.Password_box.send_keys('Hello@1234')
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            if log.Toggle_Visibility_Button.is_enabled():
                print("Toggle Visibility Button box is enabled")
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            if log.Sign_In_button.is_enabled():
                print("Sign In button is clickable")
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(7)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        print("****************** Create PHP Laravel Application based on Team: none *********************")
        # click on create button from header

        print("-----------------------Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                print("CreateNew_H button is enable")
                CreateNew_H.click()
                time.sleep(2)
            else:
                print("CreateNew_H In button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                print("NewApplication_H button is enable")
                NewApplication_H.click()
                self.driver.implicitly_wait(30)
                driver.refresh()
                time.sleep(1)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with PHP Version: 7.3 &  Laravel version : 5.7--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Laravel = self.driver.find_element(By.XPATH, Locator.Laravel)
            if Laravel.is_displayed():
                print("Laravel button is displayed")
                Laravel.click()
                time.sleep(2)
            else:
                print("Laravel is not displayed below")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Laravel')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_Laravel_none_04')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # click on Laravel version box
        try:
            Laravel_version_box = driver.find_element(By.XPATH, Locator.Laravel_version_box)
            if Laravel_version_box.is_enabled():
                print("Laravel_version_box is enabled")
                Laravel_version_box.click()
                time.sleep(2)
            else:
                print("Laravel_version_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Laravel_version_box')

        # choose Laravel version 6.0
        try:
            Laravel_version_5_7 = driver.find_element(By.XPATH, Locator.Laravel_version_5_7)
            if Laravel_version_5_7.is_displayed():
                print("Laravel_version 5.7 is displayed")
                Laravel_version_5_7.click()
                time.sleep(2)
            else:
                print("Laravel Version 5.7 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully choose Laravel Version 5.7')

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
                time.sleep(2)
            else:
                print("Team box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        # choose Default from team box
        try:
            Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
            if Team_Default.is_displayed():
                print("Team default is selectable")
                Team_Default.click()
                time.sleep(3)
            else:
                print("Team: Default is displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Team Default')

        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                print("Next button is enable")
                Next_button.click()
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
                print("Next button is enable")
                Next_button_two.click()
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                print("Namespace is selected")
                Choose_Namespace_one.click()
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                print("Save button is enable")
                Save_button.click()
                time.sleep(2)
            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         print("Create application button is enable")
        #         Create_Application.click()
        #         time.sleep(180)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "test_Laravel_none_04_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_Laravel_none_05(self):
        # pytest.skip("Skipping test...later I will implement...")
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! URL found ')

        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        # ******************************Login**********************************
        print("----------------------Cluster LogIn-----------------------------------")
        # page object
        log = LogInPage(driver)  # LogIn page

        # input email
        try:
            if log.Email_box.is_enabled():
                print("Email box is enabled")
                log.Email_box.send_keys('admin@klovercloud.com')
                time.sleep(1)
            else:
                print("Email box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        else:
            print('Successfully inputted email')

        # input pass
        try:
            if log.Password_box.is_enabled():
                print("Password box is enabled")
                log.Password_box.send_keys('Hello@1234')
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully inputted Password')

        # To show password
        try:
            if log.Toggle_Visibility_Button.is_enabled():
                print("Toggle Visibility Button box is enabled")
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
            else:
                print("Password box is not enabled")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')

        # Click On SignIn button
        try:
            if log.Sign_In_button.is_enabled():
                print("Sign In button is clickable")
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(7)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        print("****************** Create PHP Laravel Application based on Team: none *********************")
        # click on create button from header

        print("-----------------------Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                print("CreateNew_H button is enable")
                CreateNew_H.click()
                time.sleep(2)
            else:
                print("CreateNew_H In button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = self.driver.find_element(By.XPATH, Locator.NewApplication_H)
            if NewApplication_H.is_enabled():
                print("NewApplication_H button is enable")
                NewApplication_H.click()
                self.driver.implicitly_wait(30)
                driver.refresh()
                time.sleep(1)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with PHP Version: 7.3 &  Laravel version : 5.6--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Laravel = self.driver.find_element(By.XPATH, Locator.Laravel)
            if Laravel.is_displayed():
                print("Laravel button is displayed")
                Laravel.click()
                time.sleep(2)
            else:
                print("Laravel is not displayed below")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Laravel')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_Laravel_none_05')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # click on Laravel version box
        try:
            Laravel_version_box = driver.find_element(By.XPATH, Locator.Laravel_version_box)
            if Laravel_version_box.is_enabled():
                print("Laravel_version_box is enabled")
                Laravel_version_box.click()
                time.sleep(2)
            else:
                print("Laravel_version_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Laravel_version_box')

        # choose Laravel version 6.0
        try:
            Laravel_version_5_6 = driver.find_element(By.XPATH, Locator.Laravel_version_5_6)
            if Laravel_version_5_6.is_displayed():
                print("Laravel_version 5.6 is displayed")
                Laravel_version_5_6.click()
                time.sleep(2)
            else:
                print("Laravel Version 5.6 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully choose Laravel Version 5.6')

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
                time.sleep(2)
            else:
                print("Team box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        # choose Default from team box
        try:
            Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
            if Team_Default.is_displayed():
                print("Team default is selectable")
                Team_Default.click()
                time.sleep(3)
            else:
                print("Team: Default is displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Team Default')

        # scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                print("Next button is enable")
                Next_button.click()
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
                print("Next button is enable")
                Next_button_two.click()
                time.sleep(3)
            else:
                print("Next_button_two is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully click on Next_button_two')

        # again scroll below to show Namespaces
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # Choose A Namespace for Prod Environment
        try:
            Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
            if Choose_Namespace_one.is_enabled():
                print("Namespace is selected")
                Choose_Namespace_one.click()
                time.sleep(5)
            else:
                print("Namespace is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully Choose Namespace one')

        # again scroll below
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1200")
        time.sleep(2)
        print("Scroll down to show Namespaces")

        # click on save button
        try:
            Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
            if Save_button.is_enabled():
                print("Save button is enable")
                Save_button.click()
                time.sleep(2)
            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save button')
        # click on Create application button
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         print("Create application button is enable")
        #         Create_Application.click()
        #         time.sleep(180)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "test_Laravel_none_05_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
