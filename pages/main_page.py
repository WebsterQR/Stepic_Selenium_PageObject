from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_backet(self):
        link = self.browser.find_element(*MainPageLocators.BASCKET_LINK)
        link.click()

    def check_if_bascket_is_empty(self):
        items = self.browser.find_element(*MainPageLocators.ITEMS_IN_BASCKET_LINK).text
        print(items)
        assert items == "Ваша корзина пуста Продолжить покупки"




