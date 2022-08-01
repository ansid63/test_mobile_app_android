from pathlib import Path
import os
import copy


ROOT_DIR = Path(__file__).parent.parent.parent

def get_worker_index():
    worker = os.getenv('PYTEST_XDIST_WORKER')
    return worker


def get_base_caps():
    worker_number = get_worker_index()
    ANDROID_BASE_CAPS = {
    'app': '/root/tmp/Ali.apk',
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': '11.0',
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "adbExecTimeout": 50000
    }
    match worker_number:
        case 'gw0':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
            ANDROID_BASE_CAPS["appium:adbPort"] = 5038
        case 'master':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
            ANDROID_BASE_CAPS["appium:adbPort"] = 5038
        case 'gw1':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
            ANDROID_BASE_CAPS["appium:adbPort"] = 5038
    caps = copy.copy(ANDROID_BASE_CAPS)
    return caps


def get_base_executor():
    worker_number = get_worker_index()
    match worker_number:
        case 'gw0':
            executor = 'http://android:4723/wd/hub'
        case 'master':
            executor = 'http://android:4723/wd/hub'
        case 'gw1':
            executor = 'http://android_2:4725/wd/hub'
    return executor
