# L3T11 - Introduction to NLP
Requirement for HyperionDeV SE Bootcamp - L3T11

## Introduction
This task serves as an introduction to natural language processing (NLP) - currently one of the largest fields of research in AI.

## Task Requirements:

Create a Python file called 'garden.py' which contains a list of 5 garden path sentences. Each sentence should then be tokenised and entity recognition performed.
Use the spacy.explain function to look up and print the meaning of the entities.

# How to run 'garden.py'
You can run the python file by follwing the below steps:
1. Clone this repository onto your machine
1. If you have not already done so, you will need to download Docker Desktop by visiting https://www.docker.com/products/docker-desktop/
1. If you don't already have a Docker Hub account, visit this website and create one: https://hub.docker.com
1. Navigate to the directory which contains the Dockerfile and build a Docker image by running this command in Terminal(Macbooks): "docker build --platform linux/amd64/v8 -t [name of your docker image] ./"
1. Run the program by enterin the following into your terminal: "docker run [image name]" NOTE: Afterwards the container will automatically shut down.
