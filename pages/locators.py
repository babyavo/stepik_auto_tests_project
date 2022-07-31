from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages> .alert.fade.in:nth-child(1)> .alertinner")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    REAL_PRICE = (By.CSS_SELECTOR, "#messages> .alert.fade.in:nth-child(3)> .alertinner strong")