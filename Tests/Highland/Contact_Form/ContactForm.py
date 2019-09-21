import time
import unittest
from selenium import webdriver
import helping_functions.funtions as fun
import PageObjectsPO.Sites.Highland.ContactFormPO as po
from Variables.Sites import Highland as v


class ContactForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.runner = po.ContactFormPO()

    def setUp(self):
        self.driver.get("http://qarobothighland.myrealestateplatform.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_user_can_correctly_send_contact_form_from_homepage(self):
        driver = self.driver
        runner = self.runner
        test = runner.correctlyFillTheContactForm(driver, v.firstName, v.lastName, fun.randomEmail(),fun.randomPhone(), v.question)
        self.assertTrue(test)

    def test_user_cannot_correctly_send_contact_form_with_wrong_email_and_phone(self):
        driver = self.driver
        runner = self.runner
        # driver.refresh()
        test = runner.incorrectlyFillTheContactForm(driver, v.firstName, v.lastName, v.wrongEmail, fun.randomPhone() + 100000000, v.question)
        self.assertTrue(test)

    def test_user_cannot_correctly_send_empty_contact_form(self):
        driver = self.driver
        runner = self.runner
        # driver.refresh()
        test = runner.emptyContactForm(driver)
        self.assertTrue(test)

    def test_user_can_correctly_send_contact_form_from_contact_page(self):
        driver = self.driver
        runner = self.runner
        runner.goToContactPage(driver)
        test = runner.correctlyFillTheContactForm(driver, v.firstName, v.lastName, fun.randomEmail(),fun.randomPhone(), v.question)
        self.assertTrue(test)

    def test_user_cannot_correctly_send_contact_form_from_contact_page(self):
        driver = self.driver
        runner = self.runner
        runner.goToContactPage(driver)
        test = runner.incorrectlyFillTheContactForm(driver, v.firstName, v.lastName, v.wrongEmail, fun.randomPhone() + 100000000, v.question)
        self.assertTrue(test)

    def test_user_cannot_send_empty_contact_form_from_contact_page(self):
        driver = self.driver
        runner = self.runner
        runner.goToContactPage(driver)
        test = runner.emptyContactForm(driver)
        self.assertTrue(test)
