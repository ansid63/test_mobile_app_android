from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from TestData import Data
from Locators import Locators


class TestAliTurnOffNotification:

    def test_turn_off_notification_for_sales(self, driver):
        menu_element = \
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        menu_element.click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("Settings")').click() # test find element by UIautomator
        driver.find_element(By.ID, Locators.notification_setting).click()
        notification_sales_switch = driver.find_element(By.ID, Locators.notification_switch)
        assert notification_sales_switch.is_enabled(), "Element turn off notification enabled"
        notification_sales_switch.click()
        assert notification_sales_switch.text == "OFF", "Notification haven't turned off"
