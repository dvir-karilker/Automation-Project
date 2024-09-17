import time
import pytest
from Pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


# For the entire File -
@pytest.fixture(scope="module")
def set_up():
    driver = webdriver.Firefox()
    page = LoginPage(driver)

    url = "https://www.saucedemo.com/"
    page.navigate_to_url(url)

    yield page
    # driver.quit()


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
