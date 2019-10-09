## Use case overview for turnkey Open Source Management Solution

---
### Generic use cases
- UC_G01 [Feed_input_material_into_the_system](./feed_input_material_into_the_system.md)
  
--- 
### Review for usefulness and quality (UQ)
> from Open Chain Curriculum (https://github.com/OpenChain-Project/curriculum/raw/master/slides/openchain-curriculum-for-2-0.pdf) page 42:
>> "After Program and Product Management and Engineers have reviewed proposed Open Source components for usefulness and quality, ..."

#### Engineering specific use cases
- UC_E01 [get_fast_feedback](./get_fast_feedback.md) 
- UC_E02 [create_bill-of-materials](./create_bill-of-materials.md) 
- UC_E03 [query_available_metadata_for_specific_foss_component](./query_available_metadata_for_specific_foss_component.md) 
- UC_E04 [trigger_foss_contribution](./trigger_foss_contribution.md) 

#### Product / Program Manager specific use cases
- UC_P01 [initiate_new_project_in_the_system](./initiate_new_project_in_the_system.md) 
- UC_P02 [generate_foss_compliance_bundle](./generate_foss_compliance_bundle.md) 
- UC_P03 [prepare_distribution](./prepare_distribution.md) 
  
---
### Review of the rights and obligations (RO)
> from Open Chain Curriculum (https://github.com/OpenChain-Project/curriculum/raw/master/slides/openchain-curriculum-for-2-0.pdf) page 42:
>> "... a review of the rights and obligations associated with the use of the selected components should be initiated"
>> "... The Open Source Review process includes the following steps:
>> - Gather relevant information
>> - Analyze and understand license obligations
>> - Provide guidance compatible with company policy and business objectives
>> "

#### FOSS Review Team specific use cases
- UC_F01 [trace_applications_containing_specific_foss_component](./trace_applications_containing_specific_foss_component.md)
- UC_F02 [trace_foss_components_in_applications](./trace_foss_components_in_applications.md)
- UC_F03 [monitor used components for deficiancies](./monitor_used_components.md)


##### Legal
- UC_L01 [maintain_company_policies](./maintain_company_policies.md)
- UC_L02 [maintain_org-specific_license_interpretations](./maintain_org-specific_license_interpretations.md)

##### Scanning
- UC_S01 [curate_component_metadata](./curate_component_metadata.md)
- UC_S02 [maintain_org-specific_metadata_for_foss_projects](./maintain_org-specific_metadata_for_foss_projects.md)

##### Expert
e.g. Security, Export Control, Quality,...
- Variants of above