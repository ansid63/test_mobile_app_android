from PageObject.BasePageObject import BasePageObject
from TestData import Data
from Locators import NamedLocators, TextLocators
import time
import allure


class TestAliChangeReminderFrequency:
    @allure.title("Смена частоты уведомлений")
    def test_change_reminder_frequency(self, driver):
        base_page = BasePageObject(driver)
        time.sleep(2)
        base_page.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)
        base_page.click_element_with_text(TextLocators.SETTINGS)
        base_page.click_element(NamedLocators.NOTIFICATION_SETTING)

        position_1 = base_page.get_element(NamedLocators.NOTIFICATION_SALES)
        position_2 = base_page.get_element(NamedLocators.NOTIFICATION_ORDER_UPDATE)
        driver.scroll(position_2, position_1)

        base_page.click_element(NamedLocators.REMINDER_FREQUENCY_BUTTON)
        base_page.click_element_with_text(TextLocators.EVERY_3_DAY)
        base_page.check_element_text(NamedLocators.REMINDER_FREQUENCY_BUTTON, Data.NOTIFICATION_PERIOD_TEXT)
