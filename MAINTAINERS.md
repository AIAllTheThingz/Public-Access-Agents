# Maintainers and Repository Ownership

## Purpose

This document defines repository ownership, maintainer roles, review requirements, merge authority, emergency-change authority, inactivity handling, and succession for Public-Access-Agents.

It applies to repository administration and maintenance. It does not replace the governance standards that apply to the content being changed.

## Current maintainer roster

| Maintainer | GitHub account | Roles | Status | Since |
|---|---|---|---|---|
| Metello Zuccolini | [@AIAllTheThingz](https://github.com/AIAllTheThingz) | Lead Maintainer, Repository Administrator, Release Manager, Security Maintainer, Governance Maintainer, Schema Maintainer, Tooling Maintainer | Active | 2026-07-13 |

### Current coverage limitation

The repository currently has one active maintainer.

The maintainer may hold several responsibility areas, but one person cannot provide independent review of their own change. Changes that require independent specialist review must wait for a qualified reviewer who is not the author, unless the emergency-change process applies.

This limitation must remain visible until at least two active maintainers or qualified specialist reviewers are appointed.

## Maintainer roles

### Lead Maintainer

The Lead Maintainer:

- owns the repository maintenance model
- appoints and removes maintainers through reviewed changes to this document
- coordinates releases and compatibility decisions
- resolves routine ownership disputes
- ensures that inactive-maintainer and succession rules are applied
- confirms that repository rulesets and CODEOWNERS reflect this policy

### Repository Administrator

A Repository Administrator may manage repository settings, access, rulesets, security features, and integrations.

Administrative access does not by itself grant authority to approve or merge a change that has not satisfied this policy.

### Area Maintainer

An Area Maintainer owns review quality and compatibility for one or more repository areas. Area ownership includes:

- reviewing normative and breaking changes
- keeping documentation, examples, schemas, and tests synchronized
- identifying specialist review requirements
- maintaining authoritative references and last-reviewed information
- escalating unresolved risk or ownership gaps

### Specialist Reviewer

A Specialist Reviewer provides qualified review for sensitive subject matter. A specialist reviewer does not need permanent merge access, but must be identifiable, independent from the author where required, and competent in the affected area.

### Release Manager

The Release Manager coordinates versioning, release notes, tags, release artifacts, migration notes, and release evidence. Release authority does not override required technical or specialist review.

### Security Maintainer

The Security Maintainer coordinates private vulnerability handling, security-sensitive review, emergency containment, disclosure timing, and post-incident follow-up.

## Area ownership

`CODEOWNERS` routes review requests. This table defines the review responsibility behind those routes.

| Area | Repository paths | Current owner | Required review class |
|---|---|---|---|
| Repository governance and authority | `AGENTS.md`, `MAINTAINERS.md`, `.github/CODEOWNERS`, `governance/` | @AIAllTheThingz | Governance specialist for normative changes |
| Security policy and secure-development controls | `SECURITY.md`, `governance/SECURE_DEVELOPMENT_POLICY.md`, `governance/THREAT_MODELING_POLICY.md`, `governance/VULNERABILITY_RESPONSE.md`, `disciplines/application-security/`, `profiles/security-tool/` | @AIAllTheThingz | Security specialist for normative or risk-reducing changes |
| Schemas and machine-readable contracts | `schemas/`, schema-backed JSON templates, `tools/validate-schemas/` | @AIAllTheThingz | Schema or compatibility specialist for contract changes |
| Executable tools and CI | `tools/`, `.github/workflows/` | @AIAllTheThingz | Tooling or CI specialist for executable or permission changes |
| Licensing and contribution terms | `LICENSE`, `NOTICE`, `LICENSING.md`, license sections of `README.md` and `CONTRIBUTING.md` | @AIAllTheThingz | Lead Maintainer; legal review when terms change |
| Languages | `languages/` | @AIAllTheThingz | Relevant language specialist for normative changes |
| Engineering disciplines | `disciplines/` | @AIAllTheThingz | Relevant discipline specialist for normative changes |
| Platforms | `platforms/` | @AIAllTheThingz | Relevant platform specialist for provider or operational changes |
| Virtualization | `virtualization/` | @AIAllTheThingz | Relevant virtualization specialist for hypervisor, control-plane, recovery, lifecycle, or migration changes |
| Operating systems | `operating-systems/` | @AIAllTheThingz | Relevant operating-system specialist for lifecycle, servicing, security, recovery, upgrade, or fleet-management changes |
| Frameworks | `frameworks/` | @AIAllTheThingz | Relevant framework specialist for normative changes |
| Project profiles | `profiles/` | @AIAllTheThingz | Profile and affected-area review |
| Templates and examples | `templates/`, `examples/` | @AIAllTheThingz | Affected contract or governance owner |
| Catalog and repository documentation | `README.md`, `CATALOG.md`, `MANIFEST.md`, `ROADMAP.md`, `SOURCES.md` | @AIAllTheThingz | Affected area owner |

## Review classes

### Editorial review

Editorial changes do not change normative meaning, compatibility, authority, security posture, schemas, tool behavior, or generated output.

Requirements:

- permanent CI passes
- affected links and examples remain correct
- one active maintainer reviews the final diff

The current sole maintainer may merge their own low-risk editorial change after a documented self-review and successful CI.

### Normative review

Normative changes add, remove, or alter requirements, evidence expectations, exception behavior, compatibility promises, or completion boundaries.

Requirements:

- affected area owner review
- explicit compatibility and security impact
- examples, templates, schemas, and validation updated as applicable
- permanent CI passes
- unresolved review findings are closed or explicitly accepted by an authorized maintainer

A normative change in a sensitive area also requires specialist review.

### Independent specialist review

Independent specialist review is required for:

- governance authority, precedence, approval, exception, or human-review rules
- security policy, threat-modeling, vulnerability handling, authentication, authorization, cryptography, secrets, or destructive-action controls
- schema required fields, types, enums, identifiers, versioning, extension behavior, or compatibility promises
- executable tool behavior, filesystem writes, subprocess execution, dependency changes, workflow permissions, or release automation
- changes classified as high or critical risk
- breaking repository releases

The specialist reviewer must not be the author. Re-labeling the same person as both maintainer and specialist does not create independence.

While the repository has only one active maintainer, affected changes must either:

1. obtain review from a qualified external specialist recorded in the pull request, or
2. remain unmerged, or
3. use the emergency-change process when delay would materially increase active harm.

### Legal review

Changes to the license text, contribution terms, trademark statements, warranty language, or third-party licensing interpretation should receive qualified legal review. Repository validation confirms file presence and declared markers; it is not legal advice.

## Merge authority

A person may merge into the default branch only when all of the following are true:

- they are listed as an active maintainer in this document
- they have the required GitHub repository permission
- permanent CI has passed for the final head commit
- required CODEOWNER and specialist reviews have been satisfied
- requested changes and unresolved review findings have been addressed
- compatibility, security, validation, and remaining limitations are documented
- the pull request scope is coherent and contains no unrelated changes
- the merge method is permitted by repository rules

Normal changes must use pull requests. Direct pushes to the protected default branch are prohibited except where GitHub administrative recovery makes a pull request technically impossible and the emergency process is followed.

CODEOWNERS identifies reviewers. It does not itself grant merge authority, prove specialist competence, or replace branch protection.

## Author self-merge

Until a second active maintainer is appointed, the Lead Maintainer may self-merge only when:

- the change is low or moderate risk
- no independent specialist review is required
- permanent CI passes on the final commit
- the pull request contains an explicit self-review record
- compatibility, security impact, and limitations are stated
- no unresolved external review objection remains

Self-merge is prohibited for high-risk, critical-risk, breaking, governance-authority, security-sensitive, schema-contract, or executable-tool changes unless the emergency-change process applies.

## Emergency changes

### Emergency criteria

The emergency process may be used only when delay would materially increase active harm, including:

- an exploitable vulnerability in repository tooling or automation
- published guidance that creates an immediate security or destructive-action risk
- compromised workflow, release, credential, or dependency behavior
- a broken default-branch validation path that prevents corrective review
- accidental disclosure of sensitive information

A missed deadline, inconvenient review requirement, or desire to merge quickly is not an emergency.

### Emergency authority

The active Security Maintainer or Lead Maintainer may authorize and merge the smallest corrective change necessary to contain the emergency.

The emergency change must:

- identify the triggering condition
- state why normal review cannot safely complete first
- minimize scope
- avoid unrelated cleanup or policy expansion
- preserve available evidence
- run all safe and available validation
- define rollback or containment reversal
- record the person authorizing and merging the change

### Post-merge requirements

Within seven calendar days, the maintainer must:

- open or update a public follow-up record unless confidentiality prevents it
- obtain independent specialist review
- run omitted validation
- correct any deficiencies found
- document root cause, impact, and remaining risk
- restore normal branch and review controls if they were temporarily changed

If confidentiality is required, the public record may omit exploit details but must still identify that an emergency maintenance action occurred.

## Inactivity

### Active maintainer

A maintainer is active when they:

- have performed meaningful repository maintenance within the previous 90 days, or
- have explicitly confirmed availability within the previous 90 days
- respond to direct maintainer requests within 14 calendar days when reasonably available
- retain the access and competence required for their assigned role

### Temporarily unavailable

A maintainer may declare temporary unavailability. Their review and merge responsibilities must be reassigned for the declared period. Temporary unavailability does not remove maintainer status.

### Inactive maintainer

A maintainer may be marked inactive when:

- no meaningful maintenance or availability confirmation has occurred for 90 days, and
- direct contact has received no response for 30 days, or
- the maintainer requests inactive status

Inactive maintainers:

- are removed from required CODEOWNERS routes where another owner exists
- lose merge and administrative authority where administratively possible
- may retain historical attribution
- may return through the reactivation process

### Emeritus maintainer

A former maintainer with substantial historical contributions may be listed as emeritus. Emeritus status grants recognition, not review or merge authority.

## Appointment and succession

### Appointing a maintainer

A maintainer candidate should demonstrate:

- sustained, constructive contribution history
- understanding of repository governance and validation
- sound handling of compatibility, security, and evidence
- ability to review the assigned area
- agreement to this policy and the code of conduct when one is adopted

Appointment requires a pull request updating this file and CODEOWNERS. The review record must identify the proposed roles and affected areas.

### Preferred readiness evidence

Before appointment, a candidate should normally have:

- at least three substantive merged contributions
- contributions spanning at least 60 days
- successful review of at least one normative change
- successful use of the repository toolchain
- no unresolved conduct, security, or conflict-of-interest concern

These are review criteria, not automatic entitlement.

### Lead Maintainer succession

The preferred succession order is:

1. a successor nominated by the current Lead Maintainer and approved through a reviewed ownership change
2. unanimous selection by the remaining active maintainers
3. selection by the repository owner or administrator when no active maintainer can act

A succession change must update:

- `MAINTAINERS.md`
- `.github/CODEOWNERS`
- repository permissions and rulesets
- release and security contacts
- any external automation credentials or ownership records

### Sole-maintainer continuity

While only one active maintainer exists, the repository should not claim mature succession coverage. Before promoting the repository to a stable public release, the preferred state is:

- at least two active maintainers
- at least one independent security reviewer
- at least one independent schema or tooling reviewer
- documented recovery of administrative access

No secret recovery material may be stored in this public repository.

## Reactivation and removal

An inactive maintainer may be reactivated through a reviewed pull request confirming current availability, access, assigned areas, and acceptance of current policy.

A maintainer may be removed for:

- prolonged inactivity
- loss of required access or competence
- repeated bypass of review, security, or evidence requirements
- undisclosed material conflict of interest
- abusive or unsafe conduct
- compromised account or credentials

Removal must preserve relevant evidence and follow private security handling when public detail would increase harm.

## Conflicts of interest

Maintainers and reviewers must disclose material conflicts that could affect impartial review. A conflicted person must not be the sole approver for the affected change.

Examples include:

- commercial interests directly affected by a standard
- reviewing one's own high-risk or breaking change
- undisclosed employment or contractual obligations
- personal disputes that impair objective review

## Branch protection and enforcement

Repository rules should require, where supported:

- pull requests for the default branch
- successful permanent validation
- required CODEOWNER review
- resolution of review conversations
- prevention of force pushes and branch deletion
- restricted bypass authority

This document defines policy. GitHub rulesets and permissions provide enforcement. A mismatch between policy and configuration must be treated as a repository administration defect.

## Review cadence

Review this document and CODEOWNERS:

- at least every six months
- whenever a maintainer is appointed, removed, or becomes inactive
- whenever repository ownership or organization changes
- before a major release
- after an emergency change involving authority or access
- after an incident exposes an ownership gap

The review should confirm current names, GitHub accounts, roles, permissions, area coverage, specialist availability, and succession readiness.

## Evidence and records

Pull requests, reviews, release records, security advisories, and repository settings are the authoritative evidence for maintenance actions.

This file records the operating model. It does not prove that repository permissions or branch rules are configured correctly; those settings must be reviewed separately.
