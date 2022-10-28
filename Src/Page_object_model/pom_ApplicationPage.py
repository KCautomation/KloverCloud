from selenium.webdriver.common.by import By
from Src.Locators.locators import Locator


class CreateApplicationPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.SpringBoot = driver.find_element(By.XPATH, Locator.SpringBoot)
        self.ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
        self.Next_button = driver.find_element(By.XPATH, Locator.Next_button)
        self.Choose_Namespace_one = driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
        self.Save_button_A = driver.find_element(By.XPATH, Locator.Save_button_A)
        self.Create_Application = driver.find_element(By.XPATH, Locator.Create_Application)

    def get_SpringBoot(self):
        return self.SpringBoot

    def get_ApplicationName_box(self):
        return self.ApplicationName_box

    def get_Next_button(self):
        return self.Next_button

    def get_Choose_Namespace(self):
        return self.Choose_Namespace_one

    def get_Save_button_A(self):
        return self.Save_button_A

    def get_Create_Application(self):
        return self.Create_Application





