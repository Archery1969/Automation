from playwright.sync_api import Page
from locators.storefront_home_page_locators import StorefrontHomePageLocators
from utils.helper import perform_action

class StorefrontHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontHomePageLocators(page)

    def navigate_to_storefront(self, url: str):
        self.page.goto(url)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def cookie_button_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.cookie_accept_button, action, fill_value)

    def sign_in_link_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.sign_in_link, action, fill_value)
    
    def sign_up_email_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.sign_up_field, action, fill_value)

    def sign_up_button_locator(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.sign_up_button, action, fill_value)
