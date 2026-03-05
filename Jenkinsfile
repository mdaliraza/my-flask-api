pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins automatically pulls code from GitHub because of the SCM setting
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                // We use 'sh' because the Jenkins container is Linux-based
                sh 'docker build -t my-python-api .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                // Port 5000 is where your API will live
                sh 'docker run -d -p 5000:5000 --name flask-app my-python-api'
            }
        }
    }
}