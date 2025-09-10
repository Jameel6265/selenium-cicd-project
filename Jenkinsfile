// Jenkinsfile

pipeline {
    agent any // This pipeline can run on any available Jenkins agent

    stages {
        // STAGE 1: Clean the workspace before starting
        stage('Cleanup') {
            steps {
                echo 'Cleaning up the workspace...'
                cleanWs() // Deletes files from previous builds
            }
        }

        // STAGE 2: Pull the latest code from GitHub
        stage('Checkout from Git') {
            steps {
                echo 'Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/Jameel6265/selenium-cicd-project.git'
            }
        }

        // STAGE 3: Install dependencies inside virtual environment
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // STAGE 4: Run the Selenium tests
        stage('Run Tests') {
            steps {
                echo 'Running Selenium tests...'
                sh '''
                    . venv/bin/activate
                    pytest --html=report.html || true
                '''
            }
        }
    }

    post {
        // This 'post' block runs after all stages are complete, regardless of success or failure.
        always {
            echo 'Archiving test report...'
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Selenium Test Report'
            ])
        }
    }
}
