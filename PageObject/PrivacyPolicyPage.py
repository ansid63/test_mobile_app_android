from selenium.webdriver.common.by import By
from PageObject.BasePageObject import BasePageObject
from Locators import Locators

class PrivacyPolicePageObject(BasePageObject):

    def check_dialog_window(self):
        try:
            dialog_window_enabled = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Open with Chrome")').is_enabled()
            return dialog_window_enabled
            
        except NoSuchElementException:
            dialog_window_enabled = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Open with")').is_enabled()
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Chrome")').click()
            return dialog_window_enabled


    def click_go_just_once_button(self):
        self.driver.find_element(By.ID, Locators.just_once_button).click()