from behave import given, when, then

from pages.backoffice_login_page import BackofficeLoginPage
from pages.backoffice_home_page import BackofficeHomePage
from pages.storefront_home_page import StorefrontHomePage
from pages.storefront_login_page import StorefrontLoginPage
from pages.storefront_account_page import StorefrontAccountPage
from utils.helper import *

@given(u'the user is on the storefront home page')
def step_impl(context):
    home_page = StorefrontHomePage(context.page)
    home_page.navigate_to_storefront(context.config.userdata.get("storefront_url"))
    expect(home_page.page).to_have_title(home_page.page_title())

@when(u'the user clicks the accept all cookies button')
def step_impl(context):
    home_page = StorefrontHomePage(context.page)
    home_page.cookie_button_locator(action="click")

@then(u'the cookie accept button should no longer be visible')
def step_impl(context):
    home_page = StorefrontHomePage(context.page)
    expect(home_page.cookie_button_locator()).to_be_hidden()

@given(u'the user is on the storefront login page')
def step_impl(context):
    home_page = StorefrontHomePage(context.page)
    home_page.sign_in_link_locator(action="click")
    login_page = StorefrontLoginPage(context.page)
    expect(login_page.page).to_have_title(login_page.page_title())

@when(u'the user enters valid storefront credentials')
def step_impl(context): 
    login_page = StorefrontLoginPage(context.page)
    login_page.sign_in_username_locator(action="fill",fill_value=context.config.userdata.get("storefront_login_username"))
    login_page.sign_in_password_locator(action="fill",fill_value=context.config.userdata.get("storefront_login_password"))

@when(u'the user clicks on the storefront login button')
def step_impl(context):
    login_page = StorefrontLoginPage(context.page)
    login_page.sign_in_button_locator(action="click")

@then(u'the user is redirected to the storefront account dashboard')
def step_impl(context):
    account_page = StorefrontAccountPage(context.page)
    expect(account_page.page).to_have_title(account_page.page_title())
