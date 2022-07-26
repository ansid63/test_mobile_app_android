from src.pages.BasePageObject import BasePageObject
from src.pages.Locators import NamedLocators


class SettingPageObject(BasePageObject):

    def click_privacy_policy_button(self):
        self.click_element(NamedLocators.PRIVACY_POLICY_BUTTON)
