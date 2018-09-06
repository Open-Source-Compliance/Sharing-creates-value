# Glossary for the OSS Tooling Landscape

## Company External

### Source Code Repository
Systems or services that provide source code. This is typically a version control system. The compliance tooling obtains the source code of 3rd party dependencies, i.e., FOSS components from such repositories

### (Build) Artifact Repository
Systems or services that provides (binary) software artifacts and metadata stored in a defined directory structure which is used to retrieve artifacts during a build process. Software artifacts may be of type proprietary, commercial, FOSS. The Artifact repository may also be used to store the source code of FOSS components besides the binary artifact for usage within the compliance process, e.g., for starting a license scan or creating the source code bundle to be delivered with the product.

### Security Vulnerability Database
Systems or services that provide information about publicly known security vulnerabilities of software artefacts.

### License Obligations Database
Systems or services that provide Data about obligations and prohibitions of (FOSS) licenses.

### Public License Master Database
Publicly available information about Open Source licenses (e.g. commonly accepted license identifiers).

### FOSS Metadata Database
Systems or services that provide descriptive data of software artefacts (mainly FOSS). Data could be: the declared license for a component, the source location (e.g., Git commit) for a version, details to be included in attributions (e.g., copyright holders in a Notices file), etc.

## Company Internal

### Source Code Repository
Systems or services that provide source code. This is typically a version control system. For the compliance tooling, typically the source code is needed as a folder on a file share, i.e., the source code is already checked out by, e.g., the Continuous Integration infrastructure. 

### Continuous Integration Infrastructure
Systems or services that orchestrate the build process for a software project and executes workflows triggered by different kind of events. The CI infrastructure typically runs software builds and executes further build steps like the compliance tooling

### Build Tool
A system that builds a software project and creates the binaries and executables for the software. During this process, the build technology has a technology dependent way to identify and provide dependencies needed to build and run the software. This information is used to run the compliance check on the project.

### Compliance Checker
A set of systems or services that are executed on the identified dependenciesof a project to provide the metadata for the identified components and to run a compliance check according to defined criteria, such as license compatibility, known security violations, company policies.

### FOSS bundle generator
A tool that creates all the necessary documentation needed for the distribution of a software, such as a legal document with all used components there licenses and copyrights, or a source code bundle with all the FOSS sources used in the project. The FOSS bundle is the artifact to be bundled with the delivered product to fulfil most of the license obligations found in FOSS licenses.

### Component Clearing
Dedicated tools and services which provide license information for source code and/or binaries. The tools used follow different approaches. Some get the information by looking it up in a database. Some do source code scans for copyright and license information in comments. Others scan the source code concerning copyrighted snippets. The clearing also contains a step in which the results are approved according to company criteria. 

### (Build) Artifact Repository
A system or service providing (binary) software artifacts and metadata stored in a defined directory structure which is used to retrieve artifacts during a build process. This is used as a cache for the external Artifact Repository to ensure the availability of all components used within the company, it is also the storage for the build software artifacts of the company, used in the Continuous Integration Infrastructure to store the build results.

### Security Assessment
A set of tools and services which map known vulnerabilities from an external database to components used in products and assess the relevance of the vulnerability concerning the usage pattern of the component in question.

### Product Metadata Repository
Software products and most software components are built from other software components. The Product Catalog contains this relationship information to enable the management of dependencies over the life cycle of the software.

### Component Metadata Repository
A system or service that stores metadata to used 3rd party, especially FOSS components. This includes licenses, copyrights, known vulnerabilitites and ECCN classifications. The information is used within the compliance checker to aquire the metadata for the identified components, to assess the compilation of dependent components and to provide the information for the creation of the FOSS bundle (i.e., the artifacts needed for the distribution of a software). The Component Catalog can be linked to an external FOSS Metadata Database to retrieve commonly known information and make it usable within the organization. Also the Security Vulnerability Database and other sources for e.g. ECCN classifications are linked to retrieve the necessary information and to make it available within the company.

#### ECCN Classifications
The Export Control Classification Number (ECCN) is an alpha-numeric code that identifies the level of export control for articles, technology and software that are exported from the United States or the European Union. The code is used for any kind of goods, incl. software.
The component “ECCN Classifications” hosts both the tooling to conduct ECCN classification for every software artefact, as well as the resulting ECCN number. Assumption: Close connection to Product and Component Catalogue. 

### License Metadata Repository
A list of all FOSS (and commercial?) licenses in use within an organization with all necessary metadata like implied obligations. It may use a Public License Master Database and a License Obligation Database for basic information enriched by the company for internal use.
