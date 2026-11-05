# Threat model: whole system

Draft of 4 Nov 2026 (Europe/London). Author: Isaac Adekunle. Status: **design-stage threat model for a tool that has not been built.** Every mitigation below is a design commitment tested by a Stage 0 test (T49–T66 and earlier). Nothing has been run. A human security reviewer reviews this document before any public release (T56).

## 1. Scope, assets and trust boundaries

**What is being protected.** (1) The truth of the review report: it must never be clean when the review was incomplete. (2) The integrity of the audit log and of reports. (3) The confidentiality of the records the tool reads (synthetic in Stage 0; possibly commercially sensitive for adopters later). (4) The tool's inability to sign, approve or release anything.

**Trust boundaries.**

* The **MCP client / host and its model** are untrusted callers. Anything they send is checked.
* **Record files and everything in them** are untrusted data, including text that looks like an instruction or an approval.
* The **optional LLM module**, if enabled, is untrusted: it is advisory and checked by code.
* The **operator** (the person who runs the tool, chooses the package root and the audit-log directory, and reads the report) is trusted to configure it. A certifying human reads the report and decides; the tool does not.
* The **build and release chain** is a trust boundary of its own (component C10).

**Out of scope for this tool.** Whether a record is true; the security of the host machine, the client application or the operator's network; the adopting organisation's own risk assessment. These are stated to adopters (see `docs/regulatory-path.md`).

**Method.** STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) across ten components, plus the OWASP Top 10 for LLM Applications (2025 edition) and MCP-specific risks. Sources: OWASP Top 10 for LLM Applications 2025, https://genai.owasp.org/llm-top-10/ ; MCP security best practices, https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices (confused deputy, token passthrough, SSRF, local MCP server compromise, scope minimisation; read 4 Nov 2026). Tool poisoning, tool-description injection, rug-pull changes and cross-server tool shadowing are named in community security research on MCP; no single official page for them was verified here, so those tags (MCP-TP, MCP-TDI, MCP-RP, MCP-SHADOW) are **[N] unverified as to source**; the risks themselves are handled regardless.

## 2. Components

| ID | Component |
|---|---|
| C1 | MCP client / host application |
| C2 | Transport |
| C3 | Tool calls (MCP tool surface) |
| C4 | Record files (input data) |
| C5 | Parsers |
| C6 | Rules engine |
| C7 | Optional LLM module |
| C8 | Audit log |
| C9 | Reports |
| C10 | Build, CI and supply chain |

## 3. Framework tags

| Tag | Meaning |
|---|---|
| LLM01 … LLM10 | OWASP Top 10 for LLM Applications 2025: LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Supply Chain; LLM04 Data and Model Poisoning; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM08 Vector and Embedding Weaknesses; LLM09 Misinformation; LLM10 Unbounded Consumption |
| MCP-TP | Tool poisoning |
| MCP-TDI | Tool-description injection |
| MCP-RP | Rug-pull (tool definitions change after approval) |
| MCP-CD | Confused deputy |
| MCP-EA | Excessive agency |
| MCP-TPT | Token passthrough and unauthenticated or unsecured HTTP (future mode) |
| MCP-SSRF | Server-side request forgery |
| MCP-LOC | Local MCP server compromise |
| MCP-SHADOW | Cross-server tool shadowing |

## 4. Threat register

Rule (T49): every row has a mitigation and at least one test ID that exists in `docs/trial-plan.md`. `tools/check_docs.py threat-model` checks this.

| ID | Component | STRIDE | Tag | Threat | Mitigation | Tests |
|---|---|---|---|---|---|---|
| TM-01 | C1 | S | MCP-LOC | A spoofed or malicious client, or a tampered client configuration, starts the server with an altered command (local MCP server compromise). | The server runs with the launching user's rights only and takes no credentials and no code-executing arguments. The exact start command and the release artefact hash are published; releases are signed. The client and host are outside the tool's control and this is stated to adopters. | T14, T51, T66 |
| TM-02 | C1 | R | – | A user denies having run a check, or no record shows which client asked. | Every run writes an audit-log entry (time in Europe/London, package id, input hashes, rule-set hash, report fingerprint, client name as reported by the client, treated as untrusted). | T13, T54 |
| TM-03 | C1 | I, E | MCP-CD | Confused deputy: a client or host with wider file access uses the server to read files outside the package it was meant to check. | No tool takes a free file path. Tools take a package id from the set found under one configured root; the root is canonicalised and symlinks pointing out of it are refused; access is read-only. | T53, T09, T45 |
| TM-04 | C1 | D | – | A client floods the server with calls or sends one call designed to exhaust resources. | Calls are processed one at a time under the section 3a limits (size, time, memory); over a limit ends in the REVIEW INCOMPLETE status. | T53, T50 |
| TM-05 | C1 | E | MCP-EA | Excessive agency: the host's own model chains tools to cause an effect (sign, approve, write, send). | The server has only read-only tools; there is no tool that signs, approves, releases, writes, deletes or updates. The tool manifest is checked statically and by adversarial prompts. | T09, T64, T41 |
| TM-06 | C1 | T | MCP-SHADOW | Cross-server tool shadowing: another server in the same host defines a tool with the same name or description that steers the model. | Tool names carry a fixed prefix and the manifest hash is published so adopters can pin it. The host's handling of multiple servers is outside the tool's control and is noted in the adopter guidance. | T64 |
| TM-07 | C2 | S, T, I | – | A network listener lets a remote party call tools or read records. | Stage 0 is stdio only. No host, port or transport option exists. No socket is opened. | T51, T52 |
| TM-08 | C2 | S, T, I, E | MCP-TPT | A future HTTP mode ships without authentication, with token passthrough, without TLS, or open to DNS rebinding or SSRF. | HTTP mode is blocked in the release. It can only be added by a logged amendment that requires authentication and authorisation per the MCP security guidance, TLS, Origin validation and its own tests passing first. | T52 |
| TM-09 | C2 | T | MCP-SSRF | Server-side request forgery: the server is induced to fetch internal or attacker-chosen URLs. | The server makes no outbound request and fetches no URL named in a record. Stage 0 has no OAuth discovery or any other fetch. | T51, T62 |
| TM-10 | C2 | T, S | – | Stdout contamination: record text or logs written to the protocol stream forge protocol messages. | Logs go to stderr or a file only. Record text appears only inside escaped JSON string fields produced by the protocol library. JSON-RPC look-alike text in records is in the fuzz corpus. | T53, T11 |
| TM-11 | C2 | D | – | An endless or very large message on stdin ties up the server. | Message size limit and the 30 s watchdog; over a limit ends in the REVIEW INCOMPLETE status or a refused request, never a hang. | T53, T50 |
| TM-12 | C3 | T, E | – | Tool arguments carry path traversal, injection or oversized values. | Strict Pydantic schemas with extra fields forbidden; package ids from an enumerated set; lengths capped. | T53, T48, T45 |
| TM-13 | C3 | E | – | A tool outside the allow-list exists or is added later (for example one that writes or approves). | Static manifest check, allow-list, and CI check on the manifest; adversarial prompts must not expose or call any other tool. | T09, T45, T64 |
| TM-14 | C3 | I | – | Tool results or error messages leak the environment, absolute paths or secrets. | Results contain only cited record data; errors are fixed strings plus a failure class and stage; no environment or path data; no secrets are readable by the process. | T53, T62, T09 |
| TM-15 | C3 | R | – | A finding cannot be traced to the call and record that produced it. | Every finding cites {tool-call id, record id, field, value}; citations are validated by code. | T06, T13 |
| TM-16 | C3 | D | – | One expensive tool call blocks the server. | Per-call limits and watchdog (section 3a). | T53, T50 |
| TM-17 | C3 | S, T | MCP-TP | Tool poisoning: a tool's name or description carries hidden instructions for the host's model. | Descriptions are static strings written by the author, linted (length, characters, denylisted instruction patterns), covered by a pinned manifest hash, and reviewed by a human security reviewer. | T64, T56 |
| TM-18 | C3 | T | MCP-TDI | Tool-description injection: text from records or configuration ends up in a tool description or schema. | Descriptions never contain record- or configuration-derived text; the manifest is byte-identical across all 394 packages and across runs. | T64 |
| TM-19 | C3 | T | MCP-RP | Rug-pull: tool definitions change after a user has approved the server. | The manifest is fixed at build time and its hash is checked at start-up; no tool-list-changed notification is ever sent; a manifest change needs a version bump and a changelog entry (CI check). | T64, T66 |
| TM-20 | C4 | T | – | An insider edits a record file to hide a defect or add a forged sign-off. (The tool can check completeness; it cannot establish that a record is true.) | Read-only access. A package manifest hash is checked; input hashes are written to the audit log and the report so a later edit is visible; a hash mismatch ends in the REVIEW INCOMPLETE status. Stated limit: a record that was forged before it reached the tool cannot be detected as forged, only flagged where documents are missing or inconsistent. | T50, T13, T54 |
| TM-21 | C4 | S | LLM01 | A forged supplier certificate, pasted email or forged approval text ('QA approved, release now') is read as an instruction or as a real approval. | All record text is data, never an instruction. No approval can come from text. Forged-approval and injection classes are in the corpus. Documentary indicators of suspect parts are flagged for a human (T63). | T11, T41, T09, T63 |
| TM-22 | C4 | I | LLM02 | Real or personal data in records is processed or disclosed (Stage 0 uses synthetic data only). | Synthetic data only in Stage 0; local-first with no egress and no telemetry; a data-protection checklist before any real data is considered. | T62, T14 |
| TM-23 | C4 | D | – | Oversized or very numerous record files exhaust memory or time. | Size, count and memory limits; over a limit ends in the REVIEW INCOMPLETE status. | T53 |
| TM-24 | C4 | R | – | Records change after the review and nobody can show what was reviewed. | Input hashes are recorded in the audit log and the report. | T54, T13 |
| TM-25 | C4 | E | – | Symlinks, hard links or mount tricks make the server read files outside the package directory. | Canonical path check against the configured root; symlinks and special files refused; read-only mount in tests; canary files outside the root. | T53 |
| TM-26 | C5 | D | – | Parser denial of service: deep nesting, huge numbers, repeated keys, pathological strings or regular expressions. | Depth, length and size limits; no unbounded regular expressions on record text; watchdog and memory cap. | T53, T50 |
| TM-27 | C5 | T | – | Parser ambiguity hides a defect: duplicate keys, NaN or Infinity, unpaired surrogates, or last-value-wins behaviour. | Strict parsing: duplicate keys, NaN/Infinity and invalid Unicode are rejected, never repaired; rejection ends in the REVIEW INCOMPLETE status. | T53, T08, T50 |
| TM-28 | C5 | E | – | Unsafe deserialisation or a parser bug leads to code execution. | JSON only; no pickle, no YAML loading, no eval; Bandit and Semgrep rules fail the build on these; archives are not accepted in Stage 0; human code review and penetration test of the parser. | T48, T47, T53, T56 |
| TM-29 | C5 | I | – | Error messages echo record content or file paths. | Fixed error strings with failure class and stage only. | T53, T62 |
| TM-30 | C5 | S | – | Look-alike characters or bidirectional controls make one identifier look like another or hide text. | Identifiers must match a strict character set; control, bidirectional and zero-width characters in identifiers are rejected; reports show non-printing characters escaped. | T53, T11 |
| TM-31 | C5 | T | – | A truncated or partly parsed file is treated as complete. | Any parse error ends in the REVIEW INCOMPLETE status; there is no partial-parse mode. | T50, T53 |
| TM-32 | C6 | T | – | A rule defect misses a critical fault (false negative). | Seeded-fault evaluation with 100% critical recall required, clean twins, and a rules-only baseline measured. | T07, T21, T15 |
| TM-33 | C6 | T | – | The rule set is altered or the wrong version runs. | The rule-set hash is pinned and checked at start-up and printed in every report; a mismatch ends in the REVIEW INCOMPLETE status. | T50, T14 |
| TM-34 | C6 | D | – | Crafted input drives a rule into very long run time. | Watchdog and complexity limits; fuzz corpus includes worst-case structures. | T53, T50 |
| TM-35 | C6 | R | – | Output differs between runs so a finding cannot be reproduced. | Rules-only output is byte-identical across 10 runs. | T10, T15 |
| TM-36 | C6 | T, I | – | The rules engine fills a missing value with a default (a guessed field) and reports a false 'complete'. | Missing data is listed by exact field path; no value is output for a withheld path. | T08, T40 |
| TM-37 | C6 | S | – | Rule output is read as a release or serviceability conclusion. | Fixed two-value status; forbidden-wording scan; intended-purpose statement and disclaimer in every report. | T12, T58, T59, T65 |
| TM-38 | C6 | R | – | Findings are aggregated per engineer or certifier, creating individual performance scoring. | No per-person fields, tools, aggregates or rankings anywhere. | T60 |
| TM-39 | C7 | T, E | LLM01 | Prompt injection through record text (direct, indirect, hidden PDF text, multilingual, split, tool-call hijack). | The module is advisory and optional. Untrusted text is quoted in labelled delimiters with look-alikes escaped; strict output schema; tool allow-list; rules override the model; a stub hostile model proves the defences without a real model. | T11, T38, T45 |
| TM-40 | C7 | I | LLM02 | Record content leaves the machine through a tool argument, URL, file write or a remote model endpoint. | Local-first: the default endpoint is in-process, loopback or a Unix socket; a remote endpoint needs explicit configuration, is refused in offline mode and puts a warning in the report; no write or fetch tools. | T38, T42, T62, T45 |
| TM-41 | C7 | T | LLM09 | The model invents a citation, record or regulation clause (misinformation). | Every citation is checked by code against the recorded tool results; regulatory quotes must be verbatim substrings of the T02 bundle. | T06, T39 |
| TM-42 | C7 | T | LLM05 | Model output drops or downgrades a rule finding, or states that the package is complete (improper output handling). | Output is schema-validated and rejected, not repaired; the rule layer is byte-identical with the module on or off; model items can only be added and are labelled advisory. | T45, T57, T40 |
| TM-43 | C7 | E | LLM06 | Excessive agency: the model calls tools it should not, or attempts approve, sign or release. | Allow-list; read-only tools; 0 approve or sign tool attempts across the adversarial prompts. | T09, T41, T45 |
| TM-44 | C7 | D | LLM10 | Unbounded consumption: runaway tokens, cost or time. | Spending kill switch, per-run and per-package time limits, input size limits. | T04, T44, T53 |
| TM-45 | C7 | S | – | Model-written text is mistaken for rule output or a human's words. | Machine-readable and visible label on every model-derived item, set by code, inside the report fingerprint. | T61, T54 |
| TM-46 | C7 | I | LLM07 | System prompt leakage. | The prompt holds no secrets or keys and is public in the open-source repository; no signing key is readable by the process. | T09, T45 |
| TM-47 | C7 | T | LLM03 | Substituted or tampered model weights, or a model other than the one requested answers (model supply chain). | Local weights are hash-pinned; the served model id is logged on every call; mismatches are excluded. | T42, T05 |
| TM-48 | C7 | T | LLM04 | Poisoned fine-tuning or training data. The tool does no training or fine-tuning. | No fine-tuning, no training on records and no retrieval store; third-party models are used as supplied. | T57 |
| TM-49 | C7 | T | LLM08 | Vector and embedding weaknesses. The design has no vector store, embeddings or retrieval-augmented generation. | Not used. Adding any retrieval component needs a logged amendment, a new threat row and tests. | T57 |
| TM-50 | C7 | R | – | The model is used to profile or rank individual people. | No per-person output of any kind; module output is checked by the same wording and schema tests. | T60 |
| TM-51 | C8 | T | – | Entries are edited, deleted, reordered, truncated or forged. | Hash-chained append-only log with a reference verifier and a 10,000-case tamper suite. | T13 |
| TM-52 | C8 | T, R | – | The whole chain is replaced with a consistent forged one, or two writers fork the log. | Explicit warning when there is no external anchor; optional external checkpoint; concurrency test with no fork. | T13 |
| TM-53 | C8 | I | – | The log leaks record content or personal data. | Entries hold identifiers, hashes, rule versions and times, never record free text. | T54, T62 |
| TM-54 | C8 | D | – | The disk is full or the log cannot be written. | Any audit-write failure ends in the REVIEW INCOMPLETE status; the error is printed to stderr. | T50 |
| TM-55 | C8 | E | – | A symlink or odd log path makes the server write somewhere unintended. | The log directory is fixed by configuration, created by the operator and checked; writes only to that directory and the report directory. | T53, T62 |
| TM-56 | C9 | T | – | A report is edited after it was produced (for example REVIEW INCOMPLETE changed to REVIEW COMPLETE). | SHA-256 fingerprint over the whole report body, recorded in the chained audit log; the verifier detects edits. | T54 |
| TM-57 | C9 | S | – | A forged report is presented as the tool's output. | The audit reference ties a report to a log entry; stated limit: the chain shows change, not authorship, and needs an external anchor to resist a full rewrite. | T54, T13 |
| TM-58 | C9 | I | – | A report discloses more data than the finding needs. | Reports quote the cited field values only; no environment or path data. | T62, T53 |
| TM-59 | C9 | R | – | A reader misreads a report or an empty report as an assurance (false assurance). | Fixed status vocabulary, zero-findings statement, list of checks that ran and did not run, critical-first order; human-factors note. | T65, T59, T12 |
| TM-60 | C9 | T, E | LLM05 | Rendering injection: markup, terminal escape sequences or spreadsheet formulas in record text affect the reader's screen or tools. | Plain-text and JSON output only; control and escape characters escaped; no HTML rendering; no CSV output in Stage 0. | T11, T53 |
| TM-61 | C9 | D | – | An enormous report. | Output size cap; record text length caps in citations. | T53 |
| TM-62 | C9 | T | LLM01 | Indirect injection of a downstream agent: a report quoting hostile record text steers the model that reads the report. | Record text appears only inside labelled, escaped, length-capped citation fields; the report states these fields are data; canary strings must not appear as instructions in output. | T11, T45 |
| TM-63 | C10 | T, S | LLM03 | Dependency compromise, typosquatting or a malicious update. | Hash-pinned requirements, CycloneDX SBOM, dependency audit, minimal dependency count, Dependabot-style review by hand. | T14, T48 |
| TM-64 | C10 | T, S | – | A release artefact is swapped or unsigned. | Signed release verified in a clean environment; manifest hash and rule-set hash printed; release gate record. | T14, T66 |
| TM-65 | C10 | E | – | CI workflow injection or over-privileged tokens expose secrets or allow a malicious change. | Least-privilege workflow permissions, third-party actions pinned to commit SHAs, no secrets exposed to pull requests from forks, no paid API keys in CI. | T66, T48 |
| TM-66 | C10 | R | – | The origin of a build cannot be shown. | Build provenance aimed at SLSA Build L1 now and L2 on a hosted platform before release (a target, not a claim). | T14, T66 |
| TM-67 | C10 | T | – | AI build tools introduce a flaw, a backdoor or a shared blind spot; a model sandbox bypass. | Separate roles and families, mutation testing, differential testing, human security review; containment tests for any model that runs code. | T16, T25, T26, T29, T33, T56 |
| TM-68 | C10 | I | – | A secret, including the sealed key, is committed. | Sealed key lives outside the repository and is git-ignored; secret scan in the release gate. | T01, T09, T66 |
| TM-69 | C10 | T | – | Frozen test files or the hash list are altered after the freeze. | Hash list; unsigned annotated tag plus an OpenTimestamps proof and a public post of the hash-list fingerprint; verify script; changes only through `docs/amendments.md`. | T01 |

## 5. STRIDE coverage matrix

Each cell lists the threat rows for that component and STRIDE letter, or says why none applies.

| Component | S | T | R | I | D | E |
|---|---|---|---|---|---|---|
| C1 MCP client / host application | TM-01 | TM-06 | TM-02 | TM-03 | TM-04 | TM-03, TM-05 |
| C2 Transport | TM-07, TM-08, TM-10 | TM-07, TM-08, TM-09, TM-10 | N/A: Stdio has no remote parties to repudiate; run records are in the audit log (C8). | TM-07, TM-08 | TM-11 | TM-08 |
| C3 Tool calls (MCP tool surface) | TM-17 | TM-12, TM-17, TM-18, TM-19 | TM-15 | TM-14 | TM-16 | TM-12, TM-13 |
| C4 Record files (input data) | TM-21 | TM-20 | TM-24 | TM-22 | TM-23 | TM-25 |
| C5 Parsers | TM-30 | TM-27, TM-31 | N/A: Parsers keep no state of their own; every parse outcome, including rejection, is recorded in the audit log (C8). | TM-29 | TM-26 | TM-28 |
| C6 Rules engine | TM-37 | TM-32, TM-33, TM-36 | TM-35, TM-38 | TM-36 | TM-34 | N/A: The rules engine has no privileges beyond reading the parsed package; guessed-field defaults are covered as tampering and disclosure. |
| C7 Optional LLM module | TM-45 | TM-39, TM-41, TM-42, TM-47, TM-48, TM-49 | TM-50 | TM-40, TM-46 | TM-44 | TM-39, TM-43 |
| C8 Audit log | N/A: The log is local and written only by the tool; forged entries are covered as tampering. | TM-51, TM-52 | TM-52 | TM-53 | TM-54 | TM-55 |
| C9 Reports | TM-57 | TM-56, TM-60, TM-62 | TM-59 | TM-58 | TM-61 | TM-60 |
| C10 Build, CI and supply chain | TM-63, TM-64 | TM-63, TM-64, TM-67, TM-69 | TM-66 | TM-68 | N/A: No hosted service to deny; a stalled CI run delays a release and has no safety effect. | TM-65 |

## 6. Residual risks and honest limits

* **The tool checks completeness, not truth.** A convincingly forged record is only caught if something is missing or inconsistent. The human decides.
* **A hash chain shows change, not authorship.** Without an external anchor, someone who can rewrite the whole log and report cannot be detected (T13 gives an explicit warning).
* **Prompt injection cannot be proved impossible.** The design makes the language-model module advisory, checked by code and optional, so a successful injection cannot remove a rule finding or approve anything. The core engine reads no language model.
* **Host and client behaviour is outside the tool.** Adopters must assess the host, the client and any other servers in the same host.
* **No security review has happened yet.** The model-assisted reviews in the trial (T26, T29, T46, T47) are build-tool checks, not a substitute for the human security reviewer (T56).
* **Real data.** Stage 0 uses synthetic data only. Any use on real records needs a separate data-protection assessment by the adopting organisation.

## 7. Maintenance

The threat model is re-reviewed at every change to the transport, the tool manifest, the parser, the audit log, the report format or the optional module, and before any release (`docs/quality/release-control.md`). Changes after the freeze are logged amendments.
