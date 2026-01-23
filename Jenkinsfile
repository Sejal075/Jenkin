pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                   credentialsId: 'github-token',
                   url: 'https://github.com/Sejal075/jenkin.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f myapp || true
                docker run -d -p 80:3000 --name myapp myapp:latest
                '''
            }
        }
    }
}