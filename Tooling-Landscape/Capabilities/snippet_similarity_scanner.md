| Snippet & Similarity Scanner         | |
| ---------------- | ------------------------------------------------ |
| Mission          | • Identify pieces of original code (source, object, binary) by comparing against known codebase   |
| Responsibilities | • Ensure code is free from copyright infringements due to copying routines or third party code<br>• Discover re-use of code <br>• Determine modification of identified code |
| Tasks            | • Scan files for copies <br>• Scan sources for known snippets<br>• Provide scan results including references to copies/identified origin (e.g. earliest known appearance) |
| Input            | • Repository or file(s) to scan<br>• Comparison basis (known data sets)   |
| Output           | • List of potential infringements with links to potential matches (e.g. in existing OSS)<br>• Weighting/ordering of potential matches |
| Comments         | • Snippet Scanning (e.g. plagiarism check), similarity scanning (rough check) and delta analysis (identify change) serve different purposes <br>• While similarity analysis gives indication that something might require further analysis, Snippet scanning delivers proof of re-use<br>• Similarity analysis also allows delta analysis to be performed |