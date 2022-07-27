from selenium.webdriver.common.by import By
import time


class TestMainPage1():
    def test_check_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        #time.sleep(30)
        browser.get(link)
        assert browser.find_elements(By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket"), 'basket button not found'


