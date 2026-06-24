pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run tests in Docker') {
            steps {
                sh '''
                docker run --rm \
                    -v $PWD:/app \
                    -w /app \
                    python:3.12-slim \
                    bash -c "
                        pip install -r requirements.txt &&
                        pytest -v
                    "
                '''
            }
        }
    }
}