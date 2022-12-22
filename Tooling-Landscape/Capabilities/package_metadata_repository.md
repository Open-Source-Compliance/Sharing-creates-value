| Package Metadata Repository         | |
| ---------------- | ------------------------------------------------ |
| Mission          | • Collect package information and clearing metadata on packages   |
| Responsibilities | • Single point of truth for package information |
| Tasks            | • Store package metadata and quality verification status (of that metadata concenring completeness and correctness)<br>• Support composition analysis (verification of dependency analysis)<br>• Provide search capabilities to identify existing packages<br>• Support authentication/authorization to ensure responsible data handling/editing  |
| Input            | • Package identifier (e.g. purl) + already identified metadata<br>• Package metadata   |
| Output           | • Package metadata, including package type (e.g. OSS, COTS, internal) and completion/ verification status of associated metadata<br>• Containment structures (consists of)<br>• Dependency structures (depends on)<br>• Optional: relate known vulnerability information (not OSC specific, but a good place) |
| Comments         | • Archive should be provided by archive capability. Tools supporting both functions in one are not limited by the capabilities beeing separate. |