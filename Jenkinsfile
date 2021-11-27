pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/NAVEENINTEL/java-webapp.git'
              withMaven(maven: 'mavenhome') {
                    sh "mvn -f DEV/pom.xml clean package"
                   // sh "docker run -it --rm -p 9090:9090 tomcat:9.0"
                    
                }
            }
             post {
                success {
                    echo "Now Archiving the Artifacts...."
                    archiveArtifacts artifacts: '**/*.war'
                    deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9090')], contextPath: '/', onFailure: false, war: '**/*.war'
                    deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9091')], contextPath: '/', onFailure: false, war: '**/*.war'
                }
            }
        }
       stage('Staging') {
             steps {
                 echo "Staging"
             }
           post {
                success {
                    deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9090')], contextPath: '/', onFailure: false, war: '**/*.war'
                    //deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9091')], contextPath: '/', onFailure: false, war: '**/*.war'
                }
            }
        }
        stage('QA') {
             steps {
                 echo "QA"
             }
           post {
                success {
                    echo "QA"
                    //deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9090')], contextPath: '/', onFailure: false, war: '**/*.war'
                    //deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9091')], contextPath: '/', onFailure: false, war: '**/*.war'
                }
            }
        }
        stage('Create Tomcat Docker Image'){
            steps {
                sh "docker build . -t tomcatsamplewebapp:${env.BUILD_ID}"
            }
        }
        stage('Production') {
             steps {
                 echo "Production"
             }
            
           post {
                success {
                     timeout(time:5, unit:'DAYS'){
                    input message:'Approve PRODUCTION Deployment?'
                    deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9091')], contextPath: '/', onFailure: false, war: '**/*.war'

                }
                    //deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9090')], contextPath: '/', onFailure: false, war: '**/*.war'
                    //deploy adapters: [tomcat9(credentialsId: '26401337-7b69-4467-bff3-047ce5268db5', path: '', url: 'http://147.182.216.233:9091')], contextPath: '/', onFailure: false, war: '**/*.war'
                }
            }
        }
    }
}
