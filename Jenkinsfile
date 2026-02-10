pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t find-the-word .'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                docker stop find-the-word || true
                docker rm find-the-word || true
                docker run -d -p 80:5000 --name find-the-word find-the-word
                '''
            }
        }
    }
}
