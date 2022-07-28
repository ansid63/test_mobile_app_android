import pytest
from appium import webdriver
import allure
from src.helpers.helpers import get_base_caps, get_base_executor


@pytest.fixture(scope='function')
def driver(request):
    caps = get_base_caps()
    EXECUTOR = get_base_executor()

    driver = webdriver.Remote(
        command_executor=EXECUTOR,
        desired_capabilities=caps
    )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True, scope="function")
def screenshot_on_failure(driver, request):
    def fin():
        if request.node.rep_setup.failed:
            allure.attach(driver.get_screenshot_as_png(), request.function.__name__, allure.attachment_type.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(driver.get_screenshot_as_png(), request.function.__name__, allure.attachment_type.PNG)

    request.addfinalizer(fin)
