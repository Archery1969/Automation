from playwright.sync_api import Page

class BackofficeLoginPageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "SAP CX Backoffice | Login"
        self.username_input = page.get_by_placeholder("Enter user name")
        self.password_input = page.get_by_placeholder("Enter password")
        self.signin_button =  page.get_by_role("button", name="Sign In")
