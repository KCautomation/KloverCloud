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

ss_path = "/Applications/DotNet/"


class TestCreateDotNet(EnvironmentSetup):

    def test_dot_none_01(self):
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

        # ****************************** Create Dotnet Application with 3.1 ******************************
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

        print("-----------------Create DotNet app with version 3.1 based on team: None------------------------")

        # Choose DotNet
        try:
            DotNet = self.driver.find_element(By.XPATH, Locator.DotNet)
            if DotNet.is_displayed():
                DotNet.click()
                self.driver.implicitly_wait(10)
                time.sleep(3)
                print("DotNet button is enable")
            else:
                print("DotNet button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DotNet')

        # Put Application Name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys('test-dot-none-01')
                time.sleep(1)
                print("ApplicationName_box is enable")
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully input ApplicationName')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 100")
        print("Scroll down")
        time.sleep(2)

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                time.sleep(3)
                print("Choose_Namespace_one is selected")
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
                time.sleep(2)
                print("Save button is enable")

            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save_button')

        # take action's screenshot
        ss = SS(driver)
        file_name = ss_path + "DotNet_01_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
        #
        # # click on Create application button
        # # try:
        # #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        # #     if Create_Application.is_enabled():
        # #         Create_Application.click()
        #           time.sleep(180)
        # #         print("Create application button is enable")
        # #
        # #     else:
        # #         print("Create application button is not enable")
        # # except NoSuchElementException as e:
        # #     print("NoSuchElementException error", e)
        # # else:
        # #     print('Successfully clicked on Create application')

    def test_dot_none_02(self):
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

        # ****************** Create Dotnet Application with dotnet version 3.0 based on None*******************
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

        print("----------------------Create DotNet app with version 3.0-----------------------------------")

        # Choose DotNet
        try:
            DotNet = self.driver.find_element(By.XPATH, Locator.DotNet)
            if DotNet.is_displayed():
                DotNet.click()
                self.driver.implicitly_wait(10)
                time.sleep(3)
                print("DotNet button is enable")
            else:
                print("DotNet button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DotNet')

        # Put Application Name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys('test44')
                time.sleep(1)
                print("ApplicationName_box is enable")
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully input ApplicationName')

        # click on dotnet version box to show all versions
        try:
            DoNet_v_box = driver.find_element(By.XPATH, Locator.DoNet_v_box)
            if DoNet_v_box.is_enabled():
                DoNet_v_box.click()
                time.sleep(1)
                print("DoNet_v_box is enable")
            else:
                print("DoNet_v_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on DoNet_v_box')

        # Choose DontNet version 3.0
        try:
            DontNet_V_3_0 = driver.find_element(By.XPATH, Locator.DontNet_V_3_0)
            if DontNet_V_3_0.is_enabled():
                DontNet_V_3_0.click()
                time.sleep(1)
                print("DontNet_V_3_0 is enable")
            else:
                print("DotNet Version 3.0 is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DontNet_V_3_0')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 100")
        print("Scroll down")
        time.sleep(2)
        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                time.sleep(3)
                print("Choose_Namespace_one is selected")
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
                time.sleep(2)
                print("Save button is enable")

            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save_button')

        # take action's screenshot
        ss = SS(driver)
        file_name = ss_path + "DotNet_02_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
        #
        # # click on Create application button
        # # try:
        # #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        # #     if Create_Application.is_enabled():
        # #         Create_Application.click()
        #           time.sleep(180)
        # #         print("Create application button is enable")
        # #
        # #     else:
        # #         print("Create application button is not enable")
        # # except NoSuchElementException as e:
        # #     print("NoSuchElementException error", e)
        # # else:
        # #     print('Successfully clicked on Create application')

    def test_dot_none_03(self):
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

        # *************************** Create Dotnet Application with dotnet version 2.2 ***************************
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                CreateNew_H.click()
                time.sleep(2)
                print("CreateNew_H button is clickable")
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
        print("\n----------------------Create DotNet app with version 2.0-----------------------------------\n")
        # Choose DotNet
        try:
            DotNet = self.driver.find_element(By.XPATH, Locator.DotNet)
            if DotNet.is_displayed():
                DotNet.click()
                self.driver.implicitly_wait(10)
                time.sleep(3)
                print("DotNet button is enable")
            else:
                print("DotNet button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DotNet')

        # Put Application Name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys('test44')
                time.sleep(1)
                print("ApplicationName_box is enable")
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully input ApplicationName')

        # click on dotnet version box to show all versions
        try:
            DoNet_v_box = driver.find_element(By.XPATH, Locator.DoNet_v_box)
            if DoNet_v_box.is_enabled():
                DoNet_v_box.click()
                time.sleep(1)
                print("DoNet_v_box is enable")
            else:
                print("DoNet_v_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on DoNet_v_box')

        # Choose DontNet version 3.0
        try:
            DotNet_V_2_2 = driver.find_element(By.XPATH, Locator.DotNet_V_2_2)
            if DotNet_V_2_2.is_enabled():
                DotNet_V_2_2.click()
                time.sleep(1)
                print("DotNet_V_2_2 is enable")
            else:
                print("DontNet Version 2.2 is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DotNet version 2.2')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 100")
        print("Scroll down")
        time.sleep(2)

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                time.sleep(3)
                print("Choose_Namespace_one is selected")
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
                time.sleep(2)
                print("Save button is enable")

            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save_button')

        # take action's screenshot
        ss = SS(driver)
        file_name = ss_path + "test_dot_default_03_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
        #
        # # click on Create application button
        # # try:
        # #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        # #     if Create_Application.is_enabled():
        # #         Create_Application.click()
        #           time.sleep(180)
        # #         print("Create application button is enable")
        # #
        # #     else:
        # #         print("Create application button is not enable")
        # # except NoSuchElementException as e:
        # #     print("NoSuchElementException error", e)
        # # else:
        # #     print('Successfully clicked on Create application')

    def test_dot_none_04(self):
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

        # *************************** Create Dotnet Application with dotnet version 2.2 ***************************
        # click on create button from header
        try:
            CreateNew_H = self.driver.find_element(By.XPATH, Locator.CreateNew_H)
            if CreateNew_H.is_enabled():
                CreateNew_H.click()
                time.sleep(2)
                print("CreateNew_H button is clickable")
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
        print("\n----------------------Create DotNet app with version 2.0-----------------------------------\n")
        # Choose DotNet
        try:
            DotNet = self.driver.find_element(By.XPATH, Locator.DotNet)
            if DotNet.is_displayed():
                DotNet.click()
                self.driver.implicitly_wait(10)
                time.sleep(3)
                print("DotNet button is enable")
            else:
                print("DotNet button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DotNet')

        # Put Application Name
        try:
            ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
            if ApplicationName_box.is_enabled():
                ApplicationName_box.send_keys('test44')
                time.sleep(1)
                print("ApplicationName_box is enable")
            else:
                print("ApplicationName_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully input ApplicationName')

        # click on dotnet version box to show all versions
        try:
            DoNet_v_box = driver.find_element(By.XPATH, Locator.DoNet_v_box)
            if DoNet_v_box.is_enabled():
                DoNet_v_box.click()
                time.sleep(1)
                print("DoNet_v_box is enable")
            else:
                print("DoNet_v_box is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on DoNet_v_box')

        # Choose DontNet version 3.0
        try:
            DotNet_V_2_1 = driver.find_element(By.XPATH, Locator.DotNet_V_2_1)
            if DotNet_V_2_1.is_enabled():
                DotNet_V_2_1.click()
                time.sleep(1)
                print("DotNet_V_2_1 is enable")
            else:
                print("DontNet Version 2.1 is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose DotNet version 2.1')

        # scroll down
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 100")
        print("Scroll down")
        time.sleep(2)

        #  click next button
        try:
            Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
            if Next_button.is_enabled():
                Next_button.click()
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                self.driver.implicitly_wait(5)
                time.sleep(2)
                print("Next_button is enable")
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
                time.sleep(3)
                print("Choose_Namespace_one is selected")
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
                time.sleep(2)
                print("Save button is enable")

            else:
                print("Save button is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on Save_button')

        # take action's screenshot
        ss = SS(driver)
        file_name = ss_path + "test_dot_default_03_scrrenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
        #
        # # click on Create application button
        # # try:
        # #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        # #     if Create_Application.is_enabled():
        # #         Create_Application.click()
        #           time.sleep(180)
        # #         print("Create application button is enable")
        # #
        # #     else:
        # #         print("Create application button is not enable")
        # # except NoSuchElementException as e:
        # #     print("NoSuchElementException error", e)
        # # else:
        # #     print('Successfully clicked on Create application')
