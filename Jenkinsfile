pipeline {
    agent any

    environment {
        IMAGE_NAME = "sreelasya24/first-devopsimage"     // Docker image name (your image)
        IMAGE_TAG = "v1"                                 // Image tag
        DEPLOYMENT_FILE = "deployment.yaml"              // Kubernetes Deployment manifest
        SERVICE_FILE = "service.yaml"                    // Kubernetes Service manifest
    }

    stages {

        stage('Build Docker Image') {
            steps {
                echo "🏗️ Building Docker Image..."
                bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "🔐 Logging into Docker Hub..."
                bat 'docker login -u sreelasya24 -p Shree2401!'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "📦 Pushing Docker Image to Docker Hub..."
                bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "🚀 Deploying to Kubernetes..."
                bat "kubectl apply -f ${DEPLOYMENT_FILE} -f ${SERVICE_FILE} --validate=false"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully — ${IMAGE_NAME}:${IMAGE_TAG} deployed!"
        }
        failure {
            echo "❌ Pipeline failed. Please check the logs."
        }
    }
}
