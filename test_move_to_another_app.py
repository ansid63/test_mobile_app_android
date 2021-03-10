from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from TestData import Data
from Locators import Locators
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class TestAliMoveToChromeLink:

    def test_move_to_chrome_link(self, driver):
        menu_element = \
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        menu_element.click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("Settings")').click()
        driver.find_element(By.ID, Locators.privacy_policy_button).click()
        try:
            dialog_window_enabled = driver.find_element_by_android_uiautomator('new UiSelector().text("Open with Chrome")').is_enabled()
            assert dialog_window_enabled is True, "Dialog window haven't appeared"
            driver.find_element(By.ID, Locators.just_once_button).click()
        except NoSuchElementException:
            dialog_window_enabled = driver.find_element_by_android_uiautomator('new UiSelector().text("Open with")').is_enabled()
            assert dialog_window_enabled is True, "Dialog window haven't appeared"
            driver.find_element_by_android_uiautomator('new UiSelector().text("Chrome")').click()
            driver.find_element(By.ID, Locators.just_once_button).click()
        browser_url = driver.find_element(By.ID, Locators.browser_url_field)
        assert browser_url.text == "sale.aliexpress.com/ru/__mobile/privacypolicy.htm", "Wrong link in opened browser"
        driver.find_element(By.ID, Locators.browser_switch_tab).click()
        driver.find_element(By.ID, Locators.browser_menu).click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("Close all tabs")').click()
