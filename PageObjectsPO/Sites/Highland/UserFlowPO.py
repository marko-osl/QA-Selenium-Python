import unittest
import time
import helping_functions.funtions as fun
import Variables.Sites.Highland as v

class UserFlowPO(unittest.TestCase):

    def correctlySignIn(self, driver, email, phone):
        screen_name = fun.urlify(fun.datetime_now(str(self.correctlySignIn.__name__))) + '.png'
        if (driver == 0):
            print("Emergency quit the test - No driver found")
            exit()
        else:
            loginButton = driver.find_element_by_xpath(v.loginButton)
            loginButton.click();
            emailAddress = driver.find_element_by_css_selector(v.loginEmailInput)
            emailAddress.send_keys(email)
            password = driver.find_element_by_css_selector(v.loginPasswordInput)
            password.send_keys(phone)
            signInButton = driver.find_element_by_css_selector(v.loginSignInButton)
            signInButton.click()
            time.sleep(3)
            try:
                self.assertTrue(driver.find_element_by_css_selector(v.loginVerifyHandle))
                return True
            except:
                driver.save_screenshot(fun.screenShotsFolder() + "\\%s" % screen_name)
                return False

    def signinToNotExistingAccount(self, driver, email, phone):
        screen_name = fun.urlify(fun.datetime_now(str(self.signinToNotExistingAccount.__name__))) + '.png'
        if (driver == 0):
            print("Emergency quit the test - No driver found")
            exit()
        else:
            loginButton = driver.find_element_by_xpath(v.loginButton)
            loginButton.click()
            emailAddress = driver.find_element_by_css_selector(v.loginEmailInput)
            emailAddress.send_keys(email)
            password = driver.find_element_by_css_selector(v.loginPasswordInput)
            password.send_keys(phone)
            signInButton = driver.find_element_by_css_selector(v.loginSignInButton)
            signInButton.click()
            time.sleep(3)
            try:
                self.assertTrue(driver.find_element_by_css_selector(v.loginNotExistingAccountMessage))
                return True
            except:
                driver.save_screenshot(fun.screenShotsFolder() + "\\%s" % screen_name)
                return False

    def sendingEmptySigninForm(self, driver):
        screen_name = fun.urlify(fun.datetime_now(str(self.signinToNotExistingAccount.__name__))) + '.png'
        if (driver == 0):
            print("Emergency quit the test - No driver found")
            exit()
        else:
            loginButton = driver.find_element_by_xpath(v.loginButton)
            loginButton.click()
            signInButton = driver.find_element_by_css_selector(v.loginSignInButton)
            signInButton.click()
            time.sleep(3)
            try:
                self.assertTrue(driver.find_element_by_css_selector(v.loginPasswordEmptyMessage))
                self.assertTrue(driver.find_element_by_css_selector(v.loginEmailEmptyMessage))
                return True
            except:
                driver.save_screenshot(fun.screenShotsFolder() + "\\%s" % screen_name)
                return False