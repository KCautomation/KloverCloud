import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from src.Locators.locators import Locator
from src.Page_object_model.pom_loginPage import LogInPage
from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *

ss_path = "/Applications/Python/"


class TestCreatePython(EnvironmentSetup):
    def test_dj_default_01(self):
        pytest.skip("Skipping test...later I will implement...")
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

        # ****************************** Create Python Application based on Team: default ******************************
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
                self.driver.implicitly_wait(20)
                time.sleep(5)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with Python version: 3.8.3 & Django version : 2.2.14--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Django = self.driver.find_element(By.XPATH, Locator.Django)
            if Django.is_displayed():
                Django.click()
                time.sleep(2)
                print("Django button is displayed")
            else:
                print("Django is not displayed below")
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Django')
        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_dj_default_01')
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
        file_name = ss_path + "test_dj_default_01_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_dj_default_02(self):
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

        # ****************************** Create Python Application based on Team: default ******************************
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
                self.driver.implicitly_wait(20)
                time.sleep(5)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with Python version: 3.8.3 & Django version : 2.2.14--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Django = self.driver.find_element(By.XPATH, Locator.Django)
            if Django.is_displayed():
                Django.click()
                time.sleep(2)
                print("Django button is displayed")
            else:
                print("Django is not displayed below")
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Django')

        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_dj_default_06')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')
        # Click on django version box
        try:
            Django_version_box = self.driver.find_element(By.XPATH, Locator.Django_version_box)
            if Django_version_box.is_enabled():
                print("Django_version_box  is Enable")
                Django_version_box.click()
                time.sleep(2)
            else:
                print("Django_version_box  is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Django_version_box ')

        # choose on django version 2.2.14
        try:
            Django_Version_2_2_14 = self.driver.find_element(By.XPATH, Locator.Django_Version_2_2_14)
            if Django_Version_2_2_14.is_displayed():
                print("Django_Version 2.2.14  is displayed")
                Django_Version_2_2_14.click()
                time.sleep(2)
            else:
                print("Django_version_box  is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Django_version_box ')
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
        file_name = ss_path + "test_dj_default_02_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_dj_default_03(self):
        pytest.skip("Skipping test...later I will implement...")
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

        # ****************************** Create Python Application based on Team: default ******************************
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
                self.driver.implicitly_wait(20)
                time.sleep(5)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with Python version: 3.7.8 & Django version : 3.0.8--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Django = self.driver.find_element(By.XPATH, Locator.Django)
            if Django.is_displayed():
                Django.click()
                time.sleep(2)
                print("Django button is displayed")
            else:
                print("Django is not displayed below")
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Django')
        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_dj_default_03')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # Click on Python_version_box
        try:
            Python_version_box = self.driver.find_element(By.XPATH, Locator.Python_version_box)
            if Python_version_box.is_enabled():
                print("Python_version box  is Enable")
                Python_version_box.click()
                time.sleep(2)
            else:
                print("Python_version box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Python_version_box')

        # choose on Python_version 3.7.8
        try:
            Python_version_3_7_8 = self.driver.find_element(By.XPATH, Locator.Python_version_3_7_8)
            if Python_version_3_7_8.is_displayed():
                print("Python version 3.7.8 is displayed")
                Python_version_3_7_8.click()
                time.sleep(2)
            else:
                print("Python_version 3.7.8 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Python version 3.7.8')

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
        file_name = ss_path + "test_dj_default_03_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_dj_default_04(self):
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

        # ****************************** Create Python Application based on Team: default ******************************
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
                self.driver.implicitly_wait(20)
                time.sleep(5)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with Python version: 3.7.8 & Django version : 2.2.14--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Django = self.driver.find_element(By.XPATH, Locator.Django)
            if Django.is_displayed():
                Django.click()
                time.sleep(2)
                print("Django button is displayed")
            else:
                print("Django is not displayed below")
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Django')
        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_dj_default_04')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # Click on Python_version_box
        try:
            Python_version_box = self.driver.find_element(By.XPATH, Locator.Python_version_box)
            if Python_version_box.is_enabled():
                print("Python_version box  is Enable")
                Python_version_box.click()
                time.sleep(2)
            else:
                print("Python_version box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Python_version_box')

        # choose on Python_version 3.7.8
        try:
            Python_version_3_7_8 = self.driver.find_element(By.XPATH, Locator.Python_version_3_7_8)
            if Python_version_3_7_8.is_displayed():
                print("Python version 3.7.8 is displayed")
                Python_version_3_7_8.click()
                time.sleep(2)
            else:
                print("Python_version 3.7.8 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Python version 3.7.8')

        # Click on Django_version box
        try:
            Django_version_box = self.driver.find_element(By.XPATH, Locator.Django_version_box)
            if Django_version_box.is_enabled():
                print("Django_version_box is Enable")
                Django_version_box.click()
                time.sleep(2)
            else:
                print("Django_version box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Django_version_box')

        # choose on Django_version 2.2.14
        try:
            Django_Version_2_2_14 = self.driver.find_element(By.XPATH, Locator.Django_Version_2_2_14)
            if Django_Version_2_2_14.is_displayed():
                print("Django Version 2.2.14 is displayed")
                Django_Version_2_2_14.click()
                time.sleep(2)
            else:
                print("Django Version 2.2.14 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Django Version 2.2.14')

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
        file_name = ss_path + "test_dj_default_04_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_dj_default_05(self):
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

        # ****************************** Create Python Application based on Team: default ******************************
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
                self.driver.implicitly_wait(20)
                time.sleep(5)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with Python version: 3.7.8 & Django version : 3.0.8--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Django = self.driver.find_element(By.XPATH, Locator.Django)
            if Django.is_displayed():
                Django.click()
                time.sleep(2)
                print("Django button is displayed")
            else:
                print("Django is not displayed below")
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Django')
        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_dj_default_05')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # Click on Python_version_box
        try:
            Python_version_box = self.driver.find_element(By.XPATH, Locator.Python_version_box)
            if Python_version_box.is_enabled():
                print("Python_version box  is Enable")
                Python_version_box.click()
                time.sleep(2)
            else:
                print("Python_version box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Python_version_box')

        # choose on Python_version 3.7.8
        try:
            Python_version_3_6_11 = self.driver.find_element(By.XPATH, Locator.Python_version_3_6_11)
            if Python_version_3_6_11.is_displayed():
                print("Python version 3.6.11 is displayed")
                Python_version_3_6_11.click()
                time.sleep(2)
            else:
                print("Python version 3.6.11 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Python version 3.6.11')

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
        file_name = ss_path + "test_dj_default_05_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_dj_default_06(self):
        pytest.skip("Skipping test...later I will implement...")
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

        # ****************************** Create Python Application based on Team: default ******************************
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
                self.driver.implicitly_wait(20)
                time.sleep(5)
            else:
                print("NewApplication_H In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print("-----------------------Welcome Create Application Page----------------------------------------")
        print("----Create Python app with Python version: 3.6.11 & Django version : 2.2.14--------")
        # choose Django
        # app = CreateApplicationPage(self.driver)
        try:
            Django = self.driver.find_element(By.XPATH, Locator.Django)
            if Django.is_displayed():
                Django.click()
                time.sleep(2)
                print("Django button is displayed")
            else:
                print("Django is not displayed below")
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Django')
        # put application name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                print("ApplicationName_box is enable")
                ApplicationName_box.send_keys('test_dj_default_06')
                time.sleep(2)
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully put ApplicationName')

        # Click on Python_version_box
        try:
            Python_version_box = self.driver.find_element(By.XPATH, Locator.Python_version_box)
            if Python_version_box.is_enabled():
                print("Python_version box  is Enable")
                Python_version_box.click()
                time.sleep(2)
            else:
                print("Python_version box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Python_version_box')

        # choose on Python_version 3.7.8
        try:
            Python_version_3_6_11 = self.driver.find_element(By.XPATH, Locator.Python_version_3_6_11)
            if Python_version_3_6_11.is_displayed():
                print("Python_version 3.6.11 is displayed")
                Python_version_3_6_11.click()
                time.sleep(2)
            else:
                print("Python_version 3.6.11 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Python_version 3.6.11')

        # Click on Django_version box
        try:
            Django_version_box = self.driver.find_element(By.XPATH, Locator.Django_version_box)
            if Django_version_box.is_enabled():
                print("Django_version_box is Enable")
                Django_version_box.click()
                time.sleep(2)
            else:
                print("Django_version box is not Enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Django_version_box')

        # choose on Django_version 2.2.14
        try:
            Django_Version_2_2_14 = self.driver.find_element(By.XPATH, Locator.Django_Version_2_2_14)
            if Django_Version_2_2_14.is_displayed():
                print("Django Version 2.2.14 is displayed")
                Django_Version_2_2_14.click()
                time.sleep(2)
            else:
                print("Django Version 2.2.14 is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose Django Version 2.2.14')

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
        file_name = ss_path + "test_dj_default_06_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
