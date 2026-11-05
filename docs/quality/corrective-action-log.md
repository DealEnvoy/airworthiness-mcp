# Corrective-action log

Date opened: 4 Nov 2026 (Europe/London). Owner: Isaac Adekunle.

Purpose: to record every problem found in the project (a defect, a wrong claim, a gap in a test, a security report, a reviewer finding, a near miss), its cause, what was done, and that the fix worked. Each closed item should leave a new or changed test where possible.

## 1. Template

```
ID: CA-nnnn
Date opened (Europe/London):
Source: (reviewer, test, security advisory, own review)
Area:
Description:
Severity: critical / high / medium / low (critical = could let a clean-looking result appear after an incomplete or wrong review)
Root cause:
Containment (what was done at once):
Corrective action:
Owner:
Due:
Verification (test ID and result):
Date closed and by whom:
```

## 2. Open items

Items found while preparing the Stage 0 freeze (4 and 5 Nov 2026) that are still open. "Pre-freeze review" refers to the author's private working notes, which are not part of this repository.

| ID | Opened | Area | Description | Severity | Root cause | Action | Owner | Due | Source |
|---|---|---|---|---|---|---|---|---|---|
| CA-0011 | 2026-11-04 | Repository settings | GitHub private vulnerability reporting must be switched on for the reporting route in `SECURITY.md` to work. | Medium | Manual setting | Open: Isaac to switch it on before the repository is made public or the first release (T55 manual item). | Isaac | Before release | T55 |
| CA-0012 | 2026-11-05 | Human review (T56) | The three human reviewers (B1 certifying engineer, CAMO or quality, security) are not appointed. They are required before any public claim about results or any public release. | High | No funding or recruitment yet | Open: to be funded through grants. Stage 0 proceeds without them. Competence recorded in `competence-records.md` when appointed. | Isaac | Before any public claim about results | T56, T66 |
| CA-0013 | 2026-11-05 | Reproducibility (T01) | The generated data are verified byte-identical only on Python 3.13.5. Other Python versions and platforms were not tested. | Low | Single development environment | Open: re-run `data/generate.py` on a second Python version and platform, and log the result. A difference is logged in `docs/amendments.md`. | Isaac | Before results are published | T01 |
| CA-0014 | 2026-11-05 | Tool manifest (T64) | The tool-name prefix for the MCP manifest is not yet chosen. | Low | Decision pending | Open: Isaac to choose the prefix before the manifest is built; T64 then pins it. | Isaac | Before the manifest is built | T64 |

## 3. Closed items

Closed on 5 Nov 2026 (Europe/London) by Isaac Adekunle, as part of the T01 freeze. Where possible each closure left a check in `tools/check_data.py` or `tools/check_docs.py`.

| ID | Opened | Area | Description | Severity | Root cause | Action taken | Closed | Source |
|---|---|---|---|---|---|---|---|---|
| CA-0001 | 2026-11-04 | Generated data (`data/generate.py`) | In seeded packages that carry a missing-sign-off fault, the task is forced to safety-critical, while the clean twin keeps its random safety-critical flag. A model or reader could learn the tell instead of reading the record. | Medium | Generator sets the flag only on the faulty side | Flags are set before the twin copy, so a seeded package and its clean twin differ only in the planted records. `tools/check_data.py` asserts this for every twin (it never differs on the safety-critical flag). Data regenerated; manifest updated. | 2026-11-05 | pre-freeze review item 9 |
| CA-0002 | 2026-11-04 | Plan wording (T07, README) | T07 says 'beyond limit'; the README says 'at or beyond'. The generator never plants exactly-at-limit and treats a deferral expiring today as in date. | Medium | Boundary rule not decided | Frozen (T07, README, T01): a part at or above its limit is a fault; a deferral expiring today counts as expired; an overdue directive is due before the reference date. Boundary cases are planted on both sides. A directive due exactly on the reference date and a task due exactly now are not planted and not tested; behaviour is undefined. | 2026-11-05 | pre-freeze review item 2 |
| CA-0003 | 2026-11-04 | Plan wording (T12) | T12 says 'anywhere', but the plan, README, lexicon and the regulatory documents must quote the forbidden phrases, so they would fail. Some lexicon patterns (cleared, serviceable, approved for, signed off) may hit ordinary defect text. | Medium | No documentation exemption list | T12 scope set to text the tool writes (model output, CLI strings, report templates, errors, log schema, MCP tool descriptions). Documents, README and input data are out of scope. `python3 tools/check_docs.py lexicon` checks the frozen tool strings and reports document hits for information only. A proposed exemption for record values quoted in a marked citation is stated in the lexicon scope. | 2026-11-05 | pre-freeze review item 3 |
| CA-0004 | 2026-11-04 | Preregistration design | The sealed key is not truly sealed: the generator and seed are public and deterministic, so anyone can regenerate the key. | High | Public deterministic generator | A secret salt is mixed into the generator streams. Only the SHA-256 fingerprints of the salt and the key are published at the freeze; the salt and key are published with the results. The key was regenerated and the earlier unsalted key was withdrawn. Residual risk: the salt is one file; its loss would stop the data being regenerated. | 2026-11-05 | pre-freeze review item 1 |
| CA-0005 | 2026-11-04 | Plan definitions | Undefined terms: 'repeat defect' (generator uses 3 or more, near-miss 2), the T11 'upper 95% bound' method, and how T08 checks '0 values for a withheld path'. | Medium | Terms not defined in the plan | Defined in the plan: a repeat defect is the same ATA chapter and description three or more times (two is a near miss); T11 uses the one-sided 95% Clopper-Pearson upper bound; T08 checks the exact field paths of withheld fields. | 2026-11-05 | pre-freeze review item 4 |
| CA-0006 | 2026-11-04 | Test data (T63) | The sealed key and generator have no fault class for suspected unapproved parts, so T63 has no data. | Medium | Class not in the key | The suspected-unapproved-parts fault class was added to the main generator (set `t63_sup`, 56 packages) with the same seed and a regenerated sealed key, before the freeze. No amendment was needed. | 2026-11-05 | T63 |
| CA-0007 | 2026-11-04 | Report wording (T50) | The status `REVIEW INCOMPLETE - checks could not finish; do not rely on this report` implies a ready / not-ready binary that could be read as a readiness verdict. The companion status is `REVIEW COMPLETE - findings listed; a certifying engineer decides`. | Low | Wording trade-off between clarity and implied verdict | Wording confirmed and frozen: `REVIEW COMPLETE - findings listed; a certifying engineer decides` and `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`. Exit code 3 for incomplete. Neither matches the T12 lexicon and neither is a readiness verdict (checked by `tools/check_docs.py lexicon`). | 2026-11-05 | T50, T59 |
| CA-0008 | 2026-11-04 | Fail-safe boundary (T50, T08) | The boundary between 'missing data is a finding' and 'a check could not run, so REVIEW INCOMPLETE' is a proposal. It decides what the T08 withheld-field packages must output. | Medium | Boundary not decided | Boundary confirmed and frozen: a gap in the record is a finding; a check that could not run gives REVIEW INCOMPLETE. See `docs/security/planted-failure-set-spec.md` section 3. | 2026-11-05 | T08, T50 |
| CA-0009 | 2026-11-04 | Open plan items | T44 (median of 5 minutes or less), the T47 rule, T37 and per-stage spending limits are still proposals; fallback models are not named; the T11 corpus, T06 fabrication set and T09 prompt set are not generated. | Medium | Items left open | Items marked 'set before that stage' in the plan and logged in `docs/amendments.md` when set. The T06 (25 fabrications), T09 (40 prompts) and T11 (60 payloads x 3 positions) corpora are generated and fingerprinted. Fallback model names and the T47 rule are set at Freeze 2 and are still open until then. | 2026-11-05 | pre-freeze review items 5, 6, 8 |
| CA-0010 | 2026-11-04 | Preregistration (tag) | The preregistration text says the tag is 'signed by Isaac'. A signed tag needs Isaac's own key. A TODO comment marks the decision as pending. | Low | Decision pending | Decided: an unsigned annotated tag plus an OpenTimestamps proof and a public post of the fingerprint by Isaac. `docs/preregistration.md` rewritten to match; the TODO is removed. The tag, the proof and the post are made only after Isaac's go-ahead. | 2026-11-05 | pre-freeze review section 4 |
