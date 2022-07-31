from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_right_book(self):
        item1_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        item2_in_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert item1_in_basket in item2_in_basket, "Incorrect book in basket"

    def should_be_right_prise(self):
        price1_in_basket = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE).text
        price2_in_basket = self.browser.find_element(*ProductPageLocators.REAL_PRICE).text
        assert price1_in_basket == price2_in_basket, "Incorrect price in basket"

    def should_not_be_success_message1(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
