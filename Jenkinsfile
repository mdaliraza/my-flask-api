pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                // Build the image and name it 'my-python-api'
                // On Windows, Jenkins sometimes needs 'bat' instead of 'sh'
                bat 'docker build -t my-python-api .'
            }
        }

        stage('Clean Old Container') {
            steps {
                // Stop and remove the old container if it exists so we can start a fresh one
                bat 'docker stop flask-app || exit 0'
                bat 'docker rm flask-app || exit 0'
            }
        }

        stage('Deploy & Run') {
            steps {
                // Run the new container on port 5000
                bat 'docker run -d -p 5000:5000 --name flask-app my-python-api'
            }
        }
    }
}