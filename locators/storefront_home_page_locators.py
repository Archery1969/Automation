from playwright.sync_api import Page

class StorefrontHomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "Dreams | Beds from the UK's Leading Bed & Mattress Store"
        self.cookie_accept_button = page.get_by_role("button", name="Accept All Cookies")
        self.sign_in_link = page.get_by_role("link", name="Sign in")
        self.sign_up_field = page.get_by_placeholder("Sign up for offers and sale")
        self.sign_up_button = page.get_by_role("button", name="Sign up")
