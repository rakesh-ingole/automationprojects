import random

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage
from pages.signup_page import SignUpBasePage
from utils.test_cases import test_cases


@given('user launch automation practice application')
def step_impl(context):
    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('disable-infobars')
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument("--disable-extensions")
    options.add_argument("--start-fullscreen")
    options.add_argument('--disable-gpu')
    # def launch_application(context):
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(2000)
    print("\n" + str(test_cases(0)))
    page = MainPage(context.driver)
    page.open("")
    page.check_page_loaded()
    page.check_main_page_loaded()


@When('user clicks on My Account link')
def step_impl(context):
    page = MainPage(context.driver)
    page.open_authentication_page()
    auth_page = HomePage(context.driver)
    auth_page.check_auth_page_loaded()


# @When('user fills registration email textbox with "{email}"')
@When('user fills "{text}" registration email')
def step_impl(context, text):
    n = random.randint(0, 1000)
    print(n)
    for row in context.table:
        email = row['EMAIL']
    preemail = email[:email.index("@")]
    lateremail = email[(email.index("@") + 1):]
    email = preemail + str(n) + "@" + lateremail
    print("*" + email)
    page = HomePage(context.driver)
    page.enter_email(email)


# page.click_create_account_button()


@When('user clicks create an account button')
def step_impl(context):
    page = HomePage(context.driver)
    page.click_create_account_button()


@When('user enters the registration details')
def step_impl(context):
    page = SignUpBasePage(context.driver)
    for row in context.table:
        title = row['TITLE']
        page.select_title(title)
        page.select_fname(row['FIRSTNAME'])
        page.select_lname(row['LASTNAME'])
        page.select_password(row['PASSWORD'])
        page.select_day(row['DATE'])
        page.select_month(row['MONTH'])
        page.select_year(row['YEAR'])
        page.select_newsletter(row['NEWSLETTER'])
        page.select_partner(row['PARTNERS'])
        page.select_address_fname(row['ADDRESSFIRSTNAME'])
        page.select_address_lname(row['ADDRESSLASTNAME'])
        page.select_company(row['COMPANY'])
        page.select_address(row['ADDRESS'])
        page.select_address_line_2(row['ADDRESLINE2'])
        page.select_city(row['CITY'])
        page.select_state(row['STATE'])
        page.select_zip(row['ZIP'])
        page.select_country(row['COUNTRY'])
        page.select_info(row['ADDITIONALINFO'])
        page.select_home_phone(row['HOMEPHONE'])
        page.select_mobile_phone(row['MOBILEPHONE'])
        page.select_ref_address(row['ADDRESSFORFUTUREREFERENCE'])
        page.click_on_register()


@Then('verify the registration success')
def validate_success(context):
    page = MyAccountPage(context.driver)
    page.check_my_account_page_loaded()
    page.verify_success_message()


@Then('verify that error message as "{error_msg}"')
def verify_invalid_email_address_error_message(context, error_msg):
    page = HomePage(context.driver)
    page.verify_invalid_email_error_message(error_msg)


@Then('user sing off application')
def user_sign_off(context):
    page = MainPage(context.driver)
    page.sign_off()


@Then('application quits')
def application_quits(context):
    context.driver.quit()
