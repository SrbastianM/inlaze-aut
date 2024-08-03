import sys
import pytest
import selenium
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')))
from global_scripts import GlobalScripts

load_dotenv()

base_url = os.getenv("BASE_URL")

def test_register_name_field():
    driver = GlobalScripts()
    driver.setUp()
    
    try:
        name_value =driver.nameFieldValidation("Jhon Doe")
        assert name_value is not None, "Name field should not be empty"
        assert len(name_value.split(" ")) == 2, "Name field must be at least 2 characters long"
    finally:
        driver.tearDown()
    
    
def test_register_email_field():
    driver = GlobalScripts()
    driver.setUp()
    
    


    