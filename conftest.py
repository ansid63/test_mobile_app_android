import pytest
import os
import copy
from appium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    ANDROID_BASE_CAPS = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "Samsung Galaxy S9",
        "app": "storage:61f3316b-f0bf-4df0-9127-d2758b1e67f2",
        "app_package": "com.alibaba.aliexpresshd",
        "build": "build-252",
        "noReset": "false",
        "testobject_api_key": "f873206f-f7a2-43d3-a593-99a61c2a3cbd",
    }
    EXECUTOR = "https://andrey.sidorov:f873206f-f7a2-43d3-a593-99a61c2a3cbd@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    caps = copy.copy(ANDROID_BASE_CAPS)

    driver = webdriver.Remote(command_executor=EXECUTOR,
                              desired_capabilities=caps)


    driver.implicitly_wait(10)
    yield driver
    driver.quit()
