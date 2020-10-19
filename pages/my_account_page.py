from hamcrest import assert_that, equal_to
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *
import unittest


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MyAccountPage(BasePage):
    def __init__(self, driver):
        self.locator = MyAccountPageLocators
        super().__init__(driver)  # Python3 version

    def check_my_account_page_loaded(self):
        self.wait_element(self.locator.FOOTER)

    def verify_success_message(self):
        error = "Welcome to your account. Here you can manage all of your personal information and orders."
        if error ==  self.find_element(*self.locator.SUCCESS_MESSAGE).text:
            print("Test Pass")
        else:
            print("Test Fail")

        #    self.find_element(*self.locator.SUCCESS_MESSAGE).text()
        # assert_that("Welcome to your account. Here you can manage all of your personal information and orders.",equal_to(
        #            self.find_element(*self.locator.SUCCESS_MESSAGE).text()))
        # assert self.find_element(*self.locator.SIGN_OUT_LINK).is_displayed()
        # self.assertTrue(True)


