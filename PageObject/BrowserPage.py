from selenium.webdriver.common.by import By
from PageObject.BasePageObject import BasePageObject
from Locators import Locators

class BrowserPageObject(BasePageObject):

    def get_url(self):
        browser_url = self.driver.find_element(By.ID, Locators.browser_url_field)
        return browser_url

    def click_privacy_policy_button(self):
        self.driver.find_element(By.ID, Locators.privacy_policy_button).click()

    def close_unusefull_pages(self):
        self.driver.find_element(By.ID, Locators.browser_switch_tab).click()
        self.driver.find_element(By.ID, Locators.browser_menu).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Close all tabs")').click()

    def move_browser_to_background_and_close(self):
        driver.background_app(1)
        driver.background_app(-1)
