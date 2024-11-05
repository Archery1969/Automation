from playwright.sync_api import Page

class BackofficeHomePageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = "SAP CX Backoffice"
        self.order_link = page.get_by_text("Order", exact=True)
        self.orders_link = page.get_by_text("Orders", exact=True)
