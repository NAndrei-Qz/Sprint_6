import allure
import pytest
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from data import TestData

class TestFaqAnswers:
    @allure.title("Проверка соответствия выпадающего ответа на вопрос из FAQ ожидаемому ответу")
    @allure.description("На странице производится поиск вопросов из раздела FAQ, нажатием на вопрос октрывается ответ; Производится проверка, что текст ответа"
                        "совпадает с ожидаемым текстом")
    @pytest.mark.parametrize(
        'question_locator, answer_locator, answer_txt',
        [
            (HomePageLocators.faq_price_button, HomePageLocators.faq_price_answer, TestData.answer_text_1),
            (HomePageLocators.faq_quantity_button, HomePageLocators.faq_quantity_answer, TestData.answer_text_2),
            (HomePageLocators.faq_rent_time_button, HomePageLocators.faq_rent_time_answer, TestData.answer_text_3),
            (HomePageLocators.faq_order_today_button, HomePageLocators.faq_order_today_answer, TestData.answer_text_4),
            (HomePageLocators.faq_extend_or_cancel_button, HomePageLocators.faq_extend_or_cancel_answer, TestData.answer_text_5),
            (HomePageLocators.faq_charger_button, HomePageLocators.faq_charger_answer, TestData.answer_text_6),
            (HomePageLocators.faq_cancel_order_button, HomePageLocators.faq_cancel_order_answer, TestData.answer_text_7),
            (HomePageLocators.faq_delivery_button, HomePageLocators.faq_delivery_answer, TestData.answer_text_8),
        ]
    )
    def test_faq_answers(self, driver, open_home_page, question_locator, answer_locator, answer_txt):
        home_page = HomePage(driver)
        open_home_page
        home_page.wait_load_home_page()
        home_page.click_cookie_confirm()
        answer = home_page.get_faq_answer_text(question_locator, answer_locator)
        assert answer == answer_txt