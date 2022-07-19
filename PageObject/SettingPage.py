from PageObject.BasePageObject import BasePageObject
from Locators import NamedLocators


class SettingPageObject(BasePageObject):

    def click_privacy_policy_button(self):
        self.click_element(NamedLocators.PRIVACY_POLICY_BUTTON)
