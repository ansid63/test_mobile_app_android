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
        driver.find_element_by_android_uiautomator('new UiSelector().text("Settings")').click() # test find element by UIautomator
        driver.find_element(By.ID, Locators.notification_setting).click()

        # actions = TouchAction(driver)
        # actions.scroll((By.ID, Locators.notification_setting), 10, 100)
        # actions.
        # actions.perform()
        driver.swipe(500, 1400, 500, 300, 150)
        reminder_frequency_field = driver.find_element(By.ID, Locators.reminder_frequency_button)
        reminder_frequency_field.click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("Every 3 days")').click() # test find element by UIautomator
        assert reminder_frequency_field.text == "Every 3 days", "Wronf data for reminder frequency"
