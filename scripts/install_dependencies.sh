#!/usr/bin/env bash

# Install docker
yum -y install docker
service docker start
usermod -a -G docker ec2-user
chkconfig docker on

# Install docker-compose
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose