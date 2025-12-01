import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from data import TestData


class TestCreateOrder:
    @allure.title('Проверка прохождения позитивного сценария создания заказа')
    @allure.description('Проверка перехода на страницу создания заказа из двух возможных мест '
                        'на главной странице; заполнение данных, необходимых для заказа; проверка появления уведомления '
                        'об успешном заказе')
    @pytest.mark.parametrize(
        'create_order_button, name, lastname, address, number, station, date, rent_period, checkbox_color, comment',
        [
            (HomePageLocators.header_order_button, TestData.name_1, TestData.lastname_1, TestData.address_1, TestData.number_1,
             TestData.station_1, TestData.date_1, OrderPageLocators.rent_period_1, OrderPageLocators.checkbox_black, TestData.comment_1),
            (HomePageLocators.body_order_button, TestData.name_2, TestData.lastname_2, TestData.address_2, TestData.number_2,
             TestData.station_2, TestData.date_2, OrderPageLocators.rent_period_2, OrderPageLocators.checkbox_grey, TestData.comment_2)
        ]
    )
    def test_success_create_order(self, driver, open_home_page, create_order_button, name, lastname, address, number, station, date, rent_period, checkbox_color, comment):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        open_home_page
        home_page.wait_load_home_page()
        home_page.scrolling_to_element(create_order_button)
        home_page.wait_visibility_of_element(create_order_button)
        home_page.wait_clickability_of_element(create_order_button)
        home_page.click_button_order(create_order_button)
        message = order_page.create_order(name, lastname, address, number, station, date, rent_period, checkbox_color, comment)
        assert message == 'Посмотреть статус'

