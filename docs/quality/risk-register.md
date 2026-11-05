# Risk register

Date: 4 Nov 2026 (Europe/London). Owner of every risk: **Isaac Adekunle**. Status: first draft, written before the software exists. Likelihood and impact are Isaac's initial judgements (Low / Medium / High; Critical for the worst safety impact), to be reviewed by the reviewers (`competence-records.md`) and at every release (`release-control.md`). Nothing has been built or run, so every mitigation is a design commitment with a planned test.

Scale. Likelihood: Low = not expected in normal use; Medium = could happen; High = expected. Impact: Low = inconvenience; Medium = wasted effort or a wrong claim that is caught; High = a wrong or misleading output reaches a reader, or a data exposure; Critical = a clean-looking result after an incomplete or wrong review.

| ID | Category | Risk | Likelihood | Impact | Mitigation | Tests | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| R-S01 | Safety | A report is read as an all-clear when the review was incomplete (crash, skipped file, partial parse) | Medium | Critical | Fail-safe `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`; planted-failure set; fuzz corpus; human-factors rules | T50, T53, T65 | Isaac | Open |
| R-S02 | Safety | A critical record gap (overdue AD, life-limited part over limit, deferral over interval, safety-critical task unsigned) is missed by a rule | Medium | Critical | Seeded-fault evaluation with 100% critical recall; clean twins; independent review by a B1 reviewer | T07, T21, T56 | Isaac | Open |
| R-S03 | Safety | The tool guesses a missing value and reports false completeness | Low | High | Missing data listed by exact path; no value output for a withheld path | T08, T40 | Isaac | Open |
| R-S04 | Safety | A reader treats a report as a release or airworthiness conclusion | Medium | Critical | Fixed two-value status; forbidden-wording scan; intended-purpose statement on every report; disclaimer | T12, T58, T59, T65 | Isaac | Open |
| R-S05 | Safety | A forged record (forged approval, forged supplier certificate) passes because the tool cannot tell truth from text | Medium | High | State the limit; flag missing or inconsistent documents; documentary indicators; human decides | T11, T41, T63 | Isaac | Open |
| R-S06 | Safety | Alert fatigue: too many false alarms hide a real one | Medium | High | Measure false-alarm rate and triage burden; critical-first ordering | T31, T65 | Isaac | Open |
| R-S07 | Safety | Over-reliance: users treat the tool as the check instead of a second look | Medium | High | Disclaimer; adopter guidance that procedures keep a human check; human-factors note | T58, T65 | Isaac | Open |
| R-R01 | Regulatory | The project is described as certified, approved or compliant | Low | High | Wording rule 'aligned with / designed to support'; scripted document check; Isaac's reading marked as not legal advice | T55, T12 | Isaac | Open |
| R-R02 | Regulatory | Regulatory statements are wrong or out of date | Medium | Medium | Source URLs and evidence tags [V]/[S]/[N]; reviewer R2; re-read before release | T02, T03, T55, T56 | Isaac | Open |
| R-R03 | Regulatory | The tool is reclassified as high-risk under the EU AI Act (per-person scoring, release function, UAS targeting) | Low | High | Design rules; self-assessment with re-assessment triggers | T57, T59, T60 | Isaac | Open |
| R-R04 | Regulatory | Per-person scoring of engineers drifts into the output (employment monitoring) | Low | High | No per-person fields, tools or aggregates; wording lexicon | T60 | Isaac | Open |
| R-R05 | Regulatory | Language-model text is not labelled (transparency duties) | Low | Medium | Visible and machine-readable label; transparency note | T61 | Isaac | Open |
| R-R06 | Regulatory | Real operator records (personal or commercially sensitive data) are used before a data-protection assessment | Low | High | Synthetic data only in Stage 0; data-protection checklist; local-first | T14, T62 | Isaac | Open |
| R-C01 | Security | Prompt injection through record text changes a result or causes a tool call | Medium | Critical | Core uses no model; optional module advisory, checked by code; injection corpus | T11, T38, T45 | Isaac | Open |
| R-C02 | Security | A network listener or egress exposes records or lets a remote party call tools | Low | High | stdio only; no socket; HTTP blocked; no telemetry | T10, T51, T52, T62 | Isaac | Open |
| R-C03 | Security | Parser crash, hang or exploit from hostile input | Medium | High | Strict parser; limits; fuzz corpus; human parser review and pen test | T53, T56 | Isaac | Open |
| R-C04 | Security | Tool poisoning or rug-pull via changed tool descriptions | Low | High | Pinned manifest hash; description lint; no list-changed notices | T64 | Isaac | Open |
| R-C05 | Security | Tampering with the audit log or a report is undetected | Low | High | Hash chain; report fingerprint; stated limit about external anchor | T13, T54 | Isaac | Open |
| R-C06 | Security | Supply-chain compromise (dependency, CI, release artefact) | Medium | High | Pinned hashes; SBOM; signed releases; pinned CI actions; secret scan | T14, T48, T66 | Isaac | Open |
| R-C07 | Security | The sealed key leaks, or is reconstructable from the public generator | High | Medium | Key and secret salt kept outside the repository; only their SHA-256 fingerprints are published at the freeze; salt and key published with the results (CA-0004, closed) | T01, T66 | Isaac | Open |
| R-C08 | Security | No human security review is done before release | Medium | High | T56 gate; release control; no release without three reviews; reviewers not yet appointed, to be funded through grants (CA-0012) | T56, T66 | Isaac | Open |
| R-P01 | Project | Single author: no second person to catch errors | High | Medium | Independent model reviewers and three human reviewers; frozen tests; corrective-action log | T16, T56 | Isaac | Open |
| R-P02 | Project | Build-tool bias or a shared blind spot from using one model family | Medium | Medium | Separate families and roles; mutation and differential testing | T25, T33 | Isaac | Open |
| R-P03 | Project | Cost or scope growth | Medium | Low | Per-stage spending limits; kill switch; free Stage 0 first | T04 | Isaac | Open |
| R-P04 | Project | Frozen test files change after the freeze, undermining the preregistration | Low | High | Hash list; verify script; unsigned annotated tag with an OpenTimestamps proof and a public post; changes only through `docs/amendments.md` | T01 | Isaac | Open |
| R-P05 | Project | Hosted-model changes (versions, availability, price) between stages | High | Low | Served-model logging; fallback models declared; re-verification | T05, T18, T32 | Isaac | Open |
| R-P06 | Project | Test data (synthetic) not representative of real records | High | Medium | State the limit; human reviewers; real-record use out of scope until a separate assessment | T21, T56 | Isaac | Open |
| R-P07 | Project | The ISO-style groundwork is mistaken for certification | Low | Medium | Explicit statements that certification is for an organisation and is not claimed | T55 | Isaac | Open |

## Review log

| Date | Reviewer | Change |
|---|---|---|
| 4 Nov 2026 | Isaac Adekunle | First draft |
