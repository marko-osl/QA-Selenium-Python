import time
from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
from Variables.Sites import Highland as v


class UserSignUp(OpenSite.OpenSiteWithHighlandTheme):

    def correctlySignUp(self, driver, ranEmail, ranPhone):
        print("Correctly signup new user to the site")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlySignUp.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            registerButton = driver.find_element(By.CSS_SELECTOR, v.registerButton )
            registerButton.click()
            firstName = driver.find_element(By.CSS_SELECTOR, v.registerFirstNameInput)
            firstName.send_keys(v.firstName)
            lastName = driver.find_element(By.CSS_SELECTOR, v.registerLastNameInput)
            lastName.send_keys(v.lastName)
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.registerEmailInput)
            emailAddress.send_keys(ranEmail)
            password = driver.find_element(By.CSS_SELECTOR, v.registerPasswordInput)
            password.send_keys(ranPhone)
            confirmPassword = driver.find_element(By.CSS_SELECTOR, v.registerConfirmPasswordInput)
            confirmPassword.send_keys(ranPhone)
            signUpButton = driver.find_element(By.CSS_SELECTOR, v.registerSignUpButton)
            signUpButton.click()
            time.sleep(3)
            if (driver.find_element(By.CSS_SELECTOR, ".pl_nav-wrapper .pl_lead_profile_link")):
                print("SignUp new User ---- OK")
            else:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def logOutUser(self, driver):
        print("Log out user")
        print("*" * 20)
        logOutButton = driver.find_element(By.CSS_SELECTOR, v.registerLogOutButton)
        logOutButton.click()


    def signUpExistingAccount(self,driver, ranEmail, ranPhone):
        print("Trying register existing account already")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.signUpExistingAccount.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            registerButton = driver.find_element(By.CSS_SELECTOR, v.registerButton)
            registerButton.click();
            firstName = driver.find_element(By.CSS_SELECTOR, v.registerFirstNameInput)
            firstName.send_keys(v.firstName)
            lastName = driver.find_element(By.CSS_SELECTOR, v.registerLastNameInput)
            lastName.send_keys(v.lastName)
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.registerEmailInput)
            emailAddress.send_keys(ranEmail)
            password = driver.find_element(By.CSS_SELECTOR, v.registerPasswordInput)
            password.send_keys(ranPhone)
            confirmPassword = driver.find_element(By.CSS_SELECTOR, v.registerConfirmPasswordInput)
            confirmPassword.send_keys(ranPhone)
            signUpButton = driver.find_element(By.CSS_SELECTOR, v.registerSignUpButton)
            signUpButton.click()
            time.sleep(3)
            try:
                if (driver.find_element(By.XPATH, v.registerEmailExistingMessage) is not None):
                    print(str(self.signUpExistingAccount.__name__), " ---- OK")
            except:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def signUpEmptyForm(self, driver):
        print("Trying send empty register form")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.signUpEmptyForm.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            driver.find_element(By.CSS_SELECTOR, v.registerFirstNameInput).clear()
            driver.find_element(By.CSS_SELECTOR, v.registerLastNameInput).clear()
            driver.find_element(By.CSS_SELECTOR, v.registerEmailInput).clear()
            driver.find_element(By.CSS_SELECTOR, v.registerPasswordInput).clear()
            driver.find_element(By.CSS_SELECTOR, v.registerConfirmPasswordInput).clear()
            signUpButton = driver.find_element(By.CSS_SELECTOR,v.registerSignUpButton)
            signUpButton.click()
            time.sleep(1)
            try:
                if (driver.find_element(By.XPATH, v.registerFirstNameWrongMessage)is not None):
                    if (driver.find_element(By.XPATH, v.registerLastNameWrongMessage)is not None):
                        if (driver.find_element(By.XPATH, v.registerEmailWrongMessage) is not None):
                            if (driver.find_element(By.XPATH, v.registerPasswordWrongMessage) is not None):
                                if (driver.find_element(By.XPATH,v.registerConfirmPasswordWrongMessage) is not None):
                                    print(str(self.signUpEmptyForm.__name__),  "---- OK")
                                    

            except:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                driver.close()
                exit()