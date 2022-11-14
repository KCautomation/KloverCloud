import time

from selenium.webdriver.common.by import By

from src import LogInPage

from src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *


class CreateWithCompany(EnvironmentSetup):

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
        # input email
        log = LogInPage(driver)
        if log.Email_box.is_enabled():
            print("Email box is enabled")
            log.Email_box.send_keys('admin@klovercloud.com')
            time.sleep(2)
        else:
            print("Password box is not enable")
            time.sleep(2)
        # driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("admin@klovercloud.com")
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
            self.driver.implicitly_wait(20)
            time.sleep(10)
        else:
            print("Sign In button is not clickable")

        status = self.driver.find_element(By.XPATH,
                                          "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/h1").is_displayed()
        if status == True:
            assert True
            print("Wellcome to Dashboard")
        else:
            assert False
        """
        act_title = self.driver.title
        print(act_title)
        if act_title == "KloverCloud | Dashboard":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

        """
