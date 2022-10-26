import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from NameSpace.Src.Page_object_model.pom_createPage import CreatePage

from NameSpace.Src.base.environment_setup import EnvironmentSetup


class NamespaceCreateWithCompany(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://eks.dev-66.klovercloud.io/auth/login"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        """ Login """
        call = CreatePage(driver)
        # input email
        if call.Email_box.is_enabled():
            print("Email box is enabled")
            call.Email_box.send_keys('admin@klovercloud.com')
            time.sleep(2)
        else:
            print("Password box is not enable")

        # input password

        if call.Password_box.is_enabled():
            print("Password box is enabled")
            call.Password_box.send_keys('Hello@1234')
            time.sleep(2)
        else:
            print("Password box is not enable")

        # To show password
        if call.Toggle_Visibility_Button.is_enabled():
            print("Toggle Visibility Button is enabled")
            call.Toggle_Visibility_Button.click()
            time.sleep(1)
            # To hide password
            call.Toggle_Visibility_Button.click()
            time.sleep(1)

        else:
            print("Toggle Visibility Button is not enable")

        # Click On SignIn button
        if call.Sign_In_button.is_enabled():
            print("Sign In button is clickable")
            call.Sign_In_button.click()
            time.sleep(10)
        else:
            print("Sign In button is not clickable")
