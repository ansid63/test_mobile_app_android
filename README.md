### Mobile automation tests
> Used tools Python, Appium, pytest, Allure

Before use it, add APK file to the project root.

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

If you need to use branch with docker container, start you docker emulator from current working directory with
```sudo docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container budtmo/docker-android-x86-11.0```
where -v $PWD/Ali.apk:/root/tmp/Ali.apk path to local and docker apk.

[Get more about docker emulator here](https://github.com/budtmo/docker-android)