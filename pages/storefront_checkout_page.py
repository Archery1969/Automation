from playwright.sync_api import Page
from locators.storefront_checkout_page_locators import StorefrontCheckoutPageLocators
from utils.helper import perform_action

class StorefrontCheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontCheckoutPageLocators(page)
