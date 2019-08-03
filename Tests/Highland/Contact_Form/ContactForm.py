from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
import Tests.Highland.Variables as v


class ContactForm(OpenSite.OpenSiteWithHighlandTheme):

    def correctlyOnHomepage(self, driver):
        print("Correctly Contact Form On Homepage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlyOnHomepage.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
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
                    driver.save_screenshot(".\\Screenshots\\%s" % screen_name)
                    print("Wyjście awaryjne z programu")
                    exit()
                else:
                    print(str(self.correctlyOnHomepage.__name__), " OK")

    def incorrectlyOnHomepage(self,driver):
        print("Incorrectly Contact Form On Homepage, wrong email and phone")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.incorrectlyOnHomepage.__name__))) + '.png'
        # Wrong email and phone number

        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            driver.refresh();
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
                    print(str(self.incorrectlyOnHomepage.__name__), " OK")


                else:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Wyjście awaryjne z programu")
                    exit()
            else:
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()

    def emptyForm(self, driver):
        print("Empty Contact Form On Homepage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.emptyForm.__name__))) + '.png'

        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            driver.refresh();
            # Submit
            submitButton = driver.find_element(By.CSS_SELECTOR, v.submitButtonContactFormOnHomepage)
            submitButton.click()
            if (driver.find_elements(By.XPATH, v.firstNameErrorOnHomepage)):
                if (driver.find_elements(By.XPATH, v.phoneNumberErrorOnHomepage)):
                    if (driver.find_elements(By.XPATH, v.questionErrorOnHomepage)):
                        print(str(self.emptyForm.__name__), " OK")
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
