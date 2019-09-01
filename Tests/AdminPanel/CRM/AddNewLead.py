from selenium.webdriver.common.by import By
from Tests.Highland import OpenSite
from Tests.AdminPanel.CRM.DeleteAllLeads import DeleteAllLeads as inc
from Tests.AdminPanel import Variables as v
import time

class AddNewLead(OpenSite.OpenSiteWithHighlandTheme):
        def correctlyAddNewLead(self, driver, ranEmail, ranPhone):
            print("Correctly Adding a new Lead to CRM")
            print("*" * 20)
            screen_name = self.urlify(super().datetime_now(str(self.correctlyAddNewLead.__name__))) + '.png'
            if (driver == 0):
                print("Driver error")
                exit()
            else:
                incApp = inc()
                incApp.loginToTheAdminPanelOldIncApp(driver, "moslizglo@placester.com", "wpkraken", v.domainInternal)
                incApp.enterToTheCRM(driver)
                newLeadButton = driver.find_element(By.CSS_SELECTOR, v.newLeadButton)
                newLeadButton.click()
                firstNameField = driver.find_element(By.CSS_SELECTOR, v.firstNameField)
                firstNameField.send_keys(v.firstName)
                lastNameField = driver.find_element(By.CSS_SELECTOR, v.lastNameField)
                lastNameField.send_keys(v.lastName)
                time.sleep(1)
                emailField = driver.find_element(By.CSS_SELECTOR, v.emailNewField)
                emailField.send_keys(ranEmail)
                additionalEmailField = driver.find_element(By.CSS_SELECTOR, v.additionalEmailField)
                additionalEmailField.send_keys(super().randomEmail())
                driver.find_element(By.CSS_SELECTOR, v.workEmailCheck).click()
                phoneNumberField = driver.find_element(By.CSS_SELECTOR, v.phoneNumberField)
                phoneNumberField.send_keys(ranPhone)
                additionalPhoneNumberField = driver.find_element(By.CSS_SELECTOR, v.additionalPhoneNumberField)
                additionalPhoneNumberField.send_keys(super().randomPhone())
                driver.find_element(By.CSS_SELECTOR, v.workPhoneNumberCheck).click()
                saveButton = driver.find_element(By.CSS_SELECTOR, v.saveButton)
                saveButton.click()
                time.sleep(2)
                try:
                    if (driver.find_element(By.CSS_SELECTOR, v.editLeadInFrame) is not None):
                        print(str(self.correctlyAddNewLead.__name__) + "---- OK")
                except:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Emergency exit from the program")
                    exit()

        def incorrectlyAddNewLead(self, driver):
            print("Incorrectly Adding a new Lead to CRM")
            print("*" * 20)
            screen_name = self.urlify(super().datetime_now(str(self.incorrectlyAddNewLead.__name__))) + '.png'
            if (driver == 0):
                print("Driver error")
                exit()
            else:
                driver.find_element(By.CSS_SELECTOR, ".dismiss").click()
                newLeadButton = driver.find_element(By.CSS_SELECTOR, v.newLeadButton)
                newLeadButton.click()
                firstNameField = driver.find_element(By.CSS_SELECTOR, v.firstNameField)
                firstNameField.send_keys(v.firstName)
                lastNameField = driver.find_element(By.CSS_SELECTOR, v.lastNameField)
                lastNameField.send_keys(v.lastName)
                time.sleep(1)
                emailField = driver.find_element(By.CSS_SELECTOR, v.emailNewField)
                emailField.send_keys(v.wrongEmail)
                additionalEmailField = driver.find_element(By.CSS_SELECTOR, v.additionalEmailField)
                additionalEmailField.send_keys(super().randomEmail())
                driver.find_element(By.CSS_SELECTOR, v.workEmailCheck).click()
                phoneNumberField = driver.find_element(By.CSS_SELECTOR, v.phoneNumberField)
                phoneNumberField.send_keys(v.wrongPhone)
                additionalPhoneNumberField = driver.find_element(By.CSS_SELECTOR, v.additionalPhoneNumberField)
                additionalPhoneNumberField.send_keys(super().randomPhone())
                driver.find_element(By.CSS_SELECTOR, v.workPhoneNumberCheck).click()
                saveButton = driver.find_element(By.CSS_SELECTOR, v.saveButton)
                saveButton.click()
                time.sleep(2)
                try:
                    if (driver.find_element(By.CSS_SELECTOR, v.alertWrongEmail) is not None):
                        print(str(self.incorrectlyAddNewLead.__name__) + "---- OK")
                except:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Emergency exit from the program")
                    exit()

        def emptyAddNewLead(self, driver):
            print("Empty Adding a new Lead to CRM")
            print("*" * 20)
            screen_name = self.urlify(
                super().datetime_now(str(self.emptyAddNewLead.__name__))) + '.png'
            if (driver == 0):
                print("Driver error")
                exit()
            else:
                driver.find_element(By.CSS_SELECTOR, v.firstNameField).clear()
                driver.find_element(By.CSS_SELECTOR, v.lastNameField).clear()
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, v.emailNewField).clear()
                driver.find_element(By.CSS_SELECTOR, v.additionalEmailField).clear()
                driver.find_element(By.CSS_SELECTOR, v.phoneNumberField).clear()
                driver.find_element(By.CSS_SELECTOR, v.additionalPhoneNumberField).clear()
                saveButton = driver.find_element(By.CSS_SELECTOR, v.saveButton)
                saveButton.click()
                time.sleep(2)
                try:
                    if (driver.find_element(By.CSS_SELECTOR, v.alertWrongEmail) is not None):
                        print(str(self.emptyAddNewLead.__name__) + "---- OK")
                        driver.close()
                except:
                    driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                    print("Emergency exit from the program")
                    exit()