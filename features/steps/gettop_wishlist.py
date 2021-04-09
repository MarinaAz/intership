from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BTN_WISHLIST = (By.CSS_SELECTOR, 'i.icon-heart')
PR_RESULT = (By.XPATH, "(//td[@class='product-name']/a)[1]")
PR_IMAGE = (By.CSS_SELECTOR, 'img.wp-post-image.skip-lazy')
ADD_BTN = (By.XPATH, "//a[contains(@href,'wishlist')]")


@given('Open Gettop page of product macbook-pro-13')
def open_product_page(context):
    context.app.wishlist_page.open_product_page()


@then('Add product to wishlist')
def add_to_wishlist(context):
    context.app.wishlist_page.add_to_wishlist()
    sleep(2)


@when('Go to the product page')
def go_to_product(context):
    context.app.wishlist_page.go_to_product()


@then('Verify user on {query} page')
def verify_user_on_correct_page(context, query):
    context.app.wishlist_page.verify_url_contains_query(query)


@when('Remove product from a wishlist')
def remove_product_from_wishlist(context):
    context.app.wishlist_page.remove_product()
    sleep(2)


@then('Verify confirmation message {result_msg}')
def verify_confirmation_msg(context, result_msg):
    context.app.wishlist_page.verify_confirmation_msg(result_msg)


@then('Verify {result_word} on the page')
def verify_is_correct_product(context, result_word):
    context.app.wishlist_page.verify_is_correct_product(result_word)
    # actual_text = context.driver.find_element(*PR_RESULT).text
    # expected_text = 'MacBook Pro 13-inch'
    # assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('Verify user can see {expected_links} social links')
def verify_links_count(context, expected_links):
    context.app.wishlist_page.verify_links_count(expected_links)
