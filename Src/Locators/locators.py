class Locator(object):
    # LogIn Page
    Email_box = "//input[@id='mat-input-0']"  # xpath
    Password_box = "//input[@id='mat-input-1']"  # xpath
    Toggle_Visibility_Button = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                               "4]/button "  # xpath
    Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"

    # Dashboard page
    Namespace_button_from_SideBar = "//span[contains(text(),'Namespace')]"  # XPATH
    Dashboard_title = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/h1"

    # header frame
    CreateNew_H = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/button[2]"  # XPATH
    Namespace_H = "button[role='menuitem']"  # xpath
