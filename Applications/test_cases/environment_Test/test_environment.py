import time

from selenium.webdriver.common.by import By
from Src.Locators.locators import Locator

from Src.screen_shots.screen_shots import SS
from Src.base.environment_setup import EnvironmentSetup
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen
from urllib.error import *
from Src.logIn.test_login import TestLogIn
ss_path = "/Applications/GoLang/"


class TestCreateGolang(EnvironmentSetup):

    def test_Golang(self):
        # ******************************Login**********************************
        try:
            self.login = TestLogIn()
            pageUrl = "https://eks.rakibefstestmaincluster782.klovercloud.io/"
            username = "admin@klovercloud.com"
            password = "Hello@1234"
            self.login.cluster_login(pageUrl, username, password)
            self.driver.close()
        except AttributeError:
            pass
