# Changelog

All notable changes to this repository are recorded here. Dates are in Europe/London.

## [Unreleased]

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
