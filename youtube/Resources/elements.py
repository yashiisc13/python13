from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class Base(object):
    """base class with element interactions as methods"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return Wait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        ActionChains(self.driver) \
            .scroll_to_element(self.find_element(locator)) \
            .perform()

    def click(self, locator):
        self.find_element(locator).click()

    def input(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text
