pipeline {
    agent any

  
    environment {
        // Docker Hub image info
        IMAGE_NAME = "Alibaih123/python-flask-based-application"  
        IMAGE_TAG  = "latest"            

        
        ROCKY_HOST = "192.182.29.134"      
        ROCKY_USER = "root"        
    }

    stages {
        stage('Pull Code') {
            steps {
                
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
                // Login to Docker Hub 
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
                // SSH into Rocky Linux 
                sshagent(['rocky-ssh']) {
                    sh """
                    ssh $ROCKY_USER@$ROCKY_HOST '
                        docker pull $IMAGE_NAME:$IMAGE_TAG &&
                        docker stop python-flask-based-application || true &&
                        docker rm python-flask-based-application || true &&
                        docker run -d -p 5000:5000 --name python-flask-based-applicaion $IMAGE_NAME:$IMAGE_TAG
                    '
                    """
                }
            }
        }
    }

}