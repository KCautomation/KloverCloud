from selenium.webdriver.common.by import By
from src.Locators.locators import Locator


class CreateApplicationPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.Email_box = driver.find_element(By.XPATH, Locator.Email_box)
        self.Password_box = driver.find_element(By.XPATH, Locator.Password_box)
        self.Toggle_Visibility_Button = driver.find_element(By.XPATH, Locator.Toggle_Visibility_Button)
        self.Sign_In_button = driver.find_element(By.XPATH, Locator.Sign_In_button)

        self.CreateNew_H = driver.find_element(By.XPATH, Locator.CreateNew_H)
        self.NewApplication_H = driver.find_element(By.XPATH, Locator.NewApplication_H)

        self.SpringBoot = driver.find_element(By.XPATH, Locator.SpringBoot)
        self.ApplicationName_box = driver.find_element(By.XPATH, Locator.ApplicationName_box)
        self.Next_button = driver.find_element(By.XPATH, Locator.Next_button)
        self.Choose_Namespace_one = driver.find_element(By.XPATH, Locator.Choose_Namespace_one)
        self.Save_button_A = driver.find_element(By.XPATH, Locator.Save_button_A)
        self.Create_Application = driver.find_element(By.XPATH, Locator.Create_Application)

    def get_email(self):
        return self.Email_box

    def get_Password(self):
        return self.Password_box

    def get_Toggle_Visibility_Button(self):
        return self.Password_box

    def get_Sign_In_button(self):
        return self.Sign_In_button

    def get_CreateNew_button_from_header(self):
        return self.CreateNew_H

    def get_CreateNew_H(self):
        return self.CreateNew_H

    def get_NewApplication_H(self):
        return self.NewApplication_H

    def get_SpringBoot(self):
        return self.SpringBoot

    def get_ApplicationName_box(self):
        return self.ApplicationName_box

    def get_Next_button(self):
        return self.Next_button

    def get_Choose_Namespace(self):
        return self.Choose_Namespace_one

    def get_Save_button_A(self):
        return self.Save_button_A

    def get_Create_Application(self):
        return self.Create_Application
