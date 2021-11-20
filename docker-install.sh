#!/bin/bash
# docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts-jdk11

sudo apt update
java -version
sudo apt install default-jre
java -version
sudo apt install default-jdk
java -version

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://yum.dockerproject.org/gpg | sudo apt-key add -

sudo add-apt-repository \
    "deb https://apt.dockerproject.org/repo/ \
    ubuntu-$(lsb_release -cs) \
    main"

sudo apt-get update
sudo apt install docker.io
sudo apt-get -y install docker-engine docker-compose

# add current user to docker group so there is no need to use sudo when running docker
sudo usermod -aG docker $(whoami)

docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts-jdk11
