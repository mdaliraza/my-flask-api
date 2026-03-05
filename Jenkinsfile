pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Move into the folder that we mapped from Windows
                dir('/test_app') {
                    sh 'docker build -t my-python-api .'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                sh 'docker run -d -p 5000:5000 --name flask-app my-python-api'
            }
        }
    }
}