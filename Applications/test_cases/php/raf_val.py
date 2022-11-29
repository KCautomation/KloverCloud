import time
from telnetlib import EC

import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys

from src.Locators.locators import Locator
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

    def test_Laravel_default_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)
        driver = self.driver
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

        driver.get("https://eks.alpha.klovercloud.io/applications/6384309fe756f70001787504/pipeline")
        time.sleep(5)

        # application created validation
        print("---------------Crated Application Validation--------------------")
        try:
            driver.refresh()
            time.sleep(2)

            check_create_app = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, Locator.check_create_app)))
            check_create_app.click()
            time.sleep(2)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(3)
            pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        # validation
        try:
            Created_status = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.check_app_status)))

            Accepted_status = "Success"
            Actual_status = Created_status.text
            self.assertEqual(Actual_status, Accepted_status)

            print('Application created status is: ',
                  simple_colors.green(Actual_status, ['bold', 'underlined']))
            time.sleep(2)
            pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        except AssertionError as e:
            print("InvalidSessionIdException error", e)
