import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Variables import Variables
from Helpers import Helpers

class Automations:

    def __init__(self):
        chromedriver = r"C:\Users\andyw\Dropbox\Learning\Automation\ui\chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        h = Helpers(driver)
        h.userLogin()

    def addDrmPolicy(self, name):

        pass










if __name__ == "__main__":
    RunAutomation = Automations()
    # Create an unlimited DRM policy
    RunAutomation.addDrmPolicy("Unlimited")