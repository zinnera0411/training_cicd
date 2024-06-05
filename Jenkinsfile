pipeline {
    triggers {
        // Poll SCM every minute
        pollSCM('* * * * *')
    }
    agent { 
        docker {
            image 'python:3.8' 
            // Run as user with id 1000 (jenkins)
            args '-u 1000:1000' 
        }
    }
    stages {
        // Clean workspace for a fresh start
        stage('Clean workspace') {
            steps {
                echo 'Cleaning up workspace'
                sh 'rm -rf .venv' 
            }
        }
        // Build stage to install dependencies
        stage('Build') {
            steps {
                echo "Installing dependencies"
                sh '''
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
    }
}
