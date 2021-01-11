# Tooling Landscape

## Introduction
This directory is the main directory for all information about our work on an highly automated end to end OSS compliance toolchain consisting of OSS tools.  

## Overview
The use of OSS in products, services and other offerings is increasing exponentially while release cycles of products and services become shorter and shorter. To cope with this while in the same time keeping costs under control automation of the compliance toolchain is key.

When we talk about software product developement and CI/CD toolchains to support it, we need to also consider other tools necessary for product developement. It must be mandatory to prevent any slow down of the integrated product release processes. Up to now in many companies these, so called supporting, processes are often not integrated in the CI/CD toolchain and sometimes are not as automated as they might be. This especially applies to the OSS compliance process.

In other words the OSS compliance process needs to be as automated as possible and the used tools for OSS compliance need to be fully integrated in the develpment CI/CD toolchain. This requires that the different tools need to provide suited APIs to be plugged in easily into the different developement toolchains. Moreover more and more publicly available services and data sources dealing with OSS compliance matters, these need also be considered and integrated in this workflow.

To have an integrated OSS compliance process means not only the process to produce the compliance  artifacts for outbound products, also contributions back to the OSS ecosystem have to be integrated to ensure that contributions can be fedback in a timely manner.

### Integrated or diverse?
To build an integrated end to end compliance toolchain is not about to build a monolithic monster, it is about using current available Open Source tools as well as defining and implementing the needed APIs/Data structures they need to provide, in order to plug them into the current set up CI/CD workflow and to enable them to trigger other Open Source compliance tools in a way that they seamlessly interact which each other and potential external data sources.

Building a monolithic monster will not work either. Neither for the project that aims to build it, nor for most of the entities that have a demand in tooling. This is proven by many other projects which had this objective no matter whether they were OSS or commercial ones. That's why we decided to follow a "Unix" like aproach - there is one tool - or service - for each required functionality. Knowing this speciality, it is possible to combine different functionalities to form the desired compliance pipeline. This not only supports a best of breed approach, it also fosters adoption as you will be able to start wherever the need urges most.

## Capabilities
To support mastery of this challenge, the need for a comprehensive view of all required capabilities becomes clear. To learn about the different capabilities we developed the OSC Capability Model. It outlines the different competencies requires to serve an Open Chain compliant process. Take it as orientation to develop your path along the tooling landscape or derive your path to Open Source Compliance (OSC).
