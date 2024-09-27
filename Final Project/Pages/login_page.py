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

    def checking_price_exist(self):
        items_num = self.count_elements(By.CSS_SELECTOR, 'div.inventory_item')
        prices_num = self.count_elements(By.CSS_SELECTOR, 'div.inventory_item_price')
        return items_num, prices_num

    def checking_img_exist(self):
        items_num = self.count_elements(By.CSS_SELECTOR, 'div.inventory_item')
        img_num = self.count_elements(By.CSS_SELECTOR, 'img.inventory_item_img')
        return items_num, img_num

    def directing_item_page(self):
        self.click_element(By.CSS_SELECTOR, "#item_4_title_link > div:nth-child(1)")
        item_name = self.locate_element(By.CSS_SELECTOR, 'div.inventory_details_name').text
        item_price = self.locate_element(By.CSS_SELECTOR, 'div.inventory_details_price').text
        img_src = self.locate_element(By.CSS_SELECTOR, 'img.inventory_details_img').get_attribute("src")
        return self.driver.current_url, item_name, item_price, img_src

    def going_back_to_main(self):
        self.click_element(By.ID, "back-to-products")
        page_title = self.locate_element(By.CSS_SELECTOR, 'span.title').text
        return self.driver.current_url, page_title

    def navigating_to_item_img(self):
        self.click_element(By.CSS_SELECTOR, "#item_5_img_link > img:nth-child(1)")
        item_name = self.locate_element(By.CSS_SELECTOR, 'div.inventory_details_name').text
        item_price = self.locate_element(By.CSS_SELECTOR, 'div.inventory_details_price').text
        img_src = self.locate_element(By.CSS_SELECTOR, 'img.inventory_details_img').get_attribute("src")
        return self.driver.current_url, item_name, item_price, img_src

    def adding_item_from_item_page(self):
        self.click_element(By.ID, "add-to-cart")
        items_num = self.locate_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        return items_num

    def status_change(self):
        item_status = self.locate_element(By.ID, "remove").text
        return item_status

    def checking_after_going_back(self):
        self.click_element(By.ID, "back-to-products")
        item_status = self.locate_element(By.ID, "remove-sauce-labs-fleece-jacket").text
        return self.driver.current_url, item_status

    def adding_another_item(self):
        self.click_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        items_num = self.locate_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        return items_num

    def second_item_status(self):
        item_status = self.locate_element(By.ID, "remove-sauce-labs-bike-light").text
        return item_status

    def checking_cart(self):
        self.click_element(By.CSS_SELECTOR, "#shopping_cart_container")
        items_num = self.count_elements(By.CLASS_NAME, "cart_item")
        item_one_title = self.locate_element(By.CSS_SELECTOR, "#item_5_title_link > div:nth-child(1)").text
        item_two_title = self.locate_element(By.CSS_SELECTOR, "#item_0_title_link > div:nth-child(1)").text
        item_one_quantity = self.locate_element(By.CSS_SELECTOR, "div.cart_item:nth-child(3) > div:nth-child(1)").text
        item_two_quantity = self.locate_element(By.CSS_SELECTOR, "div.cart_item:nth-child(4) > div:nth-child(1)").text
        return items_num, item_one_title, item_two_title, item_one_quantity, item_two_quantity

    def remove_item_from_cart(self):
        self.click_element(By.ID, "remove-sauce-labs-bike-light")
        items_num = self.count_elements(By.CLASS_NAME, "cart_item")
        return items_num

    def going_back_remove_check(self):
        self.click_element(By.ID, "continue-shopping")
        removed_item_status = self.locate_element(By.ID, "add-to-cart-sauce-labs-bike-light").text
        cart_number_of_items = self.locate_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        return self.driver.current_url, removed_item_status, cart_number_of_items

    def going_to_checkout(self):
        self.click_element(By.CSS_SELECTOR, "#shopping_cart_container")
        cart_url = self.driver.current_url
        self.click_element(By.ID, "checkout")
        checkout_url = self.driver.current_url
        return cart_url, checkout_url

    def filling_checkout_details(self):
        self.set_element_value(By.ID, "first-name", "Israel")
        self.set_element_value(By.ID, "last-name", "Israeli")
        self.set_element_value(By.ID, "postal-code", "12345")
        self.click_element(By.ID, "continue")
        return self.driver.current_url

    def calculating_final_price(self):
        item_total = self.locate_element(By.CSS_SELECTOR, ".summary_subtotal_label").text
        float_item_total = float(item_total.replace("Item total: $", ""))
        tax = self.locate_element(By.CSS_SELECTOR, ".summary_tax_label").text
        float_tax = float(tax.replace("Tax: $", ""))
        final_price = self.locate_element(By.CSS_SELECTOR, ".summary_total_label").text
        float_final_price = float(final_price.replace("Total: $", ""))
        return float_item_total, float_tax, float_final_price

    def finishing_order(self):
        self.click_element(By.ID, "finish")
        complete_msg = self.locate_element(By.CSS_SELECTOR, ".title").text
        button_element = self.locate_element(By.ID, "back-to-products")
        return self.driver.current_url, complete_msg, button_element

    def going_back_home(self):
        self.click_element(By.ID, "back-to-products")
        page_title = self.locate_element(By.CSS_SELECTOR, ".title").text
        return self.driver.current_url, page_title

    def expanding_menu(self):
        self.click_element(By.ID, "react-burger-menu-btn")
        menu_options_num = self.count_elements(By.CLASS_NAME, "bm-item")
        inventory_clickable = self.is_element_clickable(By.ID, "inventory_sidebar_link")
        about_clickable = self.is_element_clickable(By.ID, "about_sidebar_link")
        logout_clickable = self.is_element_clickable(By.ID, "logout_sidebar_link")
        reset_clickable = self.is_element_clickable(By.ID, "reset_sidebar_link")
        return menu_options_num, inventory_clickable, about_clickable, logout_clickable, reset_clickable

    def logging_out(self):
        self.click_element(By.ID, "logout_sidebar_link")
        return self.driver.current_url








