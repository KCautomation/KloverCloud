import time

from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from Src.Locators.locators import Locator

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.Page_object_model.pom_createPage import CreatePage
from Src.Page_object_model.pom_dashboardPage import DashboardPage
from Src.Page_object_model.pom_Header import Header
from Src.Page_object_model.pom_ApplicationPage import CreateApplicationPage
from NameSpace.screenShots.screen_shots import SS

from Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *


class TestCreateJava(EnvironmentSetup):

    def test1(self):
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

        if log.Email_box.is_enabled():
            print("Email box is enabled")
            log.Email_box.send_keys('admin@klovercloud.com')
            time.sleep(2)
        else:
            print("Password box is not enable")
            time.sleep(2)

        # input password
        if log.Password_box.is_enabled():
            print("Password box is enabled")
            log.Password_box.send_keys('Hello@1234')
            time.sleep(2)
        else:
            print("Password box is not enable")

        # To show password
        if log.Toggle_Visibility_Button.is_enabled():
            print("Toggle Visibility Button is enabled")
            log.Toggle_Visibility_Button.click()
            time.sleep(1)
            # To hide password
            log.Toggle_Visibility_Button.click()
            time.sleep(1)

        else:
            print("Toggle Visibility Button is not enable")

        # Click On SignIn button
        if log.Sign_In_button.is_enabled():
            print("Sign In button is clickable")
            log.Sign_In_button.click()
            self.driver.implicitly_wait(30)
            time.sleep(8)
        else:
            print("Sign In button is not clickable")
            time.sleep(5)

        # ************************************************ Create Application ***********************************
        # click on create button from header

        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]").click()
        time.sleep(2)

        # click on "New Application" button from dropdown
        self.driver.find_element(By.XPATH, "//span[contains(text(),'New Application')]").click()
        print("New Application button is enable")
        driver.implicitly_wait(10)
        time.sleep(4)

        # choose spring boot
        # app = CreateApplicationPage(self.driver)
        SpringBoot = self.driver.find_element(By.XPATH, Locator.SpringBoot)
        if SpringBoot.is_enabled():
            SpringBoot.click()
            print("spring boot button is enable")
            driver.implicitly_wait(5)
            time.sleep(2)
        else:
            print("spring boot button is not enable")
        time.sleep(1)

        # put application name
        ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
        if ApplicationName_box.is_enabled():
            ApplicationName_box.send_keys('test44')
            print("ApplicationName_box is enable")
            time.sleep(2)
        else:
            print("ApplicationName_box is not enable")

        # Click next button
        Next_button = self.driver.find_element(By.XPATH, Locator.Next_button)
        if Next_button.is_enabled():
            Next_button.click()
            print("Next button is enable")
            time.sleep(3)
        else:
            print("Next button is not enable")

        # Again click next button
        Next_button_two = self.driver.find_element(By.XPATH, Locator.Next_button)
        if Next_button_two.is_enabled():
            Next_button_two.click()
            print("Next button is enable")
            time.sleep(5)
        else:
            print("Next button is not enable")

        # Choose A Namespace for Prod Environment
        Choose_Namespace_one = self.driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
        if Choose_Namespace_one.is_enabled():
            Choose_Namespace_one.click()
            print("Namespace is selected")
            time.sleep(5)
        else:
            print("Namespace is not enable")

        # click on save button
        Save_button = self.driver.find_element(By.XPATH, Locator.Save_button_A)
        if Save_button.is_enabled():
            Save_button.click()
            print("Save button is enable")
            time.sleep(2)
        else:
            print("Save button is not enable")
        time.sleep(2)

        # click on Create application button
        Create_Application = self.driver.find_element(By.XPATH, Locator.Create_Application)
        if Create_Application.is_enabled():
            Create_Application.click()
            print("Create application button is enable")
            time.sleep(180)

