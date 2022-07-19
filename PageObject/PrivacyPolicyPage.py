from selenium.common.exceptions import NoSuchElementException
from PageObject.BasePageObject import BasePageObject
from Locators import TextLocators, NamedLocators


class PrivacyPolicePageObject(BasePageObject):

    def check_dialog_window(self):
        try:
            self.check_element_with_text_status(TextLocators.OPEN_WITH_CHROME, "is_enabled")
            
        except NoSuchElementException:
            self.check_element_with_text_status(TextLocators.OPEN_WITH, "is_enabled")
            self.click_element_with_text(TextLocators.CHROME)

    def click_go_just_once_button(self):
        self.click_element(NamedLocators.JUST_ONCE_BUTTON)
