
## Identified Parts of the Toolchain

![abstract-toolchain](../img/OSS-Compliance-Toolchain-Big-Picture.jfif)


In the big picture the main functional building blocks are listed that will be required to integrate and automate an end to end compliance toolchain. These blocks do not represent concrete OSS tools, but depict logical functionalities that are required. However, concrete OSS tools and initiatives can be integrated into the landscape to. This is exactly what this project aims to achieve.
Please note that the picture above does not list all the company external available data sources. The purpose of the big picture is to provide an easy to understand overview what this entire project is all about. 

## Instances

There are different OSS tools available which implement one or more functional building blocks identified as elements of the abstract toolchain. The picture below is  an example were concrete and existing tools are mapped to the corresponding building block. Note that there can also be other OSS tools mapped to a corresponding building block, which in the end results then in a different instance of such a compliance toolchain.

![instance-toolchain](../../img/toolchain-Instance-diag.jpg)

## Company External

## Public Compliance Artifact Repos
Sytems or serives that provide compliance related data and information. These data may be specific for a certain software component release or specific to a OSS compliant license, like the interpretation of certain licenses.As well as any other data needed in an license compliance process.

Public compliance artifact repos which targert OSS compliant licenses and their obligations, permissions, restrictions and risks are the  [OSADL License Checklists](https://www.osadl.org/fileadmin/checklists/unreflicenses/GPL-2.0-only.txt) or [Finos](https://github.com/finos-osr/OSLC-handbook).

The SPDX license list is also regraded as public compliance artifact repo, which provides standardized names for certain licenses please see the [SPDX License List](https://spdx.org/licenses/)

ClearlyDefined is an open source project which has the mission to help FOSS projects thrive by being, well, clearly defined. ClearlyDefined will pursue any data that makes FOSS projects easier to consume and thus more successful. Initially this work focuses on licensing data that form the core of understanding and meeting the legal obligations related to using FOSS. This includes:

+ License (declared and observed)
+ Copyright holders
+ Source location (including revision/commit)

For more details see [ClearlyDefined](https://clearlydefined.io/)

Software Heritage can also regraded as public artifact repo, although compliance information is not in the central focus, Software Heritage provides information of software which was/is available on the Internet, please see the [Software Heritage](https://www.softwareheritage.org)


## Company Internal

## Artifact Repository
A system or service providing (binary) software artifacts and metadata stored in a defined directory structure which is used to retrieve artifacts during a build process. This is used as a cache for the external Artifact Repository to ensure the availability of all components used within the company, it is also the storage for the build software artifacts of the company, used in the Continuous Integration Infrastructure to store the build results.
Example: [Archiva](https://archiva.apache.org/index.cgi)

## Binary Analyzer
A system or service that analyses binary files, like executables or libraries. Its main purpose is to identify the contents of binary files and making this information available for further analysis, such as license compliance, security research or composition analysis. 

Example: [Binary Analysis Next Generation](https://github.com/armijnhemel/binaryanalysis-ng)

## Build Tools
A system that builds a software project and creates the binaries and executables for the software. During this process, the build technology has a technology dependent way to identify and provide dependencies needed to build and run the software. This information is one data source for the compliance check on the project.

## Compliance Artifact Consistency
A system or service that takes the following elements:

+ the concrete deliverable of a software product or service 
+ the OSS disclosure document
+ the source code bundle to be delivered

The compliance artifact consistency checks whether these three artifacts are consistent and *complete*. I.e. whether all found OSS ingredients of the deliverable are listed in the disclosure document with the correct version and whether the source code bundle includes at least the component versions were copy left licenses apply. It is a kind of quality assurance functionality at the end of the OSS compliance process.

## Component Analysis Service
Dedicated tools and services which scan the source code concerning integrated 3rd party code snippets and aim to provide license information about the origin and applicable license of the  source code snippets. These kind of tools or services are often called **scanner for plagiarism**.

Example: [ScanOSS](https://www.scanoss.com/)

## Component Inventory (Metadata Repository)
A system or service that stores metadata about used software components. This includes meta data like ids of the components in other systems, licenses, copyrights, known vulnerabilities and information, that is needed to do export classifications (ECCN), such as information about the contained cryptographic functionality. The Component Metadata Repository can be linked to an external FOSS Metadata Database to retrieve commonly known information and make it usable within the organization. Also Security Vulnerability Database and other sources for e.g. export classification-relevant data, can be linked to retrieve the necessary information and to make it available within the company.
Example: [Eclipse SW360](https://projects.eclipse.org/projects/technology.sw360)

## Container Content Resolver
A system or service that analyses a given software container to determine the packages and their metadata installed in the container image. Thus the container content resolver provides the bill of material of a container image. 

Example: [Tern](https://github.com/vmware/tern)

## Continuous Integration/Deployment Infrastructure (CI/CD)
Systems or services that orchestrate the build and deployment process for a software project and executes work flows triggered by different kind of events. The CI/CD infrastructure typically runs software builds and executes further build steps like testing and the compliance checks

## FOSS Compliance Bundle Generator
A tool that creates all the necessary documentation needed for the distribution of a software e.g. a so called FOSS disclosure document consisting of:

+ required legal notices
+ optional: a written offer to provide the complete corresponding source code with data whom to  contact
+ list of all integrated components with all:

	+ copyright notices
	+ acknowledgments
	+ applicable licenses

Another output the FOSS compliance bundle generator produces is the source code bundle consisting of the source code of the integrated FOSS packages. As well as the description of the build environment.

Note that different delivery models of a product may require different FOSS compliance bundles.

Example: [Eclipse SW360antenna](https://projects.eclipse.org/proposals/sw360antenna)

## Dependency Resolver
A tool that determines the dependencies of software projects. Tt its technology and package manager specific how dependencies are expressed - thus there need to be dedicated functionality of the different package managers in use. The dependency resolver ensures the all dependencies are resolved recursively. To ensure that the output is a technology and package manager neutral complete list of dependencies.

Example: [ORT Analyzer](https://github.com/heremaps/oss-review-toolkit#analyzer)

## License & Copyright Scanner
A tool that analyses source code to identify license and copyright information. usually these tools need to provide a UI in order to be able to review the tool findings and if necessary to correct the tool findings.

Example of a license and copyright scanner, which provides review and correction capabilities : [Fossology](https://www.fossology.org/)

A list of License & copyright scanners is available at [LicenseScannerComparison](https://github.com/maxhbr/LicenseScannerComparison)


## License Obligations Database
System or service which provides for licenses its legal analysis. Usually the licenses analysis results in the more easy to understand:

+ obligations
+ restrictions
+ permissions
+ risks

An obligation is for example that the text of the license has to be provided together with the software. A restriction is for example that one is not allowed to impose further restrictions on the recipients exercise of the rights granted in the license.

Examples for a data base storing and using such data: [Eclipse SW360](https://projects.eclipse.org/proposals/sw360) or [Fossology](https://www.fossology.org/)
<br>Examples for the content are listed in [Company External](#public-compliance-artifact-repos)


## Obligation Fulfillment
A system or service where all the obligations resulting from the integrated OSS components are aggregated. How theses obligations are fulfilled for da certain deliverable is documented and made available to provide an audit trail that a certain deliverable is made available in a license compliant way. 

Example: [Eclipse SW360](https://projects.eclipse.org/projects/technology.sw360)

## Policy checker (Compliance Checker)
System or service which takes at least the concrete deliverable of a software product or service, the licenses of the the integrated OSS components and checks whether the concrete deliverable is in-line with the company policy for the specific product category and the deliverable. 

Example: [Eclipse SW360antenna](https://projects.eclipse.org/proposals/sw360antenna)

E.g. Not all licenses may be allowed for a certain product or service category or certain licenses may not be allowed for a certain deliverable, etc.

## Product Metadata Repository
Software products and most software components are built from other software components. The Product Metadata Repository contains this relationship information to enable the management of dependencies over the life cycle of the software.

Example: [Eclipse SW360](https://projects.eclipse.org/proposals/sw360)

## Source Code Repo
Systems or services that provide source code. This is typically (also) a version control system. For the compliance tooling, typically the source code is needed as a folder on a file share, i.e., the source code is already checked out by, e.g., the Continuous Integration infrastructure. 

## Source package Downloader
System or service which downloads all the source packages from external data source if they are not yet known and available inside the organization. The source package downloader transfers the downloaded packages to the component inventory.

Example: [ORT Downloader](https://github.com/heremaps/oss-review-toolkit#downloader)
