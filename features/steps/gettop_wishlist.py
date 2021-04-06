from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BTN_WISHLIST = (By.CSS_SELECTOR, 'i.icon-heart')
PR_RESULT = (By.CSS_SELECTOR, 'td.product-name')
PR_IMAGE = (By.CSS_SELECTOR, 'div.woocommerce-product-gallery')


@given('Open Gettop page of product macbook-pro-13')
def open_product_page(context):
    context.app.product_page.open_product_page()


@when('Verify Wishlist popup btn is clickable')
def verify_wishlist_btn_clickable(context):
    context.driver.wait.until(EC.presence_of_element_located(PR_IMAGE))


@then('Add product to wishlist')
def add_to_wishlist(context):
    context.app.product_page.add_to_wishlist()


@then('Verify user can see {result_word}')
def verify_is_correct_product(context, result_word):
    context.app.product_page.verify_is_correct_product(result_word)

