pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t pytest-runner .'
            }
        }

        stage('Run tests in Docker') {
            steps {
                sh '''
                rm -rf allure-results || true

                docker run --rm \
                    -v ${WORKSPACE}:/app \
                    -w /app \
                    pytest-runner \
                    pytest -v --alluredir=/app/allure-results || true
                '''
            }
        }
    }

    post {
        always {
            sh 'chown -R $(id -u):$(id -g) allure-results || true'

            script {
                allure([
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}