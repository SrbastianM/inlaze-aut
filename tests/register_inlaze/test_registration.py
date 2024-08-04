import re
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')))
from global_scripts import GlobalScripts

load_dotenv()

base_url = os.getenv("BASE_URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def test_register_name_field__has_at_least_two_words():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    try:
        name_value = driver.nameFieldValidation("Jhon Doe")
        assert name_value is not None, "Name field was not filled"
        assert len(name_value.split(" ")) >= 2, "Name field must contain at least two words"
    finally:
        driver.tearDown()

def test_name_register_is_not_field():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    name_value = driver.nameFieldValidation("")
    assert name_value is None, "Name field was not filled"
    
def test_register_email_field_contain_standard_format():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    email_value = driver.emailFieldValidation("pera@pera.com")
    assert email_value is not None, "Email field was not filled"
    assert re.match (r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_value), "Email field does not contain a valid email address"
    
    driver.tearDown()
def test_register_email_field_not_contain_standard_format():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    email_value = driver.emailFieldValidation("pera")
    assert email_value is None, "Email field was incorrectly filled with a standard format"
    driver.tearDown()
def test_password_field_contains_standard_format():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    password_value = driver.passwordFieldValidation(password)
    assert password_value is not None, "Password field was not filled"
    driver.tearDown()
    
def test_confirm_password_field_matches_with_password():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    
    password_value = driver.passwordFieldValidation(password)
    assert password_value is not None, "Password field was not filled"
    
    confirm_password_value = driver.passwordConfirmationFieldValidation(password)
    assert confirm_password_value is not None, "Password field was not filled"
    
    driver.tearDown()

def test_checks_if_all_fields_are_filled():
    driver = GlobalScripts()
    driver.setUp()
    driver.selectSignUpButton()
    
    name_value = driver.nameFieldValidation("Jhon Doe")
    assert name_value is not None, "Name field was not filled"
    
    email_value = driver.emailFieldValidation("pera@pera.com")
    assert email_value is not None, "Email field was not filled"
    
    password_value = driver.passwordFieldValidation(password)
    assert password_value is not None, "Password field was not filled"
    
    confirm_password_value = driver.passwordConfirmationFieldValidation(password)
    assert confirm_password_value is not None, "Password field was not filled"
    
    signUpEnabled = driver.signUpButtonIsEnabled()
    assert signUpEnabled, "Sign up button is not enabled"
    
    driver.tearDown()