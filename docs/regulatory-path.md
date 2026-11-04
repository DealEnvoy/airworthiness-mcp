# Regulatory path (public summary)

Date of research: 4 Nov 2026 (Europe/London). Author: Isaac Adekunle (15+ years in aircraft maintenance).

**Not legal advice.** Everything below is Isaac's reading of public texts, using free web tools only. It may be wrong or out of date. Anyone who wants to rely on it commercially should have it confirmed by a Part-145 or CAMO compliance manager, the competent authority, or a lawyer. Nothing here claims that the tool is certified, approved or compliant with anything. The wording used is "aligned with" and "designed to support".

**Evidence tags.** **[V]** = the page was opened and read in full for the cited text. **[S]** = seen only as a search-result snippet; not fully read. **[N]** = not verified from an official source (secondary source, or an inference). Inferences are labelled "Inference". Items tagged [N] are **unverified** and must not be relied on.

The long working version, with every source, is kept by the author outside this repository; this page is the public summary.

## 1. The short version

1. **Only authorised humans release aircraft to service.** Every regime names a person, or an approved organisation acting through named people. No provision was found under which software can issue a release. This is a finding about the sections read, not an explicit "software must not" sentence.
2. **There is no product certificate for maintenance-records software** in the three regimes looked at (UK, EASA, FAA). Software is used under an approved organisation's own procedures, and the authority accepts the organisation's procedure or system, not the software. The absence of a scheme is an inference from not finding one. **[N]** as an exhaustive negative.
3. **Acceptance is therefore organisational.** A tool that released aircraft would need rule changes and would sit at EASA AI Level 3, for which no guidance exists yet.
4. airworthiness-mcp as scoped (read-only, advisory, a certifying human decides) maps to **EASA AI Level 1** (human assistance) at most. If it is purely rule-based, EASA's machine-learning guidance does not strictly apply.
5. The tool does not certify, release or determine airworthiness. It checks records for completeness and reports findings for a human.

## 2. Who may release an aircraft to service (Isaac's reading)

| Regime | Provision | What it says, in short | Source | Tag |
|---|---|---|---|---|
| UK (retained Reg (EU) 1321/2014) | Part-145 point 145.A.50 | A certificate of release to service is issued by appropriately authorised certifying staff after it is verified that all ordered maintenance was properly carried out and there are no known non-compliances that endanger flight safety. | https://www.legislation.gov.uk/eur/2014/1321/annex/II | [V] |
| UK | Part-M point M.A.801 | No aircraft is released to service unless a certificate of release to service is issued by authorised certifying staff (with narrow exceptions for non-complex tasks and for an aircraft grounded where no organisation is available). Every route names a person. | https://regulatorylibrary.caa.co.uk/1321-2014/Content/Document%20Structure/01%20M/2%20Regs/00780_M.A.801.htm | [V] |
| EASA | Part-145, Part-M, Part-CAMO, Part-ML | Same structure. EASA's own FAQ says aircraft release is by Part-66 licensed certifying staff under the organisation's rating. | https://www.easa.europa.eu/en/the-agency/faqs/certification-maintenance | [V] |
| EASA | Verbatim EU text of 145.A.50 and M.A.801 | The UK retained copies were read instead; the EASA-hosted verbatim text was not. | EASA Easy Access Rules, https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-continuing-airworthiness | [S] |
| FAA | 14 CFR 43.7 | Only the Administrator and certificated persons and organisations listed in the section may approve an aircraft for return to service. | https://www.ecfr.gov/current/title-14/chapter-I/subchapter-D/part-43/section-43.7 | [V] |
| FAA | 14 CFR 43.9 | The maintenance record must include the signature, certificate number and kind of certificate of the person approving the work. | https://www.ecfr.gov/current/title-14/chapter-I/subchapter-D/part-43/section-43.9 | [V] |
| FAA | 14 CFR 91.407 | No operation after maintenance unless approved for return to service by a person authorised under 43.7 and the 43.9 or 43.11 entry is made. | https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-91/subpart-E/section-91.407 | [V] |

Electronic signing is allowed, but it is a human's signature in electronic form (EASA guidelines on electronic documents, records and signatures, Issue 1, 4 May 2023, https://www.easa.europa.eu/en/downloads/137906/en, **[V]**). The FAA's AI roadmap says AI is not accountable; the designer and maintainer remain accountable unless the law allocates it elsewhere (https://www.faa.gov/aircraft/air_cert/step/roadmap_for_AI_safety_assurance, **[V]**). EASA says that for AI Levels 1 and 2 responsibility remains with the end user (https://www.easa.europa.eu/en/downloads/139504/en, **[V]**).

**What this means for the design (inference):** the tool never outputs "airworthy", "ready for release" or anything resembling a certificate-of-release statement. Tests T09, T12 and T59 in `docs/trial-plan.md` check this.

## 3. How a tool is accepted: the organisation, not the product

* **UK / EASA.** Maintenance procedures are agreed with the authority and described in the organisation's exposition (MOE for Part-145, CAME for CAMO). Changes go through approval or the authority-approved change procedure (145.A.65, 145.A.70, 145.A.85; https://www.legislation.gov.uk/eur/2014/1321/annex/II, **[V]**). Electronic record systems must prevent unauthorised alteration and be backed up (AMC 145.A.55, AMC M.A.305(e), 145.A.45(e), **[V]**; links in the working version). EASA's electronic-records guidelines say they do not intend to approve the software, that the authority is expected to accept its use before an organisation changes over, that the software developer is not treated as a subcontractor, and that authorities are not expected to audit the software itself (sections 4.5.1 and 5.8, **[V]**). These guidelines address tools that sign or create records; a read-only advisory checker is adjacent to them, not squarely within them (Inference).
* **FAA.** Repair stations keep records "in a format acceptable to the FAA" (14 CFR 145.219) and a quality control system acceptable to the FAA (145.211) (**[V]**). Advisory Circular **AC 120-78B** (11 Dec 2024; cancels AC 120-78A) covers electronic signatures, records and manuals; for repair stations FAA acceptance is conveyed through **OpSpec A025**, and use of electronic systems is optional (**[V]**, https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1043396). AC 43-9D (22 Sep 2025; cancels AC 43-9C) covers maintenance records (**[V]**).
* **Whether a purely advisory checker needs any authority acceptance at all** depends on whether it replaces a procedure step in the organisation. **[N]** Confirm with each organisation's competent authority.
* No FAA product approval scheme for ground maintenance-records software was found. **[N]** as an exhaustive negative.

## 4. AI-specific positioning

* **EASA AI levels** (AI Roadmap 2.0, 10 May 2023, **[V]**, https://www.easa.europa.eu/en/document-library/general-publications/easa-artificial-intelligence-roadmap-20): Level 1 is assistance to a human (1A augmentation, 1B support to decision-making), Level 2 human-AI teaming, Level 3 advanced automation. An advisory report that a certifying human reads and acts on is **Level 1** (Inference). If there is doubt, EASA says to assume the higher level.
* **EASA Concept Paper Issue 02** (Level 1 and 2 machine learning; **[V]**, https://www.easa.europa.eu/en/downloads/139504/en) is initial and non-definitive, and covers machine learning only. **NPA 2025-07** (consultation; **[V]**, https://www.easa.europa.eu/en/document-library/notices-of-proposed-amendment/npa-2025-07) is a proposal, not final. The date EASA expects the next steps (Q2/2027) is **[N]**.
* **UK CAA** AI strategy CAP 3064 (v1.3.2, 3 Dec 2024; **[V]**): no AI-specific maintenance-tool rules found. A claim that initial guidance is planned for early 2027 is **[N]**.
* **EU AI Act:** see `docs/ai-act-self-assessment.md`. Verdict: likely not high-risk, with reasons and re-assessment triggers.
* **Cybersecurity:** EASA Part-IS (Implementing Regulation (EU) 2023/203, applicable from 22 Feb 2026; Delegated Regulation (EU) 2022/1645 for design and production organisations) binds the organisations in scope, such as Part-145 and CAMO organisations, **not the tool's author** (**[V]**, https://www.easa.europa.eu/en/faq/139283 and https://www.easa.europa.eu/en/faq/139292). A UK organisation holding an EASA (third-country) Part-145 approval is in scope through EASA. No UK Part-IS law was found; the CAA is still developing a UK approach (**[V]**, https://consultations.caa.co.uk/cyber-security/uk-isms-regulation/). Whether any UK-only organisation is directly bound is **[N]**. An adopting organisation will assess this tool as a supplier item in its own risk assessment. See `docs/security/standards-mapping.md`.
* **Standards that do not apply** (Inference): DO-178C (airborne software), DO-200B / ED-76B (aeronautical data), DO-330 (tool qualification for airborne lifecycles), ED-202A / DO-326A (aircraft-level security). ED-204A is plausibly relevant only if the tool touched data feeding airborne software loading, which it does not. No regulator-required software standard for ground maintenance-records tools was found. **[N]** as an exhaustive negative.

## 5. Staged path (alignment, then accepted use)

**Stage A: open-source advisory tool, aligned (what the project can do alone).** Stay read-only and advisory. No "airworthy" or "release" wording; a clear statement that a certifying human decides. Publish the intended purpose, the rule list and versions, a deterministic test suite with synthetic records, error statistics, an audit log of what was checked, and reproducible output. Do not claim certification, approval or compliance.

**Stage B: adoption by a Part-145, CAMO or FAA repair station under its own procedures.** The organisation writes a procedure in its MOE or CAME (UK/EASA) or its quality control or repair station manual (FAA) saying that the tool is advisory, who may use it, that certifying staff review every finding, what to do if the tool is unavailable or wrong, what training is needed, and who supports it. The organisation validates the tool on its own records and audits its use.

**Stage C: the competent authority accepts the organisation's procedure.** UK/EASA: an MOE or CAME amendment, approved or made under the authority-approved change procedure. FAA: acceptance of the manual, and OpSpec A025 only if the tool is an electronic recordkeeping, signature or manual system. A purely advisory tool may need little or no formal authority action; confirm with the authority. **[N]**

**Stage D: optional formal frameworks (strengthen, do not "certify").** EASA AI Level 1 objectives once the guidance is final and only if the tool is machine-learning based and in scope. ISO 9001 or AS9110C for the maintainer's organisation (`docs/quality/`; certification is for an organisation, the future Drew & Crew Ltd through a UKAS-accredited body, and is **not claimed**). ISO/IEC 27001 and Part-IS support for adopters. Independent third-party code and security review (the human security reviewer, test T56). No regulator-recognised scheme for any of these was verified. **[N]**

**If the goal were an automated release function** (it is not): rule changes naming certifying staff would be needed (145.A.50, M.A.801, 14 CFR 43.7); it would be EASA AI Level 3, whose guidance is not written; the UK and FAA have no stated path.

## 6. Re-assessment triggers

Targeting unmanned-aircraft design or production; adding any per-person analytics; adding any automatic release or sign-off; EASA adopting acts that cover AI in maintenance; the CAA publishing a UK information-security rule; changes to UK or EU AI law; adding a network transport (T52).

## 7. Not verified (summary)

EASA-hosted verbatim text of 145.A.50, M.A.801 and CAMO.A.220; the timing of CAP 3064 guidance and EASA's next NPAs; whether any national authority treats advisory checkers as needing acceptance; FAA internal policy on non-recordkeeping maintenance software; the UK/EU bilateral position for UK Part-145 holders; whether a UK-only organisation is a designated NIS operator.
