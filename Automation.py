import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
from datetime import timedelta
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

from Helpers import Helpers
from Variables import VariableClass as V

import pyautogui

class Automations:

    chromedriver = r"C:\Users\andyw\Dropbox\Learning\Automation\ui\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    h = Helpers()
    h.userLogin(driver, 'user')
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    def __init__(self):
        pass

    # Add an account
    def AddAccount(self, AccountName, AccountType, EnableDownloadPrint):
        print("...Adding a " + AccountName + " Account...")

        chromedriver = r"C:\Users\andyw\Dropbox\Learning\Automation\ui\chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)

        h = Helpers()
        h.userLogin(driver, 'admin')
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 20)

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addAccountBtn))).click()

        # Account Name
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='Name']"))).send_keys(AccountName)

        # EIP URL
        selectEipUrl = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='EipUrl']"))))
        selectEipUrl.select_by_visible_text("Custom URL")

        # Account Type
        selectAccountType = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='AccountType']"))))
        if AccountType == "Ent":
            selectAccountType.select_by_visible_text("Enterprise Edition")
        elif AccountType == "Pro":
            selectAccountType.select_by_visible_text("Pro Edition")
        elif AccountType == "Std":
            selectAccountType.select_by_visible_text("Standard Edition")

        # Custom EIP URL
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='CustomUrl']"))).send_keys(V.CustomEipUrl)

        # Enable Download to Print
        if EnableDownloadPrint:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='DownloadToPrintEnabled']"))).click()

        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()
        print("...Successful!!\n")

    # ADD WATERMARKS
    def addWatermarks(self, wmType, name, wmText, placement):

        Automations.driver.get(V.watermarkUrl)

        # 'ADD WATERMARK' button
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addWmBtn))).click()

        if wmType == 'to':
            select = Select(Automations.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='SetContentAt']"))))
            select.select_by_value("DocumentProcessingTime")

            # define watermark name
            wmNameElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, V.watermarkName)))
            wmNameElem[0].send_keys(name)

            # define watermark text
            wmTextElem = Automations.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='e.g. CONFIDENTIAL']")))
            wmTextElem.send_keys(wmText)

            # define placement
            if placement == 'up':
                upPosition = Automations.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-id='up']")))
                upPosition.click()
            elif placement == 'down':
                downPosition = Automations.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-id='down']")))
                downPosition.click()

            # Save and Exit
            time.sleep(2)
            saveBtn = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn)))
            saveBtn.click()


        elif wmType == 'us':
            # define watermark name
            wmNameElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, V.watermarkName)))
            wmNameElem[0].send_keys(name)

            # define watermark text
            wmTextElem = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.watermarkText)))
            wmTextElem.send_keys(wmText)

            # Save and Exit
            time.sleep(2)
            saveBtn = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn)))
            saveBtn.click()

    def addPolicy(self, policyName, expiryDate, expiryAfterUnlock, offlineAccess, OpenLimit, totalLimit, pdfLimit, browserLimit, webPrint, downloadPrint, accountLimit, ipLimit):

        Automations.driver.get(V.drmPolicyUrl)

        # 'ADD DRM POLICY' button
        RunAutomation.wait.until(EC.presence_of_element_located((By.XPATH, V.addDRMBtn))).click()

        policyNameElem = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.policyNameField)))
        policyNameElem.send_keys(policyName)

        time.sleep(1)


        ################### EXPIRATION CONTROL ###################

        # Expiry Date
        if expiryDate == 'Never':
            ExpiryDateElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'ExpiryF')]")))
            ExpiryDateElem[1].click()
        elif expiryDate != 'Not Set':
            ExpiryDateElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'date-picker-group')))
            ActionChains(Automations.driver).move_to_element(ExpiryDateElem[0]).click().send_keys(expiryDate).perform()

        # Expiry After First Unlock
        ExpiryUnlockElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'RelativeExpiryInDaysF')]")))
        if expiryAfterUnlock == 'Never':
            ExpiryUnlockElem[1].click()
        elif expiryAfterUnlock != 'Not Set':
            ActionChains(Automations.driver).move_to_element(ExpiryUnlockElem[2]).click().send_keys(expiryAfterUnlock).perform()


        ################### ACCESS CONTROL ###################

        # Offline Access
        offineAccessElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'OfflineDurationinDaysF')]")))
        if offlineAccess == 'Never':
            offineAccessElem[1].click()
        elif offlineAccess != 'Not Set':
            ActionChains(Automations.driver).move_to_element(offineAccessElem[2]).click().send_keys(offlineAccess).perform()

        # Content Open Limit
        openLimitElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'OpenLimitF')]")))
        if offlineAccess == 'Never':
            openLimitElem[1].click()
        elif offlineAccess != 'Not Set':
            ActionChains(Automations.driver).move_to_element(openLimitElem[2]).click().send_keys(OpenLimit).perform()

        ################### PDF/BROWSER CONTROL ###################

        totalLimitElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'ComputersMaxF')]")))
        if totalLimit == 'Never':
            totalLimitElem[1].click()
        elif totalLimit != 'Not Set':
            ActionChains(Automations.driver).move_to_element(totalLimitElem[2]).click().send_keys(totalLimit).perform()


        ################### PRINT CONTROL ###################

        # Web Browser Print Limit
        webPrintLimitElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'WebPrintLimitF')]")))
        if webPrint == 'Never':
            webPrintLimitElem[1].click()
        elif webPrint != 'Not Set':
            ActionChains(Automations.driver).move_to_element(webPrintLimitElem[2]).click().send_keys(webPrint).perform()


        # Download to Print Limit
        # It took me a while to figure out the following xpath expression!!
        downloadPrintLimitElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'PrintLimitF') and not(contains(@name, 'WebPrintLimitF'))]")))
        if downloadPrint == 'Never':
            downloadPrintLimitElem[1].click()
        elif downloadPrint != 'Not Set':
            ActionChains(Automations.driver).move_to_element(downloadPrintLimitElem[2]).click().send_keys(downloadPrint).perform()


        ################### OTHER CONTROLS ###################

        # Library or Account Limit
        accountLimitElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'DocumentLimitF')]")))
        if accountLimit == 'Never':
            accountLimitElem[1].click()
        elif accountLimit != 'Not Set':
            ActionChains(Automations.driver).move_to_element(accountLimitElem[2]).click().send_keys(accountLimit).perform()

        # IP Address Limit
        ipLimitElem = Automations.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@name, 'IpAddressesMaxF')]")))
        if ipLimit == 'Never':
            ipLimitElem[1].click()
        elif ipLimit != 'Not Set':
            ActionChains(Automations.driver).move_to_element(ipLimitElem[2]).click().send_keys(ipLimit).perform()

        time.sleep(2)
        Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()


    def addContentSettings(self, csType, name, allowPrinting, allowCP, selectWatermark, disableAnnotation, casePassword):

        Automations.driver.get(V.contentSettingsUrl)

        # 'ADD SETTINGS' button
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addCSBtn))).click()

        # define name of Content Settings
        csNameElem = Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='Name']")))
        csNameElem.send_keys(name)

        # Allow Printing
        if allowPrinting == 'true':
            Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='AllowPrint']"))).click()

        # Allow copy and paste
        if allowCP == 'true':
            Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='AllowCopy']"))).click()


        # Select Login Form
        selectLoginForm = Select(Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='FormId']"))))
        selectLoginForm.select_by_visible_text("new-login")


        # Select first watermark
        selectWatermark = Select(Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id^='MultipleSelectionForm']"))))
        selectWatermark.select_by_visible_text('Test Computer ID')

        # TODO: select more watermarks

        # go to the next Tab
        Automations.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Advanced Options"))).click()

        # disable annotation
        if disableAnnotation == 'true':
            Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='DisableAnnotations']"))).click()

        # if using a non-Case Sensitive password
        if casePassword == 'false':
            Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='CaseSensitivePassword']"))).click()

        time.sleep(2)
        saveBtn = Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn)))
        saveBtn.click()

    # ADD SINGLE USERS
    def addSingleUsers(self, name, password, notes, externalKey, customField):

        Automations.driver.get(V.usersUrl)
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addSingleUserBtn))).click()

        uNameElem = Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.uName)))
        uNameElem.send_keys(name)

        uPasswordElem = Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.uPassword)))
        uPasswordElem.send_keys(password)

        uNotesElem = Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.uNotes)))
        uNotesElem.send_keys(notes)

        uKeyElem = Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.uKey)))
        uKeyElem.send_keys(externalKey)

        uFieldElem = Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.uField)))
        uFieldElem.send_keys(customField)

        time.sleep(2)
        Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()

    # ADD MULTIPLE USERS
    def addMultipleUsers(self, name0, password0, name1, password1, name2, password2, name3, password3, name4, password4, name5, password5):

        Automations.driver.get(V.usersUrl)
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addMultipleUserBtn))).click()

        time.sleep(1)
        # Strategy: make sure the 'ADD ANOTHER' button is functional
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addOneMoreUserBtn))).click()

        uNameElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, V.uName)))
        uPasswordElem = Automations.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, V.mPassword)))

        # USER 0
        uNameElem[0].send_keys(name0)
        uPasswordElem[0].send_keys(password0)

        # USER 1
        uNameElem[1].send_keys(name1)
        uPasswordElem[1].send_keys(password1)

        # USER 2
        uNameElem[2].send_keys(name2)
        uPasswordElem[2].send_keys(password2)

        # USER 3
        uNameElem[3].send_keys(name3)
        uPasswordElem[3].send_keys(password3)

        # USER 4
        uNameElem[4].send_keys(name4)
        uPasswordElem[4].send_keys(password4)

        # USER 5
        uNameElem[5].send_keys(name5)
        uPasswordElem[5].send_keys(password5)

        time.sleep(2)
        Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()

    # Protect a content
    def protectContent(self, FilePath):
        Automations.driver.get(V.contentUrl)
        Automations.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addContentBtn))).click()
        time.sleep(2)
        Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.uploadContentBtn))).click()

        time.sleep(1)
        pyautogui.typewrite(FilePath)
        time.sleep(1)
        pyautogui.keyDown('enter')
        time.sleep(1)

        Automations.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()
        time.sleep(1)

if __name__ == "__main__":

    # Tomorrow
    tomorrow = datetime.datetime.strptime(str(datetime.date.today() + timedelta(days=1)), '%Y-%m-%d').strftime('%m/%d/%Y')
    print('The date of tomorrow is: ', tomorrow)

    RunAutomation = Automations()

    # STEP 1 - Create an Enterprise Account
    # RunAutomation.AddAccount("AndyEnt", "Ent", True)
    # RunAutomation.AddAccount("AndyPro", "Pro", True)
    # RunAutomation.AddAccount("AndyStd", "Std", True)
    # RunAutomation.AddAccount("JsonApi", "Ent", True)
    # RunAutomation.AddAccount("Inhouse", "Ent", True)
    # RunAutomation.AddAccount("WvLoginForm", "Ent", True)
    # RunAutomation.AddAccount("OAUTH2", "Ent", True)




    # [TO-DO] Manually add customer into accounts



    # Create a Professional Account

    # Create a Standard Account

    # Create a



    # STEP 2 - Create multiple DRM policies
    # addPolicy(self, policyName, expiryDate, expiryAfterUnlock, offlineAccess, OpenLimit, totalLimit, pdfLimit, browserLimit, webPrint, downloadPrint, accountLimit, ipLimit)

    # DRM Policy 1 - Unlimited
    # RunAutomation.addPolicy('Unlimited', 'Never', 'Never', 'Never', 'Never', 'Never', 'NA', 'NA', 'Never', 'Never', 'Never', 'Never')

    # DRM Policy 2 - Web Print : 2; Download Print : 3
    # RunAutomation.addPolicy('Print - Web2 - Download3', 'Never', 'Never', 'Never', 'Never', 'Never', 'NA', 'NA', '2', '3', 'Never', 'Never')


    # DRM Policy - No Offline Access
    # RunAutomation.addPolicy('No Offline Access', 'Never', 'Never', 'Not Set', 'Never', 'Never', 'NA', 'NA', '2', '3', 'Never', 'Never')

    # DRM Policy 3 - PDF_1 - Web_1
    # RunAutomation.addPolicy('PDF_1 - Web_1', 'Never', 'Never', 'Never', 'Never', 'NA', '1', '1', '2','3', 'Never', 'Never')

    # DRM Policy 4 -

    # DRM Policy 5 -


    # Create User Spcific watermarks

    # RunAutomation.addWatermarks('us', 'Test User ID', '_userId_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test User Name', '_userName_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test Date', '_date_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test Time', '_time_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test Document Code', '_docCode_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test Computer ID', '_computerId_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test New Line', '_newLine_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test User Custom Field', '_readerCustomField_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test User External Key', '_readerExternalKey_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test Unique Open ID', '_unique_open_id_', 'bc')
    # RunAutomation.addWatermarks('us', 'Test DELETE watermark', 'THIS WATERMARK WILL BE DELETED!', 'bc')
    # RunAutomation.addWatermarks('us', 'Test DELETE watermark2', 'THIS WATERMARK WILL BE DELETED!', 'bc')
    #
    # # Create Text Only Watermark
    # RunAutomation.addWatermarks('to', 'Test Text Only Watermark - CENTER', 'HELLO PYTHON - center', 'center')
    # RunAutomation.addWatermarks('to', 'Test Text Only Watermark - UP', 'HELLO PYTHON - up', 'up')
    # RunAutomation.addWatermarks('to', 'Test Text Only Watermark - DOWN', 'HELLO PYTHON - down', 'down')


    # RunAutomation.addSingleUsers('cs', 'cs', 'Created this user to test case sensitive password feature', '$ValidExternalKey$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Andy', 'Test123', 'Im the KING!!', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Ben', 'Test123', 'MBA Classmate', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Cindy', 'Test123', 'Scream Movie', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Daisy', 'Test123', 'Botanic Garden', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Eli', 'Test123', 'There will be blood!', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Frank', 'Test123', 'Everybody Loves Raymond!', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Grace', 'Test123', 'Saving Grace!', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('Hellen', 'Test123', 'Godness', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('To Be Deleted Later 1', 'Test123', 'Saving Grace!', '$Brain$', 'This is the info located in the custom field')
    # RunAutomation.addSingleUsers('To Be Deleted Later 2', 'Test123', 'Godness', '$Brain$', 'This is the info located in the custom field')

    # Add Multiple Users
    # RunAutomation.addMultipleUsers('mAndy', 'Test123', 'mBen', 'Test123', 'mCindy', 'Test123', 'mDaisy', 'Test123', 'mEli', 'Test123', 'mFrank', 'Test123')

    # Create Content Setting
    # (csType, name, allowPrinting, allowCP, selectWatermark, disableAnnotation, casePassword)
    # RunAutomation.addContentSettings('full', 'Full', 'true', 'true', 'Test Computer ID', 'false', 'true')

    # Add Single User
    # def addSingleUsers(self, name, password, notes, externalKey, customField):

    # Add GROUPS

    RunAutomation.protectContent(r"F:\Content\PDF\Test_PDF_File.pdf")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\WORD\Word2003Doc.doc")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\WORD\Word2016Docx.docx")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\Excel\Excel2003Xls.xls")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\Excel\Excel2013Xlsx.xlsx")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\PPT\PPT2003.ppt")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\PPT\PPTX2013.pptx")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\image\SYJH.jpg")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\image\PNG.png")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\image\BMP.bmp")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\image\Gif.gif")
    time.sleep(1)
    RunAutomation.protectContent(r"F:\Content\image\TIFF.tif")








