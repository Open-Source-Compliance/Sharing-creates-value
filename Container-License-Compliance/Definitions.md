## Docker image
A docker image is a file consisting of a stack of layers. It can be viewed like an software image for e.g. an embedded device. Each layer consists of one or more binary packages, config files, environment variables etc.. It is an appliance which includes the application and everything the application needs to run. 

## Docker container
A docker container is the run time instance of a Docker image. I.e. a docker container is created when the command docker run is executed. Besides the docker image a docker container includes runtime data, i.e. data which are generated and/or modified during runtime, the layer which holds these data is the so-called container layer

## Docker file 
A docker file is a text file, which contains all instructions needed to build a certain docker image. It can be seen as the makefile for a docker image.

![Relation-file-image-container](../docs/img/Relation-file-image-container.png)