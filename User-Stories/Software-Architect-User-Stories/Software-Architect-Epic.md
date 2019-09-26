## Software Architect Epic
This epic describes briefly the role, responsibilites, tasks and how the software architect interacts with the toolchain in order to accomplish his tasks in an efficient way.

## Responsibilites, Tasks and Role
As a software architect I am responsible for the overall architecture of the software (sub)system. I decide on the to be used technology, the subsystems, the composition of the subsystems, their interfaces and the orchestration of them. I also oversee the selection and integration of OSS and other 3rd party components with the objective that they are inline with the company and product specific policies, whether they are suited for the specific product or service and whether the licenses of those components define additional requirements.
My goal is to build a system consisting of independent sub-systems that are easy to test and maintain. In regard to the integrated 3rd party components my goal is that they enjoy the required maturity, define only very little additional requirements for the products /serices and that the intended usage does not raise conflicts.

## Epic
As a software architect I want to have always an up to date overview of the integrated 3rd party components per sub-system and for the entire system this includes all dependencies. The overview shall provide the following data:
* component name and version
* All applicable licenses in the current use case
* Whether there are parts which violate the product or company policy (in terms of licenses, copyright holders, maturity, security vulnerabilities, etc.). If there are parts which contradict the defined policies I want to see immediately the reason and the file(s)
* The interaction of the components enriched with license information
* An per component as well as an agreggated view of all obligations, restrictions and risks of the applicable licenses in the scope of the distribution and licensing models of the product / service

Whenever there is a component integrated/removed or updated I want to have a complete overview what changed in respect to the above mentioned data in the specific sub-systems and in respect to the entire system, e.g. which licenses were removed, which were added and all the related data e.g. the now appicable obligations, restrictions and risks in the scope of the distribution model.
I also want to see all obligations, restrictions and risks I as a software achritect have to take care of and to fulfill.

So that I can immediately notify the developres when a component integration or update causes any problem and work with them on the solution.  In case of obligations, restrictions and risk I have to care for I want to have an easy way to acknowledge that I have taken care of and how I satisfied the obligation,restriction or risk

