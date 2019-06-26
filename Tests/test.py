from AutomateHighland.ContactForm import ContactForm
from AutomateHighland.ContactPage import ContactPage
from AutomateHighland.OpenSite import OpenSiteWithHighlandTheme


class test(OpenSiteWithHighlandTheme):
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
