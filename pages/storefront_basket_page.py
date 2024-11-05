from playwright.sync_api import Page
from locators.storefront_basket_page_locators import StorefrontBasketPageLocators
from utils.helper import perform_action

class StorefrontBasketPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontBasketPageLocators(page)
