import logging
import time
import unittest

from hamcrest import assert_that, equal_to

from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = AuthenticationPageLocators
        super(HomePage, self).__init__(driver)

    def check_auth_page_loaded(self):
        self.wait_element(self.locator.CREATE_ACCOUNT_BUTTON)

    # return True if self.find_element(*self.locator.CREATE_ACCOUNT_TEXT) else False

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL_ID).send_keys(email)

    def click_create_account_button(self):
        self.find_element(*self.locator.CREATE_ACCOUNT_BUTTON).click()
        time.sleep(3)

    def verify_invalid_email_error_message(self, error):
        print("$$$$$$$$$"+error)
        if error == self.find_element(*self.locator.EMAIL_ERROR_MSG).text:
            logging.info("*************$$ Test Pass***********************")
            print("************** Test Pass***********************")
        else:
            logging.error("**************$$ Test Fail***********************")
            print("************** Test Fail***********************")

    #    assert_that(error, equal_to(str((self.locator.EMAIL_ERROR_MSG).text)))
    #   assertEqual(error, str((self.locator.EMAIL_ERROR_MSG).text))
    #    unittest.assertTrue(True)
