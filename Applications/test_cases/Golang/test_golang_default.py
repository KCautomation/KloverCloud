import time

import pytest
from selenium.webdriver.common.by import By
from src import Locator

from src import LogInPage
from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen
from urllib.error import *

ss_path = "/Applications/GoLang/"


class TestCreateGolangAppDefault(EnvironmentSetup):

    def test_golang_default_01(self):
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
                time.sleep(2)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

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
                ApplicationName_box.send_keys("testGo")
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
        try:
            TeamBox_A = driver.find_element(By.XPATH, Locator.TeamBox_A)
            if TeamBox_A.is_enabled():
                TeamBox_A.click()
                time.sleep(1)
                print("TeamBox_A is enable")
            else:
                print("TeamBox_A is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on TeamBox')

        # Choose Default from team
        try:
            Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
            if Team_Default.is_displayed():
                Team_Default.click()
                time.sleep(2)
                print("Team_Default is displayed")
            else:
                print("Team_Default is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Team_Default')

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
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         Create_Application.click()
        #         print("Create application button is enable")
        #         time.sleep(180)
        #     else:
        #         print("Create application button is not enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create application')

    def test_golang_default_02(self):
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
                time.sleep(2)
            else:
                print("Sign In button is not clickable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully logged in')

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
                ApplicationName_box.send_keys("testGo")
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
            print('Successfully chose on Goecho_V_4_1_14')

        # Click On Team box
        try:
            TeamBox_A = driver.find_element(By.XPATH, Locator.TeamBox_A)
            if TeamBox_A.is_enabled():
                TeamBox_A.click()
                time.sleep(1)
                print("TeamBox_A is enable")
            else:
                print("TeamBox_A is not enable")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully clicked on TeamBox')

        # Choose Default from team
        try:
            Team_Default = self.driver.find_element(By.XPATH, Locator.Team_Default)
            if Team_Default.is_displayed():
                Team_Default.click()
                time.sleep(2)
                print("Team_Default is displayed")
            else:
                print("Team_Default is not displayed")
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully chose on Team_Default')

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
        # try:
        #     Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        #     if Create_Application.is_enabled():
        #         Create_Application.click()
        #         print("Create application button is enable")
        #         time.sleep(180)
        #     else:
        #         print("Create application button is not enable")
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # else:
        #     print('Successfully clicked on Create application')
