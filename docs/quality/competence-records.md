# Competence records

Date: 4 Nov 2026 (Europe/London). Owner: Isaac Adekunle. Used by T56 and `release-control.md`.

Purpose: to record who reviewed what, with what background, how they were chosen, and that they were independent. **No reviewer has been appointed yet; no review has taken place.** Records are kept only with the reviewer's permission; names and employers are published only if the reviewer agrees.

Reviewers' comments are feedback on a research prototype. They are not an approval, audit or certification.

## 1. Required reviewers

| Slot | Background required | Scope | Status |
|---|---|---|---|
| R1 | A B1 certifying engineer (Part-66 B1 / Part-145 certifying background) | Rules and reports against practice; wording; usefulness; misreading risk | Not yet appointed |
| R2 | CAMO or quality background | Records handling, procedure fit, wording, corrective-action process, release control | Not yet appointed |
| R3 | Security reviewer (human) | Threat-model review; code review and penetration test of the parser, the transport, the audit log, report integrity and the tool manifest | Not yet appointed |

Independence rule: a reviewer is not the author, does not work for the author, and is not an AI build tool. Reviewers work from the frozen release-candidate commit.

## 2. Record template (one per reviewer)

```
Reviewer slot: R1 / R2 / R3
Name (or "anonymous at reviewer's request"):
Current role and organisation (if permitted to publish):
Relevant experience (years and type; no claim is made on the reviewer's behalf):
Licences or qualifications held (as stated by the reviewer; not checked by the author):
Evidence of competence seen (for example CV, references, published work):
Independence declaration (relationship to author; any payment; any conflict):
Scope agreed and checklist version:
Commit reviewed (full hash):
Date(s) of review (Europe/London):
Time spent:
Findings: ID, severity (critical / high / medium / low), description, evidence, recommendation
Author's response to each finding and date:
Re-test after fixes (date, result):
Permission to quote comments: yes / no / limited to ...
Permission to publish name: yes / no
Reviewer signature or statement:
```

## 3. Competence criteria (proposed)

* R1: holds, or has held, Part-66 B1 certifying privileges or an equivalent certifying role, and has certified work packages in practice.
* R2: has worked in a CAMO, a Part-145 quality department or an equivalent compliance role, including audit or records review.
* R3: has demonstrable experience in application security, for example penetration testing, secure code review or vulnerability research, and is able to review Python code and an MCP server.

The criteria are proposals for Isaac to confirm. Because the author is not recruiting for a regulated role, nothing here is a qualification scheme.

## 4. The author

Isaac Adekunle: 15+ years in aircraft maintenance. The author's own experience is stated in the README. The author is not an independent reviewer of his own work.

## 5. Training and awareness

For the author and any contributor: read `docs/regulatory-path.md`, `docs/security/threat-model.md` and `human-factors-note.md` before contributing code that changes a rule, a report or a tool. Record the date read here. **To complete.**
