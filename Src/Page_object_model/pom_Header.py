from selenium.webdriver.common.by import By
from Src.Locators.locators import Locator


class Header(object):
    def __init__(self, driver):
        self.driver = driver

        self.CreateNew_button_from_header = driver.find_element(By.XPATH, Locator.CreateNew_button_from_header)
        self.Namespace_H = driver.find_element(By.XPATH, Locator.Namespace_H)

    def get_CreateNew_button_from_header(self):
        return self.CreateNew_button_from_header

    def get_Namespace_H(self):
        return self.Namespace_H
