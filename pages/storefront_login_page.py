from playwright.sync_api import Page
from locators.storefront_login_page_locators import StorefrontLoginPageLocators
from utils.helper import perform_action

class StorefrontLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontLoginPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def sign_in_username_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.username_input, action, fill_value)

    def sign_in_password_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.password_input, action, fill_value)

    def sign_in_button_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.sign_in_button, action, fill_value)
