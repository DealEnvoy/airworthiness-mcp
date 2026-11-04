# Standards mapping: alignment, not compliance

Date: 4 Nov 2026 (Europe/London). Author: Isaac Adekunle.

**Alignment, not compliance.** This page shows how the project's design and tests line up with several security standards and frameworks. It does not say that the tool or the project meets, is certified to, or has been assessed against any of them. No audit has taken place. The mapping is Isaac's reading, is not legal advice, and is a design-stage plan: nothing has been built or run. Items marked [N] are not verified from an official source.

How to read the status columns: **Designed** = a design commitment with a frozen test in `docs/trial-plan.md`; **Planned** = intended but not yet specified as a test; **To complete** = not yet worked out; **Not applicable** = reason given.

Certification to ISO standards is for an organisation. The project is not an organisation and claims none. A future company (Drew & Crew Ltd) may consider certification through a UKAS-accredited certification body; that is not claimed or promised (`docs/quality/quality-policy.md`).

## 1. OWASP Top 10 for LLM Applications (2025): alignment, not compliance

Source: https://genai.owasp.org/llm-top-10/ (list names as published for the 2025 edition). The optional LLM module is off by default; the rules-engine core uses no model. Threat rows are in `threat-model.md`.

| Risk | Name | How the design lines up | Tests | Threat rows | Status |
|---|---|---|---|---|---|
| LLM01 | Prompt Injection | The core reads no model. The optional module treats all record text as data, quotes it in labelled delimiters, validates output against a schema, and cannot remove a rule finding. Tested with a stub hostile model. | T11, T38, T45 | TM-21, TM-39, TM-62 | Designed |
| LLM02 | Sensitive Information Disclosure | Local-first; no egress or telemetry; remote endpoint only by explicit setting with a warning in the report; audit log holds identifiers and hashes, no record text. | T38, T42, T62, T45 | TM-22, TM-40 | Designed |
| LLM03 | Supply Chain | Hash-pinned dependencies, SBOM, minimal dependencies; local model weights hash-pinned and served model id logged. | T14, T48, T42, T05 | TM-47, TM-63 | Designed |
| LLM04 | Data and Model Poisoning | No training, no fine-tuning, no retrieval store; third-party models used as supplied. | T57 | TM-48 | Designed |
| LLM05 | Improper Output Handling | Model output is schema-validated, rejected not repaired, and cannot change the rule layer; reports escape control characters and markup. | T45, T57, T40, T11, T53 | TM-42, TM-60 | Designed |
| LLM06 | Excessive Agency | Only read-only tools exist; no sign, approve, release, write or fetch tool; adversarial prompts must not reach any other tool. | T09, T41, T64, T45 | TM-43 | Designed |
| LLM07 | System Prompt Leakage | The system prompt holds no secrets and is public in the open-source repository. | T09, T45 | TM-46 | Designed |
| LLM08 | Vector and Embedding Weaknesses | Not applicable by design: no vector store or embeddings. Adding one needs an amendment, a threat row and tests. | T57 | TM-49 | Not applicable by design |
| LLM09 | Misinformation | Every citation is verified by code against recorded tool results; regulatory quotes must be verbatim substrings of the source bundle. | T06, T39 | TM-41 | Designed |
| LLM10 | Unbounded Consumption | Spending kill switch, time limits and input size limits. | T04, T44, T53 | TM-44 | Designed |

## 2. NIST SP 800-218, Secure Software Development Framework (SSDF) version 1.1: alignment, not compliance

Source: https://csrc.nist.gov/pubs/sp/800/218/final (Feb 2022; practice-group and practice names below follow that publication; a later revision is in draft and not used here **[N]**). The SSDF is a set of practices for software producers; it has no certification.

| Group | Practice | How the project lines up | Tests / documents | Status |
|---|---|---|---|---|
| PO: Prepare the Organization | PO.1 Define security requirements for software development | Threat model and security tests T49–T66 written before the code | T49, T55 | Designed |
| PO | PO.3 Implement supporting toolchains | Python safeguards gate in CI (formatter, type checker, static analysis, secret scan) | T48, T66 | Designed |
| PO | PO.5 Implement and maintain secure environments for software development | Sealed key kept outside the repository; least-privilege CI; no paid keys in CI | T01, T66 | Designed |
| PS: Protect the Software | PS.1 Protect all forms of code from unauthorized access and tampering | Frozen hash list and verify script; signed or timestamped tag (decision pending); protected branches before release | T01 | Designed (tag decision pending) |
| PS | PS.2 Provide a mechanism for verifying software release integrity | Signed release, published hashes, rule-set and tool-manifest hashes checked at start-up | T14, T64, T66 | Designed |
| PS | PS.3 Archive and protect each software release | Release record per release | T66, `docs/quality/release-control.md` | Designed |
| PW: Produce Well-Secured Software | PW.1 Design software to meet security requirements and mitigate security risks | Whole-system threat model; fail-safe design; stdio only | T49, T50, T51 | Designed |
| PW | PW.2 Review the software design | Independent design review; human security reviewer reviews the threat model | T24, T56 | Designed |
| PW | PW.4 Reuse existing, well-secured software | Minimal, pinned dependencies; SBOM; official MCP SDK for protocol framing | T14, T48 | Designed |
| PW | PW.5 Create source code by adhering to secure coding practices | Strict parsing, no unsafe deserialisation, banned-function static rules | T47, T48, T53 | Designed |
| PW | PW.6 Configure the compilation, interpreter, and build processes to improve executable security | Pinned toolchain; reproducible output; CI settings | T14, T48 | Planned |
| PW | PW.7 Review and/or analyze human-readable code | Code review by independent model reviewers and by a human security reviewer | T26, T46, T56 | Designed |
| PW | PW.8 Test executable code to identify vulnerabilities and verify compliance with security requirements | Fuzzing, planted failures, tamper tests, transport test | T50, T51, T53, T54 | Designed |
| PW | PW.9 Configure software to have secure settings by default | Module off by default; no network; read-only; limits on | T57, T62 | Designed |
| RV: Respond to Vulnerabilities | RV.1 Identify and confirm vulnerabilities on an ongoing basis | Dependency audit; reports through private advisories | T14, T55 | Designed |
| RV | RV.2 Assess, prioritize, and remediate vulnerabilities | Corrective-action log with severity | `docs/quality/corrective-action-log.md` | Designed |
| RV | RV.3 Analyze vulnerabilities to identify their root causes | Root cause field in every corrective action; new test added | `docs/quality/corrective-action-log.md` | Designed |

## 3. SLSA (Supply-chain Levels for Software Artifacts): alignment, not compliance

Source: https://slsa.dev/ (specification v1.2, Build track Levels 1 to 3 and Source track; read 4 Nov 2026). SLSA is a framework of levels; the project does not claim any level.

| Level or track | Meaning in short | Project position |
|---|---|---|
| Build L1 | Provenance exists | Target for the first release: a build-provenance record per release (commit, builder, hashes). Planned. |
| Build L2 | Hosted build platform signs provenance | Target before any public release, using a hosted CI platform. Planned. |
| Build L3 | Hardened, isolated builds | Not targeted in Stage 0. To complete: depends on the platform chosen. |
| Source track | Source-control practices | Version control, reviewed changes, protected branch, signed or timestamped freeze tag. Planned (tag decision pending). |

## 4. ISO/IEC 27001:2022 Annex A themes: alignment, not compliance

Source: ISO/IEC 27001:2022 Annex A has 93 controls in four themes (control titles are taken from the published contents of ISO/IEC 27002:2022 as listed by https://iso27001partners.co.uk/iso-27001-annex-a-controls/ **[S]**; the standard itself is paid and was not read). Control-level detail is in [`../quality/statement-of-applicability.md`](../quality/statement-of-applicability.md), which is largely marked **To complete**.

| Annex A theme | Controls | Project position | Status |
|---|---|---|---|
| A.5 Organizational controls | 37 | Policies, roles, supplier and supply-chain controls, incident handling, records. Partly designed for the repository; most need an organisation to exist. | Partly designed; rest to complete |
| A.6 People controls | 8 | Reviewer competence records and confidentiality for reviewers. | Planned |
| A.7 Physical controls | 14 | Depends on the premises and equipment of a future organisation. Stage 0 is run on personal development machines. | To complete |
| A.8 Technological controls | 34 | Most of the design work: access to source code, logging, secure development life cycle, secure coding, security testing, change management, vulnerability management, configuration management. | Designed in large part |

Honest limit: ISO/IEC 27001 certifies an organisation's information security management system. A single-author open-source repository is not one. Using the Annex A themes here is a way to organise the groundwork.

## 5. EASA Part-IS: support for adopting organisations (alignment, not compliance)

Sources: Implementing Regulation (EU) 2023/203 (applicable from 22 Feb 2026) and Delegated Regulation (EU) 2022/1645; EASA FAQ pages https://www.easa.europa.eu/en/faq/139283 and https://www.easa.europa.eu/en/faq/139292 (**[V]** for scope and dates as summarised in `docs/regulatory-path.md`; the EUR-Lex texts were not opened).

Part-IS binds **organisations in scope** (for example Part-145 and Part-CAMO organisations), **not the tool's author**. A Part-145 or CAMO organisation that adopts this tool would deal with it in its own information-security risk assessment, including interfaces with suppliers (EASA's Part-IS FAQ discusses supply-chain risk, IS.I.OR.205 and IS.I.OR.235). The project aims to make that assessment easy to do:

| What an adopting organisation will ask | What the project provides (designed) | Tests / documents |
|---|---|---|
| Where does data go? | Local-first, no egress, no telemetry; remote LLM endpoint only by explicit setting and flagged in the report | T62 |
| What can it access? | Read-only; one configured package root; no write, sign or approve tool | T09, T53, T64 |
| What does it store? | Audit log of identifiers, hashes and rule versions; no record text | T13, T54 |
| Who can change it, and how do I know the version? | Signed releases, SBOM, pinned dependencies, manifest and rule-set hashes printed in every report | T14, T64, T66 |
| How are vulnerabilities handled? | Private advisory route and a corrective-action process | `SECURITY.md`, T55 |
| What if it fails? | Fail-safe: `NOT READY - review incomplete`, never a clean report | T50 |
| Supplier information page | **Planned**: a short page for adopters (data handled, retention, logging, update process) | To complete |

Not claimed: that using the tool makes any organisation meet Part-IS. That is the organisation's responsibility.

## 6. What is not mapped

Standards that do not apply to a ground records-checking tool are listed in `docs/regulatory-path.md` (DO-178C, DO-200B / ED-76B, DO-330, ED-202A / DO-326A). ED-204A is not mapped.
