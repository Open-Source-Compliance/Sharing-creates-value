| Dependency Analyzer (Container)          | |
| ---------------- | ------------------------------------------------ |
| Mission          | • Provide composition analysis of a container |
| Responsibilities | • Determine all packages and dependencies used within this container  |
| Tasks            | • Download container (if necessary)<br>• Assess container content/structure and determine used packages/components<br>• Collect information and assemble Bill of Materials<br>• Provide Bill of Materials (e.g. as SPDX)<br>• Provide link between BoM and scanned container, e.g. Repo + image ID + tag<br>• Hash to identify the scanned container should be generated and archived  |
| Input            | • Container or link to container location  |
| Output           | • Bill of Materials (BoM) for particular container<br>• Status of processing (e.g. errors, incompleteness, failures in processing) |
| Comments         |  |