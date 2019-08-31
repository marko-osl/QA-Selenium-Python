from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
from Tests.AdminPanel import Variables as v
import time

class DeleteAllLeads(OpenSite.OpenSiteWithHighlandTheme):
        def loginToTheAdminPanelOldIncApp(self, driver, adminEmail, adminPassword, domain):
            print("Delete all Leads from My Accont")
            print("*" * 20)
            screen_name = self.urlify(super().datetime_now(str(self.loginToTheAdminPanelOldIncApp.__name__))) + '.png'
            if (driver == 0):
                print("Driver error")
                exit()
            else:
                driver.get("https://myrealestateplatform." + domain)
                if (driver.find_element(By.CSS_SELECTOR, v.emailField) is not None):
                    emailField = driver.find_element(By.CSS_SELECTOR, v.emailField)
                    emailField.send_keys(adminEmail)
                    passwordField = driver.find_element(By.CSS_SELECTOR, v.passwordField)
                    passwordField.send_keys(adminPassword)
                    loginButton = driver.find_element(By.CSS_SELECTOR, v.loginButton)
                    loginButton.click()
                    time.sleep(10)
                    try:
                        if (driver.find_element_by_css_selector(".sites-container apc-site-list-item:nth-child(2) h4") is not None):
                            print(str(self.loginToTheAdminPanelOldIncApp.__name__) + "---- OK")
                    except:
                        driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                        print("Emergency exit from the program")
                        exit()

        def enterToTheCRM(self, driver):
            print("I'm going to the CRM")
            print("*" * 20)
            screen_name = self.urlify(super().datetime_now(str(self.enterToTheCRM.__name__))) + '.png'
            if (driver == 0):
                print("Driver error")
                exit()
            else:
                    if (driver.find_element_by_css_selector(v.crmButton)):
                        crmButton = driver.find_element_by_css_selector(v.crmButton)
                        crmButton.click()
                        time.sleep(7)
                        try:
                            if (driver.find_element_by_css_selector(".nav--bar li:nth-of-type(2) span") is not None):
                                print(str(self.loginToTheAdminPanelOldIncApp.__name__) + "---- OK")
                        except:
                            driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                            print("Emergency exit from the program")
                            exit()

        def deleteLeads(self, driver):
            print("I'm going to delete all leads from CRM")
            print("*" * 20)
            screen_name = self.urlify(super().datetime_now(str(self.deleteLeads.__name__))) + '.png'
            if (driver == 0):
                print("Driver error")
                exit()
            else:
                try:
                    try:
                        while driver.find_element(By.CSS_SELECTOR, ".entity-count") != 0:
                            time.sleep(1)
                            selectAllLeads = driver.find_element_by_css_selector(v.selectAllLeadsOnSite)
                            selectAllLeads.click()
                            deleteButton = driver.find_element_by_css_selector(v.deleteButton)
                            deleteButton.click()
                            deleteConfirm = driver.find_element_by_xpath(v.deleteConfirm)
                            deleteConfirm.click()
                            time.sleep(2)
                    except:
                        print("0 Leads on your account ? ")
                except:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Emergency exit from the program")
                    exit()
