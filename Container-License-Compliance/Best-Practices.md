## Best practices for container handling

The following collection of "Dos" and "Don'ts" shall help to ease the handling of containers in two dimensions - security and license compliance, the latter is currently a major challenge, since the compliance process lacks behind technology.

Like for the "traditional" development the compliance process for containers shall be fully integrated in the process of creating container layers or images. It is key to have persons in charge of compliance integrated in the process of creating the artifacts. This will save time and effort, compared to the situation when a build image or layer is transferred to the OSPO for license compliance analysis and work.

## Guiding Principles

* Always publish only the minimal required artifacts. This can be in the easiest case the docker file, if this is not possible check whether it is enough to publish only a layer (containing your application). Publishing complete container images shall only be considered if the other options will not work.
* All the resulting compliance work, its effort and time needed has its origin in the docker file. Get involved in the creation process of the docker file right from the beginning
* Select carefully the docker repos you are using

## Docker File

### Dos for the docker file
* Make the docker file REUSE conformant (i.e. provide the license information for the docker file as well as a copyright string)
* Use pinning by taking advantage of the sha256 hash and digest e.g. FROM abc:2.1.0@sha256:06ebd9b1879057e24c1e87db508ba9fd0dd7f766bbf55665652d3148737793
* Always "install" the minimal required set of packages, bear in mind that everything which will be published has to undergo the license compliance as well as the security process
* Make sure that they fetch specified versions of software securely from trusted sources, and that you have mechanisms in place to update them as needed if for example it becomes necessary to use new versions of packages due to security errors.
* If you use multi stage builds make sure, that you:
	* Copy any build sources or artifacts from the build container to a host machine (for later inventorying).
	* Copy build artifacts into the release container.
	* Record build information in the release container. Use LABELs to help with this.
* Use the package manager to install dependencies when possible. Avoid wget or curl to copy in dependencies.Where you cannot do this, you should pull from a trusted source, e.g., an internal build that already has approval. That pull should be via https:// or similar mechanisms and if appropriate also check signatures.
* Handle your Dockerfile as a created/modified components, along with any software that your Dockerfile copies or installs into your layers (as an unmodified component), in your component catalouge

### Don'ts for the docker file
* Avoid squashing layers. Containers are comprised of multiple layers which can be squashed or combined into a new, single layer. You should never squash layers that are not created by you. For example, you should not squash (combine) an upstream base layer OS and any other layers as you would then be distributing the base layer. When the image is published, your new layer will contain the repackaged OS base layer. Not only is this inefficient as users will not get the benefit of caching the base layer, but there may be significant legal risks
* Avoid "upgrade all" type commands and instead pin dependency package versions. If you can't pin the version, at a minimum you should list the packages you want to install. This makes your container easier to reproducible in the future.

## Docker Layer
Some of best practices for docker layers have to be implemented in the docker file, which is the "make file" for docker layers and images.
    
### Dos for the docker layer
* For every layer you publish make sure that it contains the "OSS disclosure document" and make sure that it can be accessed easily
* For every layer you publish make sure that it contains either the source code packages of the contained binaries or provide a "source code layer" along with the "binary layer" (containing only the binaries and the OSS disclosure document)
* For every layer you publish make sure that you have an appropriate security approval in place for each package or component that is present within your layers as well as your own code. You will need to have a process whereby you update your layers whenever there is a security need, and to track the packages within your layers for security problems.

## Docker image

### Dos for the docker image
* After creating the binary docker image analyze it using tern and check whether it exactly contains the packages you have analyzed in order to proof that the disclose document is consistent with the image.
* Do the same check with the source code docker image

### Don'ts for the docker image
In general it is strongly recommended to not attempt to build or [deliver for full container tarfile images](#guiding-principles). There are multiple reasons for this:

* Many popular distributions of Linux (such as Centos or Ubuntu) do not allow you to use their trademarks with a modified image. Thus to produce a full image it is necessary to strip the marks out of the software, rebuild and QA everything.
* You will need to ensure all the binaries you have are trustworthy, and that usually means building them all within your organization, as well as being able to do all the security updates.
* You will need all the packages you ship to be on the security checked.
* You will need to fulfill all software licence obligations for everything in the tarball.There are certain special cases where it may be possible or feasible; for example if your image is a base (scratch) image and contains nothing but some kind of tool, base system libraries and perhaps BusyBox.
* You must list everything contained in the distribution (all layers), and all of it will need to be security checked.



