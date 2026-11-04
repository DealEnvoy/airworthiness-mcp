# Security policy and vulnerability disclosure

Author: Isaac Adekunle. Date: 4 Nov 2026 (Europe/London). Status: written before the software exists; applies from the first public release of any code.

## 1. How to report a vulnerability

Use **GitHub private security advisories** for this repository: open the repository's **Security** tab and choose **Report a vulnerability**. This creates a private report that only the maintainer and you can see.

* Please do **not** post details in a public issue, a discussion or social media.
* If the "Report a vulnerability" option is not visible, open a public issue that says only that you have a security report and asks for a private channel. Do not include any detail of the problem. (Private vulnerability reporting must be switched on before the first release; this is on the maintainer's checklist, test T55.)
* No e-mail address, telephone number or chat account is offered for reports. The advisory route is the only one.

A good report says: what you found, the version or commit, how to reproduce it (a minimal record file is ideal), and what you think the impact is.

## 2. What is in scope

* The server and its parsers, the transport, the tool manifest, the audit log, report integrity, the rules engine and the optional language-model module, as described in [`threat-model.md`](threat-model.md).
* The build, CI and release process (signing, hashes, dependencies).
* A way to make the tool give `REVIEW COMPLETE - findings for human review` when it should have given `NOT READY - review incomplete`.
* A way to make the tool output a release, serviceability or airworthiness conclusion, to sign or approve anything, to read or write outside its configured directories, or to open a network connection in the default configuration.

Particularly serious: anything that lets a hostile record, client or model make a missing or wrong record look clean to a reader.

## 3. What is not in scope

* Whether a maintenance record is true. The tool checks completeness; it cannot tell that a record was forged before it arrived.
* Weaknesses in the host machine, the MCP client application, other MCP servers in the same host, or a language model run by someone else.
* Findings that need an attacker who already has write access to the audit log directory and the report directory and rewrites both consistently (documented limit; see T13 and T54), unless the report claims otherwise.
* Reports about real aircraft records: the project uses synthetic data only. Please do not send real records.

## 4. What to expect

This is a one-person project. There is no service level agreement and no bug bounty.

| Step | Target |
|---|---|
| Acknowledge the report | within 7 days |
| First assessment (severity, accepted or not) | within 21 days |
| Fix or mitigation for a high or critical issue | as soon as practical; a status update at least every 30 days |
| Public advisory after a fix | coordinated with you; default no later than 90 days after the report, sooner when a fix is released |

These are targets, not promises. Credit is given in the advisory if you want it.

## 5. Severity and handling

Severity is rated high, medium or low by impact on the safety-relevant property: a clean-looking result after an incomplete or tampered review is the worst case. Every accepted report becomes a corrective action in [`../quality/corrective-action-log.md`](../quality/corrective-action-log.md) and, where possible, a new test.

## 6. Supported versions

No release exists yet. When one does, only the latest release is supported. This is a research prototype and must not be used for real aircraft or real release decisions.

## 7. Safe harbour

Good-faith research on your own copy of the code, using synthetic data, is welcome. Please do not test against other people's systems, and do not access or keep data that is not yours.

## 8. Related documents

* [`threat-model.md`](threat-model.md): STRIDE, OWASP Top 10 for LLM Applications and MCP-specific risks, each with a mitigation and a test.
* [`planted-failure-set-spec.md`](planted-failure-set-spec.md) and [`fuzz-corpus-spec.md`](fuzz-corpus-spec.md): the fail-safe and fuzz test specifications.
* [`standards-mapping.md`](standards-mapping.md): alignment, not compliance.
* [`../regulatory-path.md`](../regulatory-path.md): regulatory position (not legal advice).
