from selenium import webdriver
import time
import unittest
import helping_functions.funtions as fun
import Variables.Sites.Highland as v

class ContactFormPO(unittest.TestCase):
    def __init__(self): None

    def correctlyFillTheForm(self, driver, firstName, lastName, email, phone, question):
        screen_name = fun.urlify(fun.datetime_now(str(self.correctlyFillTheForm.__name__))) + '.png'
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
                return False
            except:
                return True

