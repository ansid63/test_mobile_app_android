from PageObject.MenuPage import MenuPageObject
from PageObject.SettingPage import SettingPageObject
from PageObject.PrivacyPolicyPage import PrivacyPolicePageObject
from PageObject.BrowserPage import BrowserPageObject
import allure


class TestAliMoveToChromeLink:
    @allure.title("Переход к политике конфидициальности, с POM")
    def test_move_to_chrome_link(self, driver):
        menu_element = MenuPageObject(driver)
        menu_element.click_menu()
        menu_element.click_setting()
        SettingPageObject(driver).click_privacy_policy_button()

        privacy_page = PrivacyPolicePageObject(driver)
        privacy_page.check_dialog_window()

        privacy_page.click_go_just_once_button()
        browser_page = BrowserPageObject(driver)
        browser_page.check_url()
        browser_page.close_unusefull_pages()
        browser_page.move_browser_to_background_and_close()
