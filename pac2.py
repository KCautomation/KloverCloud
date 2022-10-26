import time
from telnetlib import EC

from _pytest import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Src.base.environment_setup import EnvironmentSetup


class NamespaceCreationOnCompany(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(pageUrl)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)

