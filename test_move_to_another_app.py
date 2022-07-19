import allure
from selenium.common.exceptions import NoSuchElementException

from TestData import Data
from Locators import NamedLocators, TextLocators
from PageObject.BasePageObject import BasePageObject


class TestAliMoveToChromeLink:
    @allure.title("Переход в другое приложение.")
    def test_move_to_chrome_link(self, driver):
        base_page = BasePageObject(driver)
        base_page.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)
        base_page.click_element_with_text(TextLocators.SETTINGS)
        base_page.click_element(NamedLocators.PRIVACY_POLICY_BUTTON)
        try:
            base_page.check_element_with_text_status(TextLocators.OPEN_WITH_CHROME, "is_enabled")
            base_page.click_element(NamedLocators.JUST_ONCE_BUTTON)
        except NoSuchElementException:
            base_page.check_element_with_text_status(TextLocators.OPEN_WITH, "is_enabled")
            base_page.click_element_with_text(TextLocators.CHROME)
            base_page.click_element(NamedLocators.JUST_ONCE_BUTTON)
        base_page.check_element_text(NamedLocators.BROWSER_URL_FIELD, Data.PRIVACY_POLICY_LINK)
        base_page.click_element(NamedLocators.BROWSER_SWITCH_TAB)
        base_page.click_element_with_wait(NamedLocators.BROWSER_MENU, wait_type="clickable", timeout=4)
        base_page.click_element_with_text(TextLocators.CLOSE_ALL_TABS)
        base_page.click_element(NamedLocators.CONFIRM_BUTTON_CHROME)
        driver.reset()
        driver.terminate_app(app_id="com.android.chrome")
