# Existing OSS licensed OSS license compliance tools
## Credits

The overview of the tools is a derived work from [doubleOpen's Overview](https://github.com/doubleopen-project/doubleopen-publications) . DoubleOpen's Overview is copyrighted by [doubleOpen](https://www.doubleopen.org/) and available under the terms of [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). The doubleOpen overview and this list will be syncronized. If you miss any OSS based compliance tool please add it either at the [doubleOpen repo](https://github.com/doubleopen-project/doubleopen-publications) or in [our Github repo](https://github.com/Open-Source-Compliance/Sharing-creates-value/tree/master/docs/Tooling-Landscape). Help us to improve and to complete the information about the current existing OSS tools available for license compliance.



## Introduction

Open source software has eaten the world, but organizations are still struggling with effective compliance. Open source software is heterogenous and re-used, which, while positive for software development, creates a challenge for compliance. Compliance requires multiple tools and these should be ideally combined into a workflow that supports a number of business and developer requirements. One of the requirements is ease of use in a modern development environment where code development cycles are getting ever shorter and new development results are pushed to operations ever faster. For this to work, open source compliance tools likely need to integrate with development tooling.

In the following report some of these tools are listed with information of their main license, website and a summary of their features, based on accounts by the projects. The report has been crafted to map out the wide range of open source tools that one might use to help keep their open source software compliant. However, this report, ever so comprehensive, is not exhaustive. The report includes FOSS tools as well as a few commercial tools. It also has a section for Open Source Initiatives and Development Environments, as these are  also important on a way towards automated open compliance with open tooling and open data. 

This report will be complemented based on an ecosystem survey and on practical testing of the most popular open source tools.

This report is part of the first work package in the Double Open project. See [doubleopen.org](https://doubleopen.org) for more details.


## AboutCode Toolkit
**Website:**
[AboutCode](https://www.aboutcode.org/ )<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
The AboutCode Toolkit and ABOUT files provide a simple way to document the origin, license, usage and other important or interesting information about third-party software components that you use in your project. In addition, this tool is able to generate attribution notices and identify redistributable source code used in your project.


## AboutCode Manager
**Website:**
[AboutCode](https://www.aboutcode.org/ )<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
AboutCode Manager provides an advanced visual UI to help you quickly evaluate license and other notices identified by ScanCode and record your conclusion about the effective license(s) for a component. 

AboutCode Manager is based on Electron and is the primary desktop/GUI tool for using nexB’s AboutCode tools.


## Apache Rat
**Website:** [Apache Rat](http://creadur.apache.org/rat/) <br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
Apache Rat is a release audit tool, focused on licenses. Coded in Java, it runs from the command line with plugins for Maven and Ant. Rat is extensible. It is part of the Apache Creadur project.


## Apache Tentacles
**Website:**
[Apache Tentacles](http://creadur.apache.org/tentacles/)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
Apache Tentacles helps the reviewer by automating interactions with the repository containing the artifacts comprising the release. Apache Tentacles simplifies the job of reviewing repository releases consisting of large numbers of artifacts. Coded in Java, it runs from the command line.


## Apache Whisker
**Website:**
[Apache Whisker](http://creadur.apache.org/whisker/)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
Apache Whisker assists assembled applications maintain correct legal documentation.
Whisker can 

* verify - checking meta-data quality against a distribution
* generate - legal documents from meta-data

Particular useful for complex assembled applications.


## Bang
**Website:**		[Bang](https://github.com/armijnhemel/binaryanalysis-ng)<br>
**Main License:** 	[AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.txt)<br>
**Summary:** <br>
Binary Analysis Next Generation, or BANG, is a tool for analyzing binary files. Currently its main goal is to very quickly find out the contents of binary files, such as firmware updates, and making information extracted from the contents available for further analysis, such as license compliance, security research or composition analysis. It has support for around 130 different file formats, which can be detected, unpacked and labeled.


## Barista
**Website:**        [Barista  Open Source License and Vulnerability Management Tool](https://optum.github.io/barista/)<br>
**Main License:**   [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
_Developer Focused_<br>
Barista is fundamentally a scanning tool to detect open source components, licenses and potential vulnerabilities. Automatically create and maintain an open source bill of materials including multi-level dependencies.

_Customize Business Rules_<br>
Barista admins determine which obligation(s) are associated with each license detected, and assign project approval status based on deployment model, applicable license(s), and documented vulnerabilities for detected dependencies.

_Cloud Native Architecture_<br>
Barista is designed for cloud native deployment environments allowing hosting flexibility and scalability on demand.

## Bubbly
**Website:**        [Bubbly](https://github.com/valocode/bubbly/)<br>
**Main License:**   [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/)<br>
**Summary:**<br>
Bubbly is a release readiness platform helping software teams release compliant software with confidence. Gain visibility into your release process with reports and analytics to lower risk, increase quality, reduce cycle time and drive continuous improvement.

## CLA Assistant
**Website:**        [CLA Assistant](https://github.com/cla-assistant/cla-assistant)<br>
**Main License:**   [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
CLA Assistant helps to handle the legal side of contributions to a repository by enabling contributors to sign Contributor License Agreements (CLAs) from within a pull request. The CLA can be stored as a GitHub Gist file and then linked with the repository/organisation in CLA Assistant. Repository owners can review a list of users who signed the CLA for each version of it.  

## Cregit
**Website:**
[Cregit](https://github.com/cregit/cregit)<br>
**Main License:**
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)<br>
**Summary:**<br>
Cregit identifies the contributors of source code. The cregit version of a source file has two interactive features:

* Mouse-over: you will get a summary of the information of the commit that added this token. This information is:

    * Its commit id
    * Its git-author (the value of the Author field of the commit)
    * Its git-author-date (the value of the field Author Date of the commit)
    * Summary log of the commit
	
* Left-click on a token will open a new window with the details of the commit (in github). You can keep this window open and it will keep reloading the files.


## Deltacode
**Website:**
[AboutCode](https://www.aboutcode.org/ )<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
DeltaCode allows you to easily compare ScanCode scans for two versions of a package, component, codebase or product in order to quickly identify possible changes with a focus on identifying license changes. DeltaCode reports matching files with a score and a list of factors that contribute to that score. 

You can use DeltaCode with ScanCode to identify and track license and related changes in open source or third party software packages or components from release to release. 


## Eclipse SW360
**Website:**
[Eclipse SW360](https://projects.eclipse.org/projects/technology.sw360)<br>
**Main License:**
[EPL-1.0](https://www.eclipse.org/org/documents/epl-v10.php)<br>
**Summary:**<br>
A software catalogue application designed to provide a central place for sharing information about software components used by an organization. It is designed to neatly integrate into existing infrastructures related to the management of software artifacts and projects by providing separate backend services for distinct tasks and a set of portlets to access these services. It has connectors to interact with external systems such as code scan tools. Thus far the project has not provided download information.


## Eclipse SW360antenna
**Website:**
[Eclipse SW360](https://projects.eclipse.org/projects/technology.sw360.antenna)<br>
**Main License:**
[EPL-2.0](https://www.eclipse.org/legal/epl-2.0/)<br>
**Summary:**<br>
Eclipse SW360antenna is a tool to automate your open source license compliance processes as much as possible. In the end that is

* collecting all compliance relevant data,
* process that data and warn if there might be any license compliance related issues, and
* generating a set of compliance artifacts (source code bundle, disclosure document, report)

for your project.

## Flict
**Website:**[Flict](https://github.com/vinland-technology/flict)<br>
**Main License:**
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)<br>
**Summary:**<br>
FOSS License Compatibility Tool (flict) is a Free and Open Source Software tool to verify license compatibility for a package and its dependencies. You can use the tool to automate license compatibility verification in your compliance work flow.

flict can:
* verify licenses compatibilty for license expression and a packages and its dependencies
* suggest candidate outbound licenses
* simplify license expressions
* display, in misc format, compatibilies between licenses
* check outbound licenses against a policy (policy as supplied by the user)

## Fossology
**Website:**[Fossology](https://www.fossology.org/ )<br>
**Main License:**
[GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)<br>
**Summary:**<br>
Fossology is a scanning tool for license, copyright and export control scans. In one click you can generate an SPDX file, or a ReadMe with all the copyrights notices from your software. It provides a Web UI and a database for a compliance workflow. To scan, a package must be uploaded to the server. Scanners provided are Monk, Nomos and Ninka. It has version control on packages scanned, so when scanning a newer version of a previous package, only changed files are rescanned.


## FOSSLight
**Website:**[FOSSLight](https://fosslight.org/)<br>
**Main License:**
[AGPL-30 and others](https://www.gnu.org/licenses/agpl-3.0.en.html)<br>
**Summary:**<br>
FOSSLight is an integrated system that can efficiently process the open source compliance process. It provides:
* Compliance Workflow: It can process the open source compliance workflow.
* Compliance Hub: You can manage everything about open source compliance such as license, oss, vulnerability and others.
* Scalability´: It can be used with additional features (including FOSSLight scanner or other plugins).

## LDBCollector
**Website:**
[LDBcollector](https://github.com/maxhbr/LDBcollector)<br>
**Main License:**
[BSD-3-Clause](https://github.com/maxhbr/LDBcollector/blob/master/LICENSE)<br>
**Summary:**<br>
A small application which collects oss-license metadata and combines it.

## License Compatibility Checker
**Website:**
[license-compatibility-checker](https://github.com/HansHammel/license-compatibility-checker#readme)<br>
**Main License:**
[MIT](https://opensource.org/licenses/MIT)<br>
**Summary:**<br>
Check npm dependencies' package.json for license compatibility based on SPDX standards. Claimed to be a work in progress, but gives a simple comparison of the licenses in the package with an explanation to how permissive the license is (Permissive > Weakly Protective > Strongly Protective > Network Protective). Shows potential incompatibilities with a colorful scheme.


## Licensee.js
**Website:**
[Licensee.js](https://github.com/jslicense/licensee.js)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
Licensee.js is a command line utility to check npm package dependency license metadata against rules. It uses SPDX license expression and whitelisted data to capture packages that are under different license than whitelisted.


## Ninka
**Website:**
[Ninka](http://ninka.turingmachine.org/)<br>
**Main License:**
[GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)<br>
**Summary:**<br>
Ninka is a lightweight license identification tool for source code. It is sentence-based, and provides a simple way to identify open source licenses in a source code file. It is capable of identifying several dozen different licenses (and their variations).

## Opossum Tool
**Website:**
[Oposssum Tool](https://github.com/opossum-tool)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
A light-weight app to audit and inventory large codebases for open source license compliance.<br>
OpossumUI was developed with the goal to build a tool for managing and combining open source compliance data from different sources. While existing analysis tools for software compliance can provide good information, using multiple of such tools often leads to huge amounts of data due to an increased detection rate. Even though the results can be merged and noise can be filtered through automatic tools, final manual revisions are often necessary. So, OpossumUI was born: A light-weight app for review of compliance information for large codebases.
OpossumUI is a tool to:
* discover open source software used in applications.
* review licenses.
* generate reports from an open source code scan.


## OSS Attribution Builder
**Website:**
[OSS Attribution Builder](https://github.com/amzn/oss-attribution-builder)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**
OSS Attribution Builder is a website that helps teams create attribution documents for software products. 


## OSS Discovery by OpenLogic
**Website:**
[OSS Discovery](http://ossdiscovery.sourceforge.net/)<br>
**Main License:**
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)<br>
**Summary:**<br>
OSS Discovery finds the open source software embedded in applications and installed on computers. It is a scanning tool, which gives human readable and machine readable results.


## OSS Review Toolkit ORT
**Website:**
[ORT](https://github.com/heremaps/oss-review-toolkit)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
Verifies free and open source software license compliance by checking source code and dependencies. It works by analyzing the source code for dependencies, downloading the source code of the dependencies, scanning all source code for license information, and summarizing the results. The different tools that make up ORT are designed as libraries (for programmatic use) with a minimal command line interface (for scripted use). Currently the report formats are Excel sheet, NOTICE file, static HTML and Web App. 


## OSSPolice
**Website:**
[OSSPolice](https://github.com/osssanitizer/osspolice)<br>
**Main License:**
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)<br>
**Summary:**<br>
OSSPolice is a risk assessment service for developers that can quickly identify potential free software license violations and known n-day security vulnerabilities in their apps. 


## Quartermaster Project QMSTR
**Website:**
[QMSTR](https://qmstr.org/)<br>
**Main License:**
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)<br>
**Summary:**<br>
Quartermaster is a suite of command line tools and build system extensions that instruments software builds to create FOSS compliance documentation and support compliance decisions. Quartermaster runs adjacent to a software build process. A master process collects information about the software that is build. Once the build is complete, the master executes a number of analysis tools, and finally a number of reporters. All modules are executed in the context of the master, not the build machine. The master ships all dependencies of the modules without affecting the build clients file system (it runs in a container).


## ScanCode.io and ScanPipe
**Website:**
[ScanCode.io](https://scancodeio.readthedocs.io/en/latest/introduction.html#)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
ScanCode.io is a server to script and automate the process of Software Composition Analysis (SCA) to identify any open source components and their license compliance data in an application’s codebase. ScanCode.io can be used for various use cases, such as Docker container and VM composition analyses, among other applications.

ScanPipe is a developer-friendly framework and application that helps software analysts and engineers build and manage real-life software composition analysis projects as scripted pipelines.

ScanPipe provides a unified framework to the infrastructure that is required to execute and organize these software composition analysis projects.

## ScanCode Toolkit
**Website:**
[ScanCode](https://www.aboutcode.org/ )<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
ScanCode is a suite of command line utilities to reliably scan a codebase for license, copyright, package manifests and direct dependencies and other interesting origin and licensing information discovered in source and binary code files. ScanCode provides comprehensive scan results that you can save as JSON, HTML, CSV or SPDX. As a command line application returning JSON, ScanCode is easy to integrate in a code analysis pipeline and CI/CD.


## SCANOSS
**Website**: [scanoss.com](https://www.scanoss.com)<br>
**Main License**: [GPL-2.0-or-later](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
**Summary:**<br>
SCANOSS is the first free and open source SCA platform and open-data OSS knowledgebase. It performs SBOM generation in SPDX and CycloneDX and detects presence of Open Source at snippet, file and component levels. The central component is a RESTful API based on OpenAPI standards. Reference code is provided for different languages and integration with other tools.
With SCANOSS you can enable component, file and snippet matching into any tool. The Public Knowledgebase is called OSSKB and is available at osskb.org. Scanning can be performed securely and anonymously.


## SPDX Tools
**Website:**
[SPDX Tools](https://spdx.org/tools)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)<br>
**Summary:**<br>
The consolidated SPDX workgroup tool provides translation, comparison, and verification functionality in a single download. The tool is a Java command line utility.

The following functions are available:

* TagToSpreadsheet - Convert a tag format input file to a spreadsheet output file
* TagToRDF - Convert a tag format input file to an RDF format output file
* RdfToTag - Convert an RDF format input file to a tag format output file
* RdfToHtml - Convert an RDF format input file to an HTML web page output file
* RdfToSpreadsheet - Convert an RDF format input file to a spreadsheeet format output file
* SpreadsheetToRDF - Convert a spreadsheet input file to an RDF format output file
* SpreadsheetToTag - Convert a spreadsheet input file to a tag format output file
* SPDXViewer - Display an SPDX document input file (in either tag/value or RDF format)
* CompareMultipleSpdxDocs - Compare multiple SPDX documents (in either tag/value or RDF formats) and output to a spreadsheet
* CompareSpdxDocs - Compare two SPDX documents (in either tag/value or RDF format)
* GenerateVerificationCode - Geneinkrate a Verification Code from a directory of files.


## SPDX Maven Plugin
**Website:**
[SPDX Maven Plugin](https://github.com/spdx/spdx-maven-plugin)<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)<br>
**Summary:**<br>
SPDX Maven Plugin is a plugin to Maven which produces Software Package Data Exchange (SPDX) documents for artifacts described in the POM file. 


## TraceCode toolkit
**Website:**
[AboutCode](https://www.aboutcode.org/ )<br>
**Main License:**
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
TraceCode Toolkit helps you determine which components are actually distributed or deployed for your product. This is essential information for determining your open source license obligations because many are only triggered by distribution or deployment. 

TraceCode Toolkit is a tool to analyze the traced execution of a build, so you can learn which files are built into binaries and ultimately deployed in your distributed software.


## Tern
**Website:**
[Tern](https://github.com/vmware/tern)<br>
**Main License:**
[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)<br>
**Summary:**<br>
Tern is a software package inspection tool for containers written in Python. Tern is an inspection tool to find the metadata of the packages installed in a container image. It does this in two steps:

1. It uses overlayfs to mount the first filesystem layer in a container image
2. It then executes scripts from the "command library" in a chroot environment to collect information about packages installed in that layer
3. With that information as a base, it continues to iterate over step 1 and 2 for the rest of the layers in the container image
4. Once done, it generates a report in different formats. The default report is a verbose explanation of what layers brought in what software components. If a Dockerfile is provided then it will also provide what lines in the Dockerfile was used to create the layers.

 
## Vulnerability Assessment Tool
**Website:**        [Vulnerability Assessment Tool](https://github.com/SAP/vulnerability-assessment-tool)<br>
**Main License:**   [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)<br>
**Summary:**<br>
The open-source vulnerability assessment tool supports software development organizations in regards to the secure use of open-source components during application development. The tool analyzes Java and Python applications in order to detect whether they depend on open-source components with known vulnerabilities, collect evidence regarding the execution of vulnerable code in a given application context (through the combination of static and dynamic analysis techniques), and support developers in the mitigation of such dependencies. As such, it addresses the OWASP Top 10 security risk A9, Using Components with Known Vulnerabilities, which is often the root cause of data breaches.




