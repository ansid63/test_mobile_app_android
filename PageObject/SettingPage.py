from selenium.webdriver.common.by import By
from PageObject.BasePageObject import BasePageObject
from Locators import Locators

class SettingPageObject(BasePageObject):

    def click_privacy_policy_button(self):
        self.driver.find_element(By.ID, Locators.privacy_policy_button).click()
