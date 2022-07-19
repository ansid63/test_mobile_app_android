import allure
from PageObject.BasePageObject import BasePageObject
from TestData import Data
from Locators import NamedLocators


class TestAliTurnOffNotification:
    @allure.title("Выключение уведомлений")
    def test_turn_off_notification_for_sales(self, driver):
        base_page = BasePageObject(driver)
        base_page.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)
        base_page.click_element_with_text("Settings")
        base_page.click_element(NamedLocators.NOTIFICATION_SETTING)
        base_page.check_element_status(NamedLocators.NOTIFICATION_SWITCH, "is_enabled")
        base_page.click_element(NamedLocators.NOTIFICATION_SWITCH)
        base_page.check_element_text(NamedLocators.NOTIFICATION_SWITCH, "OFF")
