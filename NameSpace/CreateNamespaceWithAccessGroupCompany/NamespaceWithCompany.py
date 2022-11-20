import time
from telnetlib import EC

from _pytest import unittest
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.Locators.locators import Locator

from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.login_fun import test_cluster_login
from src.function.go_createNamespace.namespace_create_page import go_create_namespace_page

ss_path = "/Applications/PHP/"


class TestNamespaceCreation(EnvironmentSetup):
    def Namespace_company(self):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test212"
        driver = self.driver
        action = ActionChains(driver)
        # ApplicationName = input("Enter Application Name: ")
        ApplicationName = 'j-23'
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to create Namespace page *********************")

        try:
            go_create_namespace_page(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        try:
            NamespaceName_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.NamespaceName_box)))
            NamespaceName_box.send_keys(Namespace_Name)
            print("Namespace name inputted successfully")
            time.sleep(1)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        action = ActionChains(driver)
        # click the item
        # # action.send_keys(Keys.PAGE_DOWN)
        # action.perform()
        # time.sleep(2)
        # scroll to element
        action.scroll_to_element(driver.find_element(By.XPATH, Locator.CPU_box))
        action.perform()
        time.sleep(2)
        # # input Namespace name
        # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Namespace Name']").send_keys('test44')
        # time.sleep(3)

        # driver.execute_script(window.scrollBy(0, 500))
        """
        #Scroll
        #driver.execute_script("window.scrollBy()0,500", "")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print("Scroll down")
        time.sleep(3)
        """

        # # scroll down to select Cpu,memory,volume,bandwidth
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        # print("Scroll down")
        # time.sleep(4)


        # # CPU selection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(0)
        # time.sleep(2)
        #
        # # Memory Selection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(2)
        # time.sleep(2)
        #
        # # Persistent Volume seloection
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "1]/div[4]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input["
        #                               "1]").send_keys(1)
        # time.sleep(2)
        #
        # # Bandwidth selection
        # driver.find_element(By.XPATH, "//div[contains(text(),'Moderate')]").click()
        # time.sleep(2)
        #
        # driver.execute_script("return document.body.scrollHeight")
        #
        # print("Scroll success")
        #
        # # driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        # time.sleep(2)
        #
        # # scroll
        # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -550")
        # print("Scroll down")
        # time.sleep(4)
        #
        # # click create button for create
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "2]/div[1]/div[2]/button[1]").click()
        # driver.implicitly_wait(10)
        # time.sleep(5)
