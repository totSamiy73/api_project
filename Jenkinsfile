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
                rm -rf allure-results || true

                docker run --rm \
                    -v ${WORKSPACE}:/app \
                    -w /app \
                    pytest-runner \
                    pytest -v --alluredir=/app/allure-results
                '''
            }
        }

        stage('Generate Allure HTML') {
            steps {
                sh '''
                rm -rf allure-report || true
                allure generate allure-results -o allure-report --clean
                '''
            }
        }

        stage('Publish report') {
            steps {
                publishHTML([
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }
    }
}