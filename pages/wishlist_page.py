from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class WishlistPage(Page):
    BTN_WISHLIST = (By.CSS_SELECTOR, 'i.icon-heart')
    PR_RESULT = (By.XPATH, "(//td[@class='product-name']/a)[1]")
    PR_IMAGE = (By.CSS_SELECTOR, 'img.wp-post-image.skip-lazy')
    ADD_BTN = (By.XPATH, "//a[contains(@href,'wishlist')]")
    REMOVE_BTN = (By.XPATH, "//a[@class='remove remove_from_wishlist']")
    CONFIRM_MSG = (By.CSS_SELECTOR, "td.wishlist-empty")
    PR_BTN = (By.CSS_SELECTOR, 'td.product-thumbnail')
    SOCIAL_LINKS = (By.XPATH, "//a[contains(@class,'icon button')]")

    def open_product_page(self):
        self.open_url('https://gettop.us/product/macbook-pro-13/')

    def add_to_wishlist(self):
        self.hover_over(*self.PR_IMAGE)
        self.click(*self.BTN_WISHLIST)
        self.hover_over(*self.BTN_WISHLIST)
        self.driver.find_element(*self.ADD_BTN).click()

    def verify_is_correct_product(self, result_word):
        self.verify_text(result_word, *self.PR_RESULT)

    def remove_product(self):
        self.click(*self.REMOVE_BTN)

    def go_to_product(self):
        self.click(*self.PR_BTN)

    def verify_confirmation_msg(self, result_msg):
        self.verify_text(result_msg, *self.CONFIRM_MSG)

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def verify_links_count(self, expected_links):
        actual_links = self.driver.find_elements(*self.SOCIAL_LINKS)
        assert len(actual_links) == int(expected_links), f'Expected {expected_links}, but got {actual_links}'
