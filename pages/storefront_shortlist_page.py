from playwright.sync_api import Page
from locators.storefront_shortlist_page_locators import StorefrontShortlistPageLocators
from utils.helper import perform_action

class StorefrontShortlistPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = StorefrontShortlistPageLocators(page)
