import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_of_element(self, locator):
        self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_clickability_of_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def scrolling_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def change_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs

    def check_dzen_logo(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(BasePageLocators.dzen))

    def click_on_scooter(self):
        self.driver.find_element(*BasePageLocators.samokat_button).click()

    def click_on_yandex(self):
        self.driver.find_element(*BasePageLocators.yandex_button).click()

    def get_url(self):
        return self.driver.current_url
