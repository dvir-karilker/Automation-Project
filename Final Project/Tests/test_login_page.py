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
    driver.quit()


# We've added a small pause between EACH Test, Comment it out if not needed -
@pytest.fixture(scope="function", autouse=True)
def add_pause():
    yield
    time.sleep(3)


# Test 1
def test_correct_location(set_up):
    assert set_up.driver.current_url == "https://www.saucedemo.com/"


# Test 2
def test_find_username(set_up):
    username_field = LoginPage.find_username(set_up.driver)
    assert username_field is not None


# Test 3
def test_find_password(set_up):
    password_field = LoginPage.find_password(set_up.driver)
    assert password_field is not None


# Test 4
def test_find_placeholders(set_up):
    username_placeholder, password_placeholder = LoginPage.find_placeholder(set_up.driver)
    assert username_placeholder is not None
    assert password_placeholder is not None


# Test 5
def test_find_value(set_up):
    username_value, password_value = LoginPage.find_value(set_up.driver)
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
    current_url = login_page.login_no_password()
    assert current_url == "https://www.saucedemo.com/"


# Test 8
def test_login_no_username(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.login_no_username()
    assert current_url == "https://www.saucedemo.com/"


# Test 9
def test_correct_password_wrong_username(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.correct_password_wrong_username()
    assert current_url == "https://www.saucedemo.com/"


# Test 10
def test_correct_username_wrong_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.correct_username_wrong_password()
    assert current_url == "https://www.saucedemo.com/"


# Test 11
def test_wrong_username_wrong_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.wrong_username_wrong_password()
    assert current_url == "https://www.saucedemo.com/"


# Test 12
def test_correct_username_password(set_up):
    login_page = LoginPage(set_up.driver)
    current_url = login_page.correct_username_password()
    assert current_url == "https://www.saucedemo.com/inventory.html"
