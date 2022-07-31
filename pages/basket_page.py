from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, "There is no Your basket is empty message"
