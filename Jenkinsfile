pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Sejal075/jenkin.git'
            }
        }

        stage('Build/Run App') {
            steps {
                echo "This is where you can build or run your app without Docker"
                // Example: run a Node.js app
                // sh 'npm install'
                // sh 'node app.js'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
