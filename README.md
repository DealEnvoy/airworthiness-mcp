# airworthiness-mcp

**Status: pre-registration. Nothing has been built or run yet. There are no results.**

airworthiness-mcp is a planned open-source Python [MCP](https://modelcontextprotocol.io/) server that reads **synthetic** aircraft maintenance records and helps a person prepare for a release decision. It does not make that decision.

Built and verified by Isaac Adekunle (15+ years in aircraft maintenance). Licence: MIT.

**Intended purpose:** Advisory checker of maintenance records and work packages. Read-only. Does not certify, release, or determine airworthiness. A certifying human decides.

AI models are used as build and review tools under a method I designed and ran: separate architect, implementer and independent reviewer roles, with reviewers never the builder and every result checked by deterministic code before I accept it. How I chose and checked those models, including costs, is in [`docs/methods.md`](docs/methods.md).

## What it will do, in plain words

Given the (synthetic) records for one aircraft and one work package, it checks five things:

1. **Open defects and deferrals**: anything still open, and any deferral past its allowed interval.
2. **Part life limits**: life-limited parts at or beyond their limit.
3. **Tasks coming due**: scheduled tasks due or overdue.
4. **Airworthiness directives (ADs)**: AD status and anything overdue.
5. **Work-package completeness**: are all task cards, sign-offs and pages present?

It then writes a **pre-release readiness report** for a named human to read:

- **Every finding cites its source**: the exact record, field and value it came from.
- **Missing data is flagged, never guessed**: if a field is absent, the report lists exactly which one.
- **It never signs off.** The report never says an aircraft is released, ready, serviceable or airworthy. A named human reviews the report and decides; the software has no tool that can sign, approve or release.
- **Audit log**: every run is written to a hash-chained, tamper-evident log.
- **Free offline mode**: a rules-only mode that needs no network, no API key and no AI model.

An optional AI report mode may sit on top of the rules. It is **advisory only**: it can add findings for a human to read, but it can never remove or downgrade a rule finding, change a status or approve anything. Whether any AI model is good enough to ship in that mode is an open question that the trial plan tests (T38–T45). If none qualifies, the project ships rules-only.

## Safety boundaries

- **Synthetic data only.** Every aircraft, registration, part, defect, task and record is invented. No real aircraft records are used.
- **Not certified.** This is a research prototype. It is not approved, certified or accepted by any aviation authority, and it is not a maintenance or continuing-airworthiness system.
- **Never releases aircraft.** It is not intended for real aircraft or real release decisions. It does not issue, draft or imply a Certificate of Release to Service (CRS) or a return to service.
- **Required disclaimer** in every report and approval prompt: *"AI assists, a certifying human decides."*

## How this relates to CRS Pilot 0

This project builds on [CRS for AI agents, Pilot 0](https://github.com/DealEnvoy/crs-ai-agents), which asked whether an AI model, acting as an advisory reviewer, can notice when a finished work pack's own evidence does not support its "done" statements, before a human signs.

| | CRS Pilot 0 | airworthiness-mcp |
|---|---|---|
| What it is | A small, completed evaluation | A planned tool plus a pre-registered test plan |
| Input | 16 hand-built packs (aviation and software), each fault on the page | Generated synthetic records across five check areas |
| Who finds faults | The model under test | Deterministic rules first; any AI layer is advisory on top |
| Main question | Can a model spot unsupported "done" claims? | Can a tool give a cited, gap-flagging readiness report that cannot sign off, resists hostile record text and works offline? |

Pilot 0 packs are planned to be re-run blind as one test (T22).

## Pre-registration

All pass/fail criteria are fixed **before** Stage 0 starts and fingerprinted with SHA-256. See:

- [`docs/trial-plan.md`](docs/trial-plan.md): the 66 tests (T01–T66), pass/fail criteria and stages. T49–T66 (security, fail-safe, report integrity and design rules) were added before the freeze.
- [`docs/preregistration.md`](docs/preregistration.md): what is frozen, when, and how fingerprints are recorded and checked.
- [`docs/methods.md`](docs/methods.md): how I chose the AI models used as build tools, the line-up comparison, the gaps it found and the estimated costs.

Thresholds in the plan are proposals until the freeze. After it, any change is a logged amendment.

## Security, regulatory position and quality

Written before any code, as plans and tests. Nothing here has been built or run, and none of it is a claim of certification, approval or compliance. Regulatory statements are my reading of public sources, not legal advice.

- [`SECURITY.md`](SECURITY.md) and [`docs/security/SECURITY.md`](docs/security/SECURITY.md): how to report a vulnerability (GitHub private security advisories).
- [`docs/security/threat-model.md`](docs/security/threat-model.md): whole-system threat model (STRIDE, OWASP Top 10 for LLM Applications, MCP-specific risks), each threat with a mitigation and a test.
- [`docs/security/planted-failure-set-spec.md`](docs/security/planted-failure-set-spec.md) and [`docs/security/fuzz-corpus-spec.md`](docs/security/fuzz-corpus-spec.md): fail-safe and fuzz test specifications. Any failure gives `NOT READY - review incomplete`, never a clean report.
- [`docs/security/standards-mapping.md`](docs/security/standards-mapping.md): how the design lines up with OWASP, NIST SSDF, SLSA, ISO/IEC 27001 themes and EASA Part-IS. Alignment, not compliance.
- [`docs/regulatory-path.md`](docs/regulatory-path.md): who may release aircraft (only authorised humans), how tools are accepted (by the adopting organisation), and the staged path. Not legal advice.
- [`docs/ai-act-self-assessment.md`](docs/ai-act-self-assessment.md): EU AI Act self-assessment (likely not high-risk, with reasons and re-assessment triggers).
- [`docs/quality/`](docs/quality/): quality policy, risk register, traceability, corrective-action log, release control, reviewer competence records, statement of applicability (ISO/IEC 27001 Annex A groundwork), human-factors note, and suspected-unapproved-parts awareness. Certification is for an organisation and is not claimed.

Design rules: the core is a deterministic rules engine; any language-model module is optional and off by default; reports never give a release or airworthiness conclusion; the tool never scores or ranks people; language-model text is labelled when the module is on; local-first, with no egress and no telemetry. Before any public release of the software, three independent humans review it: a B1 certifying engineer, a CAMO or quality reviewer, and a security reviewer (T56).

## Repository layout

```
README.md               this file
LICENSE                 MIT, Isaac Adekunle
CHANGELOG.md            dated changes
docs/methods.md         how I chose the tools
SECURITY.md             how to report a vulnerability
docs/trial-plan.md      tests T01–T66
docs/preregistration.md freeze and fingerprint procedure
docs/security/          threat model, test specs, security policy, standards mapping
docs/quality/           quality groundwork (policy, risks, traceability, release control)
docs/regulatory-path.md public regulatory summary (not legal advice)
docs/ai-act-self-assessment.md  EU AI Act self-assessment
tools/check_docs.py     checks for T49 and T55
data/                   synthetic data generator, lexicon, 158 generated packages
results/                results (empty: nothing run)
```

## Contact and feedback

Feedback from people who work in maintenance, CAMO or airworthiness review is welcome via GitHub issues. Comments are feedback on a research prototype, not an endorsement, audit or approval.
