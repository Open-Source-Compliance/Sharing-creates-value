## Compliance Assistant Epic
This epic describes briefly the role, responsibilities, tasks and how the compliance assistant interacts with the toolchain in order to accomplish his tasks in an efficient way.

## Responsibilites, Tasks and Role
As a compliance assistant I am responsible for the clearing of integrated 3rd party software components in a specific application. I am further in charge of the clearing of an entire application. 

During the clearing of components (can be source code, images, fonts, etc.) I identify the applicable licenses, the copyright strings and the required acknowledgements. License identification require sometimes searching in the internet about the licenses which apply to certain files. Whenever this is required the way how the particular license was concluded is documented. Based on the identified licenses I provide an overall summary about the license situation of the component.

Application clearing is the process where the licenses of all integrated 3rd party components or used 3rd party services are evaluated and the fulfillment of the license obligations is documented and associated risks are mitigated. The delivery model of the application is taken into acoount when the license obligation fulfillment is documented (different delivery models may require a different kind of obligation fulfillment). During this task also the compliance artifacts are generated. 

My goal is to provide high quality clearing data as fast as possible in order to give the developers of the applications as soon as possible feedback whether the components they have integrated cause problems or not. In order to be efficient all trivial cases shall automatically be identified by tools, and only in cases where the tools can not finally identify the license I have to interact with the tools.


## Epic
As a compliance assistant I want to provide the entire licensing information of integrated 3rd party components with very short delay after they have been integrated. The tools I am interacting with point me directly to those licenses which could not be determied by the tools. Further the tools present me information when organization policies or application policies are violated and the root cause of the violation, so that I can provide all required information in nearly real time to the development staff and discuss possible solutions with the architects. Since components are updated frequently due to security requirements the tools store all my activies I have carried out during license identification and provide a means to replay them on newer versions of the component in order to avoid duplicated effort.

During application clearing also all tasks are stored so that these including all the texts written during application clearing can be applied to newer versions of the application. This reduces the manual effort to the minimum.
