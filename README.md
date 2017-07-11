# while(sharing()){value++;}
## Sharing-creates-value
This repo realizes the idea that OSS compliance activities will be less expensive by applying OSS principles
## Introduction
Free and Open Source Software development has a long and successful history. Its success is based on transperancy, sharing, collaboration and appreciation. OSS and its developement model outperform traditional software development models. Althoug OSS is _the_ success story of the last 30 years, it is not yet there where it could be. One of the main reasons is the perception that OSS license compliance is a tedious, time consuming and high effort task. another main reason is the misperception that using OSS requires you to "open" your code to the world.
## Objective
Sharing creates value targets the first perception and strive for the goal to lower the required effort for all who want to make use of OSS in a license compliant way. 

To achieve this we will develop, share and improve the artifacts commonly used to fulfill the requirements of the different Free and Open Source Software licenses by applying the Open Source Software development principles. This may turn Open Source license compliance into a straight forward task. 

Another objective of Sharing creates value is a very close collaboration with the OSS community in order to fix detected "bugs" in licensing as well as introducing the information needed for license compliance activities in the Open Source projects, i.e. provide our analysis work to the OSS projects.


Last but not least we support tools which will help you to automate and reduce you effort in component management, license identification, OSS license compliance activities.
## Our areas of work 
* Best practises in the area of OSS license compliance
* OSS package analysis files
* OSS disclosure documents
* Licenses found in the internet, in order to improve the efficiecy of recognizing licenses of a tool as well as having a collection of license texts available (it is not meant to be a competition to the SPDX license list)
* License analysis (rights, restrictions, obligations)
* Descriptions of OSS license compliance processes
* any other material which eases the OSS license compliance activities

We want to be the platform, which provides all information and artifacts for OSS license compliance. We think that there are a lot good things already available and we want to serve as a place where this information can be shared. Everybody is invited to contribute whatever he/she wants to contribute, for more details please see the FAQs.

## What is the difference to other OSS license compliance activities
There exist already some projects / activities which deal with OSS license compliance like
* [OpenChain] (https://wiki.linuxfoundation.org/openchain/start) 
* [Open Compliance Program] (https://compliance.linuxfoundation.org/)
* [Copyleft.org] (https://copyleft.org/)

The main difference is that this is an effort for everybody providing real know how how things in the area of OSS compliance can be done.
OpenChain is currently more focusing on training and assessment, but the topic "how do I xyz to be license compliant" is not touched at all. As far as I know the answer to the question is a "legal interpretation of a certain screnario" and OpenChain does not want to do legal interpretations. The same applies for the Open Compliance Program of the Linux Foundation. Copyleft.org provides practical tipps but it does not provide any license information and copyright notices of OSS packages, and this is a major objective of this project to provide such kind of information - ready to use for everybody under a very relaxed license. Thus making OSS compliance for everybody a low effort and easy task.

## OSS package analysis file
One of the tasks in OSS compliance work is the analysis of OSS packages in order to identify the licenses and copyright holders. Although tools are available which support the analysis, it is still the task which causes effort.
We believe that is does not make any sense that everyone doing checks of packages again and again. This is redundant effort in our opinion which could be much better invested in OSS development. In other words: we think increasing the code base is much better instead of spending effort for license compliance checks which are done thousand fold today in many different organizations.

## Process we follow in order to create a OSS package analysis file
We create such OSS package analysis files and make them available for download under the terms of the Creative Commons Public Domain Dedication [CC0 1.0]  (https://creativecommons.org/publicdomain/zero/1.0/). We know that the content we produce is somehow delicate. Due to this it is important to disclose how we create such content. Since we represent an Open Source project everything is transparent. The following points describe the procedure we follow in creating the "OSS package analysis file" as we call it. 

The OSS package analysis file are generated following the process described below:

* Obtain the component in source code form
	* download the component from the official web site / check the hashes
	* the component is provided by a third party
* Issue a license and copyright analysis with the GPL-2.0 licensed tool FOSSology. FOSSology searches in files for the following information:
	* License relevant text phrases
	* Copyright strings
	* Keywords for ECC (Export, Control and Customs)
* A licensing expert person will review and analyze the FOSSology result. The expert person is not necessarily a lawyer, but has several years of experience in license compliance activities.
* Result is reviewed by a person who has more experience in license compliance activities than the author.
* The final result is made available in form of a Debian copyright file or a SPDX document or another "machine & human friendly" format.
* For the analysis of the OSS packages we currently use [FOSSology version 3.0] (http://www.fossology.org/projects/fossology)
* Our work instance can be found [here] (http://54.69.38.215/repo/) 

## Quality assurance process we follow when we recieve OSS package analysis files as a contribution

Here we distinguish two cases:
### Initial contribution
This means a complete package analysis file is contributed of a package which is not contained here already.
* We inspect the package with FOSSology and do a plausibility test of the content of the document based on the FOSSology information.
* We will make the information available what we compared during the plausibility check

### Update / bug fix 
In this case we will verify the bug fix; i.e. check the information of the file of the package whether the bug report / fix is correct
