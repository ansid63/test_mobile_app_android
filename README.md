### Mobile automation tests
> Used tools Python, Appium, pytest, Allure

test_authorization.py
1. Create test "Falled authorization". Result: Authorization filed, fail notification.
2. Create test "Correct authorization". Result: Authorization passed.
3. Create test "Open left side menu by swipe'. Result: Opened menu.

test_turn_off_notification.py
1. Turn off notification. Work with switch element. Result: notification turned off.

test_change_reminder_frequency.py
1.  Change notification reminder to 3 days option. Result: reminder each 3 day.

test_move_to_another_app.py
1. Move from mobile app to web page in Chrome. Result: opened webpage https://sale.aliexpress.com/__mobile/privacypolicy.htm

test_move_to_another_app_po.py 
Same as test_move_to_another_app but with PageObject Structure
1. Move from mobile app to web page in Chrome. Result: opened webpage https://sale.aliexpress.com/__mobile/privacypolicy.htm