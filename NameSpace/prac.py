import time
import unittest
import urllib.request
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from NameSpace.Src.Page_object_model.pom_createPage import CreatePage

from NameSpace.Src.base.environment_setup import EnvironmentSetup
from urllib.request import urlopen
from urllib.error import *


class NamespaceCreateWithCompany(EnvironmentSetup):

    def test1(self):

        pageUrl = "https://www.google.com/"
        driver = self.driver

        # try block to read URL
        try:
            html = urlopen(pageUrl)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print("HTTP error", e)

        except URLError as e:
            print("Opps ! Page not found!", e)

        else:
            print('Yeah ! Url found ')
            self.driver.get(pageUrl)
            self.driver.implicitly_wait(20)
            time.sleep(2)

            self.driver.find_element(By.XPATH,
                                     "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(
                "test", Keys.ENTER)
            time.sleep(5)

            print(urllib.request.urlopen("https://www.stackoverflow.com").getcode())
