from selenium import webdriver
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
                print("Brak drivera")
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
                    time.sleep(7)
                    if (domain != "xyz"):
                        if (driver.find_element_by_css_selector("[ng-reflect-title='Main Street Realty'] h4") is not None):
                            print(str(self.loginToTheAdminPanelOldIncApp.__name__) + "---- OK")
                        else:
                            driver.save_screenshot(super().screenShotsFolder() + "\\%s" % screen_name)
                            print("Wyjście awaryjne z programu")
                            exit()
                    else:
                        driver.close()


