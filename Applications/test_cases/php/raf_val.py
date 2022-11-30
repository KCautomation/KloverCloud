import time
from telnetlib import EC
import pytest
import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.function.logIn.login_fun import test_cluster_login

ss_path = "/Applications/PHP/"


class TestCreateAppPHP:

    def test_Laravel_default_01(self, setup):
        self.driver = setup
        # pytest.skip("Skipping test...later I will implement...")
        # action = ActionChains(self.driver)
        # driver = self.driver
        ApplicationName = "laravel-0134"
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        self.driver.get("https://eks.alpha.klovercloud.io/namespace")
        self.elem = self.driver.find_element(By.XPATH, "//body/div[@id='main']/div[3]/div[1]/div[1]/a[3]")
        self.elem.send_keys(Keys.PAGE_DOWN)

        time.sleep(10)
