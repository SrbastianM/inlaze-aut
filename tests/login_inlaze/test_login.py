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

def test_login_name_field__has_at_least_two_words():
    driver = GlobalScripts()
    driver.setUp()
    try:
        email_value = driver.emailLoginFieldValidation(email)
        assert email_value is not None, "Name field was not filled"
    finally:
        driver.tearDown()

def test_password_field_is_valid():
    driver = GlobalScripts()
    driver.setUp()
    try:
        password_value = driver.passwordFieldValidation(password)
        assert password_value is not None, "Password field was not filled"
    finally:
        driver.tearDown()

def test_email_field_is_field_but_not_valid():
    driver = GlobalScripts()
    driver.setUp()
    try:
        email_value = driver.emailLoginFieldValidation("pera")
        assert email_value is None, "Email field was incorrectly filled with a standard format"
    finally:
        driver.tearDown()

def test_password_field_is_field_but_not_valid():
    driver = GlobalScripts()
    driver.setUp()
    try:
        password_value = driver.passwordFieldValidation("pera")
        assert password_value is None, "Password field was incorrectly filled with a standard format"
    finally:
        driver.tearDown()
        
def test_all_the_fields_are_filled():
    driver = GlobalScripts()
    driver.setUp()
    try:
        email_value = driver.emailLoginFieldValidation(email)
        password_value = driver.passwordFieldValidation(password)
        assert email_value is not None, "Email field was not filled"
        assert password_value is not None, "Password field was not filled"
    finally:
        driver.tearDown()

def test_login_complete():
    driver = GlobalScripts()
    driver.setUp()
    try:
        driver.enterLoginDetails(email, password)
        driver.selectLoginButton()
        driver.logout()
    finally:
        driver.tearDown()