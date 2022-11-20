import pickle
import time
from telnetlib import EC
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.Locators.locators import Locator

from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.login_fun import test_cluster_login

ss_path = "/Applications/PHP/"


class TestDeploy(EnvironmentSetup):
    def test_deploy(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        action = ActionChains(driver)
        # ApplicationName = input("Enter Application Name: ")
        ApplicationName = 'j-23'
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        try:
            pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb"))  # writing in pickle file
            print('Cookie file successfully created.')
        except Exception as e:
            print(e)

    def LoadCookie(self):
        driver = self.driver
        pageUrl = "https://eks.alpha.klovercloud.io/dashboard"

        driver.get("https://www.codespeedy.com/")  # opening the url
        try:
            cookie = pickle.load(open("cookie.pkl", "rb"))  # loading from pickle file
            for i in cookie:
                driver.add_cookie(i)
            print('Cookies added.')
        except Exception as e:
            print(e)
        time.sleep(3)
        driver.get("https://eks.alpha.klovercloud.io/dashboard")
        time.sleep(5)

    if __name__ == "__main__":
        LoadCookie()  # call the function

    # driver.get(pageUrl)
    # time.sleep(2)
    # cookies = pickle.load(open("cookies.pkl", "rb"))
    # print("\n", cookies, "\n")
    # for cookie in cookies:
    #     try:
    #         driver.add_cookie(cookie)
    #     except Exception as e:
    #         print(e)
    #
    # driver.get("https://eks.alpha.klovercloud.io/dashboard")
    # time.sleep(30)
