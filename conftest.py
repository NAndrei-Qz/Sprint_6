import pytest
from selenium import webdriver
from url import Url

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_home_page(driver):
    driver.get(Url.home_page_url)

@pytest.fixture
def open_order_page(driver):
    driver.get(Url.order_page_url)
