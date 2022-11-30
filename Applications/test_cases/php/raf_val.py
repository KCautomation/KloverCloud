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

        self.driver.get("https://eks.alpha.klovercloud.io/namespace")
        time.sleep(5)
        self.elem = self.driver.find_element(By.XPATH, "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/main/kc-vpc-list/div/div[2]/div[2]/button[10]/span/div/div[1]/div[1]/div/span")
        self.elem.send_keys(Keys.PAGE_DOWN)

        time.sleep(10)
