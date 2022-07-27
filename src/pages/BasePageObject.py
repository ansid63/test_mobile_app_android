import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.pages.Locators import NamedLocators
from src.pages.Locators import ElementWithName


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        self.click_element_with_wait(NamedLocators.MENU_BUTTON, wait_type="clickable", timeout=10)

    def get_element_with_wait(self, element: ElementWithName, wait_type, timeout):
        if wait_type == "clickable":
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((element.search_method, element.locator)))
        return element

    def get_element(self, element: ElementWithName):
        r_element = self.driver.find_element(element.search_method, element.locator)
        return r_element

    @allure.step("Нажать на {element} с ожиданием {timeout} с.")
    def click_element_with_wait(self, element: ElementWithName, wait_type, timeout):
        point = self.get_element_with_wait(element, wait_type, timeout)
        point.click()

    def get_element_with_text(self, text):
        element = self.driver.find_element_by_android_uiautomator(f'new UiSelector().text("{text}")')
        return element

    @allure.step("Нажать на элемент с текстом {text}.")
    def click_element_with_text(self, text):
        point = self.get_element_with_text(text)
        point.click()

    @allure.step("Нажать на элемент {element}.")
    def click_element(self, element: ElementWithName):
        self.driver.find_element(element.search_method, element.locator).click()

    @allure.step("Проверить что у элемента {text} состояние {condition}")
    def check_element_with_text_status(self, text, condition):
        if condition == "is_enabled":
            element = self.get_element_with_text(text)
            assert element.is_enabled()
        return element

    @allure.step("Проверить что у элемента {element} состояние {condition}")
    def check_element_status(self, element: ElementWithName, condition):
        try:
            if condition == "is_enabled":
                r_element = self.get_element(element)
                assert r_element.is_enabled()
        except NoSuchElementException:
            raise AssertionError(f"Элемент {element} не в состоянии {condition}")
        return r_element

    @allure.step("Проверить что текст элемента {element} соответствует {expected_text}")
    def check_element_text(self, element: ElementWithName, expected_text):
        received_text = self.get_element(element).text
        assert received_text == expected_text, f"Некорректный текст, ожидаемый текст {expected_text}, " \
                                               f"фактический текст {received_text}"

    @allure.step("Отправить в элемент {element} текст {text}")
    def send_text_to_element(self, element: ElementWithName, text):
        self.get_element(element).send_keys(text)

    @allure.step("Закрыть тестируемое приложение")
    def close_app(self):
        self.driver.reset()

    @allure.step("Закрыть приложение с именем пакета {package_name}")
    def close_app_with_name(self, package_name):
        self.driver.terminate_app(app_id=package_name)
