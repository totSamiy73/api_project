pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build test image') {
            steps {
                sh '''
                docker build -t pytest-runner .
                '''
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

    }

    post {
        always {
            script {
                allure([
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}