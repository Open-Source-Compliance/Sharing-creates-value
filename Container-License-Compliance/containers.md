# Containers

## Definitions and Terms

Discussions around containers contains many terms, some of which can mean more than one thing depending on their context. In particular the terms 'image' and 'layer' are often interchangeable, but also sometimes mean specifically different things. This document tries to avoid any confusion by defining and using the following terms:

Base (scratch) Image
: A base Image is composed of only a single layer, with either no parent 'FROM' or the 'scratch' layer to overlay upon

Base Layer
: In a non 'Multi-stage' Dockerfile, the base layer ('FROM') that the Dockerfile builds upon

Container
: An instantiation of an Image via a container orchestration stack or runtime such as Docker or Kubernetes

Dockerfile
: A text file that defines the steps needed to form the layers of an Image

Hub
: See 'Registry'

Image
: A set of directories or files composited from one or more Layers overlaid on top of each other. The definition of an Images layers is derived from its Dockerfile. To be differentiated from a 'tarball image' or 'pushing an image' to a Hub

Layer
: A definition of files to be overlayed onto another layer, except for the case of a 'BASE image', that has no parent Layer to overlay onto

Multi-stage
: Since Docker v17.05, Dockerfiles, and thus Images, can contain multiple 'FROM' lines, and thus be derived from multiple Base Layers

Parent Image
: An image's parent image is the image designated in the FROM directive in the image's Dockerfile. All subsequent commands are applied to this parent image. A Dockerfile with no FROM directive has no parent image, and is called a base image.

Pushing an Image
: The act of 'pushing' an Image to a Registry. In reality, all the layers the Image is composed of are pushed to the Registry (for verification), and only new layers that do not already exist on the Registry are updated and stored there

Registry
: A server/service used to upload, store and retrieve container Images. In reality, a registry works with and stores Layers

Tarball (Image)
: A single tar file comprising of all the layers that make up an Image. Generated with a 'docker save'

Tarball (container)
: A single tar file comprising of all the layers that make up a 'Container', squashed into a single Layer. Generated with a 'docker export'

## More information

There are usually three types of container-related deliveries.

### Dockerfiles

Dockerfiles are text files that describe how to build container images. They do not themselves contain any other software but instruct the building tooling to fetch software and/or manipulate the existing configuration to produce an image.

The following example Dockerfile would produce a Clear Linux based Linux image with the git tool installed:

FROM clearlinux:base
RUN swupd update && swupd bundle-add git

### Container Image (layers)

The container image layers composited from a Dockerfile. The image is composed of one or more layers, and of particular interest is what layers you have added, and which, if any, layers (images) you have based your Image upon (the FROMs in your Dockerfile).

### Container tarfile Images

These are generated from a docker 'export' or 'save'. A full disk image of a container including all the components (layers).  Not to be confused with the executable container images produced locally by the tooling for local container execution.


## Things to be taken care of, in order to get approval to deliver

There are usually three types of container-related deliveries.

### Dockerfiles

You will need to ensure that your Dockerfile scripts are security reviewed, that they fetch specified versions of software securely from trusted sources, and that you have mechanisms in place to update them as needed if for example it becomes necessary to use new versions of packages due to security errors.

As far as possible you should pull packages from the base distribution itself using the distribution installation tools (e.g., apt, dnf, yum or swupd etc.). Where you cannot do this, you should pull from a trusted source, e.g., an internal build that already has approval. That pull should be via https:// or similar mechanisms and if appropriate also check signatures.

In your approval request, you must list your Dockerfile as a created/modified components, along with any software that your Dockerfile copies or installs into your layers (as an unmodified component).

Ensure that your Dockerfile has a license.

### Container Images (layers) pushed to a registry

To get approval for layers (that is, all layers you have generated from your Dockerfile on top of your base/FROM layer), you must have an appropriate security approval in place for each package or component that is present within your layers as well as your own code. You will need to have a process whereby you update your layers whenever there is a security need, and to track the packages within your layers for security problems.

You will also need to follow any source code or credit requirements in the packages that are within your layers. You must list your Dockerfile, along with any software that your Dockerfile copies or installs into your layers. You will need to explain how you are fulfilling any source code distribution requirements. 

Ensure that your Dockerfile has a license.

### Docker tarfile Images

In general it is strongly recommended to not attempt to build or deliver for full container tarfile images. There are multiple reasons for this:

Many popular distributions of Linux (such as Centos or Ubuntu) do not allow you to use their trademarks with a modified image. Thus to produce a full image it is necessary to strip the marks out of the software, rebuild and QA everything.
You will need to ensure all the binaries you have are trustworthy, and that usually means building them all within your organization, as well as being able to do all the security updates.
You will need all the packages you ship to be on the security whitelist, or if internally developed to have the security process approval.
You will need to fulfill all software licence obligations for everything in the tarball.
There are certain special cases where it may be possible or feasible; for example if your image is a base (scratch) image and contains nothing but some kind of tool, base system libraries and perhaps BusyBox.

You must list everything contained in the distribution (all layers), and all of it will need to have obtained a security approval.

If you do have a business need to ship an image with a full Linux distribution please contact your OSPO first.


## Squashing Images

Containers are comprised of multiple layers which can be squashed or combined into a new, single layer. You should never squash layers that are not created by you. For example, you should not squash (combine) an upstream base layer OS and any other layers as you would then be distributing the base layer. When the image is published, your new layer will contain the repackaged OS base layer. Not only is this inefficient as users will not get the benefit of caching the base layer, but there may be significant legal risks.

