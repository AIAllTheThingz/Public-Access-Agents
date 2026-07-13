# Package Maturity Policy

## Purpose

This policy defines maturity states, promotion requirements, review records, demotion, deprecation, and maintenance expectations for standards packages, governance policies, schemas, templates, examples, and executable tools.

Maturity describes the evidence supporting a repository component. It is not a marketing adjective and does not certify adopting projects.

## Authority

Maturity changes are normative repository changes.

Promotion to `stable`, demotion from `stable`, and deprecation require:

- the applicable area owner
- compatibility analysis
- permanent CI
- the specialist review required by [`MAINTAINERS.md`](MAINTAINERS.md)
- a completed maturity review record

The author of a promotion change cannot provide the required independent specialist review of that same change.

## Maturity states

### Planned

A planned component is a catalog commitment or future work item.

It must not be presented as enforceable, complete, or ready for adoption.

Required evidence:

- defined purpose
- owner or proposed owner
- expected scope
- explicit `planned` status

### Draft

A draft component is available for review and experimentation but is expected to change.

Required evidence:

- coherent initial content
- known limitations
- review questions
- no claim of compatibility stability

### Baseline

A baseline component is usable as a minimum standard but has not yet met the repository's stable-evidence requirements.

Required evidence:

- complete package structure where applicable
- useful README and manifest
- normative requirements and evidence expectations
- examples and templates where applicable
- validation coverage
- authoritative source review
- explicit limitations
- accountable owner

Most repository packages currently use `baseline`.

### Stable

A stable component has a reviewed compatibility commitment within the repository release policy.

Required evidence is defined under **Promotion requirements**.

Stable does not mean frozen. Compatible improvements may continue through repository releases.

### Deprecated

A deprecated component remains available only for migration and compatibility.

Required evidence:

- replacement or retirement rationale
- deprecation date and release
- supported overlap window
- migration guidance
- removal target when removal is planned
- affected-consumer analysis

## Promotion requirements

Promotion must be based on evidence gathered against the exact component version and repository revision.

### Planned to draft

Required:

- defined owner
- initial content or implementation
- scope and non-goals
- reviewable structure
- known limitations

### Draft to baseline

Required:

- package or policy completeness
- repository validation
- examples and adoption guidance
- applicable schemas, templates, and tests
- source and compatibility review
- owner acceptance
- no unresolved critical defect

### Baseline to stable

Required:

- at least one completed package-level adoption test
- at least two representative adoptions, pilots, or independently reviewed composition exercises
- compatibility inventory for stable paths, identifiers, schemas, templates, and tool behavior
- current authoritative-source review
- positive, negative, and error-path validation where applicable
- documented migration and deprecation behavior
- review of known failure modes and operational limitations
- no unresolved critical or high defect
- explicit maintenance owner and review cadence
- independent specialist review appropriate to the component
- completed maturity review record under `maturity-reviews/`
- release-note inclusion in the release that carries the promotion

One successful example inside this repository is not, by itself, independent adoption evidence. A terrarium can be healthy without proving the plant survives outdoors.

## Baseline to stable review

The review must evaluate:

1. **Scope**
   - purpose, applicability, non-goals, and boundaries remain accurate
2. **Normative quality**
   - requirements are specific, testable, evidence-based, and proportionate
3. **Compatibility**
   - stable paths, identifiers, schemas, templates, and tool contracts are inventoried
4. **Security and safety**
   - threat, misuse, privilege, destructive action, and sensitive-data implications are reviewed
5. **Adoption evidence**
   - representative adopters could select, tailor, validate, and maintain the component
6. **Source currency**
   - authoritative references and provider/runtime facts are current
7. **Validation**
   - positive, negative, boundary, and failure behavior are exercised
8. **Maintenance**
   - owner, review cadence, deprecation path, and compatibility response are defined
9. **Limitations**
   - unresolved assumptions and residual risks are visible
10. **Decision**
   - approve, approve with conditions, defer, or reject

## Review record

Use [`maturity-reviews/TEMPLATE.md`](maturity-reviews/TEMPLATE.md).

Each record must identify:

- component and current version
- proposed maturity transition
- repository commit
- owner and reviewers
- review date
- adoption evidence
- compatibility inventory
- validation commands and results
- source-review date
- security and operational findings
- open conditions
- decision and rationale
- next review date

Accepted decisions are:

- `approved`
- `approved-with-conditions`
- `deferred`
- `rejected`

`approved-with-conditions` may promote a component only when the conditions are non-blocking, time-bounded, owned, and visible in the release notes.

## Demotion and deprecation

A stable component may be demoted to baseline when:

- compatibility cannot be maintained
- authoritative sources materially changed
- adoption evidence exposed serious ambiguity
- validation no longer reflects the documented contract
- ownership or maintenance coverage disappeared
- a critical or high defect remains unresolved

Demotion requires release-note disclosure and migration impact analysis.

Deprecation is appropriate when:

- a component is superseded
- its underlying technology is no longer supported
- the repository can no longer maintain its compatibility promise
- continued use creates security, safety, or operational risk

Deprecation windows follow [`RELEASE_POLICY.md`](RELEASE_POLICY.md).

## Emergency maturity change

An emergency security or safety change may temporarily demote or deprecate a component before the normal review completes.

The emergency process in `MAINTAINERS.md` applies. Independent review and complete follow-up are required within seven calendar days.

## Review cadence

- stable components: at least annually
- cloud/provider-specific stable components: at least every six months
- security-sensitive stable components: at least every six months
- deprecated components: at each release until removal or indefinite-retention decision
- baseline components: when material sources, runtimes, schemas, or adoption feedback change

A review date passing does not automatically invalidate a component, but it must create a visible maintenance item and block unsupported claims of current review.

## 1.0.0 relationship

The repository may publish `1.0.0` while some components remain baseline only when:

- the stable compatibility surface is explicitly identified
- baseline components are clearly outside the stable promise
- release notes list the baseline components and limitations
- adopters can determine which contracts are covered

The repository must not imply that every file is stable merely because the repository version reached `1.0.0`.

## Policy maintenance

Changes to maturity definitions or promotion requirements are normative governance changes and require independent specialist review.
