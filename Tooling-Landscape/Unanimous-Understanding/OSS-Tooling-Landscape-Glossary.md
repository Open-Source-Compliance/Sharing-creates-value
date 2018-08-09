# Glossary for the OSS Tooling Landscape

## Company External

### Source Code Repository
Systems or services that provide source code. These systems or services can provide plain source code only or – in addition – also have version control. 

### Build Artefacts Repository
Systems or services that provides (binary) software artefacts and metadata stored in a defined directory structure which is used to retrieve artefacts during a build process. Software artefacts may be of type proprietary, commercial, FOSS, …

### Security Vulnerabilities
Systems or services that provide information about publicly known security vulnerabilities of software artefacts.

### License Obligations
Systems or services that provide (machine readable?) Data about obligations and prohibitions of (FOSS) licenses.

### Public License Master Data
Publicly available information about Open Source licenses (e.g. commonly accepted license identifiers). 

### FOSS Meta Data
Systems or services that provide descriptive data of software artefacts (mainly FOSS). Data could be: the declared license for a component, the source location (e.g., Git commit) for a version, details to be included in attributions (e.g., copyright holders in a Notices file), etc.

## Company Internal

### CI/CD Pipeline
A system that enables automating the creation of a software build and the associated processes including: compiling source code into binary code, packaging binary code,and running automated tests. 

### Source Code Repository
Systems or services that provide source code. These systems or services can provide plain source code only or – in addition – also have version control. 

### License Scanning
Dedicated tools which provide license information for source code and/or binaries. These tools follow different approaches. Some get the information by looking it up in a database. Some do source code scans.

### Build Artefacts Repository
A collection of (binary) software artefacts and metadata stored in a defined directory structure which is used to retrieve artefacts during a build process. Software artefacts may be of type proprietary, commercial, FOSS, …

### Security Scanning
Dedicated tools which scan source code and/or binaries to detect code vulnerabilities, both in proprietary as well as in FOSS components.

###Product and Component Catalogue
Software products and most software components are built from other software components. Therefore, a software product can be viewed as a graph of interconnected software components and fragments. The properties of the constituent parts of a product and their relationships are all relevant to product governance and need to be modeled precisely. The product and component catalog contains such information and potentially other meta data.

### ECCN Classifications
The Export Control Classification Number (ECCN) is an alpha-numeric code that identifies the level of export control for articles, technology and software that are exported from the United States or the European Union. The code is used for any kind of goods, incl. software.
The component “ECCN Classifications” hosts both the tooling to conduct ECCN classification for every software artefact, as well as the resulting ECCN number. Assumption: Close connection to Product and Component Catalogue. 

### License Master Data
A list of all FOSS (and commercial?) licenses in use within an organization.
