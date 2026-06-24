pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t pytest-runner .'
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                rm -rf allure-results allure-report || true

                docker run --rm \
                    -v ${WORKSPACE}:/app \
                    -w /app \
                    pytest-runner \
                    pytest -v --alluredir=/app/allure-results
                '''
            }
        }

        stage('Generate Allure report') {
            steps {
                sh '''
                allure generate allure-results -o allure-report --clean
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
        }
    }
}