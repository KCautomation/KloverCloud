from selenium.webdriver.common.by import By
from Src.Locators.locators import Locator


class DashboardPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.Dashboard_title = driver.find_element(By.XPATH, Locator.Dashboard_title)

    def get_Dashboard_title(self):
        return self.Dashboard_title
