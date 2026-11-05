# Traceability

Date: 4 Nov 2026 (Europe/London); updated 5 Nov 2026 (REQ-33 to REQ-37). Owner: Isaac Adekunle. Status: seeded with the requirements that exist now. Rules are not written yet, so rule rows name rule families; **rule IDs are assigned when the rules are written** and this table is then updated.

Chain: requirement, then source or rule, then test ID. Every requirement has at least one test in `docs/trial-plan.md`. Security threats are traced separately in `docs/security/threat-model.md` (threat row to mitigation to test ID); the requirements below point to them.

| Requirement | Statement | Source | Rule or design element | Test IDs |
|---|---|---|---|---|
| REQ-01 | Report open defects and deferrals; flag a deferral past its allowed interval (critical) | README check 1; seeded-fault class 'deferral beyond interval' (T07) | Rule family OPEN-DEFECT / DEFERRAL (rule IDs assigned when the rules are written) | T07, T21 |
| REQ-02 | Flag life-limited parts at or beyond their limit (critical) | README check 2; T07 | Rule family LIFE-LIMIT | T07, T21 |
| REQ-03 | Flag scheduled tasks due or overdue | README check 3 | Rule family TASK-DUE | T21 |
| REQ-04 | Flag airworthiness directive status and overdue ADs (critical) | README check 4; T07 | Rule family AD-STATUS | T07, T21 |
| REQ-05 | Flag work-package incompleteness: missing task cards, sign-offs, pages; safety-critical task with no sign-off page is critical | README check 5; T07 | Rule family WP-COMPLETE | T07, T21 |
| REQ-06 | Every finding cites record, field and value | README; `docs/trial-plan.md` T06 | Citation validator | T06, T39 |
| REQ-07 | Missing data is listed by exact field path and never guessed | README; T08 | Missing-data block | T08, T40 |
| REQ-08 | No tool signs, approves, releases or writes | README; T09; regulatory path section 1 (145.A.50, M.A.801, 14 CFR 43.7) | Read-only tool allow-list | T09, T41, T64 |
| REQ-09 | Rules-only offline mode needs no network, key or model | README; T10, T15 | Rules engine core | T10, T15, T62 |
| REQ-10 | Record text cannot change a result, status or tool call | T11 | Data/instruction separation; schema | T11, T38, T45 |
| REQ-11 | No release, serviceability or airworthiness wording anywhere; disclaimer in every report | T12; `data/t12_lexicon.json` F01–F32 | Report schema, lexicon scan | T12, T59 |
| REQ-12 | Tamper-evident hash-chained audit log | T13 | Audit log | T13 |
| REQ-13 | Supply-chain controls: SBOM, pinned hashes, signed releases | T14 | Build and release | T14, T66 |
| REQ-14 | Any failure gives `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`, never a clean report | `docs/security/planted-failure-set-spec.md` | Fail-safe wrapper | T50 |
| REQ-15 | stdio only; no socket; HTTP mode blocked until secured | `docs/security/threat-model.md` TM for C2 | Transport | T51, T52 |
| REQ-16 | Hostile or malformed input cannot crash, hang, escape the package root or slip through | `docs/security/fuzz-corpus-spec.md` | Strict parsers, limits | T53 |
| REQ-17 | An edited report is detected | `docs/security/threat-model.md` C9 | Report fingerprint chained to the audit log | T54, T13 |
| REQ-18 | Threat model complete; every threat has a mitigation and a test | T49 | `docs/security/threat-model.md` | T49 |
| REQ-19 | Vulnerability disclosure policy and standards mapping, without overclaiming | T55 | `SECURITY.md`, `docs/security/` | T55 |
| REQ-20 | Three independent human reviews before any public release | T56 | `competence-records.md` | T56 |
| REQ-21 | Core is a rules engine; the language-model module is optional and off by default | `docs/ai-act-self-assessment.md` | Module separation | T57 |
| REQ-22 | Intended-purpose statement in README, server description and every report | `docs/ai-act-self-assessment.md`; `docs/regulatory-path.md` | Report header | T58 |
| REQ-23 | Never score or rank individual people | `docs/ai-act-self-assessment.md` 3.3 (Annex III 4(b)) | Schema without person-keyed fields | T60 |
| REQ-24 | Language-model text is labelled visibly and in machine-readable form | `docs/ai-act-self-assessment.md` 3.5 (Article 50) | Label block inside the fingerprint | T61 |
| REQ-25 | Local-first: no egress, no telemetry | `docs/regulatory-path.md` section 4 (Part-IS support) | Configuration, static scan | T62, T10 |
| REQ-26 | Documentary indicators for suspected unapproved parts, never a conclusion | `suspected-unapproved-parts-awareness.md` | Parts check | T63 |
| REQ-27 | Tool manifest is static, pinned and read-only | `docs/security/threat-model.md` C3 (tool poisoning, rug-pull) | Manifest hash check | T64 |
| REQ-28 | Report layout prevents misreading; zero-findings statement | `human-factors-note.md` | Report builder | T65 |
| REQ-29 | Release only after tests pass and Isaac signs off | `release-control.md` | Release record and script | T66, T35 |
| REQ-30 | Pre-registration: criteria frozen and fingerprinted before any test | `docs/preregistration.md` | `verify_prereg.py`, hash list | T01 |
| REQ-31 | Python safeguards in CI | `docs/trial-plan.md` T48 | CI gate | T48, T47 |
| REQ-32 | Seeded-fault evaluation against clean twins (394 generated packages in 8 sets, including the T63 and T11 sets) | `data/generate.py` (seed 20261104) | Generator, sealed key | T21, T08, T38, T41 |
| REQ-33 | Default mode: command-line client and rules engine only; model off, network off; enabling anything needs an explicit setting | `docs/deployment-modes.md` section 2 | Default configuration | T68, T67, T57 |
| REQ-34 | No plaintext egress: every off-machine connection is TLS 1.3 with certificate checks; default mode makes no connection | `docs/security/threat-model.md` section 7 | Transport rules | T67, T52 |
| REQ-35 | Mode C sends only pseudonymised data; the key never leaves the machine | `docs/deployment-modes.md` section 4 | Pseudonymiser | T69 |
| REQ-36 | Warning against pasting raw records into chat or AI apps in README, deployment document and client output | `docs/deployment-modes.md` | Frozen lexicon string | T70 |
| REQ-37 | Optional local model (IBM Granite first, Mistral second) reads free text only and never decides a finding | `docs/deployment-modes.md` section 3 | Module separation | T57, T38–T45 |

## Maintenance

* A new requirement is added here with its source before code is written.
* A new rule gets a rule ID, a requirement, a source (where the check comes from) and at least one test (a seeded fault and a clean twin).
* Every release record (`release-control.md`) states the traceability version. Unmapped requirements block a release.
