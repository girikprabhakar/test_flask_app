pipeline {
    environment {
        imagename = "8285/test_flask_app"
        registryCredential = 'docker-hub'
        dockerImage = ''
    }
    agent any
    stages{
        stage("Building image"){
            steps{
                echo "========Builing Image========"
                script {
                    dockerImage = docker.build(imagename)
                }
                // sh 'docker build -t 8285/test_flask_app:latest .'
            }
            // post{
            //     always{
            //         echo "========always========"
            //     }
            //     success{
            //         echo "========A executed successfully========"
            //     }
            //     failure{
            //         echo "========A execution failed========"
            //     }
            // }
        }
        stage("push"){
            steps{
                echo "========Pushing Image========"
                script {
                    docker.withRegistry( "https://registry.hub.docker.com", registryCredential ) {
                    // dockerImage.push("$BUILD_NUMBER")
                    dockerImage.push('latest')
                }
                }
            }
            // post{
            //     always{
            //         echo "========always========"
            //     }
            //     success{
            //         echo "========A executed successfully========"
            //     }
            //     failure{
            //         echo "========A execution failed========"
            //     }
            // }
        }
        stage("deploy"){
            steps{
                echo "========Deploying========"
                sh 'docker-compose up -d'
                sh 'docker image prune -f'
            }
            // post{
            //     always{
            //         echo "========always========"
            //     }
            //     success{
            //         echo "========A executed successfully========"
            //     }
            //     failure{
            //         echo "========A execution failed========"
            //     }
            // }
        }
    }
    
}