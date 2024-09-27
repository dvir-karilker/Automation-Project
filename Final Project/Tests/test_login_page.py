import time
import pytest
from Pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


# For the entire File (Comment out "driver.quit()" to keep browser open) -
@pytest.fixture(scope="module")
def set_up():
    driver = webdriver.Firefox()
    page = LoginPage(driver)

    url = "https://www.saucedemo.com/"
    page.navigate_to_url(url)

    yield page
    driver.quit()


# We've added a small pause between EACH Test, Comment it out if not needed -
@pytest.fixture(scope="function", autouse=True)
def add_pause():
    yield
    time.sleep(1)


# Test 1
def test_correct_location(set_up):
    assert set_up.driver.current_url == "https://www.saucedemo.com/"


# Test 2
def test_find_username(set_up):
    login_page = LoginPage(set_up.driver)
    username_field = login_page.find_username()
    assert username_field is not None


# Test 3
def test_find_password(set_up):
    login_page = LoginPage(set_up.driver)
    password_field = login_page.find_password()
    assert password_field is not None


# Test 4
def test_find_placeholders(set_up):
    login_page = LoginPage(set_up.driver)
    username_placeholder, password_placeholder = login_page.find_placeholder()
    assert username_placeholder is not None
    assert password_placeholder is not None


# Test 5
def test_find_value(set_up):
    login_page = LoginPage(set_up.driver)
    username_value, password_value = login_page.find_value()
    assert username_value == ""
    assert password_value == ""


# Test 6
def test_login_no_crede(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.login_no_crede()
    assert current_url == "https://www.saucedemo.com/"


# Test 7
def test_login_no_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, error_message = login_page.login_no_password()
    assert current_url == "https://www.saucedemo.com/"
    assert error_message == "Epic sadface: Password is required"


# Test 8
def test_login_no_username(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, error_message = login_page.login_no_username()
    assert current_url == "https://www.saucedemo.com/"
    assert error_message == "Epic sadface: Username is required"


# Test 9
def test_correct_password_wrong_username(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, error_message = login_page.correct_password_wrong_username()
    assert current_url == "https://www.saucedemo.com/"
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


# Test 10
def test_correct_username_wrong_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, error_message = login_page.correct_username_wrong_password()
    assert current_url == "https://www.saucedemo.com/"
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


# Test 11
def test_wrong_username_wrong_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, error_message = login_page.wrong_username_wrong_password()
    assert current_url == "https://www.saucedemo.com/"
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


# Test 12
def test_correct_username_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.correct_username_password()
    assert current_url == "https://www.saucedemo.com/inventory.html"
    # print("Logged In!")


# Test 13
def test_checking_price_exist(set_up):
    login_page = LoginPage(set_up.driver)
    items_num, prices_num = login_page.checking_price_exist()
    assert items_num == prices_num
    # print(f"{items_num} = {prices_num}")


# Test 14
def test_checking_img_exist(set_up):
    login_page = LoginPage(set_up.driver)
    items_num, img_num = login_page.checking_img_exist()
    assert items_num == img_num


# Test 15
def test_directing_item_page(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, item_name, item_price, img_src = login_page.directing_item_page()
    assert current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    assert item_name == "Sauce Labs Backpack"
    assert item_price == "$29.99"
    assert img_src == "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"
    # print("\n", current_url, "\n", item_name, "\n", item_price, "\n", img_src)


# Test 16
def test_going_back_to_main(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, page_title = login_page.going_back_to_main()
    assert current_url == "https://www.saucedemo.com/inventory.html"
    assert page_title == "Products"


# Test 17
def test_navigating_to_item_img(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, item_name, item_price, img_src = login_page.navigating_to_item_img()
    assert current_url == "https://www.saucedemo.com/inventory-item.html?id=5"
    assert item_name == "Sauce Labs Fleece Jacket"
    assert item_price == "$49.99"
    assert img_src == "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg"


# Test 18
def test_adding_item_from_item_page(set_up):
    login_page = LoginPage(set_up.driver)
    items_num = login_page.adding_item_from_item_page()
    assert items_num == "1"


# Test 19
def test_status_change(set_up):
    login_page = LoginPage(set_up.driver)
    item_status = login_page.status_change()
    assert item_status == "Remove"


# Test 20
def test_checking_after_going_back(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, item_status = login_page.checking_after_going_back()
    assert current_url == "https://www.saucedemo.com/inventory.html"
    assert item_status == "Remove"


# Test 21
def test_adding_another_item(set_up):
    login_page = LoginPage(set_up.driver)
    items_num = login_page.adding_another_item()
    assert items_num == "2"


# Test 22
def test_second_item_status(set_up):
    login_page = LoginPage(set_up.driver)
    item_status = login_page.second_item_status()
    assert item_status == "Remove"


# Test 23
def test_checking_cart(set_up):
    login_page = LoginPage(set_up.driver)
    items_num, item_one_title, item_two_title, item_one_quantity, item_two_quantity = login_page.checking_cart()
    assert items_num == 2
    assert item_one_title == "Sauce Labs Fleece Jacket"
    assert item_two_title == "Sauce Labs Bike Light"
    assert item_one_quantity == "1"
    assert item_two_quantity == "1"


# Test 24
def test_remove_item_from_cart(set_up):
    login_page = LoginPage(set_up.driver)
    items_num = login_page.remove_item_from_cart()
    assert items_num == 1


# Test 25
def test_going_back_remove_check(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, removed_item_status, cart_number_of_items = login_page.going_back_remove_check()
    assert current_url == "https://www.saucedemo.com/inventory.html"
    assert removed_item_status == "Add to cart"
    assert cart_number_of_items == "1"


# Test 26
def test_going_to_checkout(set_up):
    login_page = LoginPage(set_up.driver)
    cart_url, checkout_url = login_page.going_to_checkout()
    assert cart_url == "https://www.saucedemo.com/cart.html"
    assert checkout_url == "https://www.saucedemo.com/checkout-step-one.html"


# Test 27
def test_filling_checkout_details(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.filling_checkout_details()
    assert current_url == "https://www.saucedemo.com/checkout-step-two.html"


# Test 28
def test_calculating_final_price(set_up):
    login_page = LoginPage(set_up.driver)
    item_subtotal, tax, final_price = login_page.calculating_final_price()
    assert item_subtotal + tax == final_price


# Test 29
def test_finishing_order(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, complete_msg, button_element = login_page.finishing_order()
    assert current_url == "https://www.saucedemo.com/checkout-complete.html"
    assert complete_msg == "Checkout: Complete!"
    assert button_element is not None


# Test 30
def test_going_back_home(set_up):
    login_page = LoginPage(set_up.driver)
    current_url, page_title = login_page.going_back_home()
    assert current_url == "https://www.saucedemo.com/inventory.html"
    assert page_title == "Products"


# Test 31
def test_expanding_menu(set_up):
    login_page = LoginPage(set_up.driver)
    menu_options_num, inventory_clickable, about_clickable, logout_clickable, reset_clickable = login_page.expanding_menu()
    assert menu_options_num == 4
    inventory_clickable is True
    about_clickable is True
    logout_clickable is True
    reset_clickable is True


# Test 32
def test_logging_out(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.logging_out()
    assert current_url == "https://www.saucedemo.com/"
