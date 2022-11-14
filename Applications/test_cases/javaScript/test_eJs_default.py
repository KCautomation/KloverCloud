import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from src import Locator

from src import LogInPage
from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *

ss_path = "/Applications/JavaScript/"


class TestCreateJavascript(EnvironmentSetup):

    def test_eJs_default_01(self):
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
                log.Email_box.send_keys('admin@klovercloud.com')
                print("Email box is enabled")
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
                log.Password_box.send_keys('Hello@1234')
                print("Password box is enabled")
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
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                print("Password box is enabled")
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
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(5)
                print("Sign In button is clickable")
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        # ****************************** Create Express JS Application ******************************
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
                ApplicationName_box.send_keys('test44')
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
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         Create_Application.click()
        #         time.sleep(180)
        #         print("Create application button is enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "JavaScript_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    def test_eJs_default_02(self):
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
                log.Email_box.send_keys('admin@klovercloud.com')
                print("Email box is enabled")
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
                log.Password_box.send_keys('Hello@1234')
                print("Password box is enabled")
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
                log.Toggle_Visibility_Button.click()
                time.sleep(1)
                log.Toggle_Visibility_Button.click()
                print("Password box is enabled")
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
                log.Sign_In_button.click()
                self.driver.implicitly_wait(10)
                time.sleep(5)
                print("Sign In button is clickable")
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

        # **************** Create Express Js  Application with Version: 4.17.0 ********************

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
                ApplicationName_box.send_keys('test44')
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
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         Create_Application.click()
        #         time.sleep(180)
        #         print("Create application button is enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create_Application')
        ss = SS(driver)
        file_name = ss_path + "JavaScript_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
