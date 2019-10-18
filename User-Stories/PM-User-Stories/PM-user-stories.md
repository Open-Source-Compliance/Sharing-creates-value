#Project Manager (PM) user stories
We assume this role as a principal role compared to a developer. Thus this player has the right to task the developer (agent) and influences the priotization of the agents work. Typically such a role is a team lead or project manager or in modern words a product owner. For ease of read, we will title the role PO, konwing that this simplification will not cover all details associated with the different role models. But from a compliance perspective the models can be treated as equivalent.

##Responsibilites, tasks and role
The ```primary goal``` of this role is to deliver a software solution while minimizing all related risks. This may comprise security, export controls or the incompliance with obligations resulting from the application of open source components. 

Thus this role will be ```accountable``` for:
* Execution of all reuired tasks to provide a risk minimized software solutions
* Arrange and provide all relevnat tasks to cope with resulting obligations
* Completeness of files/data/code to be assessed and delivered within the scope of this project

This typically results in the follwing ```tasks```:
* Ensure code is scanned for composition on a regular basis - optimally as part of the CI/CD-chain
* Ensure that _all_ components _and_ resources comprised within the solution will be captured/covered by the scans (incl. runtime components)
* Initiate appropriate measures to cope with obligations and provide associated documentation
* Initiate measures to cope with violations and warnings
* Initiate approval requests
* Escalate questionnable components/licenses to Compliance Manager/OS board

Therefor the most ```critical success factors``` of theis role are:
* Understanding of the Open Source Policy
* Willingness to provide a proper and sound documentation (at min. composition and compliance, some cases (e.g. MDD) might require even backgrounds, supplier data, usage scenarios, etc.)
* Determine the legal circumstances to correctly interpret the legal obligations resulting from open source usage

This role does not have a direct report in this scenario. A kind of dotted line mihgt be the associated ```Compliance Manager``` for the project, because these two should work together where the Compliance Manager finally has to confirm compliance. Thus this role naturally has some authority over the PM. To overcome discrepancies between Compliance Manager and PM, it is suggested to escalate to the ```Open Source Board```

The role has a strong dependency towards the ```Open Source Policy``` and the provided ```Tooling Environment```. For this exercise, we may assume a tooling chain like the one proposed will be available.

In a real life environment, this role may be taken by any of the following role models:
* Product Manager
* Product Owner
* Project Manager
* SCRUM Master
* Dev-Team Manager
* Senior Developer

## Epic
As a PM 
I want my product to be compliant
so that neither my team nor my organization will face any problems resulting from unwanted or unattended open source usage

###UC0#1: Provide architecture overview of solution

###UC#02: Ensure continuos scanning of new components (CI/CD integration)

###UC#03: Ensure completeness of components covered

###UC#04: Determine legal cricumstances

###UC#05: Determine resulting obligations

###UC#06: Ensure obligations will be met / provide documentation

###UC#07: Initiate resolution of conflicts

###UC#08: Escalate unclear or critical aspects

###UC#09: Ensure confirmation from legal side (approval)


