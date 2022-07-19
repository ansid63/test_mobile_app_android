from selenium.webdriver.common.by import By
from PageObject.BasePageObject import BasePageObject


class MenuPageObject(BasePageObject):

    def click_setting(self):
        self.click_element_with_text("Settings")
