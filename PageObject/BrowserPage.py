from PageObject.BasePageObject import BasePageObject
from Locators import TextLocators, NamedLocators
from TestData import Data


class BrowserPageObject(BasePageObject):

    def check_url(self):
        self.check_element_text(NamedLocators.BROWSER_URL_FIELD, Data.PRIVACY_POLICY_LINK)

    def close_unusefull_pages(self):
        self.click_element(NamedLocators.BROWSER_SWITCH_TAB)
        self.click_element_with_wait(NamedLocators.BROWSER_MENU, wait_type="clickable", timeout=4)
        self.click_element_with_text(TextLocators.CLOSE_ALL_TABS)
        self.click_element(NamedLocators.CONFIRM_BUTTON_CHROME)

    def move_browser_to_background_and_close(self):
        self.driver.background_app(1)
        self.driver.background_app(-1)
