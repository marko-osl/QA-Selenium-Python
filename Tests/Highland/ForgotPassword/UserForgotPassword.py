import time
from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
import Tests.Highland.Variables as v

class UserForgotPassword(OpenSite.OpenSiteWithHighlandTheme):
    def correctlySendingForgotPassword(self, driver, ranEmail):
        print("Correctly sending forgot password form")
        print("*" *20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlySendingForgotPassword.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            loginButton = driver.find_element(By.XPATH, v.forgotPasswordLoginLink)
            loginButton.click()
            forgotPasswordButton = driver.find_element(By.CSS_SELECTOR, v.forgotPasswordButton)
            forgotPasswordButton.click()
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.forgotPasswordEmailInput)
            emailAddress.send_keys(ranEmail)
            resetPasswordButton = driver.find_element(By.CSS_SELECTOR, v.forgotPasswordResetPasswordButton)
            resetPasswordButton.click()
            try:
                if (driver.find_element(By.CSS_SELECTOR, v.forgotPasswordSuccessHandle) is not None):
                    print(self.correctlySendingForgotPassword.__name__ + "----- OK")
            except:
                print("Error, exiting...")
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                driver.quit()
                exit()

    def incorrectlySendingForgotPasswordEmptyEmail(self, driver):
            print("Sending Forgot Password without email")
            print("*" *20)
            screen_name = self.urlify(super().datetime_now(str(self.incorrectlySendingForgotPasswordEmptyEmail.__name__))) + '.png'
            if (driver == 0):
                print("Brak drivera")
                exit()
            else:
                exitButton = driver.find_element(By.CSS_SELECTOR, v.forgotPasswordExitButton)
                exitButton.click()
                time.sleep(2)
                loginButton = driver.find_element(By.XPATH, v.forgotPasswordLoginLink)
                loginButton.click()
                forgotPasswordButton = driver.find_element(By.CSS_SELECTOR, v.forgotPasswordButton)
                forgotPasswordButton.click()
                resetPasswordButton = driver.find_element(By.CSS_SELECTOR, v.forgotPasswordResetPasswordButton)
                resetPasswordButton.click()
                try:
                    if (driver.find_element(By.XPATH, v.forgotPasswordEmptyEmailMessage) is not None):
                        print(self.incorrectlySendingForgotPasswordEmptyEmail.__name__ + "----- OK")
                except:
                    print("Error, exiting...")
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    driver.quit()
                    exit()