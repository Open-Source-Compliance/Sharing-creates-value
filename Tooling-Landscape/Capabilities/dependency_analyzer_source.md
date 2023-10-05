| Dependency Analyzer (Source)          | |
| ---------------- | ------------------------------------------------ |
| Mission          | • Provide composition analysis of software to be built from these sources |
| Responsibilities | • Determine all packages and dependencies (incl. transitive) used to build the software<br>• Determine the way of linking of dependencies  |
| Tasks            | • Integrate with build process (CI/CD)<br>• Determine composition (_complete_ Bill of Materials)<br>• Provide output for further analysis, e.g. as SPDX<br>• Provide link between scanned source and BoM information, e.g. Commit ID  |
| Input            | • Build description, e.g. POM or requirements.txt   |
| Output           | • Bill of Materials (BoM) for particular build   |
| Comments         | Analysis and dependency resolution is highly language specific. Thus a language specific implementation might be required<br>Discussion: Would it make sense to declare a task or responsibility to stop CI/CD in sit of violation? |