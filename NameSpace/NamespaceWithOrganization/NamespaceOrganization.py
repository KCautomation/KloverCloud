import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class NamespaceCreationOrganization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        pageUrl = "https://eks.hkmd7dff3.klovercloud.io/"
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(pageUrl)
        time.sleep(2)

        """ Login """

        # input email
        driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("admin@klovercloud.com")
        time.sleep(2)

        # input password
        driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("klovercloud")
        time.sleep(2)

        # click eye button to check password
        driver.find_element(By.XPATH,
                            "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/div[1]/mat-form-field[2]/div["
                            "1]/div[1]/div[4]/button[1]/span[1]/mat-icon[1]/*[1]").click()
        time.sleep(2)

        # again click on eye button to hide password
        driver.find_element(By.XPATH,
                            "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/div[1]/mat-form-field[2]/div["
                            "1]/div[1]/div[ "
                            "4]/button[1]/span[1]/mat-icon[1]/*[1]").click()
        time.sleep(2)

        # click on  SignUp
        driver.find_element(
            By.XPATH, "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]").click()
        driver.implicitly_wait(10)
        time.sleep(5)
        print("LogIn successfully ")

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
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Namespace Name']").send_keys('test45')
        time.sleep(3)

        # driver.execute_script(window.scrollBy(0, 500))

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("Scroll down")
        time.sleep(4)

        # Choose access organization from Access Group
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "1]/div[3]/div[1]/button[2]/span[1]/div[1]").click()
        time.sleep(2)

        # click search box and choose a organization
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "1]/div[3]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[4]").click()
        time.sleep(2)

        # Organization selection
        # driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/div[1]/mat-option[2]/div[1]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'default')]").click()
        time.sleep(4)

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

        # Scroll
        driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -550")
        print("Scroll up")
        time.sleep(4)

        # click create button for create
        driver.find_element(By.XPATH, "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container["
                                      "1]/mat-sidenav-content[1]/main[1]/kc-vpc-form[1]/div[1]/div[1]/div[1]/div["
                                      "2]/div[1]/div[2]/button[1]").click()
        driver.implicitly_wait(10)
        print("Create Successfully")
        time.sleep(5)


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
