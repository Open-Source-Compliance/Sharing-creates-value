### Name: Create Bill of Materials

**Identifier:** UC_E02

**Description:** tbd

**Goal:** tbd

**Preconditions:** *(List the state(s) the system can be in before this use case starts)*
1. The "project" was initiated in the system
2. The Application Architecture is available
3. The input is Source Code
4. AltA: The input is a manual created list of component (electronically processable)
5. AltB: The input are binaries of a package managed technology
6. AltC: The input are binaries of a non-package managed technology
7. AltD: The input is a SW Container containing the application(s)

**Assumptions:** tbd

**Frequency:** tbd

**Basic Course:** *(Describe the “normal” processing path, aka, the Happy Path)*
1.	Use case begins when development team has created a new application increment
2.	The system identifies the components in the input and assigns a unique id
3.  (The system resolves the dependencies of the components)
4.  The system lists the contained components incl. transitive dependencies with their ids
5.	Use case ends when the bill of material is created


**Alternate Course A:** Input is manual created list of component

***Condition:*** Input is manual created list of component

A.2.1	The system maps the manual entries with existing components in the database
A.2.2	The system uses the database to resolve the dependencies

**Alternate Course B:** Input are binaries of a package managed technology

***Condition:*** Input are binaries of a package managed technology

A.2.1	The system creates identifiers for the binaries
A.2.2	The system compares the identifiers with the existing identifiers in the database

**Alternate Course C:** Input are binaries of a non-package managed technology

***Condition:*** Input are binaries of a non-package managed technology

A.2.1	The system creates identifiers for the binaries
A.2.2	The system compares the identifiers with the existing identifiers in the database

**Alternate Course D:** Input is a SW Container containing the application(s)

***Condition:*** Input is a SW Container containing the application(s)

A.2.1	The system detects the applications in the container
A.2.2	The system creates identifiers for the detected applications
A.2.3   The system resolves the dependencies for the applications with their identifiers
A.2.4	The system compares the identifiers with the existing identifiers in the database

**Post conditions:** *(List the state(s) the system can be in when this use case ends)*
1.	Bill of material is available in the system and mapped to the specific application
2. Each component on the bill of material has a unique ID

**Actors:**
tbd

**Included Use Cases:**
tbd

**Extended Use Cases:**
tbd

**Notes:**
tbd