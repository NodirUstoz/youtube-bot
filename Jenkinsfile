pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'YTD-ssh', url: 'git@github.com:ZeroNiki/Youtube-Downloader-Bot.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'YTD-ssh', url: 'git@github.com:ZeroNiki/Youtube-Downloader-Bot.git'
                sh 'touch .env'
                sh 'rm .env'
                sh 'mkdir -p output/video output/mp3 output/jpg'
                sh 'ls -ld /var/lib/YTD-db/'
                sh 'echo "TOKEN=AAGpbHWKlTCYegMipoNqBHkfi6YhCWo2UYQ" >> .env'
                sh 'echo "ADMIN=ADMIN_ID" >> .env'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                sh 'nohup python3 main.py > logfile.log &2>&1 &'
            }
        }
    }
}
