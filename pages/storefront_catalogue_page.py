from playwright.sync_api import Page
from locators.storefront_catalogue_page_locators import StorefrontCataloguePageLocators
from utils.helper import perform_action

class StorefrontCheckoutGuestPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontCataloguePageLocators(page)
