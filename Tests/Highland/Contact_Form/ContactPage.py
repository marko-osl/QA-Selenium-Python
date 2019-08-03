from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
import Tests.Highland.Variables as v

class ContactPage(OpenSite.OpenSiteWithHighlandTheme):

    def correctlyTyping(self, driver):
        print("Correctly Contact Form On ContactPage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlyTyping.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            contactPage = driver.find_element(By.CSS_SELECTOR, v.contactPageLinkMenu)
            contactPage.click()
            firstName = driver.find_element(By.ID, v.firstNameOnHomepage)
            firstName.send_keys(v.firstName)
            lastName = driver.find_element(By.CSS_SELECTOR, v.lastNameOnHomepage)
            lastName.send_keys(v.lastName)
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.emailContactFormOnHomepage)
            emailAddress.send_keys(super().randomEmail())
            phoneNumber = driver.find_element(By.CSS_SELECTOR, v.phoneNumberContactFormOnHomepage)
            phoneNumber.send_keys(super().randomPhone())
            question = driver.find_element(By.CSS_SELECTOR, v.questionContactFormOnHomepage)
            question.send_keys(v.question)
            # Submit
            submitButton = driver.find_element(By.CSS_SELECTOR, v.submitButtonContactFormOnHomepage)
            submitButton.click()
            if (driver.find_elements(By.XPATH, v.firstNameErrorOnHomepage)):
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
            else:
                if (driver.find_elements(By.XPATH, v.phoneNumberErrorOnHomepage)):
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Wyjście awaryjne z programu")
                    exit()
                else:
                    print(str(self.correctlyTyping.__name__), " OK")


    def incorrectlyTyping(self, driver):
        print("Incorrectly Contact Form On ContactPage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.incorrectlyTyping.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            contactPage = driver.find_element(By.CSS_SELECTOR, v.contactPageLinkMenu)
            contactPage.click()
            firstName = driver.find_element(By.ID, v.firstNameOnHomepage)
            firstName.send_keys(v.firstName)
            lastName = driver.find_element(By.CSS_SELECTOR, v.lastNameOnHomepage)
            lastName.send_keys(v.lastName)
            emailAddress = driver.find_element(By.CSS_SELECTOR, v.emailContactFormOnHomepage)
            emailAddress.send_keys(v.wrongEmail)
            phoneNumber = driver.find_element(By.CSS_SELECTOR, v.phoneNumberContactFormOnHomepage)
            phoneNumber.send_keys(super().randomPhone() + 10000000000000)
            question = driver.find_element(By.CSS_SELECTOR, v.questionContactFormOnHomepage)
            question.send_keys(v.question)
            # Submit
            submitButton = driver.find_element(By.CSS_SELECTOR, v.submitButtonContactFormOnHomepage)
            submitButton.click()
            # try:
            if (driver.find_elements(By.XPATH, v.emailErrorOnHomepage)):
                if (driver.find_elements(By.XPATH, v.phoneNumberErrorOnHomepage)):
                    print(str(self.incorrectlyTyping.__name__), " OK")

                else:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Wyjście awaryjne z programu")
                    exit()
            else:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def emptyFormOnContactPage(self, driver):
        print("Empty Contact Form On Contact Page")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.emptyFormOnContactPage.__name__))) + '.png'

        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            contactPage = driver.find_element(By.CSS_SELECTOR, v.contactPageLinkMenu)
            contactPage.click()
            # Submit
            submitButton = driver.find_element(By.CSS_SELECTOR, v.submitButtonContactFormOnHomepage)
            submitButton.click()
            if (driver.find_elements(By.XPATH, v.firstNameErrorOnHomepage)):
                if (driver.find_elements(By.XPATH, v.phoneNumberErrorOnHomepage)):
                    if (driver.find_elements(By.XPATH, v.questionErrorOnHomepage)):
                        print(str(self.emptyFormOnContactPage.__name__), " OK")
                        super().closeDriver(driver)
                    else:
                        driver.save_screenshot(
                            "D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
                        print("Wyjście awaryjne z programu")
                        exit()
                else:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Wyjście awaryjne z programu")
                    exit()
            else:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
