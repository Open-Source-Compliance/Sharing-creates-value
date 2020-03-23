## Best practices for license compliant containers

The following collection of "Dos" and "Don'ts" shall help to achieve license complaint containers, which is currently a major challenge, since the compliance process lacks behind technology.

Like for the "traditional" development the compliance process for containers shall be fully integrated in the process of creating container layers or images. It is key to have persons in charge of compliance integrated in the process of creating the artifacts. This will save time and effort, compared to the situation when a build image or layer is transferred to the OSPO for license compliance analysis and work.

## Guiding Principles

* Always publish only the minimal required artifacts. This can be in the easiest case the docker file, if this is not possible check whether it is enough to publish only a layer (containing your application). Publishing complete container images shall only be considered if the other options will not work.
* All the resulting compliance work, its effort and time needed has its origin in the docker file. Get involved in the creation process of the docker file right from the beginning
* Select carefully the docker repos you are using

## Docker File

### Dos for the docker file
* Make the docker file REUSE conformant (i.e. provide the license information for the docker file as well as a copyright string)
* Use pinning by taking advantage of the sha256 hash and digest e.g. FROM abc:2.1.0@sha256:06ebd9b1879057e24c1e87db508ba9fd0dd7f766bbf55665652d3148737793
* Always "install" the minimal required set of packages, bear in mind that everything which will be published has to undergo the license compliance process
* If you use multi stage builds make sure, that you:
** Copy any build sources or artifacts from the build container to a host machine (for later inventorying).
** Copy build artifacts into the release container.
** Record build information in the release container. Use LABELs to help with this.
* Use the package manager to install dependencies when possible. Avoid wget or curl to copy in dependencies.

### Don'ts for the docker file
* Avoid squashing layers
* Avoid "upgrade all" type commands and instead pin dependency package versions. If you can't pin the version, at a minimum you should list the packages you want to install. This makes your container easier to reproducible in the future.

## Docker Layer
Some of best practices for docker layers have to be implemented in the docker file, which is the "make file" for docker layers and images.
    
### Dos for the docker layer
* For every layer you publish make sure that it contains the "OSS disclosure document" and make sure that it can be accessed easily
* For every layer you publish make sure that it contains either the source code packages of the contained binaries or provide a "source code layer" along with the "binary layer" (containing only the binaries and the OSS disclosure document)

## Docker image
### Dos for the docker image
* After creating the binary docker image analyze it using tern and check whether it exactly contains the packages you have analyzed in order to proof that the disclose document is consistent with the image.
* Do the same check with the source code docker image


