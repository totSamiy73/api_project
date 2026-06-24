stage('Run tests') {
    steps {
        sh '''
        rm -rf allure-results allure-report || true

        docker run --rm \
            -v ${WORKSPACE}:/app \
            -w /app \
            pytest-runner \
            pytest -v --alluredir=/app/allure-results || true
        '''
    }
}

post {
    always {
        sh 'allure generate allure-results -o allure-report --clean || true'

        archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
    }
}