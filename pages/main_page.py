from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    ACCOUNT_ICON = (By.CSS_SELECTOR, "i.icon-user")
    LOG_FORM = (By.CSS_SELECTOR, 'h3.uppercase')

    def open_gettop_page(self):
        self.open_url('https://gettop.us/')

    def click_account_icon(self):
        self.click(*self.ACCOUNT_ICON)

    def verify_form_is_appears(self, result_word):
        self.verify_text(result_word, *self.LOG_FORM)