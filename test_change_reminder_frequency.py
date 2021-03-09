from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from TestData import Data
from Locators import Locators
from appium.webdriver.common.touch_action import TouchAction


class TestAliChangeReminderFrequency:

    def test_change_reminder_frequency(self, driver):
        menu_element = \
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        menu_element.click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("Settings")').click()
        driver.find_element(By.ID, Locators.notification_setting).click()

        position_1 = driver.find_element(By.ID, Locators.notification_sales)
        position_2 = driver.find_element(By.ID, Locators.notification_order_update)
        driver.scroll(position_2, position_1)

        reminder_frequency_field = driver.find_element(By.ID, Locators.reminder_frequency_button)
        reminder_frequency_field.click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("Every 3 days")').click()
        assert reminder_frequency_field.text == "Every 3 days", "Wrong data for reminder frequency"
