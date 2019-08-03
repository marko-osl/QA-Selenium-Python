import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Tests.Highland import OpenSite


class UserSignIn(OpenSite.OpenSiteWithHighlandTheme):

    def correctlySignIn(self, driver, ranEmail, ranPhone):
        # ranEmail = super().randomEmail()
        # ranPhone = super().randomPhone()
        print("Correctly signin as a user on the site")
        print("*" * 20)
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            driver.get(super().baseURL)
            loginButton = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[3]/div[2]/a[1]' )
            loginButton.click();
            emailAddress = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .login-email  input[name="email"]')
            emailAddress.send_keys(ranEmail)
            password = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .login-password input[name="password"]')
            password.send_keys(ranPhone)
            signInButton = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Log In"]')
            signInButton.click()
            time.sleep(3)
            if (driver.find_element(By.CSS_SELECTOR, '.pl_lead_profile_link')):
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
            loginButton = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[3]/div[2]/a[1]')
            loginButton.click();
            emailAddress = driver.find_element(By.CSS_SELECTOR,
                                               '.pl_wrapper--open .js-form-content .login-email  input[name="email"]')
            emailAddress.send_keys('proba@proba.pl')
            password = driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .login-password input[name="password"]')
            password.send_keys(ranPhone)
            signInButton = driver.find_element(By.CSS_SELECTOR,
                                               '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Log In"]')
            signInButton.click()
            time.sleep(3)
            try:
                if (driver.find_element(By.CSS_SELECTOR, "#pl_login > .js-pl_membershipForm > #pl_login_form_inner_wrapper > div[style='display: block;']") is not None):
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
            loginButton = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[3]/div[2]/a[1]')
            loginButton.click();
            signInButton = driver.find_element(By.CSS_SELECTOR,
                                               '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Log In"]')
            signInButton.click()

            try:
                if (driver.find_element(By.CSS_SELECTOR, '.pl_wrapper--open .login-password input[name="password"]') is not None):
                    if (driver.find_element(By.CSS_SELECTOR,
                                               '.pl_wrapper--open .js-form-content .login-email  input[name="email"]') is not None):
                        print(str(self.signInEmptyForm.__name__), "---- OK")
                        driver.close()
                        
            except:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()