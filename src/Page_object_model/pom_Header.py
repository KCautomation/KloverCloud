from selenium.webdriver.common.by import By
from src.Locators.locators import Locator


class Header(object):
    def __init__(self, driver):
        self.driver = driver

        self.CreateNew_H = driver.find_element(By.XPATH, Locator.CreateNew_H)
        self.Namespace_H = driver.find_element(By.XPATH, Locator.Namespace_H)
        self.NewApplication_H = driver.find_element(By.XPATH, Locator.NewApplication_H)

    def get_CreateNew_button_from_header(self):
        return self.CreateNew_H

    def get_CreateNew_H(self):
        return self.Namespace_H

    def get_NewApplication_H(self):
        return self.NewApplication_H


