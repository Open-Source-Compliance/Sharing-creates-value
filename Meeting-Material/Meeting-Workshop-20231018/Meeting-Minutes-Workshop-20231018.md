# Sharing FOSS Compliance Metadata

Oct.18, 2023 - EclipseCon - Ludwigsburg

The aim is to establish a common ground to be able to share FOSS compliance metadata, regardless of the specific tools used to produce them, focusing on  audit process and audit criteria, in order to create a common pool of trusted and consistent data.

## Context: distribution of embedded operating systems

Peculiar issues with respect to other contexts (eg. distribution of applications, libraries, etc.):

- high number of **third party components**;

- **hardware diversity and hardware integration**: Yocto: no pre-packaged distributions, but Yocto-baked custom distros -> flexibility and complexity;

- hardware support implies frequent issues with **proprietary licenses** and **patented technologies**

## General perspective

- **legal risk management**, putting ourselves in the shoes of a device manufacturer who wants to reasonably minimize risks; improve viability of FOSS products and platforms:
  - by **solving upstream potential legal risks** for users;
  - by **spotting possible issues** that cannot be solved upstream and **collecting relevant information** to enable users (and their legal teams) to make **informed decisions** on such issues (criteria and policies to make legal decisions may vary across organizations, but they all need the same information);

- **reusability** and **trustworthiness** of compliance work is key, otherwise such work cannot be shared; reusability should work in both ways, i.e. we reuse others' work, too, if we trust it (eg. Debian). Using the same format (SPDX) is not enough, we need to share general principles and some common audit criteria and guidelines;

- **continuous compliance**: **automation** is key, but automated processes should be consistently **integrated** with **human audit process**, in order to allow the latter to integrate with a **continuous development process**;

- **upstream first**:
  - legal issues should be opened and solved upstream whenever possible
  - ideally, compliance metadata should be made available by the upstream, so we should push for REUSE standard adoption by the upstream as much as possible, also by (automatically?) opening PRs to add REUSE compliance metadata, as long as we produced that information; but this is a long-term solution.

## What to scan and how

### What to scan, and information we need to collect from the build system

- original upstream sources, coming from a known download location -> reusability in both ways (we can reuse others' work, others can reuse ours, even in different contexts from Yocto). This requires to trace source files back to their respective download location, which is not trivial with Yocto recipes mixing multiple upstream sources;

- binary packages/files built from sources: we need to map binary artifacts to their respective source files (and licenses), because different binary packages/files built from the same source may have different licenses

### How we scan and audit source files

- human validation (with some tool) is needed; the focus is not on the tool but on the results

- handling non-code files, test and documentation files, binary blobs

- handling non-SPDX licenses: a solution would be to adopt [Scancode license tags](https://scancode-licensedb.aboutcode.org/) but we should also push the SPDX team to expand their license list; in any case, even when using scancode license db tags, complete license text should be always included

- produce "layered" metadata:

  - first layer: just validated license tags and copyrights

  - second layer: information useful to interpret metadata and to make decisions on possible legal issues; license interpretation and classification, as well as handling of legal issues generally is organization-specific, but we should provide information to enable organizations to do these activities (eg. we may report proprietary licenses with kill-switch clauses, patent warnings, etc.; then it is up to each organization to assess the risk and make decisions based on such information);

  - third layer: reduce complexity due to license diversity (aggregate license tags); check possible license incompatibilities among dependencies. We should cover just areas that are not organization-specific.

- to **manage legal issues** we should use the **same tools as developers**(issues and MRs/PRs)

## License obligations' management

- helping users/device makers in **managing** their OSS **license obligations** through a database of obligations: adjusting the detail level is key


## Last but not least: the License

- metadata as such are not covered by copyright, but may be covered by database *sui generis* rights, so we need to agree on a license
- disclaimer of warranty is key; this is not legal advice, but just a joint research effort, provided on an "as is" basis, that can be used as a basis one may build upon, just like in OSS

## Guinea Pig wanted

To start creating a common pool of compliance metadata, we may jointly work on a guinea pig project that mostly includes generally used components. There are some Eclipse Foundation embedded OS projects that may be good candidates (we need to ask).

