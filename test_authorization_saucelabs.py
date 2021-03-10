from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from TestData import Data
from Locators import Locators


class TestAliAuthorizationAndMenuSwipe:

    def test_authorization_with_wrong_data(self, driver):
        menu_element = \
            WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        menu_element.click()
        authorization_button = driver.find_element(By.ID, Locators.login_menu_button)
        authorization_button.click()
        login_button = driver.find_element(By.ID, Locators.log_button)
        login_button.click()
        email_field = driver.find_element(By.ID, Locators.email_input_field)
        email_field.send_keys(Data.WRONG_EMAIL)
        password_field = driver.find_element(By.ID, Locators.password_input_field)
        password_field.send_keys(Data.WRONG_PASSWORD)
        sign_in_button = driver.find_element(By.ID, Locators.confirm_button)
        sign_in_button.click()
        dialog_window = driver.find_element(By.CLASS_NAME, Locators.dialog_window_el).is_enabled()
        assert dialog_window is True, "Dialog window haven't appeared"
