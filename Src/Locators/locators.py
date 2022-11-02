class Locator(object):
    # LogIn Page

    Email_box = "//input[@id='mat-input-0']"  # xpath
    Email_box_test = "//input[@id='mat-inpu-0']"  # xpath
    Password_box = "//input[@id='mat-input-1']"  # xpath
    Toggle_Visibility_Button = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                               "4]/button "  # xpath
    Sign_In_button = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"

    # Dashboard page
    Namespace_button_from_SideBar = "//span[contains(text(),'Namespace')]"  # XPATH
    Dashboard_title = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/h1"

    # header frame
    CreateNew_H = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/button[2]"  # XPATH
    CreateNew_H_test = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/buttn[2]"
    Namespace_H = "button[role='menuitem']"  # xpath
    NewApplication_H = "//span[contains(text(),'New Application')]"

    # Create Application page

    SpringBoot = "//span[contains(text(),'Spring Boot')]"
    SpringBoot_Version_box = "//mat-select[@id='mat-select-1']"
    SpringBoot_Version_2_1_11 = "//span[contains(text(),'2.1.11')]"  # XPATH
    Java_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]"
    Java_Version_11 = "//span[contains(text(),'11')]"
    Java_Version_8 = "//span[contains(text(),'8')]"

    JavaScript = "//span[contains(text(),'JavaScript')]"
    ExpressJS = "//mat-tab-body/div[1]/div[1]/div[2]"
    Express_Js_Version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # Xpath
    JS_V_4_17_1 = "//span[contains(text(),'4.17.1')]"

    Django = "//span[contains(text(),'Django')]"
    Python_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]"  # XPATH
    Python_version_3_7_8 = "//span[contains(text(),'3.7.8')]"  # XPATH
    Python_version_3_6_11 = "//span[contains(text(),'3.6.11')]"  # XPATH
    Django_version_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"  # XPATH
    Django_Version_2_2_14 = "//span[contains(text(),'2.2.14')]"  # XPATH


    DotNet = "//mat-tab-body/div[1]/div[1]/div[4]"
    DoNet_v_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[2]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[1]"
    DontNet_V_3_0 = "//span[contains(text(),'3.0')]"
    DotNet_V_2_2 = "//span[contains(text(),'2.2')]"
    DotNet_V_2_1 = "//span[contains(text(),'2.1')]"

    Laravel = "//mat-tab-body/div[1]/div[1]/div[5]"

    # Golang
    GoLang = "//mat-tab-body/div[1]/div[1]/div[6]"
    Goecho_box = "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[3]/div[1]/div[1]/div[3]"
    Goecho_V_4_1_14 = "//span[contains(text(),'4.1.14')]"

    ApplicationName_box = "/html[1]/body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]"
    TeamBox_A = "//*[@id='mat-select-2']"
    Team_Default = "//mat-option[@id='mat-option-1']"
    Next_button = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/div[3]/button[2]"

    Choose_Namespace_one = "//mat-tab-body/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]/div[1]"
    Save_button_A = "//body[1]/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-application-form[1]/div[1]/div[1]/kc-horizontal-stepper[1]/section[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[2]/kc-application-resource-selection-form[1]/div[1]/form[1]/div[7]/div[1]/button[2]"
    Create_Application = "//*[@id='msgContainer']/div/kc-horizontal-stepper/section/div/form/div[3]/button[2]"
