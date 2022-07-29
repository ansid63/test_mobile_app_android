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
    'app': os.path.abspath(os.path.join(ROOT_DIR, "Ali.apk")),
    'automationName': 'UIAutomator2',
    'deviceName': 'android',
    'version': '10.0',
    "enableVNC": True,
    }
    match worker_number:
        case 'gw0':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
            # ANDROID_BASE_CAPS["appium:adbPort"] = 5038
        case 'master':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
            # ANDROID_BASE_CAPS["appium:adbPort"] = 5038
        case 'gw1':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
            # ANDROID_BASE_CAPS["appium:adbPort"] = 5037
    caps = copy.copy(ANDROID_BASE_CAPS)
    return caps


def get_base_executor():
    worker_number = get_worker_index()
    match worker_number:
        case 'gw0':
            executor = 'http://selenoid:4444/wd/hub'
        case 'master':
            executor = 'http://selenoid:4444/wd/hub'
        case 'gw1':
            executor = 'http://selenoid:4444/wd/hub'
    return executor
