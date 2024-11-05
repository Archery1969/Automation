from playwright.sync_api import Page
from locators.backoffice_home_page_locators import BackofficeHomePageLocators
from utils.helper import perform_action

class BackofficeHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BackofficeHomePageLocators(page)

    def navigate_to_backoffice(self, url: str):
        self.page.goto(url)

    def page_title(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.page_title, action, fill_value)

    def order_link(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.order_link, action, fill_value)
    
    def orders_link(self, action: str = None, fill_value: str = None):
        return perform_action(self.locators.orders_link, action, fill_value)
