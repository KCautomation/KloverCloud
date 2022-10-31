import time

from selenium.webdriver.common.by import By
from Src.Locators.locators import Locator

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.Page_object_model.pom_ApplicationPage import CreateApplicationPage
from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen
from urllib.error import *

ss_path = "/Applications/GoLang/"


class TestLogIn(EnvironmentSetup):

    def cluster_login(self, pageUrl, username, password):
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

        driver.get(pageUrl)
        driver.implicitly_wait(20)
        time.sleep(2)
        username_box = self.driver.find_element(By.XPATH, Locator.Email_box)
        username_box.send_keys(username)
        time.sleep(1)

        password_box = self.driver.find_element(By.XPATH, Locator.Password_box)
        password_box.send_keys(password)
        time.sleep(1)

        login_box = self.driver.find_element(By.XPATH, Locator.Sign_In_button)
        login_box.click()
        time.sleep(5)
        self.cluster_login(pageUrl, username, password)

    # def test1(self):
    #     pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
    #     username = "admin@klovercloud.com"
    #     password = "Hello@1234"
    #
    #     self.cluster_login(pageUrl, username, password)

    # # ******************************Login**********************************
    #
    # # page object
    # log = LogInPage(driver)  # LogIn page
    #
    # # input email
    # try:
    #     if log.Email_box.is_enabled():
    #         log.Email_box.send_keys('admin@klovercloud.com')
    #         print("Email box is enabled")
    #         time.sleep(1)
    #     else:
    #         print("Email box is not enabled")
    # except NoSuchElementException as e:
    #     print("NoSuchElementException error", e)
    #
    # else:
    #     print('Successfully inputted email')
    #
    # # input pass
    # try:
    #     if log.Password_box.is_enabled():
    #         log.Password_box.send_keys('Hello@1234')
    #         print("Password box is enabled")
    #         time.sleep(1)
    #     else:
    #         print("Password box is not enabled")
    # except NoSuchElementException as e:
    #     print("NoSuchElementException error", e)
    # else:
    #     print('Successfully inputted Password')
    #
    # # To show password
    # try:
    #     if log.Toggle_Visibility_Button.is_enabled():
    #         log.Toggle_Visibility_Button.click()
    #         time.sleep(1)
    #         log.Toggle_Visibility_Button.click()
    #         print("Password box is enabled")
    #         time.sleep(1)
    #     else:
    #         print("Password box is not enabled")
    # except NoSuchElementException as e:
    #     print("NoSuchElementException error", e)
    # else:
    #     print('Successfully showed & hided Password')
    #
    # # Click On SignIn button
    # try:
    #     if log.Sign_In_button.is_enabled():
    #         log.Sign_In_button.click()
    #         self.driver.implicitly_wait(10)
    #         time.sleep(5)
    #         print("Sign In button is clickable")
    #         time.sleep(2)
    #     else:
    #         print("Sign In button is not clickable")
    # except NoSuchElementException as e:
    #     print("NoSuchElementException error", e)
    # else:
    #     print('Successfully logged in')
