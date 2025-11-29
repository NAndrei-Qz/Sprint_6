from selenium.webdriver.common.by import By


class HomePageLocators:
    header_order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    body_order_button = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button']
    header_scooter = [By.CLASS_NAME, 'Home_Header__iJKdX']
    faq_price_button = [By.ID, 'accordion__heading-0']
    faq_quantity_button = [By.ID, 'accordion__heading-1']
    faq_rent_time_button = [By.ID, 'accordion__heading-2']
    faq_order_today_button = [By.ID, 'accordion__heading-3']
    faq_extend_or_cancel_button = [By.ID, 'accordion__heading-4']
    faq_charger_button = [By.ID, 'accordion__heading-5']
    faq_cancel_order_button = [By.ID, 'accordion__heading-6']
    faq_delivery_button = [By.ID, 'accordion__heading-7']
    faq_price_answer = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    faq_quantity_answer = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    faq_rent_time_answer = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    faq_order_today_answer = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    faq_extend_or_cancel_answer = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    faq_charger_answer = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    faq_cancel_order_answer = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    faq_delivery_answer= [By.XPATH, '//div[@id="accordion__panel-7"]/p']
    cookie_button = [By.ID, 'rcc-confirm-button']
