from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Helpers:

    def __init__(self):
        pass

    def userLogin(self, driver):
        wait = WebDriverWait(driver, 10)

        Username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        Username.clear()
        Username.send_keys("andyw@vitrium.com")

        Password = wait.until(EC.presence_of_element_located((By.ID, "password")))
        Password.clear()
        Password.send_keys("admin")

        Login = wait.until(EC.presence_of_element_located((By.ID, "login")))
        Login.click()

    def addDrmPolicy(self):
        pass