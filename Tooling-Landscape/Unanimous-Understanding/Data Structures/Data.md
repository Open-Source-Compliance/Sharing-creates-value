# Compliance workflow data collection
This data collection shall define all required data to implement a software compliance workflow taken company specific rules and policies into account.

## Build environment description
Sometimes a description of the build environment, which was used to build the software product, is required. This data type implements this. It is assumed that the description of the build environment qualifies a distinct deliverable. Like an embedded firmware image or a container(s) or simply a certain executable
### Defintion 
Name := String

Version := String

Unique Identifier := String (e.g. SHA Hash)

Text := textfield (the description itself)

## Content
This class is the representation of a certain piece of "software". It can be a binary package or a source package.
### Definition
Type := Enumeration { binary, other, source}

UniqueIdentifier := String

Artifact := Archive 

This is the "real" piece of "software"

## Constraint 
Contraints are requirements that have to be fulfilled. These are for example the obligations a license defines or constrains that products have to fulfill when they integrate other products. The design of an contstraint shall be in a way that a constraint can be defined in a specific company environment in accordance to the company specific poliy. On the other hand a constraint can also be made available via a publicly available resource. Besides a license or a product also ECC qualitication can define a certain constraint.
### Definition
Type := Enumeration { Exception, Obligation, Permission Resctriction, Risk, Other }

Unique Identifier := String (e.g. SHA Hash)

Name := String

Description := textfield 

Scope := Enumeration {distribution, modifications, usage, other}

This defines the context of the constraint. E.g. in case a certain information is required when doing modifications of the software 


### Examples
#### Example 1:
Type:Restriction 

UniqueIdentifier: SHA1

Name: restricted use

Description: cannot be used in nuclear facilities

Scope: usage

#### Example 2:
Type:Obligation 

UniqueIdentifier: SHA1

Name: disclosure document

Description: provide OSS disclosure document

Scope: distribution

#### Example 3:
Type:Other

UniqueIdentifier: SHA1

Name: Jurisdiction

Description: license determines the jurisdiction – US

Scope: other

## Data model meta information
This is the meta information of the model itself, like name, version, etc.
### Defintion
Name := String

Version := String

Unique Identifier := String (e.g. SHA hash)

## Deliverable
A deliverable implements a real deliverable of a product. A product can be made available in different formats, like as container(s), an executable, an image etc. The different options are modelled as deliverable
### Definition
Type := Enumeration {app, container, executable, firmware, image, other, service}

UniqueIdentifier := String

Name := String

Version := String

Description := textfield

DistributionModel := Enumeration

LicensingModel := Enumeration

RiskExposure := Enumeration

DeliveredItem := SwBundle

## Digital Artifact 
A digital artifact represents an distinct identifiable part of a product, i.e. an element of the bill of material. It can be an OSS pacakge, a commercial library, a cerain font, an icon, a picture, a called 3rd party service. Especially in case of mobile apps these artifacts have to be taken into account.
### Definition
Type := Enumeration{ commercial, icon, internal, font, graphic, oss, service, other }

Unique Identifier := String (e.g. SHA Hash)

Name := String

Version := String

Unique Identifier Source (e.g. SHA Hash) := String

isModified := Boolean

Source Code package := set of Content

Binary package := set of Content

General license assessment := textfield (this textfield is foreseen to provide an overview about the license situation of the package, like an executive summary)

Licenses := set of License

Copyright information := set of CopyrightECCInformation

ECC information := set of CopyrightECCInformation



## Disclosure document
The disclosure document is often named as OSS delcaration or OSS disclosure document or ReadME_OSS
### Definition
Name := String

Version := String

Unique Identifier := String (e.g. SHA Hash)

LegalWording := textfield

ContactData := textfield (in case a contact for any request, like source code is present)

Integrated 3rd party artifacts :=

	set of
	
		DigitalArtifact.Name
	
		DigitalArtifact.Version
	
		set of 
			License.Name
		
			License.SPDX short Identifier
		
			License.Acknowledgement
		
			License.Text
		
		DigitalArtifact.CopyrightECCInformation
		

## License
The license data model is based on the current SPDX definition of a license, the SPDX specification itself is licensed und CC-BY-3.0. The SPDX license definiton lacks from a compliance process point of view some data which are important to implement an integrated compliance workflow taking care of company specific requirements. This defintion has the purpose to provide such abbtional data.
### Definition
Name := String

Unique Identifier :=String (e.g. SHA hash)

SPDX short Identifier := String

Risk level := Enumeration { 1,2,3,4,5}

Cathegory := Enumeration {commercial, other, permissive, limited-copyleft, restrictive, strong-copyleft, ultra-strong-copyleft} 

Acknowledgement := String

OSI-approved := Enumeration {yes, no, unknown}

Text := textfield (this is the text of the license)

Characteristics := set of Constraint

Notes := textfield

References := set of URLs

Standard-header := textfield

### Examples
#### Example 1:
Name: GPL-2.0 

UniqueIdentifier: SHA1

SPDX short identifier: GPL-2.0

Risk level: 3

Cathegory: strong-copyleft

OSI-approved: yes

Text: GPL-2.0 text

Characteristics:

contstraint1; constraint2; constraint3

Notes: any company or public available information

References:
https://www.gnu.org/licenses/old-licenses/gpl-2.0.de.html

Standard-header:

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.



## Productinformation
This data type defines is the meta information of a specific product. A product in this context can be everything a company makes available to 3rd parties. Note that a product can consist of other products, which may introduce certain constraints to the integrating product.
### Definition
Name := String

Version := String

Unique Identifier := String (e.g. SHA Hash)

Description := textfield (short description of the product itself)

Development details := textfield

Constraints to be handled by the using/integrating project := set of Constraint

Criticality := Enumeration {0,1,2,3,4,5}

Integrated DigitalArtifacts := set of DigitalArtifacts

ECC qualification := set of CopyrightECCInformation

Deliverables := set of Deliverable

## SwBundle
This represents the real item which is made available to 3rd parties,e.g. it is the executable, which is made available to 3rd parties.
### Definition
Type := Enumeration

Items := set of Content





