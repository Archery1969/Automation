from playwright.sync_api import Page

class StorefrontLoginPageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "Login"
        self.username_input = page.locator("input[name=\"j_username\"]")
        self.password_input = page.locator("input[name=\"j_password\"]")
        self.sign_in_button = page.get_by_role("button", name="SIGN IN")
