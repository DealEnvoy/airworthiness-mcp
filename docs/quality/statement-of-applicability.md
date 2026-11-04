# Statement of applicability (ISO/IEC 27001:2022 Annex A): groundwork

Date: 4 Nov 2026 (Europe/London). Owner: Isaac Adekunle. Status: **groundwork, largely incomplete; not an ISMS and not for certification.**

**Alignment, not compliance. No certification is claimed.** ISO/IEC 27001 certification is for an organisation's information security management system, awarded by a certification body. This project is a single-author open-source repository, not an organisation. A future company (Drew & Crew Ltd) may consider certification through a UKAS-accredited certification body; that is not claimed or promised. This table is groundwork that organises the Annex A themes and shows what the project's design already supports.

Source of control names: the 93 Annex A controls in four themes (A.5 Organizational 37, A.6 People 8, A.7 Physical 14, A.8 Technological 34). Titles are taken from the published contents of ISO/IEC 27002:2022 as listed at https://iso27001partners.co.uk/iso-27001-annex-a-controls/ **[S]** and cross-checked against two other public lists; the standard itself is a paid document and was **not read**. No control text or guidance is reproduced or paraphrased beyond the titles. "How met or planned" describes what this project does or intends, not what the control requires.

Status words: **Designed** = a design commitment with a frozen test; **Planned** = intended, not yet specified as a test; **To complete** = not yet worked out; **Not applicable now** = reason given, revisit on change. Nothing is implemented yet because nothing is built.

Scope for this statement: the airworthiness-mcp repository, its tests and test data, its build and release process, and the author's development machines. Risk assessment that would normally decide applicability is in `risk-register.md` (first draft).

## A.5 Organizational controls (37)

| Control | Title | Applicable | How met or planned | Evidence | Status |
|---|---|---|---|---|---|
| A.5.1 | Policies for information security | Yes | Quality policy and security policy (`SECURITY.md`) exist as drafts | quality-policy.md; SECURITY.md | Planned |
| A.5.2 | Information security roles and responsibilities | Yes | One author owns all roles; reviewer roles defined | quality-policy.md section 4; competence-records.md | Planned |
| A.5.3 | Segregation of duties | Yes | Author cannot approve own work: three independent reviewers before release | T56 | Designed |
| A.5.4 | Management responsibilities | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.5 | Contact with authorities | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.6 | Contact with special interest groups | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.7 | Threat intelligence | Yes | Watch advisories for dependencies and MCP guidance | T14; RV.1 in standards-mapping.md | Planned |
| A.5.8 | Information security in project management | Yes | Threat model and security tests written before the code | T49–T66 | Designed |
| A.5.9 | Inventory of information and other associated assets | Yes | Assets: source, test data, sealed key, hash list, audit log; list to be written | To complete | To complete |
| A.5.10 | Acceptable use of information and other associated assets | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.11 | Return of assets | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.12 | Classification of information | Yes | Stage 0 data is synthetic; classification of real adopter records is the adopter's | T62 | Planned |
| A.5.13 | Labelling of information | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.14 | Information transfer | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.15 | Access control | Yes | Tool is read-only with one configured package root | T53, T64 | Designed |
| A.5.16 | Identity management | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.17 | Authentication information | Yes | Sealed key held outside the repository; no secrets in CI | T01, T66 | Designed |
| A.5.18 | Access rights | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.19 | Information security in supplier relationships | Yes | Supplier relationships limited to hosted model providers used as build tools; no data of adopters is sent | docs/methods.md; T62 | Planned |
| A.5.20 | Addressing information security within supplier agreements | Not applicable now | No supplier agreements for the tool at Stage 0. Revisit if an organisation exists | – | Not applicable now |
| A.5.21 | Managing information security in the ICT supply chain | Yes | Pinned and hash-checked dependencies, SBOM, signed releases | T14, T48, T66 | Designed |
| A.5.22 | Monitoring, review and change management of supplier services | Yes | Review of supplier (model and dependency) changes between stages | T05, T18, T32 | Planned |
| A.5.23 | Information security for use of cloud services | Yes | No cloud service in the tool; hosted models only as build tools; optional remote LLM endpoint needs explicit configuration | T62 | Designed |
| A.5.24 | Information security incident management planning and preparation | Yes | Vulnerability handling via private advisories; corrective-action log | SECURITY.md; corrective-action-log.md | Planned |
| A.5.25 | Assessment and decision on information security events | Yes | Severity rating of reports | docs/security/SECURITY.md section 5 | Planned |
| A.5.26 | Response to information security incidents | Yes | Response targets and withdrawal rule | docs/security/SECURITY.md; release-control.md section 5 | Planned |
| A.5.27 | Learning from information security incidents | Yes | Root cause and new test for each corrective action | corrective-action-log.md | Planned |
| A.5.28 | Collection of evidence | Yes | Audit log and report fingerprints preserve evidence of what was checked | T13, T54 | Designed |
| A.5.29 | Information security during disruption | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.30 | ICT readiness for business continuity | To complete | To complete: depends on an organisation that does not exist yet | – | To complete |
| A.5.31 | Legal, statutory, regulatory and contractual requirements | Yes | Regulatory position documented, marked not legal advice | docs/regulatory-path.md; docs/ai-act-self-assessment.md | Designed |
| A.5.32 | Intellectual property rights | Yes | MIT licence; dependency licences to be listed in the SBOM | LICENSE; T14 | Planned |
| A.5.33 | Protection of records | Yes | Audit log and reports protected from alteration (tamper-evident) | T13, T54 | Designed |
| A.5.34 | Privacy and protection of PII | Yes | Synthetic data only; data-protection checklist before any real data | T14, T62 | Planned |
| A.5.35 | Independent review of information security | Yes | Independent human security review before release | T56 | Designed |
| A.5.36 | Compliance with policies, rules and standards for information security | Yes | Release gate checks policies and tests | T66 | Designed |
| A.5.37 | Documented operating procedures | Yes | Operating procedures documented in README and release-control | release-control.md | Planned |

## A.6 People controls (8)

| Control | Title | Applicable | How met or planned | Evidence | Status |
|---|---|---|---|---|---|
| A.6.1 | Screening | To complete | To complete | – | To complete |
| A.6.2 | Terms and conditions of employment | To complete | To complete | – | To complete |
| A.6.3 | Information security awareness, education and training | Yes | Contributors read threat model and regulatory documents; record kept | competence-records.md section 5 | To complete |
| A.6.4 | Disciplinary process | To complete | To complete | – | To complete |
| A.6.5 | Responsibilities after termination or change of employment | To complete | To complete | – | To complete |
| A.6.6 | Confidentiality or non-disclosure agreements | Yes | Reviewers agree confidentiality terms before seeing non-public material | competence-records.md | Planned |
| A.6.7 | Remote working | Yes | Development done on personal machines; guidance to be written | To complete | To complete |
| A.6.8 | Information security event reporting | Yes | Security events reported through private advisories | SECURITY.md | Planned |

## A.7 Physical controls (14)

| Control | Title | Applicable | How met or planned | Evidence | Status |
|---|---|---|---|---|---|
| A.7.1 | Physical security perimeters | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.2 | Physical entry | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.3 | Securing offices, rooms and facilities | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.4 | Physical security monitoring | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.5 | Protecting against physical and environmental threats | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.6 | Working in secure areas | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.7 | Clear desk and clear screen | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.8 | Equipment siting and protection | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.9 | Security of assets off-premises | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.10 | Storage media | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.11 | Supporting utilities | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.12 | Cabling security | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.13 | Equipment maintenance | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |
| A.7.14 | Secure disposal or re-use of equipment | To complete | To complete: depends on the premises and equipment of a future organisation; Stage 0 runs on personal development machines | – | To complete |

## A.8 Technological controls (34)

| Control | Title | Applicable | How met or planned | Evidence | Status |
|---|---|---|---|---|---|
| A.8.1 | User endpoint devices | To complete | To complete | – | To complete |
| A.8.2 | Privileged access rights | Yes | The tool has no privileged operation; it runs with the launching user's rights | T51, T64 | Designed |
| A.8.3 | Information access restriction | Yes | Only the configured package root is readable; canary files test it | T53 | Designed |
| A.8.4 | Access to source code | Yes | Branch protection and sealed key outside repository; planned access control on the repository | T01 | Planned |
| A.8.5 | Secure authentication | Yes | Repository access with multi-factor authentication for maintainers (to be confirmed) | To complete | To complete |
| A.8.6 | Capacity management | Yes | Fixed size, time and memory limits | T53, T50 | Designed |
| A.8.7 | Protection against malware | Yes | Parsers accept data only; no execution; archives refused | T53 | Designed |
| A.8.8 | Management of technical vulnerabilities | Yes | Dependency audit; advisory process | T14 | Designed |
| A.8.9 | Configuration management | Yes | Pinned toolchain; rule-set and manifest hashes checked at start-up | T14, T64 | Designed |
| A.8.10 | Information deletion | Yes | The tool stores no record data; audit log holds identifiers and hashes only | T54, T62 | Designed |
| A.8.11 | Data masking | Yes | Stage 0 uses synthetic data; masking is not needed in the tool; adopters use their own | T62 | Planned |
| A.8.12 | Data leakage prevention | Yes | No egress; no telemetry; output limited to cited fields | T62, T53 | Designed |
| A.8.13 | Information backup | Yes | Source in version control; audit-log backup is the operator's | To complete | To complete |
| A.8.14 | Redundancy of information processing facilities | To complete | To complete | – | To complete |
| A.8.15 | Logging | Yes | Hash-chained audit log of every run | T13 | Designed |
| A.8.16 | Monitoring activities | Yes | Operator reads the log; no remote monitoring (no telemetry) | T62 | Planned |
| A.8.17 | Clock synchronization | Yes | Audit entries carry time in a stated zone (Europe/London) and UTC offset | T13 | Planned |
| A.8.18 | Use of privileged utility programs | To complete | To complete | – | To complete |
| A.8.19 | Installation of software on operational systems | To complete | To complete | – | To complete |
| A.8.20 | Networks security | Yes | No network listener or connection | T51, T10 | Designed |
| A.8.21 | Security of network services | Yes | No network services used | T51, T62 | Designed |
| A.8.22 | Segregation of networks | Not applicable now | No network components; revisit if HTTP mode is ever added (T52) | T52 | Not applicable now |
| A.8.23 | Web filtering | Not applicable now | The tool makes no web requests | T62 | Not applicable now |
| A.8.24 | Use of cryptography | Yes | SHA-256 hashes for integrity; signing of releases; no encryption of data is implemented; any future HTTP mode requires TLS | T14, T52, T54 | Designed |
| A.8.25 | Secure development life cycle | Yes | Pre-registered test plan, threat model, security tests, independent review | docs/trial-plan.md | Designed |
| A.8.26 | Application security requirements | Yes | Security requirements are tests T49–T66 | docs/trial-plan.md section 3a | Designed |
| A.8.27 | Secure system architecture and engineering principles | Yes | Fail-safe, least-privilege, stdio-only, rules-engine core | T50, T51, T57 | Designed |
| A.8.28 | Secure coding | Yes | Strict parsing, no unsafe deserialisation, static analysis in CI | T47, T48, T53 | Designed |
| A.8.29 | Security testing in development and acceptance | Yes | Fuzzing, planted failures, tamper tests, transport tests, human penetration test | T50, T51, T53, T54, T56 | Designed |
| A.8.30 | Outsourced development | Yes | AI build tools are used as tools under independent review; no outsourced development | docs/methods.md; T25, T33 | Planned |
| A.8.31 | Separation of development, test and production environments | Yes | Tests run in sandboxed copies of synthetic data; no production environment exists | T53 | Planned |
| A.8.32 | Change management | Yes | Changes after the freeze are logged amendments; release record; changelog | docs/preregistration.md; release-control.md | Designed |
| A.8.33 | Test information | Yes | Test data is synthetic and generated deterministically | data/generate.py | Designed |
| A.8.34 | Protection of information systems during audit testing | Yes | Fuzz and penetration tests run on copies, never on live adopter data | T53, T56 | Planned |

## Summary

| Status | Controls |
|---|---|
| Designed | 30 |
| Not applicable now | 3 |
| Planned | 22 |
| To complete | 38 |
| **Total** | **93** |

## Next steps

1. Complete the **To complete** rows once there is an organisation and premises, or mark them not applicable with a reason.
2. Tie each applicable control to a risk in `risk-register.md`.
3. Have the security reviewer (R3, `competence-records.md`) read this table.
4. Do not describe the project as certified, compliant or accredited against ISO/IEC 27001 at any point.
