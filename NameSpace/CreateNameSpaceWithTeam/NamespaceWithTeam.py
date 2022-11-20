import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException, InvalidSessionIdException, NoSuchElementException
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.Locators.locators import Locator
from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.login_fun import test_cluster_login


class NamespaceCreationTeam(EnvironmentSetup):
    def test3(self):

        driver = self.driver
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        """ Create Namespace """

        # Click On Namespace From Side Navigation
        driver.find_element(By.XPATH, "//span[contains(text(),'Namespace')]").click()
        driver.implicitly_wait(10)
        time.sleep(6)

        # click on create button from header
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
        driver.find_element(By.CSS_SELECTOR, Locator.NamespaceName_box).send_keys('test46')
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

        # # click create button for create
        # driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
        #                               "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
        #                               "2]/div[1]/div[2]/button[1]").click()
        # driver.implicitly_wait(10)
        # time.sleep(5)


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
