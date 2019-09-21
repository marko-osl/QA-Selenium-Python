from Tests.AdminPanel.CRM.DeleteAllLeads import DeleteAllLeads
from OpenSite import OpenSiteWithHighlandTheme
from Tests.AdminPanel import Variables as v
import OpenSite

class test(OpenSite.OpenSiteWithHighlandTheme):

    def openTestEnv(self):
        driver = super().openAdmin();
        return driver
    def startDeleteAllLeadsInternal(self, driver):
        print("*" * 10 + "Start DeleteAllLeads from internal" + "*" * 10)
        deleteLeads = DeleteAllLeads()
        deleteLeads.loginToTheAdminPanelOldIncApp(driver, "qa.pl.robot+com@gmail.com", "placester123", v.domainInternal)
        deleteLeads.enterToTheCRM(driver)
        deleteLeads.deleteLeads(driver)
        driver.quit()

    def startDeleteAllLeadsStaging(self, driver):
        print("*" * 10 + "Start DeleteAllLeads test from staging" + "*" * 10)
        deleteLeads = DeleteAllLeads()
        deleteLeads.loginToTheAdminPanelOldIncApp(driver, "qa.pl.robot+com@gmail.com", "placester123", v.domainStaging)
        deleteLeads.enterToTheCRM(driver)
        driver.quit()

    def startDeleteAllLeadsProduction(self, driver):
        print("*" * 10 + "Start DeleteAllLeads test from production" + "*" * 10)
        deleteLeads = DeleteAllLeads()
        deleteLeads.loginToTheAdminPanelOldIncApp(driver, "qa.pl.robot+com@gmail.com", "placester123", v.domainProduction)
        deleteLeads.enterToTheCRM(driver)
        driver.quit()


Env = OpenSiteWithHighlandTheme()
ranEmail = Env.randomEmail()
ranPhone = Env.randomPhone()
start = test()
start.startDeleteAllLeadsInternal(Env.openAdmin())
start.startDeleteAllLeadsStaging(Env.openAdmin())
start.startDeleteAllLeadsProduction(Env.openAdmin())
