# EU AI Act self-assessment (Article 6)

Date: 4 Nov 2026 (Europe/London). Author: Isaac Adekunle. Status: **self-assessment, not legal advice, not reviewed by a lawyer.** The reading of the Regulation is Isaac's. Evidence tags: **[V]** page opened and read; **[S]** search snippet only; **[N]** not verified from an official source. Items tagged [N] are unverified.

Text base: the EU AI Act Service Desk's display of the consolidated text of Regulation (EU) 2024/1689 as at 27 July 2026, including the Digital Omnibus on AI, Regulation (EU) 2026/1744 (**[V]** for the Service Desk pages cited below; the EUR-Lex act itself **[S]**).

## 1. System assessed

airworthiness-mcp: an open-source, read-only, advisory Python MCP server that checks maintenance work packages and records for completeness and reports findings. **Intended purpose (frozen statement, T58):** "Advisory checker of maintenance records and work packages. Read-only. Does not certify, release, or determine airworthiness. A certifying human decides."

Two parts are assessed separately:

* **Part 1: the rules-engine core** (deterministic, fixed rules defined by a person, no model).
* **Part 2: the optional LLM module** (off by default, separate; reads record text and may add advisory findings).

## 2. Verdict

**Likely not high-risk.** Confidence: moderate-high for the rules-engine core; moderate for the optional LLM module. Any one of the layers below is enough on its own.

## 3. Reasons

### 3.1 The core is probably not an "AI system" (Article 3(1))

Article 3(1) requires a system that infers, from the input it receives, how to generate outputs (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3). The Commission's guidelines on the definition say systems based on rules defined solely by natural persons, and basic data processing, are outside it (**[S]**, https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-01/guide-definition_en.pdf). A fixed-rule check such as "task card step has no sign-off" or "life limit exceeded" is probably not an AI system (Inference). The optional LLM module probably is one, so it is the only part with a scope question.

### 3.2 Article 6(1) and Annex I do not reach the tool

Article 6(1) needs both a safety component of a product covered by Annex I legislation and a product that needs third-party conformity assessment (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6). Regulation (EU) 2018/1139 appears in Annex I **Section B**, but only for the design, production and placing on the market of unmanned aircraft and their engines, propellers, parts and equipment to control them remotely (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-1). Maintenance of manned aircraft and a ground-side records checker are not within that wording. For Section B products, Article 2(2) applies only Articles 6(1), 60a and 102 to 112, and Article 108 means the substantive requirements reach 2018/1139 only through later delegated or implementing acts (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-2 and /article-108). No such act covering ground maintenance tools was found. **[N]** as an exhaustive negative.

Caution: the Commission's **draft** Article 6 guidelines (19 May 2026, non-binding) list "monitoring and detection of a need for maintenance or inspections" as an example of a safety function (**[V]**, https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems). The tool could be argued to be a safety component in the ordinary sense, but that matters only if Annex I coverage is also met, and it is not for manned aircraft. The advisory, Level-1 framing is kept anyway.

### 3.3 Annex III does not list aviation

Annex III point 2 (critical infrastructure) lists safety components in critical digital infrastructure, road traffic and the supply of water, gas, heating and electricity. Air transport is not listed (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3).

**The trap is Annex III point 4(b):** AI used to monitor and evaluate the performance and behaviour of persons in work relationships. If findings were aggregated per engineer or certifier, the tool could drift into it, and profiling of natural persons would defeat any Article 6(3) argument. **Design rule (test T60, hard fail): report on documents, tasks and rules; never score or rank individual people.**

### 3.4 Article 6(3), as a fallback only

If an Annex III category applied, a system is not high-risk when it poses no significant risk, for example when it does a narrow procedural task, detects deviations without replacing or influencing a prior human assessment, or does a preparatory task, but it is always high-risk if it profiles natural persons (**[V]**, article-6 page above). A read-only, advisory tool where a human decides fits those limbs, which is why T59 and T60 exist. This is a fallback, not the main reason.

### 3.5 Open-source exclusion, Article 2(12), and its limits

The Act does not apply to AI systems released under free and open-source licences unless they are placed on the market or put into service as high-risk systems or fall under Article 5 or 50 (**[V]**, article-2 page above). Limits: it does not help if the tool were high-risk; **Article 50 transparency still applies** to a system that generates synthetic text; Article 50 applies from 2 Aug 2026 with a grace period for marking to 2 Dec 2026 for systems already on the market (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50 and /article-113). Whether an LLM-written findings report triggers Article 50(2) marking is **[N]**. Mitigation: when the module is on, model-generated text is labelled visibly and in machine-readable form (T61).

### 3.6 General-purpose AI models (Chapter V)

Provider duties under Article 53 fall on the model provider. Calling a third-party model, or running local inference without fine-tuning at large scale, does not make the tool's author a provider of a general-purpose AI model (Inference; thresholds in the Commission's scope guidelines, **[S]**). The project does not fine-tune any model.

### 3.7 Timing

Under the Digital Omnibus, high-risk rules for Annex III systems apply from 2 Dec 2027 and for Article 6(1) / Annex I systems from 2 Aug 2028 (**[V]**, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113). Even if high-risk applied, nothing high-risk-specific would bind before those dates.

### 3.8 UK author

The Act reaches providers who place AI systems on the Union market wherever they are established, and third-country providers whose output is used in the Union (Article 2(1), **[V]**). Publishing on GitHub, reachable from the EU, is probably "making available", and the open-source exclusion then does the work for a non-high-risk tool, except Article 50. Whether free publication is a "commercial activity" is **[N]**. No UK AI statute was researched. **[N]**

## 4. Design rules that keep the tool in the "likely not high-risk" lane

Each is a frozen test in `docs/trial-plan.md` section 3a.

| Rule | Test |
|---|---|
| The core is a deterministic rules engine; the LLM module is optional, separate and off by default | T57 |
| The intended-purpose statement is in the README and on every report | T58 |
| Never output a release, serviceability or airworthiness conclusion | T59 (extends T09, T12) |
| Never score or rank individual people | T60 (hard fail) |
| Language-model text is labelled visibly and in machine-readable form when the module is on | T61 |
| Local-first: no egress, no telemetry unless explicitly configured | T62 |
| Not used as a blocking step in a release workflow; no automatic sign-off | T09, T64 |

## 5. Re-assessment triggers

Re-do this assessment before any of: targeting unmanned-aircraft design or production; adding any per-person analytics; adding any automatic release or sign-off, or use as a gating step; enabling the LLM module by default; adding retrieval or training on records; EASA or the Commission adopting acts that cover AI in maintenance; final (not draft) Commission Article 6 guidelines; changes to the Omnibus dates; a change to the scope of the open-source exclusion; a UK AI statute.

## 6. Not verified

A primary-text reading of Regulation (EU) 2026/1744 itself (the EUR-Lex fetch failed; the Service Desk consolidated text was used); the final Commission Article 6 guidelines; whether free publication on GitHub is a commercial activity; whether an LLM-written report triggers Article 50(2); whether any EASA act under 2018/1139 applies the Chapter III Section 2 requirements to ground maintenance tools.

## 7. Record

Prepared by Isaac Adekunle. Not signed off by a lawyer. Next review date: before the first public release of the software and at every trigger above.
