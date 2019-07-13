from Tests.ContactForm import ContactForm
from Tests.ContactPage import ContactPage
import Tests.OpenSite


class test(Tests.OpenSite.OpenSiteWithHighlandTheme):
    def startContactFormOnHomepage(self):
        print("*" * 10 + "Start startContactFormOnHomepage" + "*" * 10)
        contactForm = ContactForm()
        contactForm.correctlyOnHomepage()
        contactForm.incorrectlyOnHomepage()
        contactForm.emptyForm()

    def startContactFormOnContactPage(self):
        print("*" * 10 + "Start startContactFormOnContactPage" + "*" * 10)
        contactForm = ContactPage()
        contactForm.correctlyTyping()
        contactForm.incorrectlyTyping()
        contactForm.emptyFormOnContactPage()


startup = test()
startup.startContactFormOnHomepage()
startup.startContactFormOnContactPage()
