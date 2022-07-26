from src.pages.MainPage import MainPageObject
from src.pages.MenuPage import MenuPageObject
from src.pages.SettingPage import SettingPageObject
from src.pages.PrivacyPolicyPage import PrivacyPolicePageObject
from src.pages.BrowserPage import BrowserPageObject
import allure
import time


class TestAliMoveToChromeLink:
    @allure.title("Переход к политике конфидициальности, с POM")
    def test_move_to_chrome_link(self, driver):
        main_page = MainPageObject(driver)
        main_page.click_menu_button()
        menu_page = MenuPageObject(driver)
        menu_page.click_setting()
        SettingPageObject(driver).click_privacy_policy_button()

        privacy_page = PrivacyPolicePageObject(driver)
        privacy_page.check_dialog_window()

        privacy_page.click_go_just_once_button()
        browser_page = BrowserPageObject(driver)
        browser_page.check_url()
        browser_page.close_unusefull_pages()
        browser_page.close_app()
        browser_page.close_app_with_name("com.android.chrome")
