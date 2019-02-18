# Compliance workflow data collection
This data collection shall define all required data to implement a software compliance workflow taken company specific rules and policies into account.

## Build environment description
Sometimes a description of the build environment, which was used to build the software product, is required. This data type implements this.
### Defintion 
#### Name
String
#### Version
String
#### Unique Identifier 
String (e.g. SHA Hash)
#### Text
textfield (the description itself)


## Constraint 
Contraints are requirements that have to be fulfilled. These are for example the obligations a license defines or constrains that products have to fulfill when they integrate other products. The design of an contstraint shall be in a way that a constraint can be defined in a specific company environment in accordance to the company specific poliy. On the other hand a constraint can also be made available via a publicly available resource
### Definition
#### Type
Enumeration { Exception, Obligation, Permission Resctriction, Risk, Other }
#### Unique Identifier 
String (e.g. SHA Hash)
#### Name
String
#### Description
textfield 
#### Scope
This defines the context of the constraint. E.g. in case a certain information is required when doing modifications of the software 
enumeration {distribution, modifications, usage, other}

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
#### Name
String
#### Version
String
#### Unique Identifier
String (e.g. SHA hash)

## Disclosure document
The disclosure document is often named as OSS delcaration or OSS disclosure document or ReadME_OSS
### Definition
#### Name
String
#### Version
String
#### Unique Identifier 
String (e.g. SHA Hash)
#### Text
textfield (the content of the document)
#### Contact Data
textfield (in case a contact for any request, like source code is present)
#### Integrated 3rd party artifacts

	set of
	
		Integrated 3rd party software.Name
	
		Integrated 3rd party software.Version
	
		set of 
			License.Name
		
			License.SPDX short Identifier
		
			License.Acknowledgement
		
			License.Text
		
		Integrated 3rd party software.Copyright information
		

## License
The license data model is based on the current SPDX definition of a license, the SPDX specification itself is licensed und CC-BY-3.0. The SPDX license definiton lacks from a compliance process point of view some data which are important to implement an integrated compliance workflow taking care of company specific requirements. This defintion has the purpose to provide such abbtional data.
### Definition
#### Name
String
#### Unique Identifier
String (e.g. SHA hash)
#### SPDX short Identifier
String
#### Risk level
enumeration { 1,2,3,4,5}
##### Cathegory
enumeration {commercial, other, permissive, limited-copyleft, restrictive, strong-copyleft, ultra-strong-copyleft} 
##### Acknowledgement
String
##### OSI-approved
enumeration {yes, no, unknown}
#### Text
textfield (this is the text of the license)
#### Characteristics
set of Constraint
#### Notes
textfield
#### References
set of URLs
#### Standard-header
textfield

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
#### Name
String
#### Version
String
#### Unique Identifier 
String (e.g. SHA Hash)
#### Description
textfield (short description of the product itself)
#### Distribution model (distribution shall not be taken literally)
enumeration { distribution, HW-SW-Bundle, other, SaaS }
#### Development details
textfield
#### Constraints to be handled by the using/integrating project
set of Constraint
#### integrated artifacts
set of Integrated 3rd party software


## Integrated 3rd party software 
Integrated 3rd party software shall not to be taken literally. An integrated 3rd party software it can also be services provided by 3rd parties or graphics or fonts, etc. Especially in case of mobile apps these artifacts have to be taken into account.
### Definition
#### Type
Enumeration { commercial, internal, oss, service, Other }
#### Unique Identifier 
String (e.g. SHA Hash)
#### Name
String
#### Version
String
#### Unique Identifier Source (e.g. SHA Hash)
String
#### Source Code package
file (it is an archive)
#### Unique Identifier Binary (e.g. SHA Hash)
String
#### Binary package
file
#### Component license assessment
##### General Assessment
textfield (this textfield is foreseen to provide an overview about the license situation of the package, like an executive summary)
##### Licenses
set of License
##### Constraints
set of Constraint
##### Copyright information
set of String
##### ECC information
set of String




