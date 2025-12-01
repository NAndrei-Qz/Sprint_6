import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from url import Url


class TestRedirectYandex:
    @allure.title('Проверка открытия новой вкладки с главной страницей Дзена, путём нажатия на лого "Яндекс"')
    @allure.description('Переход на страницу заказа с главной странциы; Нажатие на лого "Яндекс"; Проверка открытия новой вкладки с главной страницей Дзена')
    def test_redirect_yandex(self, driver, open_home_page):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        open_home_page
        home_page.wait_load_home_page()
        home_page.scrolling_to_element(HomePageLocators.header_order_button)
        home_page.wait_visibility_of_element(HomePageLocators.header_order_button)
        home_page.click_button_order(HomePageLocators.header_order_button)
        order_page.click_on_yandex()
        order_page.change_tab()
        order_page.check_dzen_logo()
        url = order_page.get_url()
        assert url == Url.dzen_page_url

