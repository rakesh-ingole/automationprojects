import sys
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from utils.locators import *
from pages.base_page import BasePage


class SignUpBasePage(BasePage):

    def __init__(self, driver):
        self.locator = RegistrationPageLocators
        super(SignUpBasePage, self).__init__(driver)

    def check_registration_page_loaded(self):
        self.wait_element(self.locator.REGISTER)

    def select_fname(self, fname):
        print(fname)
        sys.stdout.write("Hello")
        self.find_element(*self.locator.FIRSTNAME).send_keys(fname)

    def select_title(self, title):
        if title == "MR":
            self.find_element(*self.locator.MRTITLE).click()
        else:
            self.find_element(*self.locator.MRsTITLE).click()

    def select_lname(self, lname):
        print(lname)
        self.find_element(*self.locator.LASTNAME).send_keys(lname)

    def select_password(self, passw):
        print(passw)
        self.find_element(*self.locator.PASSWORD).send_keys(passw)

    def select_day(self, day):
        print(day)
        option = Select(self.find_element(*self.locator.DATE))
        option.select_by_value(day)

    def select_month(self, month):
        print(month)
        self.find_element(*self.locator.MONTH).click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def select_year(self, year):
        print(year)
        option = Select(self.find_element(*self.locator.YEAR))
        option.select_by_value(year)

    def select_newsletter(self, flag):
        print(flag)
        if flag == "Y":
            self.find_element(*self.locator.NEWSLETTER).click()

    def select_partner(self, flag):
        print(flag)
        if flag == "Y":
            self.find_element(*self.locator.PARTNERS).click()

    def select_address_fname(self, addfname):
        print(addfname)
        self.find_element(*self.locator.ADDRESSFIRSTNAME).send_keys(addfname)

    def select_address_lname(self, addlname):
        print(addlname)
        self.find_element(*self.locator.ADDRESSLASTNAME).send_keys(addlname)

    def select_address(self, address):
        print(address)
        self.find_element(*self.locator.ADDRESS).send_keys(address)

    def select_address_line_2(self, address_l2):
        print(address_l2)
        self.find_element(*self.locator.ADDRESLINE2).send_keys(address_l2)

    def select_company(self, company):
        print(company)
        self.find_element(*self.locator.COMPANY).send_keys(company)

    def select_city(self, city):
        print(city)
        self.find_element(*self.locator.CITY).send_keys(city)

    def select_zip(self, zipcode):
        print(zipcode)
        self.find_element(*self.locator.ZIP).send_keys(zipcode)

    def select_info(self, info):
        print(info)
        self.find_element(*self.locator.ADDITIONALINFO).send_keys(info)

    def select_home_phone(self, home_phone):
        print(home_phone)
        self.find_element(*self.locator.HOMEPHONE).send_keys(home_phone)

    def select_mobile_phone(self, mobile_phone):
        print(mobile_phone)
        self.find_element(*self.locator.MOBILEPHONE).send_keys(mobile_phone)

    def select_ref_address(self, ref_address):
        print(ref_address)
        self.find_element(*self.locator.ADDRESSFORFUTUREREFERENCE).send_keys(ref_address)

    def select_state(self, state):
        print(state)
        option = Select(self.find_element(*self.locator.STATE))
        option.select_by_visible_text(state)

    def select_country(self, country):
        print(country)
        option = Select(self.find_element(*self.locator.COUNTRY))
        option.select_by_visible_text(country)

    def click_on_register(self):
        print("click on submit")
        self.find_element(*self.locator.REGISTER).click()
