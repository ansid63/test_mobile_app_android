import allure
from src.pages.BasePageObject import BasePageObject
import time
from src.pages.Locators import NamedLocators
from src.pages.MainPage import MainPageObject
from src.pages.MenuPage import MenuPageObject


class TestAliTurnOffNotification:
    @allure.title("Выключение уведомлений")
    def test_turn_off_notification_for_sales(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        menu_page = MenuPageObject(driver)
        menu_page.click_setting()
        menu_page.click_element(NamedLocators.NOTIFICATION_SETTING)
        menu_page.check_element_status(NamedLocators.NOTIFICATION_SWITCH, "is_enabled")
        menu_page.click_element(NamedLocators.NOTIFICATION_SWITCH)
        menu_page.check_element_text(NamedLocators.NOTIFICATION_SWITCH, "OFF")
