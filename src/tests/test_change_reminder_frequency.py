from src.data.TestData import Data
from src.pages.Locators import NamedLocators, TextLocators
import allure
from src.pages.MainPage import MainPageObject
from src.pages.SettingPage import SettingPageObject


class TestAliChangeReminderFrequency:
    @allure.title("Смена частоты уведомлений, scroll 1 вариант")
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

    @allure.title("Смена частоты уведомлений, scroll 2 вариант")
    def test_change_reminder_frequency_2(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        main_page.click_element_with_text(TextLocators.SETTINGS)
        setting_page = SettingPageObject(driver)
        setting_page.click_element(NamedLocators.NOTIFICATION_SETTING)
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"Reminder Frequency\").instance(0))")

        setting_page.click_element(NamedLocators.REMINDER_FREQUENCY_BUTTON)
        setting_page.click_element_with_text(TextLocators.EVERY_3_DAY)
        setting_page.check_element_text(NamedLocators.REMINDER_FREQUENCY_BUTTON, Data.NOTIFICATION_PERIOD_TEXT)

    @allure.title("Смена частоты уведомлений, scroll 3 вариант")
    def test_change_reminder_frequency_3(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        main_page.click_element_with_text(TextLocators.SETTINGS)
        setting_page = SettingPageObject(driver)
        setting_page.click_element(NamedLocators.NOTIFICATION_SETTING)
        driver.execute_script("mobile: scroll", {"direction": "down", "strategy": "-android uiautomator", "selector": "new UiSelector().textContains(\"Reminder Frequency\")"})
        setting_page.click_element(NamedLocators.REMINDER_FREQUENCY_BUTTON)
        setting_page.click_element_with_text(TextLocators.EVERY_3_DAY)
        setting_page.check_element_text(NamedLocators.REMINDER_FREQUENCY_BUTTON, Data.NOTIFICATION_PERIOD_TEXT)
