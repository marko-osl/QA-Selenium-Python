import datetime
import re
from selenium import webdriver
import os
import random

class OpenSiteWithHighlandTheme():

    baseURL = "http://qarobothighland.myrealestateplatform.xyz/"
    def open(self):
        # Setting webdriver
        screen_name = self.urlify(self.datetime_now(str(self.open.__name__))) + '.png'
        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get(self.baseURL)
            return driver
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot(super().screenShotsFolder() + "/%s" % screen_name)
            exit();

    def closeDriver(self, driver):
        driver.close();
    def randomEmail(self):
        email = "qaselenium"
        rand = random.randint(10000, 99999)
        domena = "@gmail.com"
        email = email + str(rand) + domena
        print(email)
        return email

    def randomPhone(self):
        phone = random.randint(1000000000, 9999999999)
        print(phone)
        return phone

    def urlify(self, s):
        # Remove all non-word characters (everything except numbers and letters)
        s = re.sub(r"[^\w\s]", '', s)
        # Replace all runs of whitespace with a single dash
        s = re.sub(r"\s+", '-', s)
        return s

    def datetime_now(self, prefix):
        symbols = str(datetime.datetime.now())
        return prefix + "-" + "".join(symbols)

    def screenShotsFolder(self):
        path = os.getcwd()
        dl = len(path)
        final = path[0:dl - 6]
        final = str(final) + "/Screenshots/"
        return final