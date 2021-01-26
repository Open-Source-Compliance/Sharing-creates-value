# OSS Based Tooling Group Meeting

## Location

BMW Car IT, Moosacher Str. 86, Muenchen, Germany

online: circuit://circuit.siemens.com/guest?token=1c2527a2-444e-4dc0-ab68-7be8bd8efcb4

## Attendees

In the room, in seating order:

| Person | e-mail |
| --- | --- | 
| Helio | helio.chissini-de-castro@bmw.de |
| Oliver | oliver.fendt@siemens.com |
| Monika | monika.schnizer@ts.fujitsu.com |
| Marcel | marcel.kurzmann@bosch-si.com  |
| Lars | lars.geyer-blaumeiser@bosch-si.com |
| Michael P. | michael.picht@sap.com |
| Stefan | stefan.gustafsson@sap.com |
| Lennart | Lennart.Seck@bmw.de |
| Thomas | thomas.steenbergen@here.com |
| Martin | Martin.vonWillebrand@hhpartners.fi |
| Klaus | Klaus.Gmeinwieser@oce.com |
| Andreas | a.isenmann@vega.com |
| Michael | michael.c.jaeger@siemens.com |
| Peter | Peter.Ellsiepen@esa.int |

On telco, via conf call:

| Person | e-mail |
| --- | --- | 
| Gergei | gergely.csatari@nokia.com |
| Hama Kouka | kouki1.hama@toshiba.co.jp |
| Maximilian | maximilian.huber@tngtech.com |
| Takuya Koda | takuya.koda@toshiba.co.jp |
| Anton Kharitonov | (SAP) |

# Agenda and Action Items


## Agenda

(see slides)

* Introduction
* Updates on Tools
* Questions on Tools
* Website and Wiki
* Lunch
* Data Model
* Other Tooling Efforts
* Closing

## Action Items

| Volunteering Person | Item |
| --- | ---| 
| Marcel | good practise / example process documentation  |
| Marcel  | BMPN notation of sequence diagrams |
| Michael P.  | make big picture terminology OpenChain compliant | 
| Peter and Andreas  | volunteer to review the existing material: "unanimous understanding" after it has been updated |
| Oliver | volunteers to provide a website |
| All | (not really action item but suggestion) vote for Marcel's and Lars' submission to EclipseCon Europe Oct 2019 |
| Oliver  | Review SPDX Spec for updating the data model terms |

# Notes on the Meeting

(raw notes from notable items from discussion)

## Introduction

* 0935 general introduction to the location
* 0940 Starting introduction of every participant
* 0958 Presentation and discussion of the agenda
* Question: What about involving security persons from the security community?
* Answer: Vulas has been presented at previous meetings, three companies are in contact with their security colleagues about OSS based compliance tooling. Generally, this effort is open to persons from sec domain

## Updates on Tools

* 1013 CLA Assistant
  * CLA Assistant was remote so the questions were added directly at the meeting
  * Question: why does it make sense to have own instance? Answer: to own the data, customize appearance
  * Question: is it also going with gitlab? Answer: maybe, not supported now
  * Question: CLA acceptance data ... depending in 10 years  in export possible? Answer: UI for export is there, and export of list, but no general dump, note there is no SLA from the OSS project)
* 1034 License Metadata Mining
  * new project at github.com/maxhbr/LDBcollector
* 1040 Eclipse SW360
* 1046 Eclipse SW360 Antenna
* 1052 LF's FOSSology
* 1058 Open Source Review Toolkit

## Tools Question and Answers

(see picture)

## Lunch

* going out of room at 1224
* Website topic postponed

## Website and Wiki

* start at 1350
* brief discussion about enrolling new members and its mode: keep it, no concerns

## Dissemination Activities

* Past: presenting the LLW of FFSFE workshop in April 2019 in Barcelona
* Question: what are TODO resulting from the meeting -> suggestion is to have more process view on the oss license compliance
* Proposed to have a non-siemens slide deck.
* Proposal: agree on a common slide deck for joint tooling efforts
* Proposal: work on the reference tool chain (again)
  * expressing need for having a reference tool chain
  * Action item good practise / example process: volunteering: Marcel
  * Action item BMPN notation of sequence diagrams: Marcel
  * Action item make big picture terminology OpenChain compliant: Michael P.
  * Peter and Andreas volunteering to review the exiting material: "unanimous understanding"
  * Oliver: review SPDX Spec for updating the data model terms

* Suggestions: EclipseCon does voting so there could be an opportunity to do some voting for the talks for Lars and Marcel.

## Data Model Discussion

* start at 1448 
* discussing issue #48 on the sharing-creates-value repo (https://github.com/Open-Source-Compliance/Sharing-creates-value/issues/48)
* same for issue #47 (https://github.com/Open-Source-Compliance/Sharing-creates-value/issues/47)
* discussing the data model in general: how to deal with individual attributes if they get too fine grained
* discussion: about what could be shared or what could be reused, how is it reflected in the picture?
* first of all: main rationale is "data model is capable for implementing an end to end compliance workflow"
* Question about the copyright and ECC information: is there a particular file? -> not yes existing
* Discussing for example the flexibility of the copyright / ECC part fits in
* Question: how to deal with many artefacts ...?
* Question: is there is a SPDX artefact somewhere covered, how to translate this into the model -> not all, disclosure document
* Action Item Oliver: review SPDX Spec for updating the data model terms
* Question data model discussion: is there license compatibility problem covered? (lead to discussion about)
  * in the model it is not checked, discussion points out that lic compatibility bears the problem, to understand the actually required dependencies
  * suggestion is to have such information as "deliverable", but lik style is missing, which is relevant Here
  * disclosure document would be a result (deliverable), assessment result should be defined in the mode somehow
* concluding that this data model to have this as the kernel for tooling, and then the process,

## Double Open

* separate presentation at 1552
* "double open": open open source compliance
* funded by Finland gvmnt grant
* discussion about yocto and it would be nice to have SPDX generation to it (noting that some individual solutions exist)
* proposing also to look into the civil infrastructure platform (Debian based) for testing.
* mentioning alternative projects to yocto: buildbot and elbe

## More Tooling Efforts

* start at 1622
* OpenChain turn key compliance solution
* OpenChain persons is willing to drive the open source tool chain inside the open chain project
* interest observed among members in Asia

## Wrap Up

1628 Closing and Wrap up

* closing: asking first time attendees for feedback
  * good to see that others share same problems and it is worth to have such group
* Next meeting time: two weeks before EclipseCon Europe 2019
* next meeting location: Three volunteers, order set, waiting for first party to clarify