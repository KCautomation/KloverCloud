import time
from telnetlib import EC

import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys

from src.Locators.locators import Locator
from src.function.deploy_validation.deploy_validation import test_deploy_validation
from src.function.go_application.go_to_application_page import go_create_app_page

from src.screen_shots.screen_shots import SS
from src.base.environment_setup import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.function.logIn.login_fun import test_cluster_login
from src.function.deploy_appication.deploy_app import test_deploy
from src.function.delete_app.delete_application import test_delete_app

ss_path = "/Applications/PHP/"


class TestCreateAppPHP(EnvironmentSetup):

    def test_Laravel_default_02(self):
        # pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
        ss = SS(driver)
        ApplicationName = "laravel-0170"
        print("****************** Try to Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go Create Application Page *********************")
        try:
            driver.refresh()
            time.sleep(3)
            go_create_app_page(self)

            WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, Locator.Laravel)))
            driver.refresh()
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        else:
            page = driver.title
            print(page)

        print("***************Create PHP application with PHP Version: 7.3 &  Laravel version : 6.0***************")

        print("----try to choose Laravel from below--------")
        try:
            Laravel = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, Locator.Laravel)))
            # driver.refresh()
            Laravel.click()
            driver.implicitly_wait(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully to chose Laravel")

        print("----Try to put application name--------")
        try:
            ApplicationName_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, Locator.ApplicationName_box)))
            if ApplicationName_box.is_displayed():
                print("ApplicationName_box is visible")
                ApplicationName_box.send_keys(ApplicationName)
                time.sleep(2)
                file_name = ss_path + "ApplicationName_box_" + time.asctime().replace(":", "_") + ".png"
                ApplicationName_box.screenshot('app.png')
            else:
                file_name = ss_path + "ApplicationName_box_" + time.asctime().replace(":", "_") + ".png"
                ApplicationName_box.screenshot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully to put application name")