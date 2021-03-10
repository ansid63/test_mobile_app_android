from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver


    def click_menu(self):
        menu_element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        menu_element.click()
