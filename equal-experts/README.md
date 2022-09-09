# Equal Experts Challenge

## Question

### Mini Kube
Write a simple hello world application in any one of these languages: Python, Ruby, Go. Build the application within a Docker container and then load balance the application within Minikube. You are not required to automate the installation of Minikube on the host machine.

## Answer: Hello World Python Application

This is a simple "Hello, World!" application that is written in Python and uses Docker as Container service. The application displays a Hello, World! webpage under the URL http://localhost:55000 when the docker image is executed. This application can also be deployed into the Kubernetes using the "helloworld.yaml" file. 

## Requirements
- Python 3.9
- Docker (latest version)
- Minikube (latest version)

## Prerequisite
Docker and Minikube should be up and running. The Docker environment must be set to the Minikube. This can be configured by running the command below.

```sh
eval $(minikube docker-env)
```
or 
```sh
minikube -p minikube docker-env
```

## How to run

As mentioned in the requirements, it is important the Docker and Minikube are working fine and has enough memory to launch the required pods before running the application. I assume that the user knows how to use these two tools in general. 
