# Install Docker
curl -s https://get.docker.io/ubuntu/ | sudo sh

# Pull jenkins docker image trusted build
sudo docker pull orchardup/jenkins

# Start jenkins container
sudo docker run -d -p 80:5050 orchardup/jenkins
