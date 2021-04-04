from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ACCOUNT_ICON = (By.CSS_SELECTOR, "i.icon-user")
LOG_FORM = (By.CSS_SELECTOR, 'h3.uppercase')


@given('Open Gettop page')
def open_gettop_page(context):
    context.app.main_page.open_gettop_page()


@when('Click on Account icon')
def click_account_icon(context):
    context.app.main_page.click_account_icon()


@then('Verify {result_word} is appears on Gettop')
def verify_form_is_appears(context, result_word):
    context.app.main_page.verify_form_is_appears(result_word)



