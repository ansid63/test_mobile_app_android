### Mobile automation tests
> Used tools Python, Appium, pytest, Allure

Before use it, add APK file to the project root.

Where is no clear POM used, all locators in one file, because of main purpose is check mobile testing in different environment.

### Docker branch

If you need to start tests with local docker emulator use branch 'docker': 
1. start you docker emulator from current working directory with
```sudo docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container budtmo/docker-android-x86-11.0```
where -v $PWD/Ali.apk:/root/tmp/Ali.apk path to local_apk:docker_apk. 
2. Use ```EXECUTOR = 'http://127.0.0.1:4723/wd/hub'``` in conftest.py

[Get more about docker emulator here](https://github.com/budtmo/docker-android)
### Start in Jenkins
1. Setup Jenkins, Docker
2. Add Jenkins user to Docker group ```sudousermod-a -G dockerjenkins```
3. Add Pipeline project to Jenkins, similar to [this](https://habr.com/ru/company/simbirsoft/blog/597703/)
4. Use branch 'docker' and ```EXECUTOR = 'http://android:4723/wd/hub'```
5. Launch build in Jenkins

### Parallel execution branch
Just local execution in 2 threads with xdist. pytest-xdist & appium it was interesting.

### Parallel execution docker branch
Tests start in 2 threads, connected to docker containers emulator.
Start emulators with commands from you project root directory:
```
sudo docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5038:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container budtmo/docker-android-x86-11.0

sudo docker run --privileged -d -p 6081:6080 -p 4725:4723 -p 5556:5554 -p 5037:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container-2 budtmo/docker-android-x86-11.0
```

You could look at your test execution at http://localhost:6080/ and http://localhost:6081/
Don't forget to change desired capabilities path to APK,  like 'app': '/root/tmp/Ali.apk'
<br>
<br>

### Автотесты мобильного приложения
> Используемые инструменты Python, Appium, pytest, Allure

Перед использованием проекта, необходимо положить APK файл приложения в корневую папку.


### Docker branch

Если вы хотите прогнать тесты с помощью локального эмулятора, используйте ветку 'docker': 
1. Запустите docker эмулятор из текущей директории с помощью
```sudo docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container budtmo/docker-android-x86-11.0```
где -v $PWD/Ali.apk:/root/tmp/Ali.apk путь к локальное_расположение_apk:docker_apk. 
2. Используйте ```EXECUTOR = 'http://127.0.0.1:4723/wd/hub'``` в conftest.py

[Больше информации про docker эмуляторы здесь](https://github.com/budtmo/docker-android)
### Запуск в Jenkins
1. Настройте Jenkins, Docker
2. Добавьте пользователя Jenkins в Docker группу ```sudousermod-a -G dockerjenkins```
3. Добавьте Pipeline проект в Jenkins, можно ориентироваться на [эту статью](https://habr.com/ru/company/simbirsoft/blog/597703/)
4. Используйте ветку 'docker' и ```EXECUTOR = 'http://android:4723/wd/hub'```
5. Запустите билд в Jenkins

### Ветка parallel execution
Запуск тестов в два потока с использванием библиотеки pytest-xdist.

### Ветка parallel execution docker
Тесты запускаются в 2 потока на docker эмуляторах.
Запустите эмуляторы из корневой директории проекта:
```
sudo docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5038:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container budtmo/docker-android-x86-11.0

sudo docker run --privileged -d -p 6081:6080 -p 4725:4723 -p 5556:5554 -p 5037:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container-2 budtmo/docker-android-x86-11.0
```

Выполнение тестов можно посмотреть на адресам http://localhost:6080/ и http://localhost:6081/
Не забудьте поменять в desired capabilities путь к APK,  например 'app': '/root/tmp/Ali.apk'
<br>