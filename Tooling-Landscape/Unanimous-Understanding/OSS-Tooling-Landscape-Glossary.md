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
Publicly available information about Open Source licenses (e.g. commonly accepted license identifiers). It could furthermore provide (potentially machine readable) data about the corresponding obligations and prohibitions of a license.

### FOSS Metadata Database
Systems or services that provide descriptive data of software artefacts (mainly FOSS). Data could be: the declared license for a component, the source location (e.g., Git commit) for a version, details to be included in attributions (e.g., copyright holders in a Notices file), etc.

## Company Internal

### Source Code Repository
Systems or services that provide source code. This is typically a version control system. For the compliance tooling, typically the source code is needed as a folder on a file share, i.e., the source code is already checked out by, e.g., the Continuous Integration infrastructure. 

### Continuous Integration Infrastructure
Systems or services that orchestrate the build process for a software project and executes workflows triggered by different kind of events. The CI infrastructure typically runs software builds and executes further build steps like the compliance tooling

### License Scanner
A set of systems or services that are executed on the source code and/or binaries of a project to identify third party software, especially FOSS components, to provide the metadata for the identified components and to run a compliance check according to defined criteria, such as license compatibility, use if software with security violations.

#### Dependency Identifier
A tool to identify the dependencies referenced by a software project. It is deeply embedded into the build technology and uses the means of the technology to identify the dependent components. The result of the dependency identification is stored in the Product Catalog for further traceability of the software project.

#### Metadata Provider
A tool to enrich the list of dependent components in a software project with the relevant metadata. It typically uses the Component Catalog to retrieve the metadata. It is also the trigger for the Component Clearing service in the case that metadata for a component is not available.

#### Policy Engine
A tool within the compliance tooling that applies criteria on the compilation of dependent components of a software project. It checks for aspects like compatibility of licenses used, company policies towards the used licenses, status concerning vulnerabilities of components. It basically produces the result of the compliance tooling towards the CI infrastructure, so that the build result can be influenced according to the company prerequisites.

#### FOSS bundle generator
A tool that creates all the necessary documentation needed for the distribution of a software. This includes the attribution/disclosure document with all used components there licenses and copyrights, but also a source code bundle with all the FOSS sources used in the project. The FOSS bundle is the artifact to bundled with the delivered product to fulfil most of the license obligations found in FOSS licenses.

### Component Clearing
Dedicated tools and services which provide license information for source code and/or binaries. The tools used follow different approaches. Some get the information by looking it up in a database. Some do source code scans for copyright and license information in comments. Others scan the source code concerning copyrighted snippets. The clearing also contains a step in which the results are approved according to company criteria. 

### (Build) Artifact Repository
A system or service providing (binary) software artifacts and metadata stored in a defined directory structure which is used to retrieve artifacts during a build process. This is used as a cache for the external Artifact Repository to ensure the availability of all components used within the company, it is also the storage for the build software artifacts of the company, used in the Continuous Integration Infrastructure to store the buidl results.

### Security Scanning
Dedicated tools which scan source code and/or binaries to detect code vulnerabilities, both in proprietary as well as in FOSS components.

### Product Catalog
Software products and most software components are built from other software components. Therefore, a software product can be viewed as a graph of interconnected software components and fragments. The Product Catalog contains the information on this graph to enable the management of dependencies over the life cycle of the software, e.g., to ensure that a new vulnerability in a FOSS component can be evaluated and actions toward updating software in the field can be initiated.

### Component Catalog
A system or service that stores metadata to used 3rd party, especially FOSS components. This includes licenses, copyrights, known vulnerabilitites and ECCN classifications. The information is used within the compliance tooling to aquire the metadata for the identified components, to assess the compilation of dependent components and to provide the information for the creation of the FOSS bundle (i.e., the artifacts needed for the distribution of a software). The Component Catalog can be linked to an external FOSS Metadata Database to retrieve commonly known information and make it usable within the organization. Also the Security Vulnerability Database and other sources for e.g. ECCN classifications are linked to retrieve the necessary information and to make it available within the company.

#### ECCN Classifications
The Export Control Classification Number (ECCN) is an alpha-numeric code that identifies the level of export control for articles, technology and software that are exported from the United States or the European Union. The code is used for any kind of goods, incl. software.
The component “ECCN Classifications” hosts both the tooling to conduct ECCN classification for every software artefact, as well as the resulting ECCN number. Assumption: Close connection to Product and Component Catalogue. 

### License Master Database
A list of all FOSS (and commercial?) licenses in use within an organization with all necessary metadata like implied obligations. It may use a Public License Master Database for basic information enriched by the company for internal use.
