from selenium.webdriver.common.by import By


class Namespace:

    def __init__(self, driver):
        self.driver = driver

        self.Email_box = driver.find_element(By.XPATH, "//input[@id='mat-input-0']")
        self.Password_box = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")
        self.Toggle_Visibility_Button = driver.find_element(By.XPATH,
                                                            "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[4]/button")
        self.Sign_In_button = driver.find_element(By.XPATH,
                                                  "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]")
        self.LogIn_Authentication_Error = driver.find_element(By.XPATH, "//body[1]/kc-toastr[1]/div[1]/div[1]")

    def get_email(self):
        return self.Email_box

    def get_Password(self):
        return self.Password_box

    def get_Toggle_Visibility_Button(self):
        return self.Password_box

    def get_Sign_In_button(self):
        return self.Sign_In_button

    def LogIn_Authentication_Error(self):
        return self.LogIn_Authentication_Error
