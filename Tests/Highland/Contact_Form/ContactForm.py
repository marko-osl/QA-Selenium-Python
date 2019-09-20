import unittest
from selenium import webdriver
import helping_functions.funtions as fun
import PageObjectsPO.Sites.Highland.ContactFormPO as po
from Variables.Sites import Highland as v


class ContactForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://qarobothighland.myrealestateplatform.net")
        cls.driver.maximize_window()
        cls.runner = po.ContactFormPO()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_user_can_correctly_send_contact_form_from_homepage(self):
        driver = self.driver
        runner = self.runner
        test = runner.correctlyFillTheForm(driver, v.firstName, v.lastName, fun.randomEmail(),fun.randomPhone(), v.question)
        self.assertTrue(test)

    # def incorrectlyOnHomepage(self,driver):
    #     print("Incorrectly Contact Form On Homepage, wrong email and phone")
    #     print("*" * 20)
    #     screen_name = self.urlify(super().datetime_now(str(self.incorrectlyOnHomepage.__name__))) + '.png'
    #     # Wrong email and phone number
    #
    #     if (driver == 0):
    #         print("Brak drivera")
    #         exit()
    #     else:
    #         driver.refresh();
    #         firstName = driver.find_element(By.ID, v.firstNameOnHomepage)
    #         firstName.send_keys(v.firstName)
    #         lastName = driver.find_element(By.CSS_SELECTOR, v.lastNameOnHomepage)
    #         lastName.send_keys(v.lastName)
    #         emailAddress = driver.find_element(By.CSS_SELECTOR, v.emailContactFormOnHomepage)
    #         emailAddress.send_keys(v.wrongEmail)
    #         phoneNumber = driver.find_element(By.CSS_SELECTOR, v.phoneNumberContactFormOnHomepage)
    #         phoneNumber.send_keys(super().randomPhone() + 10000000000000)
    #         question = driver.find_element(By.CSS_SELECTOR, v.questionContactFormOnHomepage)
    #         question.send_keys(v.question)
    #         # Submit
    #         submitButton = driver.find_element(By.CSS_SELECTOR, v.submitButtonContactFormOnHomepage)
    #         submitButton.click()
    #         # try:
    #         if (driver.find_elements(By.XPATH, v.emailErrorOnHomepage)):
    #             if (driver.find_elements(By.XPATH, v.phoneNumberErrorOnHomepage)):
    #                 print(str(self.incorrectlyOnHomepage.__name__), " OK")
    #
    #
    #             else:
    #                 driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
    #                 print("Wyjście awaryjne z programu")
    #                 exit()
    #         else:
    #             driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
    #             print("Wyjście awaryjne z programu")
    #             exit()
    #
    # def emptyForm(self, driver):
    #     print("Empty Contact Form On Homepage")
    #     print("*" * 20)
    #     screen_name = self.urlify(super().datetime_now(str(self.emptyForm.__name__))) + '.png'
    #
    #     if (driver == 0):
    #         print("Brak drivera")
    #         exit()
    #     else:
    #         driver.refresh();
    #         # Submit
    #         submitButton = driver.find_element(By.CSS_SELECTOR, v.submitButtonContactFormOnHomepage)
    #         submitButton.click()
    #         if (driver.find_elements(By.XPATH, v.firstNameErrorOnHomepage)):
    #             if (driver.find_elements(By.XPATH, v.phoneNumberErrorOnHomepage)):
    #                 if (driver.find_elements(By.XPATH, v.questionErrorOnHomepage)):
    #                     print(str(self.emptyForm.__name__), " OK")
    #                     super().closeDriver(driver)
    #
    #                 else:
    #                     driver.save_screenshot(
    #                         "D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
    #                     print("Wyjście awaryjne z programu")
    #                     exit()
    #             else:
    #                 driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
    #                 print("Wyjście awaryjne z programu")
    #                 exit()
    #         else:
    #             driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
    #             print("Wyjście awaryjne z programu")
    #             exit()
