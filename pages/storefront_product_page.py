from playwright.sync_api import Page
from locators.storefront_product_page_locators import StorefrontProductPageLocators
from utils.helper import perform_action

class StorefrontProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontProductPageLocators(page)
