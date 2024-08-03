import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver
URL = "https://test-qa.inlaze.com/auth/sign-in"
class GlobalScripts:
    
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def setUp(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        
    def selectSignUpButton(self):
        try:
            self.driver.find_element(By.XPATH("//a[@class='font-bold text-primary'][contains(.,'Sign up')]").click())
        except NoSuchElementException:
            print("Sign up button not found")
            self.driver.quit()
            
    def nameFieldValidation(self, name):
        name_element = self.driver.find_element(By.XPATH,  "//input[contains(@formcontrolname,'fullName')]")
        name_element.send_keys(name)
        try:
            if not  isinstance(name, str) or len(name) < 2:
                print("Name field must be at least 2 characters long")
                self.driver.quit()
        except NoSuchElementException:
            print("Name field not found")
            self.driver.quit()
        
    def selectLoginButton(self):
        try:
            self.driver.find_element(By.XPATH("//a[@href='/auth/sign-in']").click())
        except NoSuchElementException:
            print("Login button not found")
            self.driver.quit()
            
    
    def tearDown(self):
        self.driver.quit()
    