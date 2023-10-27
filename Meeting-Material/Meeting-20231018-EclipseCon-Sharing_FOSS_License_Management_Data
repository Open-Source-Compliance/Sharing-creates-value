# Kick-off Meeting: Sharing FOSS License Management Data
Location: Ludwigsburg next to EclipseCon + Zoom

list of topics to discuss during the meeting:
- Context: Embedded Operating Systems
  - the main issue is hardware diversity and hardware integration -> no pre-packaged distributions, but Yocto-baked custom distros -> flexibility and complexity;
  - hardware support implies issues with proprietary licenses and patented technologies
- General Perspective
  - legal risk management - putting ourselves in the shoes of a device manufacturer that cannot avoid legal risks at any cost but should try to reasonably minimize them; improving viability of the product by solving upstream potential legal risks for customers
  - reusability and trustworthiness of compliance work is key, otherwise such work cannot be shared; reusability should work in both ways, i.e. we reuse others' work, too, if we trust it (eg. Debian). Using the same format (SPDX) is not enough, we need to share general principles and some common audit guidelines.
  - continuous compliance: automation is key, but automated processes should be consistently integrated with human audit process, in order to allow the latter to integrate with a continuous development process
  - upstream first: legal issues should be opened and solved upstream whenever possible
- What to scan: original upstream sources, coming from a known download location -> reusability in both ways (we can reuse others' work, others can reuse ours, even in different contexts from Yocto). This requires to trace source files back to their respective download location, which is not trivial with Yocto recipes mixing multiple upstream sources.
-	How we scan and audit source files
  -	handling non-code files, test and documentation files, binary blobs
  -	tagging proprietary licenses by category, based on a risk management perspective (eg. proprietary licenses with kill-switch clauses)
-	managing legal issues we find during the development process, using the same tools as developers (issues and PRs)
-	Still open legal issues, patent and other IP disclaimers are passed downstream with a notice to project users at release time
-	helping users/device makers in managing their OSS license obligations through a database of obligations: adjusting the detail level is key
