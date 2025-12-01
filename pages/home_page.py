import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    @allure.step('Ожидание открытия главной страницы')
    def wait_load_home_page(self):
        self.wait_visibility_of_element(HomePageLocators.header_scooter)

    @allure.step('Нажатие на кнопку "{locator}"')
    def click_button_order(self, locator):
        self.click_on_element(locator)

    @allure.step('Закрытие уведомления о куках')
    def click_cookie_confirm(self):
        self.click_on_element(HomePageLocators.cookie_button)

    @allure.step('Поиск элемента {answer_locator} с выпадающим ответом в разделе "Вопросы о важном"')
    def get_faq_answer_text(self, question_locator, answer_locator):
        self.scrolling_to_element(HomePageLocators.faq_delivery_button)
        self.wait_visibility_of_element(question_locator)
        self.wait_clickability_of_element(question_locator)
        self.click_on_element(question_locator)
        self.wait_visibility_of_element(answer_locator)
        answer_text = self.get_text(answer_locator)
        return answer_text

    