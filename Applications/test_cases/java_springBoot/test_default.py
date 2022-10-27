import time

from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

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

        app = CreateApplicationPage(driver)
        # choose spring boot
        if app.SpringBoot.is_enabled():
            app.SpringBoot.click()
            print("spring boot button is enable")
            driver.implicitly_wait(10)
            time.sleep(2)
        else:
            print("spring boot button is not enable")
            # self.driver.find_element(By.XPATH, "//mat-tab-body/div[1]/div[1]/div[1]").click()

        # put application name
        if app.ApplicationName_box.is_enabled():
            app.ApplicationName_box.click()
            print("ApplicationName_box is enable")
            driver.implicitly_wait(10)
            time.sleep(2)
        else:
            print("ApplicationName_box is not enable")
            # self.driver.find_element(By.XPATH, "//mat-tab-body/div[1]/div[1]/div[1]").click()

        # Click next button

        if app.Next_button.is_enabled():
            app.Next_button.click()
            print("Next button is enable")
            driver.implicitly_wait(10)
            time.sleep(2)
        else:
            print("Next button is not enable")
            # self.driver.find_element(By.XPATH, "//mat-tab-body/div[1]/div[1]/div[1]").click()
        # Again click next button
        self.driver.find_element(By.XPATH,
                                 "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/div[3]/button[2]").click()
        print("Next button is enable")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        self.driver.find_element(By.XPATH,
                                 "//mat-tab-body/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/div[1]").click()
        print("Namespace is enable")
        time.sleep(2)

        # click on save button
        self.driver.find_element(By.XPATH,
                                 "//body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[2]/kc-application-resource-selection-form[1]/div[1]/form[1]/div[7]/div[1]/button[2]").click()
        print("Save button is enable")
        time.sleep(5)

        # click on Create application button

        # self.driver.find_element(By.XPATH, "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/form/div[3]/button[2]").click()
        print("Create application is enable")
