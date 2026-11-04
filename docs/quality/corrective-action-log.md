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

## 2. Known issues at 4 Nov 2026

These are real issues found while preparing the Stage 0 freeze. All are open. "Pre-freeze review" refers to the author's private working notes, which are not part of this repository.

| ID | Opened | Area | Description | Severity | Root cause | Action | Owner | Due | Source |
|---|---|---|---|---|---|---|---|---|---|
| CA-0001 | 2026-11-04 | Generated data (`data/generate.py`) | In seeded packages that carry a missing-sign-off fault, the task is forced to safety-critical, while the clean twin keeps its random safety-critical flag. A model or reader could learn the tell instead of reading the record. | Medium | Generator sets the flag only on the faulty side | Open: decision pending (pre-freeze review item 9); align the twin so twin and fault differ only in the fault. If changed, regenerate the 158 packages and the manifest, and re-hash before the freeze. | Isaac | Before freeze | pre-freeze review item 9 |
| CA-0002 | 2026-11-04 | Plan wording (T07, README) | T07 says 'beyond limit'; the README says 'at or beyond'. The generator never plants exactly-at-limit and treats a deferral expiring today as in date. | Medium | Boundary rule not decided | Open: Isaac to confirm both boundary rules before the freeze; then align the README and T07. | Isaac | Before freeze | pre-freeze review item 2 |
| CA-0003 | 2026-11-04 | Plan wording (T12) | T12 says 'anywhere', but the plan, README, lexicon and the regulatory documents must quote the forbidden phrases, so they would fail. Some lexicon patterns (cleared, serviceable, approved for, signed off) may hit ordinary defect text. | Medium | No documentation exemption list | Open: Isaac to define a documentation exemption list and review broad patterns. | Isaac | Before freeze | pre-freeze review item 3 |
| CA-0004 | 2026-11-04 | Preregistration design | The sealed key is not truly sealed: the generator and seed are public and deterministic, so anyone can regenerate the key. | High | Public deterministic generator | Open: Isaac to choose. Recommended: freeze a hash of a secret salt mixed into the seed and publish the salt with the results. Alternatives: keep the generator private until results are out, or accept and state the limit. | Isaac | Before freeze | pre-freeze review item 1 |
| CA-0005 | 2026-11-04 | Plan definitions | Undefined terms: 'repeat defect' (generator uses 3 or more, near-miss 2), the T11 'upper 95% bound' method, and how T08 checks '0 values for a withheld path'. | Medium | Terms not defined in the plan | Open: Isaac to define each before the freeze. | Isaac | Before freeze | pre-freeze review item 4 |
| CA-0006 | 2026-11-04 | Test data (T63) | The sealed key and generator have no fault class for suspected unapproved parts, so T63 has no data. | Medium | Class not in the key | Open: a logged amendment adds `data/generate_sup.py` (specified in `docs/security/fuzz-corpus-spec.md` section 6) before T63 runs. | Isaac | Before T63 | T63 |
| CA-0007 | 2026-11-04 | Report wording (T50) | The status `NOT READY - review incomplete` implies a ready / not-ready binary that could be read as a readiness verdict. The companion status is `REVIEW COMPLETE - findings for human review`. | Low | Wording trade-off between clarity and implied verdict | Open: Isaac to confirm the exact wording before the freeze (it is frozen by T01). T12 does not match 'NOT READY' today. | Isaac | Before freeze | T50, T59 |
| CA-0008 | 2026-11-04 | Fail-safe boundary (T50, T08) | The boundary between 'missing data is a finding' and 'a check could not run, so NOT READY' is a proposal. It decides what the T08 withheld-field packages must output. | Medium | Boundary not decided | Open: Isaac to confirm the proposal in `docs/security/planted-failure-set-spec.md` section 3. | Isaac | Before freeze | T08, T50 |
| CA-0009 | 2026-11-04 | Open plan items | T44 (median of 5 minutes or less), the T47 rule, T37 and per-stage spending limits are still proposals; fallback models are not named; the T11 corpus, T06 fabrication set and T09 prompt set are not generated. | Medium | Items left open | Open: freeze as numbers, or write that each is set before its stage and logged as an amendment. | Isaac | Before freeze | pre-freeze review items 5, 6, 8 |
| CA-0010 | 2026-11-04 | Preregistration (tag) | The preregistration text says the tag is 'signed by Isaac'. A signed tag needs Isaac's own key. A TODO comment marks the decision as pending. | Low | Decision pending | Open: signed tag, or an unsigned annotated tag plus an external timestamp with the text edited to match. | Isaac | Before tag | pre-freeze review section 4 |
| CA-0011 | 2026-11-04 | Repository settings | GitHub private vulnerability reporting must be switched on for the reporting route in `SECURITY.md` to work. | Medium | Manual setting | Open: Isaac to switch it on before the repository is made public or the first release (T55 manual item). | Isaac | Before release | T55 |

## 3. Closed items

None yet.
