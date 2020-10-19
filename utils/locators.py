from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    # LOGO = (By.ID, 'nav-logo')
    #    ACCOUNT = (By.ID, 'nav-link-accountList')
    #    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    #    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    #    SEARCH = (By.ID, 'twotabsearchtextbox')
    #    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
    LOGO = (By.XPATH, '//div[@id="header_logo"]/a/img')
    # MY_ACCOUNT_LINK = (By.XPATH, "//a[contains(text(),'My account')]")
    # MY_ACCOUNT_LINK = (By.XPATH, '//a[@title="Manage my customer account"]')
    MY_ACCOUNT_LINK = (By.XPATH, '//*[ @ id = "footer"]/div/section[5]/h4/a')

    # //a[contains(text(),'Sign in')]
    LOGIN = (By.CSS_SELECTOR, '.login')
    SEARCH = (By.ID, 'search_query_top')
    SIGN_OUT_LINK = (By.XPATH, '//a[@title="Log me out"]')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')


class MyAccountPageLocators(object):
    FOOTER = (By.XPATH, '//*[@id="center_column"]/ul/li/a/span/i')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="center_column"]/p')
    SIGN_OUT_LINK = (By.XPATH, '//a[@title="Log me out"]')


class AuthenticationPageLocators(object):
    EMAIL_ID = (By.ID, 'email_create')
    CREATE_ACCOUNT_TEXT = (By.XPATH, '//*[@id="create-account_form"]/h3')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="SubmitCreate"]/span')
    EMAIL_ERROR_MSG = (By.XPATH, '//div[@id="create_account_error"]/ol/li')


# EMAIL = (By.ID, 'ap_email')
# PASSWORD = (By.ID, 'ap_password')
# SUBMIT = (By.ID, 'signInSubmit-input')
# ERROR_MESSAGE = (By.ID, 'message_error')

class RegistrationPageLocators(object):
    MRTITLE = (By.ID, 'id_gender1')
    MRsTITLE = (By.ID, 'id_gender2')
    FIRSTNAME = (By.ID, 'customer_firstname')
    LASTNAME = (By.ID, 'customer_lastname')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    DATE = (By.ID, 'days')
    MONTH = (By.ID, 'uniform-months')
    YEAR = (By.ID, 'years')
    NEWSLETTER = (By.ID, 'newsletter')
    PARTNERS = (By.ID, 'optin')
    ADDRESSFIRSTNAME = (By.ID, 'firstname')
    ADDRESSLASTNAME = (By.ID, 'lastname')
    COMPANY = (By.ID, 'company')
    ADDRESS = (By.ID, 'address1')
    ADDRESLINE2 = (By.ID, 'address2')
    CITY = (By.ID, 'city')
    STATE = (By.ID, 'id_state')
    ZIP = (By.ID, 'postcode')
    COUNTRY = (By.ID, 'id_country')
    ADDITIONALINFO = (By.ID, 'other')
    HOMEPHONE = (By.ID, 'phone')
    #  MOBILEPHONE = (By.NAME, 'phone_mobile')
    MOBILEPHONE = (By.XPATH, '//input[@id = "phone_mobile" and @type="text"]')
    ADDRESSFORFUTUREREFERENCE = (By.NAME, 'alias')
    REGISTER = (By.XPATH, '//button[@id="submitAccount"]')
