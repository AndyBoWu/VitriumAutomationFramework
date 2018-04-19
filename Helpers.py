import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Variables import VariableClass as V

class Helpers:

    def __init__(self):
        pass

    '''
    type: user || admin
    '''
    def userLogin(self, driver, type):

        wait = WebDriverWait(driver, 20)

        driver.get(V.stagingUrl)

        Username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        # Username.clear()

        Password = wait.until(EC.presence_of_element_located((By.ID, "password")))
        # Password.clear()

        if type == 'user':
            Password.send_keys(V.passWord)
            Username.send_keys(V.userName)
        elif type == 'admin':
            Username.send_keys(V.AndyEmail)
            Password.send_keys(V.AndyPassword)

        Login = wait.until(EC.presence_of_element_located((By.ID, "login")))
        Login.click()


    def addDrmPolicy(self):
        pass