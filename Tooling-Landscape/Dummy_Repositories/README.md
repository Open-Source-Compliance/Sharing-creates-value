This section shall collect all information about the use, handling and maintenance of dummy repositories
(based on presentation held in 2025-05: https://github.com/Open-Source-Compliance/Sharing-creates-value/tree/master/Meeting-Material/Meeting-20240515 )

# Background
## Need
A reproducible quality for the Software Composition Analysis and the handling of findings needs to be ensured.
In order to be able to test different infrastructure setups (with different tools) „test-sets“ are necessary

## Idea / Concept
1. Identify „Hello World+“ (+ = using dependencies) example repositories in the respective communities (ideally maintained by the stewards of the respective technology, e.g. maven-example by the Maven-community etc.)
2. Fork the example repository to Sharing_creates_value as a „dummy“
3. Establish branches to enrich the „dummy“ with test-cases of interest and provide a description of the „expected behaviour“ if analyzed by an Open Source Management tool (e.g. ORT, Fossology,…)
4. Use the dummies for testing and share test-cases as new branches in the respective repositories

Ideally the upstream is maintained by the „stewards“ of the respective language (e.g. https://github.com/rust-lang/rust; https://github.com/golang/example  ) to ensure that the „raw“ dummies (w/o modification) are in line with the build standards and avoid discussions/irritations.

## Benefit
A. Tool communities could use the Dummies to test against them => „golden repositories“ (in relation to „golden files“ e.g. https://medium.com/@jarifibrahim/golden-files-why-you-should-use-them-47087ec994bf )
B. Establish standardized processing independent from the technology

# Overview of existing dummy repositories
- GO-Dummy: https://github.com/Open-Source-Compliance/Go-Dummy 


# Dummy handling and maintenance
## Dummy repository standard setup
- „master“ stays the unchanged repository content from upstream
- Dummy-specific branches are added according to the following standard:
  - Three sub-branches: doc, demo and test 
    - doc – contains additional dummy-readme.md with detail-information about the demo and test-branches
      - E.g. detail description about demo/case_xxx 
      - rationale: as the master-branch shall be unmodified, the documentation needs to be in an extra branch
    - demo with potentially several cases e.g.
      - demo/case_xxx with xxx as ascending identifiers – description about the contents in the „doc“ branch
    - test with potentially several cases e.g.
      - test/tc_xxx with xxx as ascending identifiers – description about the details in the „doc“ branch
      - The test branches shall additionally contain a tc_xxx_spec.md-file with a tool-agnostic test-specification

Maintained by Open Chain Automation Workgroup.

# Setup for potential use for tool evaluation
- The dummy repository may be forked into the specific tool-project or evaluation setup with all branches, e.g. https://github.com/oss-review-toolkit 
- The dummy-specific branches are refined for the respective tool-/evaluation-context:
  - doc – branch may be enhanced with more detailed description
  - test with test-cases may be extended in the following way
    - test/tc_xxx stays unmodified input for the test-case to provoque a finding
    - test/tc_xxx_resolution may contain necessary tool-specific resolutions handle the provoqued finding in the special setup (e.g. by an additional .ort.yml-file in the root-folder in case of OSS-review toolkit).
    - test/tc_xxx_auto may contain test-automation scripts and accompanying documentation for reproducability (e.g. for Robotframework) to run the test automatically

Maintained by the respective tool-community.

# Re-use for tool installation/configuration check

- The tool-specific dummy repository may be used for installation checks
- Once the respective tool is set up and the infrastructure is running, the dummy may be used as input
- Comparing the results with the expected results will show if installation and configuration was correctly done

Maintained by yourself.


