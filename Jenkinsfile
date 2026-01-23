pipeline {
    agent any

    stages {

        stage('Clone Repository') {
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

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f myapp || true
                docker run -d -p 80:3000 --name myapp myapp:latest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Application deployed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
