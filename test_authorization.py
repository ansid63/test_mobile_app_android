import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from TestData import Locators, Data


class TestAliAuthorizationAndMenuSwipe:

    def test_authorization_with_wrong_data(self, driver):
        menu_element = \
            WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
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
        dialog_window = driver.find_element(By.ID, Locators.dialog_window_el)
        dialog_window_text = dialog_window.text
        assert dialog_window_text == 'Password is incorrect. Please try again.'

    def test_authorization_correct_data(self, driver):
        menu_element = \
            WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        menu_element.click()
        authorization_button = driver.find_element(By.ID, Locators.login_menu_button)
        authorization_button.click()
        login_button = driver.find_element(By.ID, Locators.log_button)
        login_button.click()
        email_field = driver.find_element(By.ID, Locators.email_input_field)
        email_field.send_keys(Data.CORRECT_EMAIL)
        password_field = driver.find_element(By.ID, Locators.password_input_field)
        password_field.send_keys(Data.CORRECT_PASSWORD)
        sign_in_button = driver.find_element(By.ID, Locators.confirm_button)
        sign_in_button.click()
        order_button = driver.find_element_by_id(Locators.order_button_el)
        order_button_enabled = order_button.is_enabled()
        order_button_text = order_button.text
        assert order_button_enabled is True and order_button_text == 'My Orders'

    def test_menu_swipe(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, Locators.menu_button)))
        driver.swipe(0, 1080, 500, 1080, 250)
        time.sleep(3)
