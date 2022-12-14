import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
# from webdrivermanager.chrome import ChromeDriverManager


class EnvironmentSetup(unittest.TestCase):

    # setUP contains the browser setup attributes
    def setUp(self):
        # self.driver = webdriver.Chrome()
        # if you need solve version issues
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Run Started at :" + str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    # tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if (self.driver != None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            # self.driver.stop()
            # # self.driver.close()
            # # self.driver.quit()
