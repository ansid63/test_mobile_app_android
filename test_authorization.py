from PageObject.BasePageObject import BasePageObject
from TestData import Data
from Locators import NamedLocators
import time
import allure


class TestAliAuthorizationAndMenuSwipe:
    @allure.title("Авторизация с некорректными данными")
    def test_authorization_with_wrong_data(self, driver):
        base_page = BasePageObject(driver)
        time.sleep(2)
        base_page.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)
        base_page.click_element(NamedLocators.LOGIN_MENU_BUTTON)
        base_page.click_element(NamedLocators.SIGN_IN_BUTTON)
        base_page.send_text_to_element(NamedLocators.EMAIL_INPUT_FIELD, Data.WRONG_EMAIL)
        base_page.send_text_to_element(NamedLocators.PASSWORD_INPUT_FIELD, Data.WRONG_PASSWORD)
        base_page.click_element(NamedLocators.CONFIRM_BUTTON)
        base_page.check_element_text(NamedLocators.DIALOG_WINDOW_ELEMENT, Data.WRONG_AUTH_TEXT)

    @allure.title("Авторизация с корректными данными. ! Подставьте корректные данные в Data")
    def test_authorization_correct_data(self, driver):
        base_page = BasePageObject(driver)
        time.sleep(2)
        base_page.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)
        base_page.click_element(NamedLocators.LOGIN_MENU_BUTTON)
        base_page.click_element(NamedLocators.SIGN_IN_BUTTON)
        base_page.send_text_to_element(NamedLocators.EMAIL_INPUT_FIELD, Data.CORRECT_EMAIL)
        base_page.send_text_to_element(NamedLocators.PASSWORD_INPUT_FIELD, Data.CORRECT_PASSWORD)
        base_page.click_element(NamedLocators.CONFIRM_BUTTON)
        base_page.check_element_status(NamedLocators.ORDER_BUTTON_ELEMENT, "is_enabled")
        base_page.check_element_text(NamedLocators.ORDER_BUTTON_ELEMENT, Data.MY_ORDER_BUTTON_TEXT)

    @allure.title("Открытие бокового меню свайпом")
    def test_menu_swipe(self, driver):
        BasePageObject(driver).get_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=3)
        driver.swipe(0, 1080, 500, 1080, 250)
        time.sleep(3)
