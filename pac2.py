import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from Src.Locators.locators import Locator

from Src.Page_object_model.pom_loginPage import LogInPage
from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *

ss_path = "/Applications/GoLang/"


class TestCreateGolang(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.google.com/"
        try:
            if driver.title == expected_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, expected_title)
        except Exception as e:
            print(e + "WebPage Failed to load")
