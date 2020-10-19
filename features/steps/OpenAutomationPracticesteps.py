from lib2to3.fixes.fix_input import context
from behave import *
from selenium import webdriver


@given('I launch Chrome browser')
def step_impl(context):
    # def launch_application(context):
    context.driver = webdriver.Chrome()


@when('I open automation practice home page')
def step_impl(context):
    # def open_application(context):
    context.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")


@then('I verify that the logo present on page')
def step_impl(context):
    # def verify_logo (context):
    # context.driver.find_element(By.cssSelect(".logo img-responsive"))
    # context.driver.find_element_by_css_selector(self=".logo img-responsive")
    visible = context.driver.find_element_by_xpath("//*[@id='header_logo']/a/img").is_displayed()
    print(visible)
    context.driver.close()
