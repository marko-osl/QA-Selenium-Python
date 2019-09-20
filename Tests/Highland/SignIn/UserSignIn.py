import time
from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
from Variables.Sites import Highland as v


class UserSignIn(OpenSite.OpenSiteWithHighlandTheme):

    def correctlySignIn(self, driver, ranEmail, ranPhone):

        print("Correctly signin as a user on the site")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlySignIn.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            driver.get(super().baseURL)
            loginButton = driver.find_element(By.XPATH, v.loginButton)
            loginButton.click();
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.loginEmailInput)
            emailAddress.send_keys(ranEmail)
            password = driver.find_element(By.CSS_SELECTOR, v.loginPasswordInput)
            password.send_keys(ranPhone)
            signInButton = driver.find_element(By.CSS_SELECTOR, v.loginSignInButton)
            signInButton.click()
            time.sleep(3)
            if (driver.find_element(By.CSS_SELECTOR, v.loginVerifyHandle)):
                print("SignUp new User ---- OK")
                driver.refresh()
            else:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def signInToNotExistingAccount(self, driver, ranPhone):
        print("Trying login to not existing account already")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.signInToNotExistingAccount.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            loginButton = driver.find_element(By.XPATH, v.loginButton)
            loginButton.click();
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.loginEmailInput)
            emailAddress.send_keys(v.wrongEmail)
            password = driver.find_element(By.CSS_SELECTOR, v.loginPasswordInput)
            password.send_keys(ranPhone)
            signInButton = driver.find_element(By.CSS_SELECTOR, v.loginSignInButton)
            signInButton.click()
            time.sleep(3)
            try:
                if (driver.find_element(By.CSS_SELECTOR, v.loginNotExistingAccountMessage) is not None):
                    print(str(self.signInToNotExistingAccount.__name__), " ---- OK")
                    driver.close()
            except:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def signInEmptyForm(self, driver):
        print("Trying send empty register form")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.signInEmptyForm.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            loginButton = driver.find_element(By.XPATH, v.loginButton)
            loginButton.click();
            signInButton = driver.find_element(By.CSS_SELECTOR, v.loginSignInButton)
            signInButton.click()

            try:
                if (driver.find_element(By.CSS_SELECTOR, v.loginPasswordEmptyMessage) is not None):
                    if (driver.find_element(By.CSS_SELECTOR, v.loginEmailEmptyMessage) is not None):
                        print(str(self.signInEmptyForm.__name__), "---- OK")
                        driver.close()
                        
            except:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()