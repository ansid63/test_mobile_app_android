import pytest
import os
import textwrap
import sys
import copy
from datetime import datetime
from appium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    ANDROID_BASE_CAPS = {
    'app': os.path.abspath('Ali.apk'),
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': '11.0',
    'deviceName': 'Android Emulator',
    }
    PACKAGE = 'io.appium.android.apis'
    ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples'


    EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

    caps = copy.copy(ANDROID_BASE_CAPS)

    driver = webdriver.Remote(
        command_executor=EXECUTOR,
        desired_capabilities=caps
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    driver.implicitly_wait(10)
    return driver