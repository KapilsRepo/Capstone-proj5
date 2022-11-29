
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Shubhi87/UdacityCapstone/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Shubhi87/UdacityCapstone/tree/master)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Shubhi87/UdacityCapstone/tree/master.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/Shubhi87/UdacityCapstone/tree/master)

## Project Overview

In this project, I have applied the skills which I have acquired in the complete course- Cloud Devops Nanodegree.

I have used here circle ci orb for creating kubernetes cluster and running and deploying the app.The app is just a simple Hello World Python flask app. Linting and testing is added to check for errors in the format of files as well as testing the basic routing.
- Continuous integration- circle ci 
- Deployment Type - Rolling deployment
- Application - Hello world build by docker , deployed by AWS Kubernetes


## References
https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html
https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html
https://circleci.com/developer/orbs/orb/circleci/aws-eks#usage-create-k8s-deployment
https://circleci.com/developer/orbs/orb/circleci/aws-eks
https://github.com/CircleCI-Public/circleci-demo-aws-eks
  
## Circle CI Pipeline
The Circle CI Pipeline workflow will have four basic steps
* Build : This will build the environment and install all dependencies. Also LInting and testing will be done in it.
* Docker -Build : Docker is build for the application and the docker image is then pushed to [Docker hub repository] (https://hub.docker.com/repository/docker/shubhi87/myudacitycapstone1)
* aws-eks/create-cluster : AWS Kubernetes Cluster is created.
* create-deployment : Rolling deployment is used to roll out the application to Production

## Important Links
* Docker hub Repo : https://hub.docker.com/repository/docker/shubhi87/myudacitycapstone1
* Github Repo: https://github.com/Shubhi87/UdacityCapstone
* Load Balancer Link: http://a280d6538b64e46829d69e3c8c502f68-927335322.us-east-1.elb.amazonaws.com/

### Files:
*	Makefile - This is a basic file which is used to consolidate commands to be run like set up environment, install dependencies, runs tests and run lints.
*	Dockerfile - This file is to build Docker image and then run the image to make app running on docker container
*	requirements.txt - This is used to enable what all dependencies are to be installed.
*	app.py - Hello World python flask application
*	app-test.py - To test the Hello World python application 
*	networksetup.yml - This is to setup the load balancer configuration
*	release.yml - This is to do the steps for rolling deployment of appliaction in production