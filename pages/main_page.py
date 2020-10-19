import time

from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    def open_authentication_page(self):
        self.find_element(*self.locator.MY_ACCOUNT_LINK).click()

    def check_main_page_loaded(self):
        self.wait_element(self.locator.MY_ACCOUNT_LINK)

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text

    def click_sign_up_button(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpBasePage(self.driver)

    def click_sign_in_button(self):
        self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)

    def sign_off(self):
        self.find_element(*self.locator.SIGN_OUT_LINK).click()
        time.sleep(3)

    def check_page_loaded(self):
        pass
