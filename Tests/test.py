from Tests.ContactForm import ContactForm
from Tests.ContactPage import ContactPage
import Tests.OpenSite
from Tests.OpenSite import OpenSiteWithHighlandTheme
from Tests.UserSignUp import UserSignUp


class test(Tests.OpenSite.OpenSiteWithHighlandTheme):

    def openTestEnv(self):
        driver = super().open();
        return driver
    def startContactFormOnHomepage(self, driver):
        print("*" * 10 + "Start startContactFormOnHomepage" + "*" * 10)
        contactForm = ContactForm()
        contactForm.correctlyOnHomepage(driver)
        contactForm.incorrectlyOnHomepage(driver)
        contactForm.emptyForm(driver)

    def startContactFormOnContactPage(self, driver):
        print("*" * 10 + "Start startContactFormOnContactPage" + "*" * 10)
        contactForm = ContactPage()
        contactForm.correctlyTyping(driver)
        contactForm.incorrectlyTyping(driver)
        contactForm.emptyFormOnContactPage(driver)

    def startSignUp(self, driver, ranEmail, ranPhone):
        print("*" * 10 + "Start startSignUp" + "*" * 10)
        signUp = UserSignUp()
        signUp.correctlySignUp(driver, ranEmail, ranPhone)
        signUp.signUpExistingAccount(ranEmail, ranPhone)



Env = OpenSiteWithHighlandTheme()
ranEmail = Env.randomEmail()
ranPhone = Env.randomPhone()
start = test()
start.startContactFormOnHomepage(Env.open())
start.startContactFormOnContactPage(Env.open())
start.startSignUp(Env.open(), ranEmail, ranPhone)