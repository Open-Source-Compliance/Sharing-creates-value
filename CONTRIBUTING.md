## Introduction

We welcome contributions via
[pull requests](https://help.github.com/articles/about-pull-requests/) filed against
[our repository](https://github.com/Open-Source-Compliance/Sharing-creates-value). A contribution can be code, bugfixes, documentation, presentation or any other content. 

In order to be clear - we will not accept any pull request which deals with proprietary tools. In case you are not sure what this means please check the README file in the root directory of this project.

## Signing each commit

We do not require a CLA to be signed by you, we follow the more lightweight DCO (Developer Certificate of Origin) approach. A DCO is a way for a contributor to confirm that he/she wrote or otherwise has the right to submit code or documentation to a project. Simply add `Signed-off-by` as shown in the example below to indicate that you agree with the DCO. Only signed off PRs will be accepted

You can find the text of the [DCO here](https://developercertificate.org/ ) 

An example signed commit message:

```
    Data Structures: Add attributes to class xyz
    Signed-off-by: Cary Carlson <cary.carlson@someorg.org>
```

## Rules you should care about

We have defined only very few rules how your commits shall look like and how they shall be phrased:

  * Make separate commits for logically separate changes
  * Provide meaningful commit messages
  * Describe your changes well and in imperative
  * To resolve conflicts, rebase pull request branches onto their target branch 
  * please make sure that your contributions are [REUSE](https://reuse.software/) conformant
 
For reuse conformance please provide the following information in every new file you intend to contribute:
```
# SPDX-FileCopyrightText: 2020 name of Copright owner
# SPDX-License-Identifier: License you have chosen
```
In case you contribute binaries, like pictures etc., check for the reuse best practice for binaries.
 
If you want to learn more the git project provides very good documentation about [how to submit patches](https://github.com/git/git/blob/master/Documentation/SubmittingPatches)
