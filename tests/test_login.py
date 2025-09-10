import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_cicd_project.pages.login_page import LoginPage
from selenium_cicd_project.pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_page_title()=='Products'

def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_error_message() == expected_error
