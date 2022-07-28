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
    "appium:app": os.path.abspath(os.path.join(ROOT_DIR, "Ali.apk")),
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': '11.0',
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
    }
    match worker_number:
        case 'gw0':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
        case 'master':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5554'
        case 'gw1':
            ANDROID_BASE_CAPS["appium:udid"] = 'emulator-5556'
    caps = copy.copy(ANDROID_BASE_CAPS)
    return caps
