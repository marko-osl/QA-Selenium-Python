import datetime
import re
from selenium import webdriver
import os
import random
import time


class OpenSiteWithHighlandTheme():

    baseURL = "http://moslizlo.myrealestateplatform.xyz/"
    def open(self):
        # Setting webdriver
        driverLocation = "C:\\bin\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome()
        # Open site in maximalize window
        screen_name = self.urlify(self.datetime_now(str(self.open.__name__))) + '.png'
        try:
            driver.maximize_window()
            driver.get("https://johnsnow.myrealestateplatform.net")
            driver.find_element_by_xpath("/html//p[@id='site-title']/span[@class='full']")
            time.sleep(2)
        except:
            print("Awaryjne wyjście z programu, nie udało się otworzyć strony")
            driver.save_screenshot("D:\\Python\AutomateHighland\\AutomateHighland\\Screenshots\\%s" % screen_name)
            exit();

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
