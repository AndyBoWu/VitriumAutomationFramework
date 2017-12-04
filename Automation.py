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
        wmNameElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[id$='Name']")))
        wmNameElem[0].send_keys(name)

        # define watearmark text
        wmTextElem = Automations.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='e.g. Unlocked by John Smith']")))
        wmTextElem.send_keys(wmText)

        # Save and Exit
        saveBtn = Automations.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-action='save']")))
        saveBtn.click()

if __name__ == "__main__":
    RunAutomation = Automations()


    # Create User Spcific watermarks
    RunAutomation.addWatermarks('us', 'Test User ID', '_userId_')
    RunAutomation.addWatermarks('us', 'Test User Name', '_userName_')
    RunAutomation.addWatermarks('us', 'Test Date', '_date_')
    RunAutomation.addWatermarks('us', 'Test Time', '_time_')
    RunAutomation.addWatermarks('us', 'Test Document Code', '_docCode_')
    RunAutomation.addWatermarks('us', 'Test Computer ID', '_computerId_')
    RunAutomation.addWatermarks('us', 'Test New Line', '_newLine_')
    RunAutomation.addWatermarks('us', 'Test User Custom Field', '_readerCustomField_')
    RunAutomation.addWatermarks('us', 'Test User External Key', '_readerExternalKey_')
    RunAutomation.addWatermarks('us', 'Test Unique Open ID', '_unique_open_id_')

    # Create Text Only Watermark



    # Create an unlimited DRM policy
    # RunAutomation.addDrmPolicy("Unlimited")