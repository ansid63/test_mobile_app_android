import time
import allure
from src.pages.BasePageObject import BasePageObject
from src.data.TestData import Data
from src.pages.Locators import NamedLocators, TextLocators
from src.pages.MainPage import MainPageObject
from src.pages.MenuPage import MenuPageObject


class TestAliAuthorizationAndMenuSwipe:
    @allure.title("Авторизация с некорректными данными")
    def test_authorization_with_wrong_data(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        menu_page = MenuPageObject(driver)
        menu_page.click_element(NamedLocators.LOGIN_MENU_BUTTON)
        menu_page.click_element(NamedLocators.SIGN_IN_BUTTON)
        menu_page.send_text_to_element(NamedLocators.EMAIL_INPUT_FIELD, Data.WRONG_EMAIL)
        menu_page.send_text_to_element(NamedLocators.PASSWORD_INPUT_FIELD, Data.WRONG_PASSWORD)
        menu_page.click_element(NamedLocators.CONFIRM_BUTTON)
        menu_page.check_element_text(NamedLocators.DIALOG_WINDOW_ELEMENT, Data.WRONG_AUTH_TEXT)

    @allure.title("Авторизация с корректными данными. ! Подставьте корректные данные в Data")
    def test_authorization_correct_data(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        menu_page = MenuPageObject(driver)
        menu_page.click_element(NamedLocators.LOGIN_MENU_BUTTON)
        menu_page.click_element(NamedLocators.SIGN_IN_BUTTON)
        menu_page.send_text_to_element(NamedLocators.EMAIL_INPUT_FIELD, Data.CORRECT_EMAIL)
        menu_page.send_text_to_element(NamedLocators.PASSWORD_INPUT_FIELD, Data.CORRECT_PASSWORD)
        menu_page.click_element(NamedLocators.CONFIRM_BUTTON)
        menu_page.check_element_status(NamedLocators.ORDER_BUTTON_ELEMENT, "is_enabled")
        menu_page.check_element_text(NamedLocators.ORDER_BUTTON_ELEMENT, Data.MY_ORDER_BUTTON_TEXT)

    @allure.title("Открытие бокового меню свайпом")
    def test_menu_swipe(self, driver):
        main_page = MainPageObject(driver)
        main_page.get_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=3)
        main_page.make_swipe(x_from=0, y_from=0.5, x_to=0.5, y_to=0.5, swipe_length=0.25)
        assert main_page.get_element_with_text(TextLocators.SETTINGS).text == "Settings"
