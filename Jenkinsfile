pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Clean Allure results') {
            steps {
                sh 'rm -rf allure-results || true'
            }
        }

        stage('Run tests in Docker') {
            steps {
                sh '''
                docker run --rm \
                    --user $(id -u):$(id -g) \
                    -v ${WORKSPACE}:/app \
                    -w /app \
                    python:3.12-slim \
                    bash -c "
                        pip install -r requirements.txt &&
                        pytest -v --alluredir=/app/allure-results
                    "
                '''
            }
        }

        stage('Prepare Allure History') {
            steps {
                sh '''
                if [ -d allure-report/history ]; then
                    cp -r allure-report/history allure-results/
                fi
                '''
            }
        }

    }

    post {
        always {
            script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}