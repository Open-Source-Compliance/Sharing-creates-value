# Compliance workflow data collection
This data collection shall define all required data to implement a software compliance workflow taken company specific rules and policies into account.

## Build environment description
Sometimes a description of the build environment, which was used to build the software product, is required. This data type implements this. It is assumed that the description of the build environment qualifies a distinct deliverable. Like an embedded firmware image or a container(s) or simply a certain executable

### Defintion
name := String

version := String

uniqueIdentifier := String (e.g. SHA Hash)

text := Textfield (the description itself)

## Content
This class is the representation of a certain piece of "software". It can be a binary package or a source package.

### Definition
type := Enumeration { binary, other, source}

uniqueIdentifier := String (Typically the hash code of the artifact, to identify it uniquely)

artifact := Archive (E.g. a Jar-File containing the content)

externalSource := URL (Link to the external artifact source)

internalSource := URL (Link to the internal storage of the artifact)

softwareHeritageSource := URL (Link to the tag basis of the content in Software Heritage)

This is the "real" piece of "software"

## Constraint
Contraints are requirements that have to be fulfilled. These are for example the obligations a license defines or constrains that products have to fulfill when they integrate other products. The design of an contstraint shall be in a way that a constraint can be defined in a specific company environment in accordance to the company specific poliy. On the other hand a constraint can also be made available via a publicly available resource. Besides a license or a product also ECC qualitication can define a certain constraint.

### Definition
type := Enumeration { Exception, Obligation, Permission Resctriction, Risk, Other }

uniqueIdentifier := String (e.g. SHA Hash)

name := String

description := Textfield

scope := Enumeration {distribution, modifications, usage, other}

This defines the context of the constraint. E.g. in case a certain information is required when doing modifications of the software

### Examples

#### Example 1:
type:Restriction

uniqueIdentifier: SHA1

name: restricted use

description: cannot be used in nuclear facilities

scope: usage

#### Example 2:
type:Obligation

uniqueIdentifier: SHA1

name: disclosure document

description: provide OSS disclosure document

scope: distribution

#### Example 3:
type:Other

uniqueIdentifier: SHA1

name: Jurisdiction

description: license determines the jurisdiction – US

scope: other

## CopyrightECCInformation

This is a representation of additional information like copyrights or ecc information
### Definition
type := Enumeration { copyright, ecc }

content := Textfield

## DataModelMetaInformation
This is the meta information of the model itself, like name, version, etc.

### Defintion
name := String

version := String

uniqueIdentifier := String (e.g. SHA hash)

## Deliverable
A deliverable implements a real deliverable of a product. A product can be made available in different formats, like as container(s), an executable, an image etc. The different options are modeled as deliverable

### Definition
type := Enumeration {app, container, executable, firmware, image, other, service}

uniqueIdentifier := String

name := String

version := String

description := Textfield

distributionModel := Enumeration

licensingModel := Enumeration

riskExposure := Enumeration

## Disclosure document
The disclosure document is often named as OSS declaration or OSS disclosure document or ReadME_OSS

### Definition
name := String

version := String

uniqueIdentifier := String (e.g. SHA Hash)

legalWording := Textfield

contactData := Textfield (in case a contact for any request, like source code is present)

## Digital Artifact
A digital artifact represents an distinct identifiable part of a product, i.e. an element of the bill of material. It can be an OSS pacakge, a commercial library, a cerain font, an icon, a picture, a called 3rd party service. Especially in case of mobile apps these artifacts have to be taken into account. In SPDX this is called a Package.

### Definition
type := Enumeration{ commercial, icon, internal, font, graphic, oss, service, other }

uniqueIdentifier := String (e.g. SHA Hash)

name := String

version := String

homepage := URL (e.g. Project Homepage)

isModified := Boolean

generalLicenseAssessment := Textfield (this textfield is foreseen to provide an overview about the license situation of the package, like an executive summary)

## Coordinates
This class represents the coordinates of a DigitalArtifact in a certain technology, i.e., the typical reference of a unique component version in this technology. E.g., maven coordinates for a component on maven central.

### Definition
coordinate := String

## LicenseExpression
Representation of a SPDX license expression that combines a set of licenses to the licenses expression attached to a DigitalArtifact

### Definition
uniqueIdentified := String

licenseExpression := String (An SPDX licenses expression stored as String, uses the SPDX short identifier to reference a license)

## LicenseSelector
Property of the usage of a DigitalArtifact in a Deliverable, used to express the used licenses in cases where a DigitalArtifact allows license selection.

### Definition

## License
The license data model is based on the current SPDX definition of a license, the SPDX specification itself is licensed und CC-BY-3.0. The SPDX license definiton lacks from a compliance process point of view some data which are important to implement an integrated compliance workflow taking care of company specific requirements. This definition has the purpose to provide such abbtional data.

### Definition
name := String

uniqueIdentifier :=String (e.g. SHA hash)

spdxShortIdentifier := String

Risk level := Enumeration { 1,2,3,4,5 }

category := Enumeration {commercial, other, permissive, limited-copyleft, restrictive, strong-copyleft, ultra-strong-copyleft}

acknowledgement := String

osiApproved := Enumeration {yes, no, unknown}

text := Textfield (this is the text of the license)

notes := Textfield

references := set of URLs

standardHeader := Textfield

### Examples
#### Example 1:
name: GPL-2.0

uniqueIdentifier: SHA256

spdxShortIdentifier: GPL-2.0-only

riskLevel: 3

category: strong-copyleft

osiApproved: yes

text: GPL-2.0 text

notes: any company or public available information

references: [https://www.gnu.org/licenses/old-licenses/gpl-2.0.de.html]

standardHeader:

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

## ProductInformation
This data type defines is the meta information of a specific product. A product in this context can be everything a company makes available to 3rd parties. Note that a product can consist of other products, which may introduce certain constraints to the integrating product.

### Definition
name := String

version := String

uniqueIdentifier := String (e.g. SHA Hash)

description := Textfield (short description of the product itself)

criticality := Enumeration {0,1,2,3,4,5}

developmentDetails := Textfield

## SwBundle
This represents the real item which is made available to 3rd parties,e.g. it is the executable, which is made available to 3rd parties.

### Definition
type := Enumeration

Items := set of Content
