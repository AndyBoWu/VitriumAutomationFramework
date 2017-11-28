import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Helpers import Helpers
from Variables import VariableClass as V

class Automations:

    chromedriver = r"C:\Users\andyw\Dropbox\Learning\Automation\ui\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    h = Helpers()
    h.userLogin(driver)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    def __init__(self):
        pass

    def addWatermarks(self, wmType, name, wmText):

        Automations.driver.get(V.watermarkUrl)

        # 'ADD WATERMARK' button
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addWmBtn))).click()

        if wmType == 'to':
            pass

        # define watermark name
        wmName = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[id$='Name']")))
        wmName[0].clear()
        wmName[0].send_keys(name)

        #
        wmText = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder='e.g. Unlocked by John Smith']")))
        wmText[0].clear()
        wmText[0].send_keys(wmText)








if __name__ == "__main__":
    RunAutomation = Automations()


    # Create User Spcific watermarks
    RunAutomation.addWatermarks('us', 'Test User ID', '_userId_')
    # RunAutomation.addWatermarks('us', 'Test User Name')
    # RunAutomation.addWatermarks('us', 'Test Date')
    # RunAutomation.addWatermarks('us', 'Test Time')
    # RunAutomation.addWatermarks('us', 'Test Document Code')
    # RunAutomation.addWatermarks('us', 'Test Computer ID')
    # RunAutomation.addWatermarks('us', 'Test New Line')
    # RunAutomation.addWatermarks('us', 'Test User Custom Field')
    # RunAutomation.addWatermarks('us', 'Test User External Key')
    # RunAutomation.addWatermarks('us', 'Test Unique Open ID')

    # Create Text Only Watermark



    # Create an unlimited DRM policy
    # RunAutomation.addDrmPolicy("Unlimited")