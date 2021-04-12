pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Bash') {
            steps {
                sh '''#!/bin/bash
                    echo "Hello from bash"
                '''
            }
        }
    }
}
