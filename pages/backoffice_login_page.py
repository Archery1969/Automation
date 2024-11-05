from playwright.sync_api import Page
from locators.backoffice_login_page_locators import BackofficeLoginPageLocators
from utils.helper import perform_action

class BackofficeLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BackofficeLoginPageLocators(page)

    def navigate_to_backoffice(self, url: str):
        self.page.goto(url)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def sign_in_username_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.username_input, action, fill_value)

    def sign_in_password_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.password_input, action, fill_value)

    def sign_in_button_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.signin_button, action, fill_value)
