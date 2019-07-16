from Tests.ContactForm import ContactForm
from Tests.ContactPage import ContactPage
import Tests.OpenSite
from Tests.OpenSite import OpenSiteWithHighlandTheme


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


Env = OpenSiteWithHighlandTheme()
start = test()
start.startContactFormOnHomepage(Env.open())
start.startContactFormOnContactPage(Env.open())