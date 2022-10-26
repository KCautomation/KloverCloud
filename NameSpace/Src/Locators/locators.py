class Locator(object):
    # LogIn Page
    Email_box = "//input[@id='mat-input-0']"  # xpath
    Password_box = "//input[@id='mat-input-1']"  # xpath
    Toggle_Visibility_Button = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                               "4]/button "  # xpath
    Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"

    # Dashboard page
    Namespace_button_from_SideBar = "//span[contains(text(),'Namespace')]"  # XPATH

    # header frame
    CreateNew_button_from_header = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/kc-toolbar[1]/div[1]/button[2]/span[1]" # XPATH

