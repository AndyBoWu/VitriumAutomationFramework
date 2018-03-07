import unittest
import os
import time
from selenium import webdriver
from Variables import VariableClass as V
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Helpers import Helpers
from selenium.webdriver.support.ui import Select

import pyautogui

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions


class BVT_TestCases(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.chromedriver = r"C:\Users\andyw\Dropbox\Learning\Automation\ui\chromedriver"
        os.environ["webdriver.chrome.driver"] = self.chromedriver
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.maximize_window()

    def tearDown(self):
        print('tearDown\n')


    '''
    Forgot your password
    
    1. Go to Outlook System folder to check out the automatically generated email
    2. Click the URL, and change the password
    
    '''

    # def test_forgotPassword(self):
    #     print('TC - Forgot your password...')
    #     # h = Helpers()
    #     # h.userLogin(driver)
    #     self.driver.maximize_window()
    #     wait = WebDriverWait(self.driver, 20)
    #
    #     self.driver.get(V.stagingUrl)
    #     wait.until(EC.presence_of_element_located((By.LINK_TEXT, V.forgotPwd))).click()
    #     (wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.uName)))).send_keys(V.AndyEmail)
    #     time.sleep(1)
    #     wait.until(EC.presence_of_element_located((By.XPATH, V.requestBtn))).click()

    '''
    Learn More Button

    1. 

    '''

    # def test_LearnMoreBtn(self):
    #     print('TC - Learn more button...')
    #     # h = Helpers()
    #     # h.userLogin(driver)
    #     self.driver.maximize_window()
    #     wait = WebDriverWait(self.driver, 20)
    #
    #     self.driver.get(V.stagingUrl)
    #     wait.until(EC.presence_of_element_located((By.LINK_TEXT, V.learnMoreBtn))).click()

    '''
    Add Login Form

    1. 
    
    '''

    def test_AddLoginForm(self):
        print('TC - Add Login Form...')
        self.wait = WebDriverWait(self.driver, 20)
        h = Helpers()
        h.userLogin(self.driver, 'user')
        time.sleep(1)

        self.driver.get(V.loginFormUrl)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addLoginFormBtn))).click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, V.uploadLoginForm))).click()
        time.sleep(1)
        pyautogui.typewrite(r"F:\Login Forms\LOGIN PAGES TEMPLATES\new-login.pdf")
        time.sleep(1)
        pyautogui.keyDown('enter')
        time.sleep(1)

        self.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()

    '''
    Test Case Sensitive Password - 1
    
    Test Case: 
    1. Create an user cs || cs
    2. (cs || cs) can unlock a document in webviewer and pdf
    3. (cs || CS) can NOT unlock the document 
    '''


    '''
    Test Case Sensitive Password - 2

    Test Case: 
    1. Create an user cs || cs
    2. (cs || CS) can unlock the document TOO!
    '''



    '''
    Define Support URL and Adjust Time Zone
    Set Support URL to: https://www.apple.com/ca/
    Set time zone to:   Pacific Time (-08:00)
    
    '''



    '''
    Test the functionality to delete users
    
    '''




    '''
    Test the functionality to delete watermarks
    
    
    '''



    '''
    Test the functionality to delete groups
    
    '''



    '''
    Test the functionality to DELETE documents
    
    '''


    '''
    Test the functionality to DEACTIVE a document
    
    '''





    '''
    Test 'Disable Webviewer' in super admin UI
    
    '''


    '''
    Test the functionality to deactive an account on super admin UI
    '''


    '''
    Test 'Pages to leave unprotected' functionality
    '''



    '''
    Test 'Disable Web Viewer' in Content Protection UI
    
    '''



    '''
    Test floating login form in ADOBE READER
    
    Tips: 1. Update 'UseFloatingForms' in the tblPub table in API DB from FALSE to TRUE
    
    '''

    '''
    Test web viewer login form
    
    '''



    '''
    Test 'Keep me logged in' DEV-948
    Grant marked this bug 'INVALID' on Feb 26, 2018
    '''

    '''
    Test to add an Enterprise Account
    '''

    # def test_AddEntAccount(self):
    #     print('TC - Add Enterprise Account...')
    #     self.wait = WebDriverWait(self.driver, 20)
    #     h = Helpers()
    #     h.userLogin(self.driver, 'admin')
    #
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addAccountBtn))).click()
    #
    #     # Account Name
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='Name']"))).send_keys("AndyEnt")
    #
    #     # EIP URL
    #     selectEipUrl = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='EipUrl']"))))
    #     selectEipUrl.select_by_visible_text("Custom URL")
    #
    #     # Account Type
    #     selectAccountType = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='AccountType']"))))
    #     selectAccountType.select_by_visible_text("Enterprise Edition")
    #
    #     # Custom EIP URL
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='CustomUrl']"))).send_keys(V.CustomEipUrl)
    #
    #     # Enable Download to Print
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='DownloadToPrintEnabled']"))).click()
    #
    #     time.sleep(1)
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()


    # def test_AddJsonApiAccount(self):
    #     print('TC - Adding a JsonApi Account...')
    #     self.wait = WebDriverWait(self.driver, 20)
    #     h = Helpers()
    #     h.userLogin(self.driver, 'admin')
    #
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addAccountBtn))).click()
    #
    #     # Account Name
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='Name']"))).send_keys("JsonApi")
    #
    #     # EIP URL
    #     selectEipUrl = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='EipUrl']"))))
    #     selectEipUrl.select_by_visible_text("Custom URL")
    #
    #     # Account Type
    #     selectAccountType = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='AccountType']"))))
    #     selectAccountType.select_by_visible_text("Enterprise Edition")
    #
    #     # Custom EIP URL
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='CustomUrl']"))).send_keys(V.CustomEipUrl)
    #
    #     # Enable Download to Print
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='DownloadToPrintEnabled']"))).click()
    #
    #     time.sleep(1)
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()

    # def test_AddProAccount(self):
    #     print('TC - Adding a Professional Account...')
    #     self.wait = WebDriverWait(self.driver, 20)
    #     h = Helpers()
    #     h.userLogin(self.driver, 'admin')
    #
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addAccountBtn))).click()
    #
    #     # Account Name
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='Name']"))).send_keys("AndyPro")
    #
    #     # EIP URL
    #     selectEipUrl = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='EipUrl']"))))
    #     selectEipUrl.select_by_visible_text("Custom URL")
    #
    #     # Account Type
    #     selectAccountType = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='AccountType']"))))
    #     selectAccountType.select_by_visible_text("Pro Edition")
    #
    #     # Custom EIP URL
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='CustomUrl']"))).send_keys(V.CustomEipUrl)
    #
    #     # Enable Download to Print
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='DownloadToPrintEnabled']"))).click()
    #
    #     time.sleep(1)
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()

    # def test_AddStdAccount(self):
    #     print('TC - Adding a Standard Account...')
    #     self.wait = WebDriverWait(self.driver, 20)
    #     h = Helpers()
    #     h.userLogin(self.driver, 'admin')
    #
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, V.addAccountBtn))).click()
    #
    #     # Account Name
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='Name']"))).send_keys("AndyStd")
    #
    #     # EIP URL
    #     selectEipUrl = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='EipUrl']"))))
    #     selectEipUrl.select_by_visible_text("Custom URL")
    #
    #     # Account Type
    #     selectAccountType = Select(self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[id$='AccountType']"))))
    #     selectAccountType.select_by_visible_text("Standard Edition")
    #
    #     # Custom EIP URL
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='CustomUrl']"))).send_keys(V.CustomEipUrl)
    #
    #     # Enable Download to Print
    #     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='DownloadToPrintEnabled']"))).click()
    #
    #     time.sleep(1)
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, V.saveBtn))).click()



    '''
    Test Printing. Web : 2; Download : 3 
    '''


