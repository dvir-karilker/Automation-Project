from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.base_page import Base


class LoginPage(Base):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def find_username(self):
        return self.locate_element(By.ID, "user-name")

    def find_password(self):
        return self.locate_element(By.ID, "password")

    def find_placeholder(self):
        username_placeholder = self.locate_element(By.ID, "user-name").get_attribute("placeholder")
        password_placeholder = self.locate_element(By.ID, "password").get_attribute("placeholder")
        return username_placeholder, password_placeholder

    def find_value(self):
        username_value = self.locate_element(By.ID, "user-name").get_attribute("value")
        password_value = self.locate_element(By.ID, "password").get_attribute("value")
        return username_value, password_value

    def login_no_crede(self):
        self.click_element(By.ID, "login-button")
        return self.driver.current_url

    def login_no_password(self):
        self.click_element(By.CSS_SELECTOR, 'button.error-button')
        self.set_element_value(By.ID, "user-name", "standard_user")
        self.clear_element(By.ID, "password")
        self.click_element(By.ID, "login-button")
        error_value = self.locate_element(By.CSS_SELECTOR, 'div.error-message-container h3')
        return self.driver.current_url, error_value.text

    def login_no_username(self):
        self.click_element(By.CSS_SELECTOR, 'button.error-button')
        self.set_element_value(By.ID, "password", "secret_sauce")
        self.clear_element(By.ID, "user-name")
        self.click_element(By.ID, "login-button")
        error_value = self.locate_element(By.CSS_SELECTOR, 'div.error-message-container h3')
        return self.driver.current_url, error_value.text

    def correct_password_wrong_username(self):
        self.click_element(By.CSS_SELECTOR, 'button.error-button')
        self.set_element_value(By.ID, "password", "secret_sauce")
        self.set_element_value(By.ID, "user-name", "wrongwrong")
        self.click_element(By.ID, "login-button")
        error_value = self.locate_element(By.CSS_SELECTOR, 'div.error-message-container h3')
        return self.driver.current_url, error_value.text

    def correct_username_wrong_password(self):
        self.click_element(By.CSS_SELECTOR, 'button.error-button')
        self.set_element_value(By.ID, "user-name", "standard_user")
        self.set_element_value(By.ID, "password", "wrongwrong")
        self.click_element(By.ID, "login-button")
        error_value = self.locate_element(By.CSS_SELECTOR, 'div.error-message-container h3')
        return self.driver.current_url, error_value.text

    def wrong_username_wrong_password(self):
        self.click_element(By.CSS_SELECTOR, 'button.error-button')
        self.set_element_value(By.ID, "user-name", "wrongwrong")
        self.set_element_value(By.ID, "password", "wrongwrong")
        self.click_element(By.ID, "login-button")
        error_value = self.locate_element(By.CSS_SELECTOR, 'div.error-message-container h3')
        return self.driver.current_url, error_value.text

    def correct_username_password(self):
        self.set_element_value(By.ID, "user-name", "standard_user")
        self.set_element_value(By.ID, "password", "secret_sauce")
        self.click_element(By.ID, "login-button")
        return self.driver.current_url
