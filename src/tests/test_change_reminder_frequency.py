from src.pages.BasePageObject import BasePageObject
from src.data.TestData import Data
from src.pages.Locators import NamedLocators, TextLocators
import time
import allure
from src.pages.MainPage import MainPageObject
from src.pages.SettingPage import SettingPageObject


class TestAliChangeReminderFrequency:
    @allure.title("Смена частоты уведомлений")
    def test_change_reminder_frequency(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        main_page.click_element_with_text(TextLocators.SETTINGS)
        setting_page = SettingPageObject(driver)
        setting_page.click_element(NamedLocators.NOTIFICATION_SETTING)
        position_1 = setting_page.get_element(NamedLocators.NOTIFICATION_SALES)
        position_2 = setting_page.get_element(NamedLocators.NOTIFICATION_ORDER_UPDATE)
        driver.scroll(position_2, position_1)

        setting_page.click_element(NamedLocators.REMINDER_FREQUENCY_BUTTON)
        setting_page.click_element_with_text(TextLocators.EVERY_3_DAY)
        setting_page.check_element_text(NamedLocators.REMINDER_FREQUENCY_BUTTON, Data.NOTIFICATION_PERIOD_TEXT)
