import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
from datetime import timedelta


from selenium.webdriver.common.action_chains import ActionChains

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
        wmNameElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, V.watermarkName)))
        wmNameElem[0].send_keys(name)

        # define watearmark text
        wmTextElem = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.watermarkText)))
        wmTextElem.send_keys(wmText)

        # Save and Exit
        saveBtn = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn)))
        saveBtn.click()

    def addPolicy(self, policyName, expiryDate, expiryAfterUnlock, offlineAccess, OpenLimit, totalLimit, pdfLimit, browserLimit, webPrint, downloadPrint, accountLimit, ipLimit):

        Automations.driver.get(V.drmPolicyUrl)

        # 'ADD DRM POLICY' button
        RunAutomation.wait.until(EC.presence_of_element_located((By.XPATH, V.addDRMBtn))).click()

        policyNameElem = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.policyNameField)))
        policyNameElem.send_keys(policyName)

        time.sleep(1)

        # Expiry Date
        if expiryDate == 'Never':
            ExpiryDateElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'ExpiryF')]")))
            ExpiryDateElem[1].click()
        elif expiryDate != 'Not Set':
            ExpiryDateElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'date-picker-group')))
            ActionChains(Automations.driver).move_to_element(ExpiryDateElem[0]).click().send_keys(expiryDate).perform()

        # Expiry After First Unlock
        # if expiryDate == 'Never':
        #     ExpiryDateElem = Automations.wait.until(
        #         EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'ExpiryF')]")))
        #     ExpiryDateElem[1].click()
        # elif expiryDate != 'Not Set':
        #     ExpiryDateElem = Automations.wait.until(
        #         EC.presence_of_all_elements_located((By.CLASS_NAME, 'date-picker-group')))
        #     ActionChains(Automations.driver).move_to_element(ExpiryDateElem[0]).click().send_keys(
        #         expiryDate).perform()




        # Expiry After First Unlock


        # Offline Access


        # Content Open Limit




if __name__ == "__main__":

    # Tomorrow
    tomorrow = datetime.datetime.strptime(str(datetime.date.today() + timedelta(days=1)), '%Y-%m-%d').strftime('%m/%d/%Y')
    print(tomorrow)

    RunAutomation = Automations()



    # Create a DRM policy
    RunAutomation.addPolicy('Unlimited', tomorrow, 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test')


    # Create User Spcific watermarks
    # RunAutomation.addWatermarks('us', 'Test User ID', '_userId_')
    # RunAutomation.addWatermarks('us', 'Test User Name', '_userName_')
    # RunAutomation.addWatermarks('us', 'Test Date', '_date_')
    # RunAutomation.addWatermarks('us', 'Test Time', '_time_')
    # RunAutomation.addWatermarks('us', 'Test Document Code', '_docCode_')
    # RunAutomation.addWatermarks('us', 'Test Computer ID', '_computerId_')
    # RunAutomation.addWatermarks('us', 'Test New Line', '_newLine_')
    # RunAutomation.addWatermarks('us', 'Test User Custom Field', '_readerCustomField_')
    # RunAutomation.addWatermarks('us', 'Test User External Key', '_readerExternalKey_')
    # RunAutomation.addWatermarks('us', 'Test Unique Open ID', '_unique_open_id_')

    # Create Text Only Watermark








    # RunAutomation.addDrmPolicy("Unlimited")