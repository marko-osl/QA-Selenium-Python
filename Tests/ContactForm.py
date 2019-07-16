from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests import OpenSite


class ContactForm(OpenSite.OpenSiteWithHighlandTheme):

    def correctlyOnHomepage(self, driver):
        print("Correctly Contact Form On Homepage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlyOnHomepage.__name__))) + '.png'
        if (driver == 0):
            print("Brak drivera")
            exit()
        else:
            firstName = driver.find_element(By.ID, "first_name")
            firstName.send_keys("Marek")
            lastName = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--name #last_name")
            lastName.send_keys("Oslizlo")
            emailAddress = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--email #email")
            emailAddress.send_keys(super().randomEmail())
            phoneNumber = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--phone #phone")
            phoneNumber.send_keys(super().randomPhone())
            question = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--questions #question")
            question.send_keys("Marek")
            # Submit
            submitButton = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact-column-right input[type='submit']")
            submitButton.click()
            if (driver.find_elements(By.XPATH, "/html//p[.='Your name is required.']")):
                driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
            else:
                if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
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
            firstName = driver.find_element(By.ID, "first_name")
            firstName.send_keys("Marek")
            lastName = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--name #last_name")
            lastName.send_keys("Oslizlo")
            emailAddress = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--email #email")
            emailAddress.send_keys("WrongEmail")
            phoneNumber = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--phone #phone")
            phoneNumber.send_keys(super().randomPhone() + 10000000000000)
            question = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--questions #question")
            question.send_keys("Marek")
            # Submit
            submitButton = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact-column-right input[type='submit']")
            submitButton.click()
            # try:
            if (driver.find_elements(By.XPATH, "/html//p[.='A valid email is required.']")):
                if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
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
            submitButton = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact-column-right input[type='submit']")
            submitButton.click()
            if (driver.find_elements(By.XPATH, "/html//p[.='Your name is required.']")):
                if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
                    if (driver.find_elements(By.XPATH, "/html//textarea[@id='question']")):
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
