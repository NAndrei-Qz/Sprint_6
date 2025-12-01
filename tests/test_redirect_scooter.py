import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from url import Url


class TestRedirectScooter:
    @allure.title('Проверка перехода на главную страницу, путём нажатия на лого "Самокат"')
    @allure.description('Переход на страницу заказа с главной странциы; Возврат на главную страницу путём нажатия на лого "Самокат"')
    def test_redirect_scooter(self, driver, open_home_page):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        open_home_page
        home_page.wait_load_home_page()
        home_page.wait_visibility_of_element(HomePageLocators.header_order_button)
        home_page.click_button_order(HomePageLocators.header_order_button)
        home_page.click_on_scooter()
        home_page.wait_visibility_of_element(HomePageLocators.header_scooter)
        url = order_page.get_url()
        assert url == Url.home_page_url

