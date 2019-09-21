import unittest
from selenium import webdriver
import helping_functions.funtions as fun
import PageObjectsPO.Sites.Highland.UserFlowPO as po
from Variables.Sites import Highland as v


class UserSignIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.runner = po.UserFlowPO()

    def setUp(self):
        self.driver.get("http://qarobothighland.myrealestateplatform.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_user_can_correctly_signin(self):
        driver = self.driver
        runner = self.runner
        test = runner.correctlySignIn(driver, "test@test.pl", "test")
        self.assertTrue(test)

    def test_user_cannot_signin_to_not_existing_account(self):
        driver = self.driver
        runner = self.runner
        driver.delete_all_cookies()
        driver.refresh()
        test = runner.signinToNotExistingAccount(driver, fun.randomEmail(), fun.randomPhone() )
        self.assertTrue(test)

    def test_user_cannot_send_empty_signin_form(self):
        driver = self.driver
        runner = self.runner
        driver.delete_all_cookies()
        driver.refresh()
        test = runner.sendingEmptySigninForm(driver)
        self.assertTrue(test)