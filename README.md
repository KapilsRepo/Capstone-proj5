[![CircleCI](https://dl.circleci.com/status-badge/img/gh/KapilsRepo/Capstone-proj5/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/KapilsRepo/Capstone-proj5/tree/main)
      

## Project Overview

## Step 1: Propose and Scope the Project

## 1.1 How the Pipeline will look like ?

The Circle CI Pipeline workflow will have four basic steps
* Build : This will build the environment and install all dependencies. Also LInting and testing will be done in it.
* Docker -Build : Docker is build for the application and the docker image is then pushed to [Docker hub repository] ()
* aws-eks/create-cluster : AWS Kubernetes Cluster is created.
* create-deployment : Rolling deployment is used to roll out the application to Production

## 1.2 Deployment strategy

We would use the concept learned as part of the course and would utilise them 

- Continuous integration- circle ci 
- Connectivity to the Git respository
- Deployment Type - Rolling deployment
- Application - Hello world build by docker , deployed by AWS Kubernetes

## Step 2: Use Jenkins or Circle CI, and implement blue/green or rolling deployment.

- If you're using Circle CI, set up your circle CI account and connect your git repository.
- Set up your environment to which you will deploy code.

## Step 3: Build your own Kubernetes cluster.

- Use Ansible or CloudFormation to build your “infrastructure”; i.e., the Kubernetes Cluster.
- Set up new EC2 instances

## Step 4 Build your pipeline

- Git hub pipeline (supply - url to the git hub)
- circleci screen shots (supply - circleci screenshots)
- Docker and Makefile
- Failed and Successful linting

## Step 5 Test your pipeline
- screen shots of the newly created instances
- verify pipeline


## Important Links
* Docker hub Repo : https://hub.docker.com/repository/docker/kapmydock23/kapilscaps
* Github Repo: https://github.com/KapilsRepo/Capstone-proj5
* Load Balancer Link: https://us-east-2.console.aws.amazon.com/ec2/home?region=us-east-2#LoadBalancers:

### Files:
*	Makefile - This is a basic file which is used to consolidate commands to be run like set up environment, install dependencies, runs tests and run lints.
*	Dockerfile - This file is to build Docker image and then run the image to make app running on docker container
*	requirements.txt - This is used to enable what all dependencies are to be installed.
*	app.py - Hello World python flask application
*	app-test.py - To test the Hello World python application 
*	networksetup.yml - This is to setup the load balancer configuration
*	resourcesetup.yml - This is to do the steps for rolling deployment of appliaction in production

## References
https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html
https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html
https://circleci.com/developer/orbs/orb/circleci/aws-eks#usage-create-k8s-deployment
https://circleci.com/developer/orbs/orb/circleci/aws-eks
https://github.com/CircleCI-Public/circleci-demo-aws-eks