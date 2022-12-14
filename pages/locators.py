from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages> .alert.fade.in:nth-child(1)> .alertinner")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    REAL_PRICE = (By.CSS_SELECTOR, "#messages> .alert.fade.in:nth-child(3)> .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
