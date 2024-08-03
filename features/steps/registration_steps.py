import re
import sys
import os
from dotenv import load_dotenv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')))
from global_scripts import GlobalScripts

load_dotenv()
from behave import given, when, then

@given('the user is on the web page')
def step_impl(context):
    context.driver = GlobalScripts()
    context.driver.setUp()

@when('the user select the "Sign Up" option')
def step_impl(context):
    context.driver.selectSignUpButton()

@when('the user can see the "Sign Up" page')
def step_impl(context):
    context.driver.signUpPage()

@when('the user put the registration details like: {fullName}, {email}, {password},{repeatYourPassword}')
def step_impl(context, fullName, email, password, repeatYourPassword):
    context.driver.enterRegistrationDetails(fullName, email, password, repeatYourPassword)

@when('the user select the "Sign Up" button')
def step_impl(context):
    context.driver.signUpButtonIsEnabled()

@then('the user is register on the web page')
def step_impl(context):
    context.driver.isUserRegistered()
    context.driver.tearDown()

@then('the user should see a message indicating the user already exists')
def step_impl(context):
    context.driver.userAlreadyRegistered()

@then ('the user cannot register with the same details again: {fullName}, {email}, {password},{repeatYourPassword}')
def step_impl(context, fullName, email, password, repeatYourPassword):
    context.driver.enterRegistrationDetails(fullName, email, password, repeatYourPassword)
    context.driver.signUpButtonIsEnabled()
    
    if context.driver.userAlreadyRegistered():
        print("The system correctly identified that the user is already registered.")
    else:
        raise AssertionError("The system did not correctly handle the duplicate registration attempt.")
    