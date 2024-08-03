import re
import allure_commons
import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType
from selenium import webdriver
URL = "https://test-qa.inlaze.com/auth/sign-in"
class GlobalScripts:
    
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def setUp(self):
        self.driver.get(URL)
        allure.attach(self.driver.get_screenshot_as_png(), name="open_web_driver", attachment_type=AttachmentType.PNG)
        self.driver.maximize_window()
        
    def selectSignUpButton(self):
        self.driver.find_element(By.XPATH, "//a[@class='font-bold text-primary'][contains(.,'Sign up')]").click()
        allure.attach(self.driver.get_screenshot_as_png(), name="select_signup_button", attachment_type=AttachmentType.PNG)

    def putNameField(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,  "//input[contains(@formcontrolname,'fullName')]"))).send_keys(name)
        allure.attach(self.driver.get_screenshot_as_png(), name="put_name_field", attachment_type=AttachmentType.PNG)
            
            
    def nameFieldValidation(self, name):
        try:
            name_element  =  WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//input[contains(@formcontrolname,'fullName')]")))
            name_element.send_keys(name)
            allure.attach(self.driver.get_screenshot_as_png(), name="put_name_field", attachment_type=AttachmentType.PNG)
            if not isinstance(name, str) or len(name) < 2:
                self.driver.quit()
                return None
            
            return name_element.get_attribute("value")
                
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")
            print("El campo de nombre no se encontró o no fue visible a tiempo")
            self.driver.quit()
            return None
    
    def emailFieldValidation(self, email):
        try:
            email_element  =  WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//input[@type='email']")))
            email_element.send_keys(email)
            allure.attach(self.driver.get_screenshot_as_png(), name="put_email_field", attachment_type=AttachmentType.PNG)
            email_value =email_element.get_attribute("value")
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if not re.match(email_regex, email_value):
               print("The email format is not valid")
               self.driver.quit()
               return None
            return email_value
        
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")
            print("The email field is not visible or not found")
            self.driver.quit()
            return None  
    
    def passwordFieldValidation(self, password):
        try:
            password_element  =  WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//input[@autocomplete='password']")))
            password_element.clear()
            password_element.send_keys(password)
            allure.attach(self.driver.get_screenshot_as_png(), name="put_password_field", attachment_type=AttachmentType.PNG)
            password_value =password_element.get_attribute("value")
            password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
            
            if not re.match(password_regex, password_value):
               print("The password format is not valid")
               self.driver.quit()
               return None
            return password_value
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")
            print("The password field is not visible or not found")
            self.driver.quit()
            return None
    
    def passwordConfirmationFieldValidation(self, password):
        try:
            confirm_password_element  =  WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//input[contains(@autocomplete,'confirm-password')]")))
            confirm_password_element.clear()
            confirm_password_element.send_keys(password)
            allure.attach(self.driver.get_screenshot_as_png(), name="confirm_password_field", attachment_type=AttachmentType.PNG)
            password_value =confirm_password_element.get_attribute("value")
            password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
            
            if not re.match(password_regex, password_value):
               print("The password format is not valid")
               self.driver.quit()
               return None
           
            if password_value != password:
               print("The password confirmation does not match the password")
               self.driver.quit()
               return None
            return password_value
        
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")
            print("The password field is not visible or not found")
            self.driver.quit()
            return None
    
    def selectLoginButton(self):
        try:
            self.driver.find_element(By.XPATH("//a[@href='/auth/sign-in']").click())
            allure.attach(self.driver.get_screenshot_as_png(), name="select_login_button", attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            print("Login button not found")
            self.driver.quit()
    
    def signUpButtonIsEnabled(self):
        try:
            signUpEnabled = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//button[@type='submit'][contains(.,'Sign up')]"))
                )
            allure.attach(self.driver.get_screenshot_as_png(), name="sign_up_button_is_enabled", attachment_type=AttachmentType.PNG)
            return signUpEnabled.is_enabled()
        
        except NoSuchElementException:
            print("Sign up button is not found or is not enabled")
            allure.attach(self.driver.get_screenshot_as_png(), name="sign_up_button_is_not_enabled", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            return False
    
    def tearDown(self):
        self.driver.quit()