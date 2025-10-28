pipeline{
    agent { label "worker-node"}
    
    environment {
        SONAR_HOME= tool "sonar-sc"
    }
    stages{
        stage("Clean Workspace"){
            steps{
                cleanWs()
            }
        }
        stage("Checkout from Git"){
            steps{
                git url: "https://github.com/biswarup65/Two-tier-app-flask.git", branch: "main"
            }
        }
        stage("SonarQube Code Analysis"){
            steps{
                withSonarQubeEnv("sonarqube-server"){
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=flask-app -Dsonar.projectKey=flask-app -X"
                }
            }
        }
        stage("SonarQube Quality Gate"){
            steps{
                script{
                    waitForQualityGate abortPipeline: false, credentialsId: "sonar"
                }
            }
        }
        
        stage("Install Dependencies"){
            steps{
                
                sh "pip install --no-cache-dir -r requirements.txt"
            }
        }
        
        stage("OWASP Dependency Check"){
            steps{
                dependencyCheck additionalArguments: '--scan ./ --disableYarnAudit --disableNodeAudit', odcInstallation: 'owasp-dc'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
        stage("Docker Build & Test"){
            steps{
                sh "docker build --no-cache -t two-tier-flask:latest ."
            }
        }
        stage("Trivy Scanning"){
            steps{
                sh "trivy image two-tier-flask:latest "
            }
        }
        stage("Trivy File System Scan"){
            steps{
                sh "trivy fs --format table -o trivy-fs-report.html . "
            }
        }
        stage("Docker Push"){
            steps{
                withCredentials([usernamePassword(credentialsId: "docker-hub",usernameVariable:"dockerhub_user",passwordVariable:"dockerhub_pass")]){
                    sh "docker login -u ${env.dockerhub_user} -p ${env.dockerhub_pass}"
                    sh "docker tag two-tier-flask:latest ${env.dockerhub_user}/two-tier-flask:v5  "
                    sh "docker push ${env.dockerhub_user}/two-tier-flask:v5 "
                }
            }
        }
        stage("Deploy the app"){
            steps{
                sh "docker run -d --name two-tier-flask -p 5000:5000 biswarup65/two-tier-flask:v5"
            }
        }
    }
}