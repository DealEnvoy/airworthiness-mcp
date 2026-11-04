# Quality policy

Author: Isaac Adekunle (15+ years in aircraft maintenance). Date: 4 Nov 2026 (Europe/London). Status: draft groundwork, written before the software exists.

## 1. Scope

This policy covers the design, build, test and release of **airworthiness-mcp**: an open-source, read-only, advisory Python MCP server that checks maintenance work packages and records for completeness and reports findings for a human to read.

**Intended purpose (frozen statement):** "Advisory checker of maintenance records and work packages. Read-only. Does not certify, release, or determine airworthiness. A certifying human decides."

In scope: the rules engine, the parsers, the transport, the audit log, the reports, the optional language-model module, the tests and test data, the documentation, and the release process.

Out of scope: maintaining aircraft; any decision to release an aircraft; any real aircraft record (Stage 0 uses synthetic data only); the quality system of any organisation that adopts the tool.

## 2. What the tool never does

* It never certifies, releases, approves, signs or determines airworthiness. A certifying human decides (`docs/regulatory-path.md`).
* It never outputs a release, serviceability or airworthiness conclusion (T09, T12, T59).
* It never scores or ranks individual people (T60).
* It never presents a clean result after a failed or partial review (T50).
* It never sends data anywhere unless an operator explicitly configures it, and it has no telemetry (T62).
* It never changes, writes or deletes the records it reads.
* It is never described as certified, approved or compliant. The wording is "aligned with" and "designed to support".

## 3. Quality commitments

1. **Requirements first.** Requirements are written and traced to a source and a test before code (`traceability.md`).
2. **Tests fixed before results.** Pass and fail criteria are frozen and fingerprinted before any test runs (`docs/preregistration.md`). Changes after the freeze are logged amendments.
3. **Hard fails have no waiver.** One failure of a safety-relevant test is a failure.
4. **Independent review.** A certifying-engineer reviewer, a CAMO or quality reviewer and a security reviewer review the tool before any public release (T56). Reviewer competence is recorded (`competence-records.md`).
5. **Controlled release.** Nothing is released until the evidence exists and Isaac has signed off (`release-control.md`, T66).
6. **Risks and problems are recorded and closed.** `risk-register.md` and `corrective-action-log.md` are kept up to date, with root causes and a new test for each problem.
7. **Human factors.** Reports are designed so that a tired reader is not misled (`human-factors-note.md`, T65).
8. **Suspected unapproved parts awareness.** The parts checks raise documentary indicators for a human to review; they never conclude (`suspected-unapproved-parts-awareness.md`, T63).
9. **Honesty about evidence.** Third-party figures are labelled as reported; regulatory statements are Isaac's reading, with sources; unverified items are flagged [N].

## 4. Roles

| Role | Holder | Responsibility |
|---|---|---|
| Author, owner of this policy, release approver | Isaac Adekunle | everything above; signs off every release |
| Certifying-engineer reviewer (B1 background) | not yet appointed | review of reports and rules against practice |
| CAMO / quality reviewer | not yet appointed | review of records handling, wording and procedure fit |
| Security reviewer | not yet appointed | threat-model review; code review and penetration test (parser, transport, audit log) |

Build tools (AI models used under the method in `docs/methods.md`) are tools, not roles with authority.

## 5. Certification: not claimed

Certification to ISO 9001, AS9110 or ISO/IEC 27001 is awarded to an **organisation** by a certification body. This project is a single-author open-source repository and is **not certified to any standard**. A future company (Drew & Crew Ltd) may consider certification through a UKAS-accredited certification body. That is not claimed, planned to a date or promised. The documents in `docs/quality/` are groundwork that would be useful if that decision is taken. AS9110C is voluntary and aimed at maintenance organisations (`docs/regulatory-path.md`).

## 6. Review

This policy is reviewed before each release and at each risk-register review. Last review: 4 Nov 2026 (first draft).
