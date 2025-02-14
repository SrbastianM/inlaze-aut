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
    
    def selectSignInButton(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Sign in')]").click()
        allure.attach(self.driver.get_screenshot_as_png(), name="select_signin_button", attachment_type=AttachmentType.PNG)

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
    
    def emailLoginFieldValidation(self, email):
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
            login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit'][contains(.,'Sign in')]")))
            login_button.click()
            allure.attach(self.driver.get_screenshot_as_png(), name="select_login_button", attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            print("Login button not found")
            self.driver.quit()
    
    def signUpButtonIsEnabled(self):
        try:
            signUpEnabled = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//button[@type='submit'][contains(.,'Sign up')]"))
                )
            signUpEnabled.click()
            allure.attach(self.driver.get_screenshot_as_png(), name="sign_up_button_is_enabled", attachment_type=AttachmentType.PNG)
            return signUpEnabled.is_enabled()
        
        except NoSuchElementException:
            print("Sign up button is not found or is not enabled")
            allure.attach(self.driver.get_screenshot_as_png(), name="sign_up_button_is_not_enabled", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            return False
    
    def enterRegistrationDetails(self, name, email, password, confirm_password):
        self.driver.find_element(By.XPATH, "//input[contains(@formcontrolname,'fullName')]").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@autocomplete='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[contains(@autocomplete,'confirm-password')]").send_keys(confirm_password)
    
    def signUpPage(self):
        try:
            is_on_signup_page = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//h1[@class='text-4xl font-extrabold mb-4'][contains(.,'Sign up')]"))
            )
            allure.attach(self.driver.get_screenshot_as_png(), name="search_page", attachment_type=AttachmentType.PNG)
            return is_on_signup_page
        except NoSuchElementException:
            print("Sign up page is not found")
            allure.attach(self.driver.get_screenshot_as_png(), name="search_page", attachment_type=AttachmentType.PNG)
            self.driver.quit()
        
    def isUserRegistered(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//div[@class='ml-3 text-sm font-normal'][contains(.,'Successful registration!')]"))
            )
            allure.attach(self.driver.get_screenshot_as_png(), name="success_registration", attachment_type=AttachmentType.PNG)
            return True
        except NoSuchElementException:
            print("Alert is not found or is not enabled")
            allure.attach(self.driver.get_screenshot_as_png(), name="unsuccess_registration", attachment_type=AttachmentType.PNG)
            return False
        finally:
            self.driver.quit()
    def userAlreadyRegistered(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//div[@class='ml-3 text-sm font-normal'][contains(.,'Successful registration!')]"))
            )
            allure.attach(self.driver.get_screenshot_as_png(), name="user_duplicated_in_database", attachment_type=AttachmentType.PNG)
            print("User is already registered")
            return False
        except NoSuchElementException:
            try: 
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'User already exists')]"))
                )
                print("User Already registered")
                allure.attach(self.driver.get_screenshot_as_png(), name="user_already_registered", attachment_type=AttachmentType.PNG)
                return False
            except NoSuchElementException:
                print("No registration message status found")
                allure.attach(self.driver.get_screenshot_as_png(), name="user_already_registered", attachment_type=AttachmentType.PNG)
                return False
        finally:
            self.driver.quit()

    def userNotFound(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//div[@class='ml-3 text-sm font-normal'][contains(.,'User not found')]"))
            )
            allure.attach(self.driver.get_screenshot_as_png(), name="user_not_found", attachment_type=AttachmentType.PNG)
            return True
        except NoSuchElementException:
            print("User not found message not found")
            allure.attach(self.driver.get_screenshot_as_png(), name="user_not_found", attachment_type=AttachmentType.PNG)
            return False
        finally:
            self.driver.quit()
   
    def isUserLoggedIn(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,  "//h2[@class='text-center font-extrabold text-5xl mb-4 text-transparent bg-clip-text bg-gradient-to-r from-primary to-cyan-500'][contains(.,'Welcome to Lorem')]"))
            )
            allure.attach(self.driver.get_screenshot_as_png(), name="success_login", attachment_type=AttachmentType.PNG)
            return True
        
        except NoSuchElementException:
            print("User is not logged in")
            allure.attach(self.driver.get_screenshot_as_png(), name="unsuccess_login", attachment_type=AttachmentType.PNG)
            return False
        finally:
            self.driver.quit()
    
    def logout(self):
        try:
            logout_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Rengoku']")))
            logout_button.click()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="logout_image", attachment_type=AttachmentType.PNG)
            logout_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Logout')]")))
            logout_link.click()
            allure.attach(self.driver.get_screenshot_as_png(), name="logout_link", attachment_type=AttachmentType.PNG)
            self.driver.quit()
        except NoSuchElementException:
            print("Logout button not found")
            self.driver.quit()
    
    def enterLoginDetails(self, email, password):
        email_field = self.driver.find_element(By.XPATH, "//input[contains(@type,'email')]")
        password_field = self.driver.find_element(By.XPATH, "//input[contains(@class,'input input-bordered join-item w-full')]")
        email_field.send_keys(email)
        password_field.send_keys(password)
        
    def tearDown(self):
        self.driver.quit()