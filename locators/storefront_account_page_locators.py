from playwright.sync_api import Page

class StorefrontAccountPageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "My Account"
