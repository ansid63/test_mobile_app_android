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
              docker.image('budtmo/docker-android-x86-11.0').withRun('---privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -v $PWD/Ali.apk:/root/tmp/Ali.apk -e DEVICE="Nexus 5" -e APPIUM=true -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 --name android-container') {
                  docker.image('python-mobile-tests').inside("--link android-container") {
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
