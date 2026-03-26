pipeline {
    agent any

    // Global environment variables
    environment {
        // Docker Hub image info
        IMAGE_NAME = "Alibaih123/Python-Flask-based-application"   // Replace with your Docker Hub username & repo
        IMAGE_TAG  = "latest"             // Can also use version tags like v1.0.0

        // Deployment server info
        ROCKY_HOST = "192.182.29.134"      // Replace with Rocky Linux IP
        ROCKY_USER = "root"         // SSH user on Rocky Linux
    }

    stages {
        stage('Pull Code') {
            steps {
                // Pull latest code from GitHub
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image locally on Jenkins
                sh """
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Login to Docker Hub securely using Jenkins credentials
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-credenials', 
                    usernameVariable: 'DOCKER_USER', 
                    passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    """
                }
            }
        }

        stage('Deploy to Rocky Linux') {
            steps {
                // SSH into Rocky Linux and deploy the latest image
                sshagent(['rocky-ssh']) {
                    sh """
                    ssh $ROCKY_USER@$ROCKY_HOST '
                        docker pull $IMAGE_NAME:$IMAGE_TAG &&
                        docker stop Python-Flask-based-application || true &&
                        docker rm Python-Flask-based-application || true &&
                        docker run -d -p 5000:5000 --name Python-Flask-based-applicaion $IMAGE_NAME:$IMAGE_TAG
                    '
                    """
                }
            }
        }
    }

}