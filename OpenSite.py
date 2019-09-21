import datetime
import re
from selenium import webdriver
import os
import random
from selenium.common.exceptions import NoSuchElementException

class OpenSiteWithHighlandTheme():

    baseURL = "http://qarobothighland.myrealestateplatform.xyz/"
    def openSites(self):
        # Setting webdriver
        screen_name = self.urlify(self.datetime_now(str(self.openSites.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get(self.baseURL)
            return driver
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot(super().screenShotsFolder() + "/%s" % screen_name)
            exit();
    def openAdmin(self):
        # Setting webdriver
        screen_name = self.urlify(self.datetime_now(str(self.openAdmin.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            return driver
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot(super().screenShotsFolder() + "/%s" % screen_name)
            exit();

    def closeDriver(self, driver):
        driver.close();
