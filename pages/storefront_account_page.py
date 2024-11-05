from playwright.sync_api import Page
from locators.storefront_account_page_locators import StorefrontAccountPageLocators
from utils.helper import perform_action

class StorefrontAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontAccountPageLocators(page)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)
