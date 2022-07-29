pipeline {
  agent any
  stages {
    stage("Build image") {
      steps {
        catchError {
          script {
            docker.build("python-mobile-tests", "-f Dockerfile .")
          }
         }
      }
    }
    stage('Pull emulator') {
      steps {
        catchError {
          script {
          docker.image('budtmo/docker-android-x86-11.0')
          }
        }
      }
    }
    stage('Run tests') {
      steps {
        catchError {
          script {
              docker.image('budtmo/docker-android-x86-11.0').withRun('--privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5038:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android')
              docker.image('budtmo/docker-android-x86-11.0').withRun('--privileged -d -p 6081:6080 -p 4725:4723 -p 5556:5554 -p 5037:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android_2')
              {
                  docker.image('python-mobile-tests').inside("--link android android_2") {
                        sh "sleep 2m"
                        sh "pytest ${CMD_PARAMS}"
                    }
                  }
               }
            }
          }
        }
    stage('Reports') {
      steps {
        allure([
          includeProperties: false,
          jdk: '',
          properties: [],
          reportBuildPolicy: 'ALWAYS',
          results: [[path: 'report']]
        ])
      }
    }
  }
}