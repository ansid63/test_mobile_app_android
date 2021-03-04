import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestAliAutorization():

    def test_authorization_with_wrong_data(self, driver):
        menu_element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, 'com.alibaba.aliexpresshd:id/left_action')))
        menu_element.click()
        authorization_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/profile_name_text')
        authorization_button.click()
        login_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/btn_sign_in')
        login_button.click()
        email_field = driver.find_element_by_id('com.alibaba.aliexpresshd:id/et_email')
        email_field.send_keys('77345@yahoo.com')
        password_field = driver.find_element_by_id('com.alibaba.aliexpresshd:id/et_password')
        password_field.send_keys('12345')
        sign_in_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/tv_signin_btn_label')
        sign_in_button.click()
        dialog_window = driver.find_element_by_id('android:id/message')
        dialog_window_text = dialog_window.text
        assert dialog_window_text == 'Password is incorrect. Please try again.'


    def test_authorization_correct_data(self, driver):
        menu_element = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, 'com.alibaba.aliexpresshd:id/left_action')))
        menu_element.click()
        authorization_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/profile_name_text')
        authorization_button.click()
        login_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/btn_sign_in')
        login_button.click()
        email_field = driver.find_element_by_id('com.alibaba.aliexpresshd:id/et_email')
        email_field.send_keys('email')
        password_field = driver.find_element_by_id('com.alibaba.aliexpresshd:id/et_password')
        password_field.send_keys('Password')
        sign_in_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/tv_signin_btn_label')
        sign_in_button.click()
        order_button = driver.find_element_by_id('com.alibaba.aliexpresshd:id/tv_all_orders')
        order_button_enabled = order_button.is_enabled()
        order_button_text = order_button.text
        assert order_button_enabled is True and order_button_text == 'My Orders'
