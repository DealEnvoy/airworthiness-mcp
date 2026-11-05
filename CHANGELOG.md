# Changelog

All notable changes to this repository are recorded here. Dates are in Europe/London.

## [Unreleased]

### 2026-11-05 - Deployment modes, encryption and key handling (before the T01 freeze; freeze package re-prepared locally, not tagged)
- Approved design decision (Isaac): the default is the simple command-line client with the rules engine only (mode A: read-only, deterministic, no model, no network). IBM Granite is the optional local model for free-text reading, off by default (mode B; Mistral second choice). Open WebUI and private-cloud setups are documented as supported options for organisations that want chat (mode C), with pseudonymisation, TLS, no-retention terms, and the organisation's own sign-off. The rules engine decides every finding in every mode.
- Added `docs/deployment-modes.md` with the three modes, the Granite licence and governance verification (sources and dates, unverified items marked [N]), the Mistral caveat, and a prominent warning against pasting raw maintenance records into any chat or AI app.
- `docs/security/threat-model.md`: new section 7 "Encryption and key handling" (TLS 1.3, encryption at rest with organisation-held keys, the pseudonymisation key never leaving the machine, rotation and storage, no protection during cloud inference, confidential computing as an option); new threat rows TM-70 to TM-79; Maintenance is now section 8.
- `docs/trial-plan.md`: 4 new tests T67–T70 (section 3b). Hard fails: T67 (no plaintext egress; default mode makes zero connections), T68 (default configuration: model off, network off), T69 (pseudonymisation leak test with planted identifiers). Gate: T70 (raw-records warning in README, deployment document and client output). Plan is now 70 tests; hard fails 15, gates 7; new gap G48.
- Data: `data/generate.py` adds the T69 leak-canary corpus (`data/corpora/t69_leak_canaries.json`, 40 canary sets) on its own random stream. Every existing package and corpus file and the sealed key are byte-identical. `tools/check_data.py` checks the new corpus.
- `tools/check_docs.py`: T67–T69 added to the hard-fail list; `warning` check added (T70, documents); `docs/deployment-modes.md` added to the overclaim scan. `data/t12_lexicon.json`: frozen string `raw_records_warning`.
- Updated: README (plain description, deployment modes, warning), both SECURITY.md files, standards mapping, risk register (R-C09 to R-C12), traceability (REQ-33 to REQ-37), statement of applicability, AI Act self-assessment (model off by default; Article 50 only when a model is on), preregistration, release-control (hard-fail and gate lists), methods (cost table row), data README.
- `PREREG_HASHES.txt` regenerated (new fingerprint; `docs/deployment-modes.md` added to the frozen list). Nothing tagged, pushed or timestamped.

### 2026-11-05 - T01 freeze package (Freeze 1), prepared locally
- Decisions on the nine open freeze items applied. Freeze 1 covers the product tests; the build-tool tests are frozen separately in Freeze 2 (`docs/amendments.md`).
- Data: `data/generate.py` 1.1.0 uses a secret salt (the sealed key and salt are outside the repository; only their SHA-256 fingerprints are listed). Twin packages no longer differ on the safety-critical flag. Boundary rules fixed (at or above a limit is a fault; a deferral expiring today is expired; a repeat defect is three or more).
- Data added: suspected-unapproved-parts set `t63_sup` (56 packages), T11 injection set (180), and the T06 (35 cases), T09 (40 prompts) and T11 (60 payloads) corpora. 394 packages in 8 sets in total.
- Report vocabulary: the two status lines are now `REVIEW COMPLETE - findings listed; a certifying engineer decides` and `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`. Exit code 3 for incomplete.
- T12 scope: tool-written text only. `tools/check_docs.py lexicon` added; `tools/check_data.py` added (independent rule oracle).
- `docs/preregistration.md` rewritten: unsigned annotated tag, OpenTimestamps proof, one fingerprint posted publicly by Isaac. `docs/amendments.md` added. Thresholds and spend caps not yet set are marked "set before that stage".
- Corrective-action log: CA-0001 to CA-0010 closed; CA-0011 open; CA-0012 to CA-0014 opened. Human reviewers are not appointed; they are required before any public claim about results and are to be funded through grants.
- `PREREG_HASHES.draft.txt` replaced by `PREREG_HASHES.txt`.

### 2026-11-04 — Security, regulatory and quality groundwork (before the T01 freeze)
- `docs/trial-plan.md`: 18 new tests T49–T66 (section 3a) with fixed limits and exact pass/fail criteria. Twelve are hard fails (T50, T51, T53, T54, T57–T62, T64, T65) and six are gates (T49, T52, T55, T56, T63, T66). New gap list entries G37–G47; T35 now re-runs them; Stage 0 cost still 0.
- Added `docs/security/`: threat model (STRIDE, OWASP Top 10 for LLM Applications, MCP-specific risks), planted-failure set specification (PF01–PF40, PC01–PC10), fuzz and abuse corpus specification (FZ-A to FZ-I, 248 targeted cases plus 10,000 seeded mutations, and the T63 data set specification), `SECURITY.md` and `standards-mapping.md` (alignment, not compliance).
- Added root `SECURITY.md` (GitHub private security advisories).
- Added `docs/regulatory-path.md` (public summary, not legal advice) and `docs/ai-act-self-assessment.md` (likely not high-risk, with re-assessment triggers).
- Added `docs/quality/`: quality policy, risk register, traceability, corrective-action log (with 11 known open issues), release control, competence records, statement of applicability (Annex A groundwork, largely to complete), human-factors note, suspected-unapproved-parts awareness. No certification is claimed.
- Added `tools/check_docs.py` (T49, T55 and specification checks).
- `docs/methods.md`: human review now has three reviewers (B1 certifying engineer, CAMO or quality, security).
- `docs/preregistration.md`: frozen list extended; TODO comment added: tag-signing decision pending Isaac.
- README: intended-purpose statement, links, layout. `PREREG_HASHES.draft.txt` regenerated.
- Data: no change. `data/generate.py`, the sealed key and the package manifest are untouched. The fail-safe, fuzz and suspected-unapproved-parts data sets are specified, not generated.

### 2026-11-04 — Funding wording
- Removed the proposed overall hard cap and fixed elapsed-time limit from `docs/methods.md` and `docs/trial-plan.md`. Cost estimate ranges and contingency kept. Free Stage 0 runs first; paid stages run in order as funding allows, each with a per-stage spending limit set by Isaac before it starts; order of cuts kept; T04 kill switch kept.

### 2026-11-04 — Methods published
- Added `docs/methods.md` ("How I chose the tools"): role split, line-up comparison and scoring panel, gaps found, estimated costs. All third-party figures labelled as reported and not independently verified.
- `docs/trial-plan.md`: added the build-tool tests (T18–T20, T23–T25, T27–T30, T32–T34, T36, T46), cost estimates, gap list and coverage matrix.
- README: authorship line and note on AI models used as build tools.

### 2026-11-04 — Pre-registration draft
- Added README, MIT licence, trial plan (`docs/trial-plan.md`, tests T01–T48) and pre-registration procedure (`docs/preregistration.md`).
- Added placeholder `data/` and `results/` folders.
- No code written yet. No test has been run. No results exist.
- SHA-256 fingerprints not yet recorded: they are recorded at the T01 freeze, before Stage 0 starts.
