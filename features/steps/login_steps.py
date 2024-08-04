import re
import sys
import os
from dotenv import load_dotenv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')))
from global_scripts import GlobalScripts

load_dotenv()
from behave import given, when, then


@when('the user put the login details like: {email}, {password}')
def step_impl(context, email, password):
    context.driver.enterLoginDetails(email, password)

@when('the user put wrong login details: {email}, {password}')
def step_impl(context, email, password):
    context.driver.enterLoginDetails(email, password)

@when('the user select the "Sign In" button')
def step_impl(context):
    context.driver.selectLoginButton()

@when('the user is logged into the aplication')
def step_impl(context):
    context.driver.isUserLoggedIn()

@then('the user logout the aplication')
def step_impl(context):
    context.driver.logout()
    
@then('the user see "User not found" message')
def step_impl(context):
    context.driver.userNotFound()
