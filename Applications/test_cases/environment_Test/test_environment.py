from src.base.environment_setup import EnvironmentSetup
from src.function.logIn.login_fun import TestLogIn
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
