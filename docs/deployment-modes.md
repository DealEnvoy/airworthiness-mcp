# Deployment modes

Date: 5 Nov 2026 (Europe/London). Author: Isaac Adekunle. Status: **design decision approved by Isaac on 5 Nov 2026, written before the software exists. Nothing in this document has been built or run.** Regulatory and data-protection statements are my reading of public sources, not legal advice. Evidence tags: **[V]** page opened and read for the cited text; **[S]** seen only as a search-result snippet; **[N]** not verified from an official or independent source (unverified; do not rely on it).

> **WARNING: Never paste raw maintenance records into any chat or AI app. Use the command-line client, or a setup your organisation has approved.**

The warning above is the frozen wording (`data/t12_lexicon.json`, key `raw_records_warning`). It is shown in the README, in this document and in the command-line client's help output, and the client repeats it at start-up whenever mode B or mode C is switched on (test T70).

## 1. The rule that holds in every mode

**The rules engine decides every finding. A person decides everything else.** In every mode the rules engine alone produces the findings, the missing-data list and the report status. A language model, where one is used at all, can only read messy free text (mode B) or present and explain a finished report (mode C). It never decides a finding, never removes or downgrades one, and has no tool that signs, approves, releases or writes (T09, T45, T57, T64). The required disclaimer ("AI assists, a certifying human decides") and the intended-purpose statement are in every report in every mode (T58).

The design starts from the strictest option (mode A). Looser modes are added on top of it, one at a time, and each is off until someone deliberately switches it on.

| | Mode A (default) | Mode B (optional) | Mode C (organisation's choice) |
|---|---|---|---|
| What runs | Simple custom command-line client + rules engine | Mode A + a local IBM Granite model that reads free text only | Open WebUI or a private-cloud client in front of the same tools |
| Model | None | Local, in-process or loopback, off by default | Chat model chosen by the organisation |
| Network | None: zero connections | None: loopback or Unix socket only | Yes, only over TLS 1.3 |
| Data leaving the machine | None | None | Pseudonymised data only |
| Who decides it is used | Default | Isaac's design makes it available; the operator switches it on in the configuration file | The adopting organisation, with its own sign-off |
| Tests | T10, T15, T51, T62, T67, T68 | T57, T61, T68, T38–T45 | T52, T67, T69, T70 |

## 2. Mode A (DEFAULT): local command-line client and rules engine only

* A simple custom command-line client reads one work package from a local folder, runs the rules engine and writes a pre-release review report and an audit-log entry. Nothing else.
* **Read-only. Deterministic** (same input, same output, byte for byte). **No model. No network:** no listener, no outbound connection, no DNS lookup, no telemetry, no update check (T10, T51, T62, T67, T68).
* This is the one fully local, deterministic route an auditor can inspect end to end. It matches the read-only, "a human decides" design: the report goes to a named person, who decides.
* The MCP server described in the README is the same rules engine behind a stdio transport (T51). It is for people who already run an MCP client on the same machine. It is not needed for mode A.
* The default configuration has the model off and the network off. Turning either on needs an explicit setting in the configuration file; an environment variable alone cannot do it (T57, T68).

## 3. Mode B (OPTIONAL): local IBM Granite for free-text reading, off by default

* **What it does.** It reads messy free text in records (for example a rectification note written in shorthand) and may add **advisory** items that are labelled as model-written (T61). It **never decides a finding**: the rule-layer findings and missing-data list are byte-identical with the module on or off (T57 check (e)).
* **Where it runs.** On the same machine, in-process or on a loopback address or Unix socket. No record text leaves the machine (T62). Weights are hash-pinned and the served model id is logged (T05, T42).
* **Off by default.** Enabling it needs an explicit setting in the configuration file and a start-up notice that repeats the raw-records warning (T57, T68, T70). When it is on, EU AI Act Article 50 transparency applies to the model-written text; when it is off it does not arise (`docs/ai-act-self-assessment.md`).
* **Which model.** IBM Granite is the designated optional model. Whether any local model is accurate enough to ship in this mode is still an open question that the runtime tests answer (T38–T45; section 7 of the trial plan). If none qualifies, the project ships mode A only. **Second choice: Mistral** (an open-weight model with an Apache 2.0 card, checked per model; see below).

### 3.1 Verification of the Granite licence and data-governance claims (read 5 Nov 2026, Europe/London)

| Claim | Source and what it said | Tag |
|---|---|---|
| Granite 4.2 language models are licensed under Apache 2.0 | Model card for Granite-4.2-8B, https://huggingface.co/ibm-granite/granite-4.2-8b : "License: Apache 2.0"; release date 25 Aug 2026. Read 5 Nov 2026. | **[V]** |
| Granite 4.0 language models are licensed under Apache 2.0 | Model card for Granite-4.0-H-Small, https://huggingface.co/ibm-granite/granite-4.0-h-small : "License: Apache 2.0". Read 5 Nov 2026. | **[V]** |
| IBM states all Granite 4.0 models are Apache 2.0 | https://github.com/ibm-granite/granite-4.0-language-models ("All Granite 4.0 Language Models are distributed under Apache 2.0 license"). Search snippet only (the page fetch returned the title only). | **[S]** |
| IBM says Granite 4.2 (3B, 8B, 30B) is Apache 2.0 | IBM Research blog, 25 Aug 2026, https://research.ibm.com/blog/introducing-granite-4-2 . Search snippet only. | **[S]** |
| IBM holds accredited ISO/IEC 42001:2023 certification for the AI management system (AIMS) of IBM Granite; audited by Schellman; zero non-conformities | IBM announcement, https://www.ibm.com/new/announcements/ibm-granite-iso-42001 . Read 5 Nov 2026. This is IBM's own statement. The certificate and its scope were not checked in a certification register. | **[V]** that IBM says it; certificate itself **[N]** |
| The certification covers the specific Granite 4.2 checkpoints used here | The IBM page says "IBM Granite language models" and does not name versions. | **[N]** |
| IBM governs Granite training data: 2.7 petabytes under metadata tracking and licence controls | Same IBM announcement. Vendor claim, not independently audited here. | **[V]** that IBM says it; claim itself **[N]** |
| IBM describes the training data as curated, ethically acquired and put through IBM's own data review | IBM Granite 4.0 announcement, https://www.ibm.com/new/announcements/ibm-granite-4-0-hyper-efficient-high-performance-hybrid-models . Search snippet only. Vendor marketing claim. | **[S]**, claim **[N]** |
| Model card description of training data (permissive public datasets, internal synthetic data, human-curated data, agentic traces) | The Granite-4.2-8B and Granite-4.0-H-Small model cards above. | **[V]** |
| Granite 4.x checkpoints are cryptographically signed | IBM Granite 4.0 announcement, same URL as above. Search snippet only. | **[S]** |
| The Apache 2.0 licence covers the weights; it says nothing about whether your records are safe | Inference. The governance claims above concern IBM's development process, not the confidentiality of any data you put in. In mode B data stays on the machine because of the design (T62, T67), not because of anything IBM states. | Inference |

**Result.** The Apache 2.0 licence for Granite 4.0 and 4.2 is **verified [V]** on the Hugging Face model cards of 5 Nov 2026. The data-governance claims (ISO/IEC 42001 certification, curated and reviewed training data, data management framework) are **IBM's own published claims**. They were read but not independently verified, and the certificate scope for the exact model used is **[N]**. Before any adopter relies on them, the exact model card and the certificate must be checked again at the time. The organisation's own licence review applies as well.

### 3.2 Second choice: Mistral

Mistral's help page (https://help.mistral.ai/en/articles/347393-under-which-license-are-mistral-s-open-models-available , dated 12 Aug 2026, read 5 Nov 2026 **[V]**) says most open models are Apache 2.0 and some are under a modified MIT licence that requires a commercial licence above US$20 million monthly revenue. The licence therefore has to be read **model by model**. A model card for Mistral Small 4 (https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) shows Apache 2.0 in a search snippet only **[S]**. Mistral's data-governance claims were not checked **[N]**. Mistral is named as the second choice because it is an open-weight family from a European provider (this is not a verified statement about data handling).

## 4. Mode C (SUPPORTED, the organisation's choice): Open WebUI or a private-cloud client

Mode C is for organisations that want a chat interface. It is a **supported option, not the default, and not something Isaac recommends for a first adoption.** It is the organisation's decision and needs the organisation's own sign-off, including its information-security risk assessment (EASA Part-IS where it applies to that organisation; `docs/security/standards-mapping.md` section 5) and a data-protection assessment. Nothing in this repository says that using mode C meets any regulation.

Nothing in mode C is built, and in Stage 0 no network transport is enabled (T51, T52). Mode C can only ship after a logged amendment that satisfies T52 and the tests T67 and T69 pass.

**Open WebUI** (a self-hosted chat front end) or a **private-cloud client** (a client and hosted model inside the organisation's own cloud tenancy) can sit in front of the same read-only tools. Open WebUI's own settings, telemetry and storage were **not reviewed here [N]**; the organisation must assess them.

### 4.1 What mode C requires before any record data reaches a chat model

1. **Local pseudonymisation first.** On the user's machine, before anything is sent, replace: aircraft **registrations**, part and aircraft **serial numbers**, **names** of people, **licence numbers** and the **operator** with random tokens. **Dates are shifted to relative days** (days before the reference date; for example `D-35`). Free-text fields are scanned for the same values and tokenised.
2. **The token key stays on the machine.** The table that maps tokens back to real values is created and kept locally, is never sent anywhere and never appears in any outbound payload (T69). It is encrypted at rest (threat model section 7).
3. **TLS 1.3** for every connection (T67). A non-TLS or lower-version connection is refused.
4. **No-retention or zero-data-retention terms** with the model provider, in writing: no storage of prompts and outputs beyond what is needed to answer, no training on them. Whether a provider's published terms really give this must be checked by the organisation **[N]**.
5. **A UK or EU region** for processing, chosen by the organisation.
6. **A data-processing agreement (DPA)** with every processor.

### 4.2 Pseudonymised data is still personal data (legal check needed)

My understanding is that data that has been pseudonymised is still personal data under UK and EU GDPR while the key exists, so a DPA, a lawful basis and a data-protection impact assessment may still be needed. This is **my reading, not verified against the ICO's or the EU's current guidance [N], and needs a legal check** by the organisation. Free text can also carry identifying detail that tokenising does not catch, so pseudonymisation lowers the risk and does not remove it. Operator and aircraft data may also be commercially sensitive even where no person is identified.

### 4.3 What encryption does not do

TLS and encryption at rest protect data in transit and in storage. **They do not hide data from a cloud model while it answers**: during inference the model sees the (pseudonymised) text. That is why mode C relies on pseudonymisation, retention terms and region, not on encryption alone. **Confidential computing** (processing inside a hardware-protected enclave) is an option an organisation may choose to reduce that exposure. Whether a given provider offers it, and what it protects, was **not verified here [N]**. See `docs/security/threat-model.md` section 7.

### 4.4 Findings stay with the rules engine

In mode C the chat model receives the finished, pseudonymised report and answers questions about it. It cannot change a finding or the status, and the rule-layer output is the same as in mode A (T57, T45). Any text it writes is labelled as model text (T61).

## 5. Choosing a mode

| Situation | Mode |
|---|---|
| Real or sensitive records; an auditor, Part-145 organisation, CAMO or funder wants the simplest data story | **A** |
| Records with messy free-text notes and a local machine with enough memory; the operator accepts advisory model text | **B** (switch on deliberately) |
| The organisation wants a chat interface and has completed its own risk and data-protection assessment and sign-off | **C** |
| Anyone tempted to paste records into a public chat app | **None of these. Do not.** |

Stage 0 uses synthetic data only. This project is not approved or certified by any authority and is not for real aircraft or real release decisions (README).
