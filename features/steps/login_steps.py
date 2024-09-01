from behave import given, when, then
from selenium import webdriver
from features.pages.login_page import LoginPage
import time

@given('User berada di halaman login')
def step_impl(context):
    subdomain = context.config.userdata.get('subdomain')
    context.driver = webdriver.Chrome()  # Atau browser lain yang sesuai
    context.base_url = f"https://{subdomain}.com"
    context.login_page = LoginPage(context.driver, context.base_url)
    context.login_page.navigate()

@when('User mengisi username dengan username dan password yang benar')
def step_impl(context):
    username = context.config.userdata.get('username')
    password = context.config.userdata.get('password')
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('User menyelesaikan captcha')
def step_impl(context):
    context.login_page.solve_captcha()  # Add a small delay for stability

@when('User menekan tombol login')
def step_impl(context):
    context.login_page.click_login()

@then('User masuk ke halaman dashboard')
def step_impl(context):
    context.login_page.close_modal_if_present() 
    context.driver.quit()