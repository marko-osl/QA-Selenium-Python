import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Tests import OpenSite

class UserSignUp(OpenSite.OpenSiteWithHighlandTheme):

    def correctlySignUp(self, driver, ranEmail, ranPhone):
        # ranEmail = super().randomEmail()
        # ranPhone = super().randomPhone()
        print("Correctly signup new user to the site")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlySignUp.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            registerButton = driver.find_element(By.CSS_SELECTOR, ".pl_header-content .pl_register_lead_link" )
            registerButton.click();
            firstName = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .reg_form_first_name  input[name="first_name"]')
            firstName.send_keys("Marek")
            lastName = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .reg_form_last_name  input[name="last_name"]')
            lastName.send_keys("Oslizlo")
            emailAddress = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .reg_form_email  input[name="email"]')
            emailAddress.send_keys(ranEmail)
            password = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .reg_form_pass input[name="password"]')
            password.send_keys(ranPhone)
            password = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .reg_form_confirm_pass input[name="confirm"]')
            password.send_keys(ranPhone)
            signUpButton = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Register"]')
            signUpButton.click()
            time.sleep(3)
            if (driver.find_element(By.CSS_SELECTOR, '.pl_lead_profile_link')):
                print("SignUp new User ---- OK")
                driver.close()
            else:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def signUpExistingAccount(self, ranEmail, ranPhone):
        print("Trying register existing account already")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.signUpExistingAccount.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get(super().baseURL)
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot(super().screenShotsFolder() + "/%s" % screen_name)
            exit();

        registerButton = driver.find_element(By.CSS_SELECTOR, ".pl_header-content .pl_register_lead_link")
        registerButton.click();
        firstName = driver.find_element(By.CSS_SELECTOR,
                                        '.pl_wrapper--open .js-form-content .reg_form_first_name  input[name="first_name"]')
        firstName.send_keys("Marek")
        lastName = driver.find_element(By.CSS_SELECTOR,
                                       '.pl_wrapper--open .js-form-content .reg_form_last_name  input[name="last_name"]')
        lastName.send_keys("Oslizlo")
        emailAddress = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .reg_form_email  input[name="email"]')
        emailAddress.send_keys("tewrRe@test.pl")
        password = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .reg_form_pass input[name="password"]')
        password.send_keys(ranPhone)
        password = driver.find_element(By.CSS_SELECTOR,
                                       '.pl_wrapper--open .reg_form_confirm_pass input[name="confirm"]')
        password.send_keys(ranPhone)
        signUpButton = driver.find_element(By.CSS_SELECTOR,
                                           '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Register"]')
        signUpButton.click()
        time.sleep(1)
        try:
            if (driver.find_element(By.XPATH, "//p[contains(text(),'This email is already in use.')]") is not None):
                print("SignUp new User ---- OK")
                driver.close()
        except:
            driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
            print("Wyjście awaryjne z programu")
            exit()