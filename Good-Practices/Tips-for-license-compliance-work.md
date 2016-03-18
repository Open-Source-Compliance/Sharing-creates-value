This file contains useful tips and answers to questions, which raise during the daily work in the context of OSS license compliance. 


Question or Problem:
--------------------
I need to make use to the "or (at your option) any later version" in the LGPL, GPL, MPL, how do I do that in a license compliant way?
The following scenario shall illustrate the question:

There is a library all the source files it consists of carry the following license information:
 
“This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.”
 
The COPYING file contains the text of the LGPL-2.0
 
For some reason it is necessary for me to use the library under the terms of LGPL-2.1, I cannot use the library under the terms of LGPL-2.0. So I need to “upgrade” the license from LGPL-2.0 to LGPL-2.1. 
How can I do this?


One way to go:
------------------
1. In case of LGPL / GPL licensed files, check whether all relevant files carry a statement whether you are allowed to use a later version of the license (like the standard header above).
Assuming that the result of the check is that all relevant files carry such a statement, proceed like follows:
2. Add the text of the LGPL-2.1 to the library (e.g. as COPYING-LGPL-2.1)
3. Keep the text of the LGPL-2.0 in the library (the COPYING file)
4. Provide the required material (complete corresponding source code, etc.) to the downstream users accompanied with a written note in the context of the library like:
"To the extend files are licensed under LGPL-2.0 or at your option any later version, in this context LGPL-2.1 has been chosen. Please take a look at COPYING-LGPL-2.1. This shall not restrict the freedom of other users to choose either LGPL-2.0 or at their option any later version.”

For MPL licensed software the procedure is very similar, the main difference is that the license text of the MPL (at least I have checked it for version 1.1 and 2.0) allows the use of a newer version of the license per default (for further details see remarks). Which means that you have to check the relevant (source) files, if there is a statement made by the original author that disallows the use of a newer version of the MPL.
Assuming that the result of the check is that no file carries such a statement, proceed like follows:
2. Add the text of the version of the MPL you want to use to the software (e.g. as COPYING-MPL-2.0)
3. Keep the text of the former version of the MPL in the software (e.g in the COPYING file)
4. Provide the required material to the downstream users accompanied with a written note in the context of that software:
"To the extend files are licensed under MPL-1.1, in this context MPL-2.0 has been chosen in accordance with section 6.2 of the MPL-1.1. This shall not restrict the freedom of other users to choose either MPL-1.1 or at their option any later version.”

Remarks / Explanations:
-----------------------

Why is it done this way:
Because I have to check whether the original author allows me to use an successor version of the License he has chosen, due to this step 1. is required.
Secondly I do not want to take away the freedom of people wanting to use the software under the elder (original) version of the license but I have to state clearly that *I* distribute the software under a newer version of the license.
Last but not least, only sending the original license text, without adding the text of the version I use, will cause a license compliance problem. Because when I choose the newer version of the license I am bound to the obligations of the newer license and thus I have to provide the license text of the newer license, too. 

References from some Licenses for more detail:

Section 13 of the LGPL-2.1:
"Each version is given a distinguishing version number.  If the Library
specifies a version number of this License which applies to it and
"any later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation.  If the Library does not specify a
license version number, you may choose any version ever published by
the Free Software Foundation."

The text of the LPGL-2.1 is available at: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
The Free Software Foundation, Inc. holds the copyright of the LGPL-2.1



Section 6.2 of the MPL-1.1
"Once Covered Code has been published under a particular version of the
License, You may always continue to use it under the terms of that
version. You may also choose to use such Covered Code under the terms
of any subsequent version of the License published by Netscape. No one
other than Netscape has the right to modify the terms applicable to
Covered Code created under this License."

The text of the MPL-1.1 is available at: https://www.mozilla.org/media/MPL/1.1/index.0c5913925d40.txt


Section 10.2 of the MPL-2.0
"You may distribute the Covered Software under the terms of the version of the License under which You originally received the Covered Software, or under the terms of any subsequent version published by the license steward."

The text of the MPL-2.0 is available at: https://www.mozilla.org/en-US/MPL/2.0/
