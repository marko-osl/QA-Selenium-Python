from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Tests import OpenSite


class ContactPage(OpenSite.OpenSiteWithHighlandTheme):

    def correctlyTyping(self):
        print("Correctly Contact Form On ContactPage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.correctlyTyping.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get(super().baseURL)
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();

        contactPage = driver.find_element(By.CSS_SELECTOR, "#menu-primary [href='\/contact']")
        contactPage.click()
        firstName = driver.find_element(By.ID, "first_name")
        firstName.send_keys("Marek")
        lastName = driver.find_element(By.ID, "last_name")
        lastName.send_keys("Oslizlo")
        emailAddress = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--email #email")
        emailAddress.send_keys(super().randomEmail())
        phoneNumber = driver.find_element(By.ID, "phone")
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
                print(str(self.correctlyTyping.__name__), " OK")
                driver.close()

    def incorrectlyTyping(self):
        print("Incorrectly Contact Form On ContactPage")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.incorrectlyTyping.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get(super().baseURL)
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();
        contactPage = driver.find_element(By.CSS_SELECTOR, "#menu-primary [href='\/contact']")
        contactPage.click()
        firstName = driver.find_element(By.ID, "first_name")
        firstName.send_keys("Marek")
        lastName = driver.find_element(By.ID, "last_name")
        lastName.send_keys("Oslizlo")
        emailAddress = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--email #email")
        emailAddress.send_keys("testtest.om")
        phoneNumber = driver.find_element(By.ID, "phone")
        phoneNumber.send_keys(super().randomPhone() + 10000000000000)
        question = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact--questions #question")
        question.send_keys("Marek")
        # Submit
        submitButton = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact-column-right input[type='submit']")
        submitButton.click()
        # try:
        if (driver.find_elements(By.XPATH, "/html//p[.='A valid email is required.']")):
            if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
                print(str(self.incorrectlyTyping.__name__), " OK")
                driver.close()
            else:
                driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
                print("Wyjście awaryjne z programu")
                exit()
        else:
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            print("Wyjście awaryjne z programu")
            exit()

    def emptyFormOnContactPage(self):
        print("Empty Contact Form On Contact Page")
        print("*" * 20)
        screen_name = self.urlify(super().datetime_now(str(self.emptyFormOnContactPage.__name__))) + '.png'

        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get(super().baseURL)
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();
        contactPage = driver.find_element(By.CSS_SELECTOR, "#menu-primary [href='\/contact']")
        contactPage.click()
        # Submit
        submitButton = driver.find_element(By.CSS_SELECTOR, ".pl_widget-contact-column-right input[type='submit']")
        submitButton.click()
        if (driver.find_elements(By.XPATH, "/html//p[.='Your name is required.']")):
            if (driver.find_elements(By.XPATH, "/html//p[.='A valid phone is required.']")):
                if (driver.find_elements(By.XPATH, "/html//textarea[@id='question']")):
                    print(str(self.emptyFormOnContactPage.__name__), " OK")
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
