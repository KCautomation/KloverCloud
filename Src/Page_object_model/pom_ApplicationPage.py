from selenium.webdriver.common.by import By
from Src.Locators.locators import Locator


class CreateApplicationPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.SpringBoot = driver.find_element(By.XPATH, Locator.SpringBoot)
        self.ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
        self.Next_button = driver.find_element(By.XPATH, Locator.Next_button)

    def get_SpringBoot(self):
        return self.SpringBoot

    def get_ApplicationName_box(self):
        return self.ApplicationName_box

    def get_Next_button(self):
        return self.Next_button





