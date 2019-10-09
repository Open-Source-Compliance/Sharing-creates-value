### Name: Get fast feedback

**Identifier:** UC_E01

**Description:** tbd

**Goal:** tbd

**Preconditions:** *(List the state(s) the system can be in before this use case starts)*
1. The development environment is set up
2. Application Architecture definition has started
2. A potential FOSS component is going to be integrated in the application

**Assumptions:** tbd

**Frequency:** tbd

**Basic Course:** *(Describe the “normal” processing path, aka, the Happy Path)*
1.	Use case begins when a new component is selected
2.	The system detects the component and queries the database for existing metadata
3.  The existing metadata is fed back 
4.	Use case ends when the metadata feedback is consumed by the user or the development environment


**Alternate Course A:** *Description of the alternate course*

***Condition:*** No metadata available in the database

A.3.1	The systems throws an exception
A.3.2	The system triggers an incident in the incident management system

**Post conditions:** *(List the state(s) the system can be in when this use case ends)*
1.	Metadata was fed back as base for component decision

**Actors:**
tbd

**Included Use Cases:**
tbd

**Extended Use Cases:**
tbd

**Notes:**
tbd