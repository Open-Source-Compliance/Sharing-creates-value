| Dependency Analyzer (Binary)          | |
| ---------------- | ------------------------------------------------ |
| Mission          | • Provide composition analysis of a software binary |
| Responsibilities | • Determine all packages and dependencies used within this binary  |
| Tasks            | • Download binary (if required)<br>• Unpack binary<br>• Assess content and determine used packages/components<br>• Collect information and assemble Bill of Materials<br>• Provide Bill of Materials (e.g. as SPDX)<br>• Provide link between BoM and scanned artefact, e.g. binary repo ID<br>• Hash to identify the binary scanned should be generated and archived  |
| Input            | • Binary or link to binary location   |
| Output           | • Bill of Materials (BoM) for particular binary<br>• Status of processing (e.g. errors, inclompleteness, failures in processing) |
| Comments         |  |