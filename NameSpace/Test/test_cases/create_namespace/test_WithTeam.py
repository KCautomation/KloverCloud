import time

from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.Page_object_model.pom_createPage import CreatePage
from Src.Page_object_model.pom_dashboardPage import DashboardPage
from Src.Page_object_model.pom_Header import Header

from Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *


class TestWithCompany(EnvironmentSetup):

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

        """ Create Namespace """

        # Click On Namespace From Side Navigation
        driver.find_element(By.XPATH, "//span[contains(text(),'Namespace')]").click()
        driver.implicitly_wait(10)
        time.sleep(6)

        # clcik on create button from header
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]").click()
        driver.implicitly_wait(10)
        time.sleep(4)

        # click namespace
        driver.find_element(By.CSS_SELECTOR, "button[role='menuitem']").click()
        driver.implicitly_wait(10)
        time.sleep(4)

        """
        # Choose cluster
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "1]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/img[1]").click()
        time.sleep(1)

        """
        # input Namespace name
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Namespace Name']").send_keys('test46')
        time.sleep(3)

        # driver.execute_script(window.scrollBy(0, 500))

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("Scroll down")
        time.sleep(4)

        # Choose Team from Access Group
        driver.find_element(By.XPATH,
                            "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]/span[1]/div[1]").click()
        time.sleep(2)

        # click on search button
        driver.find_element(By.XPATH,
                            "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]").click()
        time.sleep(2)

        # choose a team
        driver.find_element(By.XPATH, "//span[contains(text(),'default')]").click()
        time.sleep(2)

        # CPU selection
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input["
                                      "1]").send_keys(0)
        time.sleep(2)

        # Memory Selection
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input["
                                      "1]").send_keys(0)
        time.sleep(2)

        # Persistent Volume seloection
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input["
                                      "1]").send_keys(0)
        time.sleep(2)

        # Bandwidth selection
        driver.find_element(By.XPATH, "//div[contains(text(),'Moderate')]").click()
        time.sleep(2)

        # scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -550")
        print("Scroll down")
        time.sleep(4)
        print("Scroll success")

        # click create button for create
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "2]/div[1]/div[2]/button[1]").click()
        driver.implicitly_wait(10)
        time.sleep(5)