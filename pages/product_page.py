from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    BTN_WISHLIST = (By.CSS_SELECTOR, 'i.icon-heart')
    PR_RESULT = (By.CSS_SELECTOR, 'td.product-name')
    PR_IMAGE = (By.CSS_SELECTOR, 'div.product-images')

    def open_product_page(self):
        self.open_url('https://gettop.us/product/macbook-pro-13/')

    def add_to_wishlist(self):
        self.click(*self.BTN_WISHLIST)

    def verify_is_correct_product(self, result_word):
        self.verify_text(result_word, *self.PR_RESULT)