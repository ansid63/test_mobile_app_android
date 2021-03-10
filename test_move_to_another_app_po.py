from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from TestData import Data
from Locators import Locators
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from PageObject.MenuPage import MenuPageObject
from PageObject.SettingPage import SettingPageObject
from PageObject.PrivacyPolicyPage import PrivacyPolicePageObject
from PageObject.BrowserPage import BrowserPageObject


class TestAliMoveToChromeLink:

    def test_move_to_chrome_link(self, driver):
        menu_element = MenuPageObject(driver)
        menu_element.click_menu()
        menu_element.click_setting()
        SettingPageObject(driver).click_privacy_policy_button()

        privacy_page = PrivacyPolicePageObject(driver)
        dialog_window_for_redirect_is_enabled = privacy_page.check_dialog_window()
        assert dialog_window_for_redirect_is_enabled is True, "Dialog window haven't appeared"

        privacy_page.click_go_just_once_button()
        browser_page = BrowserPageObject(driver)
        browser_url= browser_page.get_url()
        assert browser_url.text == "sale.aliexpress.com/ru/__mobile/privacypolicy.htm", "Wrong link in opened browser"
        browser_page.close_unusefull_pages()
        browser_page.move_browser_to_background_and_close()
