from src.pages.BasePageObject import BasePageObject
from src.pages.Locators import NamedLocators
import time


class MainPageObject(BasePageObject):

    def click_menu_button(self):
        time.sleep(2)
        self.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)
