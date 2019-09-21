from selenium import webdriver
import time
import unittest
import helping_functions.funtions as fun
import Variables.Sites.Highland as v

class ContactFormPO(unittest.TestCase):
    def __init__(self): None

    def correctlyFillTheFormOnHomepage(self, driver, firstName, lastName, email, phone, question):
        screen_name = fun.urlify(fun.datetime_now(str(self.correctlyFillTheFormOnHomepage.__name__))) + '.png'
        if (driver == 0):
            print("Emergency quit the test - No driver found")
            exit()
        else:
            firstNameInput = driver.find_element_by_id(v.firstNameOnHomepage)
            firstNameInput.send_keys(firstName)
            lastNameInput = driver.find_element_by_css_selector(v.lastNameOnHomepage)
            lastNameInput.send_keys(lastName)
            emailAddressInput = driver.find_element_by_css_selector(v.emailContactFormOnHomepage)
            emailAddressInput.send_keys(email)
            phoneNumberInput = driver.find_element_by_css_selector(v.phoneNumberContactFormOnHomepage)
            phoneNumberInput.send_keys(phone)
            questionInput = driver.find_element_by_css_selector(v.questionContactFormOnHomepage)
            questionInput.send_keys(question)
            # Submit
            submitButton = driver.find_element_by_css_selector(v.submitButtonContactFormOnHomepage)
            submitButton.click()
            try:
                self.assertTrue(driver.find_element_by_xpath(v.firstNameErrorOnHomepage))
                driver.save_screenshot(fun.screenShotsFolder() + "\\%s" % screen_name)
                return False
            except:
                return True

    def incorrectlyFillTheFormOnHomepage(self, driver, firstName, lastName, email, phone, question):
        screen_name = fun.urlify(fun.datetime_now(str(self.incorrectlyFillTheFormOnHomepage.__name__))) + '.png'
        if (driver == 0):
            print("Emergency quit the test - No driver found")
            exit()
        else:
            firstNameInput = driver.find_element_by_id(v.firstNameOnHomepage)
            firstNameInput.send_keys(firstName)
            lastNameInput = driver.find_element_by_css_selector(v.lastNameOnHomepage)
            lastNameInput.send_keys(lastName)
            emailAddressInput = driver.find_element_by_css_selector(v.emailContactFormOnHomepage)
            emailAddressInput.send_keys(email)
            phoneNumberInput = driver.find_element_by_css_selector(v.phoneNumberContactFormOnHomepage)
            phoneNumberInput.send_keys(phone)
            questionInput = driver.find_element_by_css_selector(v.questionContactFormOnHomepage)
            questionInput.send_keys(question)
            # Submit
            submitButton = driver.find_element_by_css_selector(v.submitButtonContactFormOnHomepage)
            submitButton.click()
            try:
                self.assertTrue(driver.find_element_by_xpath(v.emailErrorOnHomepage))
                return True
            except:
                driver.save_screenshot(fun.screenShotsFolder() + "\\%s" % screen_name)
                return False

    def emptyFormOnHomepage(self, driver):
        screen_name = fun.urlify(fun.datetime_now(str(self.emptyFormOnHomepage.__name__))) + '.png'
        if (driver == 0):
            print("Emergency quit the test - No driver found")
            exit()
        else:
            # Submit
            submitButton = driver.find_element_by_css_selector(v.submitButtonContactFormOnHomepage)
            submitButton.click()
            try:
                self.assertTrue(driver.find_element_by_xpath(v.emailErrorOnHomepage))
                self.assertTrue(driver.find_element_by_xpath(v.firstNameErrorOnHomepage))
                self.assertTrue(driver.find_element_by_xpath(v.phoneNumberErrorOnHomepage))
                self.assertTrue(driver.find_element_by_xpath(v.questionErrorOnHomepage))
                return True
            except:
                driver.save_screenshot(fun.screenShotsFolder() + "\\%s" % screen_name)
                return False
