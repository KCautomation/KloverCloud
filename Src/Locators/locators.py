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
    New_Application_H = "//span[contains(text(),'New Application')]"

    # Create Application page

    SpringBoot = "//span[contains(text(),'Spring Boot')]"
    ApplicationName_box = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    Next_button = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/div[3]/button[2]"

    Choose_Namespace_one = "//mat-tab-body/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/div[1]"
    Save_button_A = "//body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[2]/kc-application-resource-selection-form[1]/div[1]/form[1]/div[7]/div[1]/button[2]"
    Create_Application = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/form/div[3]/button[2]"
