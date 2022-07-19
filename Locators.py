from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ElementWithName:
    search_method: str
    locator: str
    locator_name: str

    def __repr__(self):
        return self.locator_name


class NamedLocators:
    MENU_BUTTON = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/left_action", "Кнопка Меню")
    PRIVACY_POLICY_BUTTON = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/rl_privacy_policy_settings", "Кнопка Политика конфидициальности")
    JUST_ONCE_BUTTON = ElementWithName(By.ID, "android:id/button_once", "Кнопка Только один раз")
    BROWSER_URL_FIELD = ElementWithName(By.ID, "com.android.chrome:id/url_bar", "Адресная строка браузера")
    BROWSER_SWITCH_TAB = ElementWithName(By.ID, "com.android.chrome:id/tab_switcher_button", "Таб окна браузера")
    BROWSER_MENU = ElementWithName(By.ID, "com.android.chrome:id/menu_button_wrapper", "Меню браузера")
    CONFIRM_BUTTON_CHROME = ElementWithName(By.ID, "com.android.chrome:id/positive_button", "Кнопка подтверждения браузера")
    LOGIN_MENU_BUTTON = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/profile_name_text", "Кнопка логина меню")
    SIGN_IN_BUTTON = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/btn_sign_in", "Кнопка Залогиниться")
    EMAIL_INPUT_FIELD = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/et_email", "Поле ввода логина")
    PASSWORD_INPUT_FIELD = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/et_password", "Поле ввода логина")
    CONFIRM_BUTTON = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/tv_signin_btn_label", "Кнопка подтверждения")
    DIALOG_WINDOW_ELEMENT = ElementWithName(By.ID, "android:id/message", "Текст диалогового окна")
    ORDER_BUTTON_ELEMENT = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/tv_all_orders", "Кнопка Мои заказы")
    NOTIFICATION_SETTING = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/rl_notification_settings", "Кнопка Настройка уведомлений")
    NOTIFICATION_SALES = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/rl_promotions_sales", "Уведомления Продажи")
    NOTIFICATION_ORDER_UPDATE = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/rl_order_alerts", "Уведомления Обновления заказа")
    REMINDER_FREQUENCY_BUTTON = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/tv_price_reduction_freq", "Кнопка частота уведомлений")
    NOTIFICATION_SWITCH = ElementWithName(By.ID, "com.alibaba.aliexpresshd:id/switch_promotion", "Кнопка вкл/выкл нотификаций")


class TextLocators:
    SETTINGS = "Settings"
    OPEN_WITH_CHROME = "Open with Chrome"
    OPEN_WITH = "Open with"
    CHROME = "Chrome"
    CLOSE_ALL_TABS = "Close all tabs"
    EVERY_3_DAY = "Every 3 days"
