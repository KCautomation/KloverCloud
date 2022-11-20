import pytest
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException

from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.login_fun import test_cluster_login


class TestCreateAppPHP(EnvironmentSetup):

    def test_Laravel_default_01(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        ApplicationName = "laravel-20"
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

    def test_Laravel_default_02(self):
        pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        ApplicationName = "laravel-20"
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

    def test_Laravel_default_03(self):
        # pytest.skip("Skipping test...later I will implement...")
        driver = self.driver
        ApplicationName = "laravel-20"
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
