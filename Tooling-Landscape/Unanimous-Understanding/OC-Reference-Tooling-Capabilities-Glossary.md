# Glossary for OpenChain Reference Tooling Capabilities

## Purpose and Scope

This glossary provides the unanimous understanding of high-level functional *capabilities* of the OSS Tooling.
A separate *mapping* traces the implementation level *components* to the high-level functional capabilities identified here below.
Relationships and data flows between capabilities are captured in a UML *diagram*, which is annotated with appropriate stereotypes.
- TODO: Create proper mapping of components to capabilities (current state in stripped MD glossary document of components: OC-Reference-Tooling-Components-Glossary.md)
- TODO: Migrate PowerPoint capability overview diagram into PlantUML diagram
- TODO: Harmonise capability names with one-page picture from Oliver
- TODO: Harmonise terms with OC terminology (e.g. "supplied software" instead of "product"?)

The identified capabilities have different scope and responsibilities:
- **Compliance Capabilities** are typically required in the context of the compliance process, and are the reponsibility of the compliance tooling.
- **Provided Capabilities** are typically required to perform the compliance process, but are not the responsibility of the compliance tooling. Rather they may exist already and can be integrated with the compliance process in order to provide a complete solution. A typical example of a provided capability is the [Source Code Repository](#source-code-repository), which is typically under the responsibility of the organisation's development teams.
- **Security Capabilities** address security concerns and allow including security vulnerability  management into the overall picture. They are however a special form of provided capabilities, and shown here only to provide the context. As such, they are not in scope of the compliance tooling.

## Definition of Terms

- **Component**: any software element that is treated as a uniquely identifiable entity within the compliance process (e.g. proprietary, commercial, or FOSS component)
- **Product**: a piece of software that is analysed by the compliance process for purposes of distribution
- **Business Context**: the information defining the situation and circumstances of a foreseen distribution of a *product*, including the distribution license, distribution channel, any export related information, the foreseen audience (e.g. customers, partners, Open Source, regional constraints), etc.

## Compliance Capabilities

### Approval Flow<a name="approval-flow"/>
**Mission: To help decentralising compliance work through approval**

The *Approval Flow* allows inclusion of responsible staff into the flow of approvals required in the compliance process. This capability typically makes use of a Workflow Engine (WFE) or a Business Process Engine (BPE).
- *Responsibilities* 
  - Provide approval flow appropriate for audit
- *Typical Tasks*
  - Track all legally relevant changes to products and components 
  - Identify authors of change
  - Provide compliance status and overview
  - Allow to approve or reject an approval request
  - Document/archive all decisions (auditing)
- *Inputs*
  - Approval request for (list of components, legal situation, compliance documentation)
- *Outputs*
  - State of compliance analysis for approval request
  - Approval / rejection documentation
- *Comments*
  - The approval by a dedicated, skilled resource (Compliance Manager) combined with the automation support for all prior steps reduces the workload for Compliance Managers.
- *Examples*
  - N/A

### Business Context Repository<a name="business-context-repository"/>
**Mission: To manage all compliance relevant context information of a product distribution case**

The *Business Context Repository* collects all information about a product distribution case (distribution license, situation, constraints, circumstances, compliance status, etc.). It focuses on the business context only, and references the [Component Metadata Repository](#component-metadata-repository) for all data related directly to the product (source code location, binary location, product structure such as contained components, dependencies, etc.).
- *Responsibilities* 
  - Provide single source of truth for a product distribution case
  - Ensure completeness of product compliance documentation
- *Typical Tasks*
  - Collect all product specific information, including component change and linkage status (via history)
  - Follow the release cycle of a particular product, e.g. approvals
  - Organize access rights and assign roles
  - Build canvas for reporting and analysis of a given composition & in a given situation
- *Inputs*
  - Bill of Materials (BoM)
  - External components, e.g. runtime environments, middleware or resources
  - Participants / Stakeholders
- *Outputs*
  - Status Overview
  - History of events
  - Reporting
- *Comments*
  - N/A
- *Examples*
  - N/A

### Compliance Artefact Generator<a name="compliance-artefact-generator"/>
**Mission: To support provisioning of compliance documentation**

The *Compliance Artefact Generator* creates all the necessary documentation needed for the distribution of a (software) product, such as a document with all used components, their licenses and copyrights, or a source code bundle with all FOSS components' sources used in the product. Typically, these compliance artefacts are to be bundled with the product to fulfill license obligations found in the licenses of the used FOSS components.
- *Responsibilities* 
  - Ensure legally compliant documentation
- *Typical Tasks*
  - Generate compliance documentation according to requirements
  - Support *Compliance Managers* in completing their tasks 
  - Provide documentation parts, e.g. written offer, license texts, copyrights, modification statement, etc.
  - Provide source code bundle, i.e. source of all FOSS components used in the product
  - Link documentation with documentation objects (version management)
- *Inputs*
  - List of versioned components to be documented (BoMs)
  - Legal requirements with respect to particular circumstances
- *Outputs*
  - Stub with all documentation requirements 
  - Pre-assembled stub with all existing information (e.g. from repository) 
  - Source code bundle
  - Identified TODOs for missing bits
- *Comments*
  - TODO: Consider agreeing on a specific output format (e.g. PDF, HTML, SPDX, etc.).
- *Examples*
  - N/A

### Compliance Checker<a name="compliance-checker"/>
**Mission: To check the compliance status of a product or component**

The *Compliance Checker* performs a compliance check for a given product or component, taking as input the identified dependencies of a product or component. The compliance check is executed for all identified components according to defined criteria, such as license compatibility, known security violations, company policies.
- *Responsibilities* 
  - Provide compliance status of a product or component
- *Typical Tasks*
  - TBD
- *Inputs*
  - Product or component, together with all its dependencies
  - Compliance checking criteria
- *Outputs*
  - Compliance status and possible compliance issues
- *Comments*
  - N/A
- *Examples*
  - N/A

### Component Analyzer<a name="component-analyzer"/>
**Mission: To research and provide component metadata**

The *Component Analyzer* determines the metadata of a component (e.g. license, home page, source code repository, version history, viability information etc.).
Existing tools follow different approaches. 
Some get the information by looking it up in a database.
Some do source code scans for copyright and license information in comments. 
Others scan the source code concerning copyrighted snippets. 
The clearing also contains a step in which the results are approved according to an organisation's criteria.
- *Responsibilities* 
  - Collect and provide accurate metadata about the component
  - Alert if the component cannot be matched/found
- *Typical Tasks*
  - Scan [Package Managers](#package-manager) for new packages or versions of packages
  - Scan source code and/or binary files
  - Collect component metadata
  - Transfer component metadata to the [Component Metadata Repository](#component-metadata-repository)
- *Inputs*
  - Component descriptor or name, and/or
  - Component source code, and/or
  - Component binary file(s) and/or
  - Component container(s)
- *Outputs*
  - Component metadata, such as: 
    - effective license (e.g. [SPDX](https://spdx.org/) ID, 
	  license text, license URL)
	- home page location (URL)
	- source code repository location (URL)
	- version history
	- viability information (e.g. commit count, stars, last commit date, etc.)
- *Comments*
  - TODO: Harmonise use of [Package Managers](#package-manager) with [Dependency Analyzer](#dependency-analyzer).
  - TODO: Harmonise use of code scanners with [License & Copyright Scanner](#license-copyright-scanner).
- *Examples*
  - N/A

### Component Metadata Repository<a name="component-metadata-repository"/>
**Mission: To store component metadata, including clearing data**

A *Component Metadata Repository* stores metadata about software components, especially used FOSS components, but possibly including other third-party components and proprietary components, discriminated by their type.
The metadata includes licenses, copyrights, known vulnerabilitites and information that is needed to do export classifications (ECCN), such as information about the contained cryptographic functionality.
As software products and most software components are built from other software components, the *Component Metadata Repository* also contains this relationship information, aka *Bill of Materials*, to enable the management of dependencies over the life cycle of the software.
The stored information is used within the compliance checker to aquire the metadata for the identified components, to assess the compilation of dependent components and to provide the information for the creation of the FOSS bundle (i.e., the *Compliance Artefacts* needed for the distribution of a software). 
The *Component Metadata Repository* can be linked to an external FOSS Metadata Database to retrieve commonly known information and make it usable within the organization.
Also, a [Security Vulnerability Database](#security-vulnerability-database) as well as other sources for e.g. export classification-relevant data can be linked to retrieve the necessary information and to make it available within the organisation.
- *Responsibilities* 
  - Single source of truth for component metadata and dependency information
- *Typical Tasks*
  - Store components' metadata and dependencies
  - Allow discrimination component by their type (e.g. proprietary, commercial, FOSS)
  - Support custom attributes for components and dependencies
  - Support composition analysis (verification of dependency analysis)
  - Provide search capabilities to identify existing components
  - Support authentication/authorization to ensure responsible data handling/editing 
- *Inputs*
  - Component identification
  - For storage/upload:
    - Component metadata (if known)
    - Component containment relationships (consists of)
	- Component dependency relationships (depends on)
- *Outputs*
  - Component identification and metadata, including component type (e.g. proprietary, commercial, FOSS) and completion/verification status of associated metadata
  - Containment structures (consists of)
  - Dependency structures (depends on)
  - Optional: relate known security vulnerability information
- *Comments*
  - The *Component Metadata Repository* does not store the actual source code or binary artefacts of the managed components. Rather this information is only referenced/linked from here, and stored in the [Source Code Repository](#source-code-repository) and/or [Artefact Repository](#artefact-repository).
  - It is possible to use public repositories or services as additional source of information, such as a *FOSS Metadata Database*, providing descriptive data of software artefacts (mainly FOSS), such as the declared license for a component, the source location (e.g. Git commit) for a version, details to be included in attributions (e.g. copyright holders in a Notices file), etc.
  - TODO: Clarify role of repository in relation to the archive function. SW360 comes as archive, which actually could also be served by Git or any binary repository (see comment above). Thus adding an archive function here might just duplicate the code.
  - TODO: Clarify how to uniquely identify OSS components (Package URL, ...?), harmonise the chosen mechanism with the [Dependency Analyzer](#dependency-analyzer).
- *Examples*
  - [Eclipse SW360](https://projects.eclipse.org/proposals/sw360)
  - [ClearlyDefined](https://clearlydefined.io/)

### Dependency Analyzer<a name="dependency-analyzer"/>
**Mission: To provide the complete set of component dependencies**

The *Dependency Analyzer* determines the dependencies of a software component.
The way how dependencies are expressed is specific to the used technologies and [package managers](#package-manager). 
Therefore, dedicated functionality is needed for the different package managers and technologies in use.
The term *Dependency Analyzer* is used here as an umbrella or abstraction for such specialized tools.
It ensures that all dependencies are resolved recursively, and that the output is a complete list of dependencies that is independent from the respective technology and package manager.
- *Responsibilities* 
  - Perform composition and dependency analysis of a component, which is e.g. provided as source code, binary file, or container
  - Determine all other components that the given component contains or depends on
  - Allow to stop a CI/CD chain if violations occur
- *Typical Tasks*
  - Determine composition and dependency structure, e.g.:  
    - source code: Integrate with build process (CI/CD) and collect composition and dependency information
    - binary file: Download binary (if required) and unpack according to detected binary format
    - container: Download container (if required) and unpack according to detected container format
  - Determine set of contained components (i.e. components that are provided together with the component)
  - Determine transitive set of dependencies (dependency tree), starting from the component itself and all its contained components (convex hull)
  - Compile Bill of Materials (BoM), as union of above sets of determined components, in a technology neutral format
  - Provide BoM in standardised output format
  - Provide links between BoM elements and determined components
- *Inputs*
  - Component or link to component location
- *Outputs*
  - Bill of Materials (BoM) for component
- *Comments*
  - TODO: Decide how to provide the Bill of Materials (BoM) output, e.g. [SPDX](https://spdx.org/).
  - TODO: Decide how to uniquely identify any referenced/linked elements (e.g. source files, binary files, containers). 
    Examples include using
	the commit ID for source files,
    the binary repository ID for binary files, and 
    the container repository/image ID/tag for containers. 
    Binary files and containers could also be identified by generated hashes or keys.
    More generally, the [Package URL (purl)](https://github.com/package-url/purl-spec) mechanism could come in handy in this context.
- *Examples*
  - [ORT Analyzer](https://github.com/heremaps/oss-review-toolkit#analyzer)
  
### Forensic Code Analyzer<a name="forensic-code-analyzer"/>
**Mission: To identify the origin of code**

The *Forensic Code Analyzer* analyzes code, be it source or binary code, to determine metadata about code origin, license and/or copyright. 
Snippet scanners or binary analyzers are such tools, for example.
- *Responsibilities* 
  - Ensure code is free from copyright infringements due to copying routines or third party code
- *Typical Tasks*
  - Scan code for code clones ("snippets")
- *Inputs*
  - Repository or file(s) to scan
- *Outputs*
  - List of potential infringements with links to potential code clones (e.g. in existing OSS)
  - Weighting/ordering of potential code clones
- *Comments*
  - TODO: Discuss whether this shall also search for Author and Copyright information as it could be a good place to do so (see [License & Copyright Scanner](#license-copyright-scanner)). 
    Forensic code analysis is currently separated into this extra capability as it is a very specific task, which is very time consuming, error prone, and typically involves lots of manual work.
- *Examples*
  - [Binary Analysis Next Generation](https://github.com/armijnhemel/binaryanalysis-ng)

### Legal Obligations Resolver<a name="legal-obligations-resolver"/>
**Mission: To determine legal rights and obligations resulting from the usage of the listed components within the product and business context**

The *Legal Obligations Resolver* is a process and/or tool set that supports the fulfillment of license obligations. This comprises organisation external obligations that are imposed by law as well as organisation internal obligations originating in organisation specific policies or processes. Typically, it utilizes [Compliance Checkers](#compliance-checker) and [Compliance Artefact Generators](#compliance-artefact-generator).
- *Responsibilities* 
  - Provide compliance requirements
- *Typical Tasks*
  - Assess license information from all components (recent BoMs, infrastructure and COTS)
  - Determine license obligations
  - Identify effective licenses
- *Inputs*
  - Composition analysis of all project related components, their status and licenses
  - Legal circumstances and requirements
- *Outputs*
  - List of legal obligations by component and mitigation hints
- *Comments*
  - Independent from component status the analysis results may vary depending on changes in the circumstances. Thus analysis results should be versioned to allow allocation to related circumstances.
- *Examples*
  - N/A

### License & Copyright Scanner<a name="license-copyright-scanner"/>
**Mission: To precisely scan source code and identify information for compliance proper declarations**

The *License & Copyright Scanner* analyses source code to identify license, copyright and author information.
- *Responsibilities* 
  - Ensure correctness of determined compliance information
- *Typical Tasks*
  - Identify effective licenses
  - Identify copyright statements
  - Identify authors
- *Inputs*
  - Repository or file(s) to scan
- *Outputs*
  - List of effective license declarations with references/links into code
  - List of copyright statements with references/links into code
  - List of author information with references/links into code
- *Comments*
  - TODO: Build consensus on the need and granularity of author information, which might be different from copyright holder.
  - TODO: Harmonise referencing/linking mechanism with [Dependency Analyzer](#dependency-analyzer) (see TODO there).
- *Examples*
  - [Fossology](https://www.fossology.org/), [Scancode Toolkit](https://github.com/nexB/scancode-toolkit)

### License Repository<a name="license-repository"/>
**Mission: To capture and archive legal information about licenses**

The *License Repository* captures all FOSS (and proprietary and commercial?) licenses in use within an organisation, with all necessary metadata such as implied rights and obligations. It may use a *Public License Master Database* and/or a *License Obligations Database* for basic information enriched by the organisation for internal use.
- *Responsibilities* 
  - Manage and provide legal information about licenses
- *Typical Tasks*
  - Capture all license information including derived requirements
  - Provide environment to allow license analysis
  - Track license data changes
  - Provide reference for original license texts
- *Inputs*
  - License data
- *Outputs*
  - License data (updated)
- *Comments*
  - It is possible to use public repositories or services as additional source of information, such as a a *License Obligations Database* or a *Public License Master Database*, providing for example information about obligations and prohibitions of (FOSS) licenses or commonly accepted license identifiers. 
  - TODO Should we also capture proprietary and commercial licenses here?
- *Examples*
  - [Eclipse SW360](https://projects.eclipse.org/proposals/sw360)
  - [OSADL License Checklists](https://www.osadl.org/Open-Source-License-Checklists.oss-compliance-lists.0.html)
  
### Policies & Rules Repository<a name="policies-rules-repository"/>
**Mission: To document context and evolution of the context of a product**

The *Policies & Rules Repository* manages organisation wide or product (group) specific policies and rules. In some cases it may make sense to provide lists of accetable (white) or not acceptable (black) licenses or components. Thus a developer aiming to use a new component may verify against this list whether his aim will violate any organisation/product rules. In particular critical components even a "whitelisting requirement" could be issued, so a competent sponsor may ensure that only allowed components will be applied. Modern tooling should support automated verification of such lists or a whitelist enforcement.
- *Responsibilities* 
  - Manage policies & rules, including black- and whitelists
  - Track all relevant changes in the product environment
- *Typical Tasks*
  - Allow managing and enforcing policies & rules, including black- and whitelists 
  - Allow managing groups of products with consistent policies & rules
  - Document legal circumstances, e.g. commercial aspects, trade secrets, export aspects or IP protection requirements, etc.
  - Document changes in black- or whitelists applicable to the product
  - Track changes
- *Inputs*
  - Legal requirements
  - Black- and whitelists
  - Product specific policies & rules
- *Outputs*
  - History of changes 
- *Comments*
  - TODO: How to capture policies & rules in a form that allows automation/repetition?
- *Examples*
  - N/A

## Provided Capabilities

### Artefact Repository<a name="artefact-repository"/>
**Mission: To manage (binary) artefacts, including versions and releases**

The *Artefact Repository* provides (binary) software artefacts and metadata stored in a defined directory structure, which is used to retrieve artefacts during a build process. 
Software artefacts may be of type proprietary, commercial, or FOSS.
The artefact repository may also be used to store the source code of FOSS components besides the binary artefact for usage within the compliance process, e.g., for starting a license scan or creating the source code bundle to be delivered with the product.
- *Responsibilities* 
  - Manage (binary) software artefacts
- *Typical Tasks*
  - Retrieve/download artefact(s) by coordinate (e.g. Maven groupId/artefactId/version)
  - Retrieve/download artefact(s) by location (e.g. URL)
  - Store/upload artefact(s) or replace existing artefact(s)
  - Manage releases and stages
- *Inputs*
  - Artefact coordinate or location
  - Artefact file (for storage/upload only)
- *Outputs*
  - Artefact file (for retrieval/download only)
  - Status
- *Comments*
  - Within an organisation, an artefact repository can be used as a cache for external artefact repositories to ensure the availability of all components used within the organisation. It can also be used as storage for the software artefacts created during CI/CD processes in the organisation (build results).
  - TODO Elaborate differences and commonalities of definition and functionality wrt [Package Manager](#package-manager).
- *Examples*
  - Public repositories: [Maven Central](https://mvnrepository.com/repos/central), [npm](https://www.npmjs.com/), [PyPI](https://pypi.org/), ...
  - Repository managers: [Archiva](https://archiva.apache.org/index.cgi), [Nexus Repository OSS](https://www.sonatype.com/nexus-repository-oss), ...

### Audit Log<a name="audit-log"/>
**Mission: To maintain log of changes and user actions**

The *Audit Log* maintains a central log of all changes and user actions. This is required for due diligence purposes, allowing to trace all decisions and changes retrospectively.
- *Responsibilities* 
  - Ensure confirmability of configuration changes
  - Ensure tracing and archiving of all user actions/decisions for auditing purposes
- *Typical Tasks*
  - Track user activity and changes in settings, especially legal settings
  - Track and archive user decisions and related context to enable auditing
- *Inputs*
  - User actions / events
- *Outputs*
  - History of changes with actors
  - Transparency 
- *Comments*
  - N/A
- *Examples*
  - N/A

### Build Tool<a name="build-tool"/>
**Mission: To build a software product or component**

A *Build Tool* is a system that builds a software product or component and creates the binaries and executables for the software. During this process, the build technology has a technology dependent way to identify and provide dependencies needed to build and run the software. This information is used to run the compliance check on the product or component.
- *Responsibilities* 
  - TBD
- *Typical Tasks*
  - TBD
- *Inputs*
  - TBD
- *Outputs*
  - TBD
- *Comments*
  - The [Dependency Analyzer](#dependency-analyzer) is typically integrated with the *Build Tool*.
- *Examples*
  - [Apache Ant](https://ant.apache.org/),
	[Apache Maven](https://maven.apache.org/),
	[CMake](https://cmake.org/),
	[GNU Make](https://www.gnu.org/software/make/),
    [Gradle](https://gradle.org/), 
	...

### Continuous Integration/Deployment Infrastructure (CI/CD)<a name="cicd-infrastructure"/>
**Mission: To orchestrate the build, test and deployment process**

The *CI/CD Infrastructure* is a set of systems or services that orchestrate the build and deployment process for a software product or component, and that executes workflows triggered by different kinds of events. The CI/CD infrastructure typically runs software builds and executes further build steps like testing and the compliance checks.
- *Responsibilities* 
  - TBD
- *Typical Tasks*
  - TBD
- *Inputs*
  - TBD
- *Outputs*
  - TBD
- *Comments*
  - N/A
- *Examples*
  - N/A

### Package Manager<a name="package-manager"/>
**Mission: To manage a repository of (binary) software packages**

A *Package Manager* is a collection of software tools that automates the process of creating, maintaining, installing, upgrading, configuring, and removing components within a computer system or operating system in a consistent manner.
A package manager is usually technology and/or programming language dependent.
- *Responsibilities* 
  - TBD
- *Typical Tasks*
  - TBD
- *Inputs*
  - TBD
- *Outputs*
  - TBD
- *Comments*
  - TODO Elaborate differences and commonalities of definition and functionality wrt [Artefact Repository](#artefact-repository).
- *Examples*
  - [Apache Maven](https://maven.apache.org/) (Java), 
    [Conan](https://conan.io/) (C++), 
	[CPAN](http://www.cpan.org/) (Perl), 
	[npm](https://www.npmjs.com/) (JavaScript), 
	[NuGet](https://nuget.org/) (Windows/.NET), 
	[pip](https://pip.pypa.io/) (Python),
	...

### Reporting & Analytics<a name="reporting-analytics"/>
**Mission: To visualize work, efforts and success of compliance initiative**

The *Reporting & Analytics* provides visualisations and reports about work, effort and success of a compliance initiative.
- *Responsibilities* 
  - Measure compliance related activity  
  - Provide insights into state of portfolio
- *Typical Tasks*
  - Provide lists and insights 
- *Inputs*
  - Report specific configuration
- *Outputs*
  - Reports
  - Transparency
 - *Comments*
  - TODO: Discuss whether we want to define specific reports that shall be supported.
- *Examples*
  - N/A

### Source Code Repository<a name="source-code-repository"/>
**Mission: To manage source code, including versions and branches**

The *Source Code Repository* provides source code. 
This is typically (also) a version control system. 
The compliance tooling obtains the source code of third-party dependencies, i.e. FOSS components, from such repositories.
Further, it obtains the source code of proprietary components from repositories, which are typically under the responsibility of the organisation's development teams.
- *Responsibilities* 
  - Manage source code
  - Preserve source code as long term archive (optional)
- *Typical Tasks*
  - Provide access to source code of components, with versions and branches
- *Inputs*
  - Source code location (URL), including component reference, version or branch information
  - Credentials (optional)
- *Outputs*
  - Source code files, or archive/package file (e.g. ZIP, JAR) with source code files
- *Comments*
  - For the compliance tooling, the source code is typically needed as a folder on a file share, i.e., the source code is already checked out by, e.g., the CI/CD infrastructure. As a sub function, a source code repository typically contains a source code downloader.
- *Examples*
  - [Software Heritage](https://www.softwareheritage.org/),
    [GitHub](https://www.github.com/),
    [GitLab](https://www.gitlab.com/), ...

### Tool Orchestrator<a name="tool-orchestrator"/>
**Mission: To realize overall compliance workflow and machinery**

The *Tool Orchestrator* provides support to realize the overall compliance workflow and associated (automated) processes and services.
- *Responsibilities* 
  - Arrange combination of tools to cope with compliance challenge 
  - Handle handover between capabilities
- *Typical Tasks*
  - Trigger events 
- *Inputs*
  - Events
- *Outputs*
  - Events
 - *Comments*
  - TODO: Discuss whether we want to define specific events in an underlying flow.
- *Examples*
  - N/A

### User & Role Management<a name="user-role-management"/>
**Mission: To provide role-based authorization**

The *User & Role Management* provides role-based authorization mechanisms to all other capabilities.
- *Responsibilities* 
  - Authenticate users
  - Manage roles and authorizations
  - Assign users to roles
- *Typical Tasks*
  - Identify users (Login, oAuth, MFA)
  - Manage roles and related authorizations (permissions assigned to roles)
  - Manage API Keys
- *Inputs*
  - Users
  - Roles
  - Assignments (user to project, etc.)
- *Outputs*
  - Access tokens 
- *Comments*
  - This is a provided capability, which is required in the compliance tooling to ensure proper management of users and their roles.
- *Examples*
  - [Apache Shiro](https://shiro.apache.org/)

## Security Capabilities

### Security Vulnerability Assessment<a name="security-vulnerability-assessment"/>
**Mission: To assess security vulnerabilities in terms of their risk to the organisation**

The *Security Vulnerability Assessment* maps known vulnerabilities from an external [vulnerability database](#security-vulnerability-database) to components used in products, and assesses the relevance and exploitability of the vulnerability concerning the usage pattern of the component in question.
- *Responsibilities* 
  - TBD
- *Typical Tasks*
  - TBD
- *Inputs*
  - TBD
- *Outputs*
  - TBD
- *Comments*
  - N/A
- *Examples*
  - N/A

### Security Vulnerability Database<a name="security-vulnerability-database"/>
**Mission: To inform about publicly known security vulnerabilities**

The *Security Vulnerability Database* is a system or service that provides information about publicly known security vulnerabilities of software artefacts.
- *Responsibilities* 
  - TBD
- *Typical Tasks*
  - TBD
- *Inputs*
  - TBD
- *Outputs*
  - TBD
- *Comments*
  - N/A
- *Examples*
  - [NVD](https://nvd.nist.gov/)

## Template

### Capability Name<a name="capability-name"/>
**Mission: To ...**

The *Capability Name* ...
- *Responsibilities* 
  - ...
- *Typical Tasks*
  - ...
- *Inputs*
  - ...
- *Outputs*
  - ...
- *Comments*
  - N/A
- *Examples*
  - [Title](http://link.to.example)

