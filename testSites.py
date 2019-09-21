from Tests.Highland.Contact_Form.ContactForm import ContactForm
from ContactPage import ContactPage
import OpenSite
from OpenSite import OpenSiteWithHighlandTheme
from SignIn.UserSignIn import UserSignIn
from SignUp.UserSignUp import UserSignUp
from ForgotPassword.UserForgotPassword import UserForgotPassword


class test(OpenSite.OpenSiteWithHighlandTheme):

    def openTestEnv(self):
        driver = super().openSites();
        return driver
    def startContactFormOnHomepage(self, driver):
        print("*" * 10 + "Start startContactFormOnHomepage" + "*" * 10)
        contactForm = ContactForm()
        contactForm.correctlyOnHomepage(driver)
        contactForm.incorrectlyOnHomepage(driver)
        contactForm.emptyForm(driver)
        driver.quit()

    def startContactFormOnContactPage(self, driver):
        print("*" * 10 + "Start startContactFormOnContactPage" + "*" * 10)
        contactForm = ContactPage()
        contactForm.correctlyTyping(driver)
        contactForm.incorrectlyTyping(driver)
        contactForm.emptyFormOnContactPage(driver)
        driver.quit()

    def startSignUpAndSignIn(self, driver, ranEmail, ranPhone):
        print("*" * 10 + "Start startSignUp" + "*" * 10)
        signUp = UserSignUp()
        signUp.correctlySignUp(driver, ranEmail, ranPhone)
        signUp.logOutUser(driver)
        signUp.signUpExistingAccount(driver, ranEmail, ranPhone)
        signUp.signUpEmptyForm(driver)
        SignIn = UserSignIn()
        SignIn.correctlySignIn(driver, ranEmail, ranPhone)
        driver.close()
        # driver.get(super().baseURL)
        SignIn.signInToNotExistingAccount(self.open(), ranPhone)
        SignIn.signInEmptyForm(self.open())
        driver.quit()
    def startForgotPassword(self, driver,ranEmail):
        print("*" * 10 + "Start Forgot password" + "*" * 10)
        forgot = UserForgotPassword()
        forgot.correctlySendingForgotPassword(driver,ranEmail)
        forgot.incorrectlySendingForgotPasswordEmptyEmail(driver)
        driver.quit()



Env = OpenSiteWithHighlandTheme()
ranEmail = Env.randomEmail()
ranPhone = Env.randomPhone()
start = test()
start.startContactFormOnHomepage(Env.openSites())
start.startContactFormOnContactPage(Env.open())
start.startSignUpAndSignIn(Env.open(), ranEmail, ranPhone)
start.startForgotPassword(Env.open(), ranEmail)