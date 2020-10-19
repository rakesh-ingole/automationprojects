[page-object-python-selenium] is being sponsored by the following tool; please help to support us by taking a look and signing up to a free trial

<a href="https://tracking.gitads.io/?repo=page-object-python-selenium"> <img src="https://images.gitads.io/page-object-python-selenium" alt="GitAds"/> </a>


# Selenium Page Object Model with Python 

Page-object-model (POM) is a pattern that you can apply it to develop efficient automation framework. With page-model, it is possible to minimise maintenance cost. Basically page-object means that your every page is inherited from a base class which includes basic functionalities for every pages. If you have some new functionality that every pages have, you can simple add it to the base class.

`BasePage` class include basic functionality and driver initialization
```python
base_page.py
class BasePage(object):
    def __init__(self, driver, base_url='http://www.amazon.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
```

`MainPage` is derived from the `BasePage class, it contains methods related to this page, which will be used to create test steps.
```python
# main_page.py
class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version


When you want to write tests, you should write as behave bdd scenario and followed by steps 
```python

# Scenario: logo presence on AutomationPractice home page
#     Given I launch Chrome browser
#     When I open automation practice home page
#      Then I verify that the logo present on page

#   def step_impl(context):
    # def verify_logo (context):
    # context.driver.find_element(By.cssSelect(".logo img-responsive"))
    # context.driver.find_element_by_css_selector(self=".logo img-responsive")
#    visible = context.driver.find_element_by_xpath("//*[@id='header_logo']/a/img").is_displayed()
#    print(visible)   
#    context.driver.close()
```
#### If you want to run all tests, you should type in pycharm terminal: 
behave features/registration.feature

#### If you want to run just a negative scenario, you should type: 
behave --tags=@negative features/registration.feature
