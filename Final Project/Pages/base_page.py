from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    # Finding an Element -
    def find_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    # Clicking on an Element -
    def click_element(self, by, value):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        return element

    # Clearing an Element's Value (Field clearing) -
    def clear_element(self, by, value):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        element.clear()
        return element

    # Clearing then Setting an Element's Value (like "send_keys()") -
    def set_element_value(self, by, value, text):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        element.clear()
        element.send_keys(text)
        return element

    # Counting occurrences of a specific Element -
    def count_elements(self, by, value):
        elements = self.driver.find_elements(by, value)
        return len(elements)
