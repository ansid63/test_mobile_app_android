from selenium.webdriver.common.by import By
from PageObject.BasePageObject import BasePageObject


class MenuPageObject(BasePageObject):

    def click_setting(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Settings")').click()
