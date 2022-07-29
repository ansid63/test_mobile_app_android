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
          docker.image('selenoid/android:10.0')
          }
        }
      }
    }
    stage('Run tests') {
      steps {
        catchError {
          script {
              docker.image('aerokube/selenoid:1.10.4').withRun('--name selenoid -p 4444:4444 -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/',
                '-service-startup-timeout 120s -session-attempt-timeout 120s -session-delete-timeout 120s -timeout 600s -limit 2') { c ->
                  docker.image('aerokube/selenoid-ui:1.10.4').withRun('--link selenoid -p 8888:8080', '--selenoid-uri http://selenoid:4444') {
                  docker.image('python-mobile-tests').inside("--link ${c.id}:selenoid") {
                        sh "pytest ${CMD_PARAMS}"
                    }
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