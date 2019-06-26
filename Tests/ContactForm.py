from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from AutomateHighland import OpenSite


class ContactForm(OpenSite.OpenSiteWithHighlandTheme):

    def correctlyOnHomepage(self):
        print("Correctly Contact Form On Homepage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlyOnHomepage.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get("https://johnsnow.myrealestateplatform.net")
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")

        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();
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
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            print("Wyjście awaryjne z programu")
            exit()
        else:
            if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
                driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
            else:
                print(str(self.correctlyOnHomepage.__name__), " OK")
                driver.close()

    def incorrectlyOnHomepage(self):
        print("Incorrectly Contact Form On Homepage, wrong email and phone")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.incorrectlyOnHomepage.__name__))) + '.png'
        # Wrong email and phone number

        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get("https://johnsnow.myrealestateplatform.net")
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")

        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();
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

                driver.close()

            else:
                driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
        else:
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            print("Wyjście awaryjne z programu")
            exit()

    def emptyForm(self):
        print("Empty Contact Form On Homepage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.emptyForm.__name__))) + '.png'

        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get("https://johnsnow.myrealestateplatform.net")
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")

        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();
        # Submit
        submitButton = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact-column-right input[type='submit']")
        submitButton.click()
        if (driver.find_elements(By.XPATH, "/html//p[.='Your name is required.']")):
            if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
                if (driver.find_elements(By.XPATH, "/html//textarea[@id='question']")):
                    print(str(self.emptyForm.__name__), " OK")

                    driver.close()
                else:
                    driver.save_screenshot(
                        "D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
                    print("Wyjście awaryjne z programu")
                    exit()
            else:
                driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
        else:
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            print("Wyjście awaryjne z programu")
            exit()
