# airworthiness-mcp

**Status: pre-registration (Stage 0 not started). Nothing has been built or run yet. There are no results.** The test criteria, the generated test data and the fingerprints of the sealed answer key and its secret salt are recorded in [`PREREG_HASHES.txt`](PREREG_HASHES.txt) (see [`docs/preregistration.md`](docs/preregistration.md)).

airworthiness-mcp is a planned open-source Python tool that reads **synthetic** aircraft maintenance records and helps a person prepare for a release decision. It does not make that decision. In plain words: you point it at one work package, it checks the records against fixed rules and writes a short report of what is open, overdue, missing or out of limits, with the source of every finding. A named human reads the report and decides. The default way to run it is a simple command-line program on your own machine. It also has an [MCP](https://modelcontextprotocol.io/) server for people who already use an MCP client on the same machine.

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

It then writes a **pre-release review report** for a named human to read:

- **Every finding cites its source**: the exact record, field and value it came from.
- **Missing data is flagged, never guessed**: if a field is absent, the report lists exactly which one.
- **It never signs off.** The report never says an aircraft is released, ready, serviceable or airworthy. A named human reviews the report and decides; the software has no tool that can sign, approve or release.
- **Audit log**: every run is written to a hash-chained, tamper-evident log.
- **Default mode needs nothing else**: the command-line client with the rules engine only. No network, no API key, no AI model.

**The rules engine decides every finding.** An optional local language model can only read messy free text. It never decides a finding, can never remove or downgrade a rule finding, change a status or approve anything, and is off by default. Whether any AI model is good enough to ship in that optional mode is an open question that the trial plan tests (T38–T45). If none qualifies, the project ships rules-only.

## Deployment modes

Full detail, sources and caveats: [`docs/deployment-modes.md`](docs/deployment-modes.md). The design starts from the strictest option; looser modes are added on top, one at a time.

| Mode | What it is | Status |
|---|---|---|
| **A: default** | Local command-line client plus rules engine only. Read-only, deterministic, no model, no network. The one fully local route an auditor can inspect end to end. | Default |
| **B: optional** | Mode A plus a local IBM Granite model (Apache 2.0) that only reads free text. Off by default; Mistral is the second choice. | Off until the operator switches it on |
| **C: organisation's choice** | Open WebUI or a private-cloud client for chat. Needs local pseudonymisation of registrations, serial numbers, names, licence numbers and operator (dates become relative days; the key stays on the machine), TLS 1.3, no-retention terms, a UK or EU region and a data-processing agreement. Pseudonymised data is still personal data (legal check needed). The organisation decides and signs it off (EASA Part-IS where it applies). | Supported option; not built |

**WARNING: Never paste raw maintenance records into any chat or AI app. Use the command-line client, or a setup your organisation has approved.**

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
| Main question | Can a model spot unsupported "done" claims? | Can a tool give a cited, gap-flagging review report that cannot sign off, resists hostile record text and works offline? |

Pilot 0 packs are planned to be re-run blind as one test (T22).

## Pre-registration

All pass/fail criteria are fixed **before** Stage 0 starts and fingerprinted with SHA-256. See:

- [`docs/trial-plan.md`](docs/trial-plan.md): the 70 tests (T01–T70), pass/fail criteria and stages. T49–T66 (security, fail-safe, report integrity and design rules) and T67–T70 (encryption, default configuration, pseudonymisation and the raw-records warning) were added before the freeze.
- [`docs/preregistration.md`](docs/preregistration.md): what is frozen, when, and how fingerprints are recorded and checked.
- [`docs/methods.md`](docs/methods.md): how I chose the AI models used as build tools, the line-up comparison, the gaps it found and the estimated costs.

Thresholds in the plan are frozen at the T01 freeze (Freeze 1), except those marked "set before that stage". Build-tool tests are frozen in a second logged freeze after the model line-up is chosen. After a freeze, any change is a dated entry in [`docs/amendments.md`](docs/amendments.md).

## Security, regulatory position and quality

Written before any code, as plans and tests. Nothing here has been built or run, and none of it is a claim of certification, approval or compliance. Regulatory statements are my reading of public sources, not legal advice.

- [`SECURITY.md`](SECURITY.md) and [`docs/security/SECURITY.md`](docs/security/SECURITY.md): how to report a vulnerability (GitHub private security advisories).
- [`docs/security/threat-model.md`](docs/security/threat-model.md): whole-system threat model (STRIDE, OWASP Top 10 for LLM Applications, MCP-specific risks, and a section on encryption and key handling), each threat with a mitigation and a test.
- [`docs/security/planted-failure-set-spec.md`](docs/security/planted-failure-set-spec.md) and [`docs/security/fuzz-corpus-spec.md`](docs/security/fuzz-corpus-spec.md): fail-safe and fuzz test specifications. Any failure gives `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`, never a clean report.
- [`docs/security/standards-mapping.md`](docs/security/standards-mapping.md): how the design lines up with OWASP, NIST SSDF, SLSA, ISO/IEC 27001 themes and EASA Part-IS. Alignment, not compliance.
- [`docs/regulatory-path.md`](docs/regulatory-path.md): who may release aircraft (only authorised humans), how tools are accepted (by the adopting organisation), and the staged path. Not legal advice.
- [`docs/ai-act-self-assessment.md`](docs/ai-act-self-assessment.md): EU AI Act self-assessment (likely not high-risk, with reasons and re-assessment triggers; the language model is off by default, and Article 50 transparency applies only when it is on).
- [`docs/quality/`](docs/quality/): quality policy, risk register, traceability, corrective-action log, release control, reviewer competence records, statement of applicability (ISO/IEC 27001 Annex A groundwork), human-factors note, and suspected-unapproved-parts awareness. Certification is for an organisation and is not claimed.

Design rules: the core is a deterministic rules engine; any language-model module is optional and off by default; reports never give a release or airworthiness conclusion; the tool never scores or ranks people; language-model text is labelled when the module is on; local-first, with no egress and no telemetry. Before any public release of the software, three independent humans review it: a B1 certifying engineer, a CAMO or quality reviewer, and a security reviewer (T56). The three reviewers are not yet appointed; they are required before any public claim about results and are to be funded through grants. Stage 0 proceeds without them.

## Repository layout

```
README.md               this file
LICENSE                 MIT, Isaac Adekunle
CHANGELOG.md            dated changes
docs/methods.md         how I chose the tools
SECURITY.md             how to report a vulnerability
docs/trial-plan.md      tests T01–T70
docs/deployment-modes.md deployment modes A, B, C and the raw-records warning
docs/preregistration.md freeze and fingerprint procedure
docs/security/          threat model, test specs, security policy, standards mapping
docs/quality/           quality groundwork (policy, risks, traceability, release control)
docs/regulatory-path.md public regulatory summary (not legal advice)
docs/ai-act-self-assessment.md  EU AI Act self-assessment
tools/check_docs.py     checks for T49, T55, T70 (documents) and the T12 lexicon
data/                   synthetic data generator, lexicon, 394 generated packages, test corpora (including the T69 leak canaries)
docs/amendments.md      log of changes after each freeze
PREREG_HASHES.txt       SHA-256 fingerprints of the frozen files
verify_prereg.py        recomputes the fingerprints
tools/check_data.py     checks the generated data against an independent oracle
results/                results (empty: nothing run)
```

## Contact and feedback

Feedback from people who work in maintenance, CAMO or airworthiness review is welcome via GitHub issues. Comments are feedback on a research prototype, not an endorsement, audit or approval.
