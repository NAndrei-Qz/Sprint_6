import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step('Ввод данных для заказа. Раздел: "Для кого самокат"')
    def input_customers_data(self, name, lastname, address, number, station):
        self.wait_visibility_of_element(self.locators.input_name)
        self.input_text(self.locators.input_name, name)
        self.input_text(self.locators.input_lastname, lastname)
        self.input_text(self.locators.input_address, address)
        self.input_text(self.locators.input_station, station)
        self.click_on_element(self.locators.button_station)
        self.input_text(self.locators.input_number, number)

    @allure.step('Ввод данных для заказа. Раздел: "Про аренду"')
    def input_rent_data(self, date, rent_time, color, comment):
        self.input_text(self.locators.input_date, date)
        self.click_on_element(self.locators.empty_place)
        self.click_on_element(self.locators.rent_time_drop_list)
        self.click_on_element(rent_time)
        self.click_on_element(color)
        self.input_text(self.locators.input_comment, comment)

    @allure.step('Полное создание заказа. В качестве результата возврщается текст оповещения об успешном заказе"')
    def create_order(self,  name, lastname, address, number, station, date, rent_period, color, comment):
        self.input_customers_data(name, lastname, address, number, station)
        self.click_on_element(self.locators.button_next)
        self.input_rent_data(date, rent_period, color, comment)
        self.click_on_element(self.locators.button_order)
        self.wait_visibility_of_element(self.locators.button_yes)
        self.click_on_element(self.locators.button_yes)
        success_message = self.get_text(self.locators.button_success_message)
        return success_message

    @allure.step('Переход со страницы создания заказа на главную страницу путём клика на лого "Самокат')
    def redirect_scooter(self):
        self.click_on_scooter()

    @allure.step('Переход со страницы создания заказа на страницу дзен путём клика на лого "Яндекс')
    def redirect_yandex(self):
        self.click_on_yandex()

