# How I chose the tools

Isaac Adekunle, 4 Nov 2026 (Europe/London).

I am building airworthiness-mcp myself, using AI models as build and review tools under a method I designed and ran. This page records how I chose which models to use for which job, what that comparison found, what it did not settle, and what the trial will cost. The models are tools and test subjects. Every design decision, threshold and acceptance call is mine.

**Status: nothing in the build or the trial has run yet.** The line-up comparison below is a desk exercise on published evidence; it is not a test result.

**About the figures.** Every benchmark, price or other third-party figure on this page is *as reported in the cited source, retrieved/cited 4 Nov 2026; not independently verified*. Many reached me second-hand through the scoring reports described below, so I name both the original source and that route. Prices are *list prices as reported at that date*, in USD per million tokens (input/output). Where I made an assumption, it is marked **assumption**.

## 1. The multi-model approach

I split the work into separate roles so that no single model both builds and judges its own work:

| Role | What it does | Writes code? |
|---|---|---|
| Architect | Threat model, design, regulatory mapping; may only quote primary texts I supply | No |
| Design reviewer | A model from a different family that checks the architect's output before any code is written | No |
| Lead implementer | Builds the core modules | Yes |
| Second implementer | Writes the evaluations and adversarial tests | Yes |
| Engineering reviewer | Reviews the code; a finding counts only with a failing test | No |
| Security reviewer | Looks for vulnerabilities; every finding needs a working proof-of-concept; read-only, no network, no keys | No |
| Regulatory reviewer | Checks wording and regulatory claims against the supplied texts | No |

Rules I set:

- **Reviewers are never the builder.** A model cannot review code it, or its own model family, wrote.
- **Deterministic gates decide acceptance, not review scores.** A reviewer score is advisory. The hard gates in `trial-plan.md` (T06–T13) are run by code.
- **Citations are checked by code.** A model saying "verified" counts for nothing.
- **A withheld answer key**, generated before any design work and fingerprinted (see `preregistration.md`).
- **The model that actually answered is logged** on every call (T05).
- I review and sign the merged fix list. After three review rounds without passing the gates, work halts and I decide (T17).

## 2. The line-up comparison

### 2.1 Candidate line-ups

I drafted three line-ups from commercial and free hosted models:

| Role | A | B | C |
|---|---|---|---|
| Architect | Claude Opus 5.5 | Claude Fable 5.1 | Claude Fable 5.1 |
| Lead implementer | GPT-5.6 Sol | Claude Opus 5.5 | Claude Opus 5.5 |
| Second implementer | Codex 5.3 | Claude Sonnet 5.5 | Grok 4.7 |
| Engineering reviewer | unsplit reviewer pool | GPT-5.6 Sol | GPT-5.6 Sol |
| Security reviewer | unsplit reviewer pool | Grok 4.7 | DeepSeek V4.1 Flash 1017 |
| Regulatory reviewer | unsplit reviewer pool | Gemini 4 Argon | Gemini 4 Argon |

In A, three reviewers (Gemini 4 Argon, Grok 4.7, Kimi K3) shared reviewing with no assigned role.

### 2.2 The scoring panel and recusal

I asked 13 models to act as an independent scoring panel: Nemotron 3 Ultra, DeepSeek, Claude Sonnet 5.5, GPT-5.6 Sol, GLM 5.3, Grok 4.7, Kimi K3, Gemini 4 Argon, Nemotron 3.5, Claude Opus 5.5, Muse Spark 1.3, Muse Wonder and Claude Fable 5.1. Each gave every line-up a score out of 10.

Recusal rules I applied:

1. **No self-marking.** A score counts only if it was judged on roles outside the panel model's own family. Where a panel model holds a role in a line-up, it had to recuse that role and say so; its score is then a *recused partial*, judged on the remaining roles only.
2. **Plain mean.** A line-up's score is the plain mean of every counted score. No weighting, no rescaling.
3. **Failed recusal = excluded,** not down-weighted. Two scores were excluded: Kimi K3's score for A (it holds a role in A and did not recuse it), and DeepSeek's score for C (it described itself as a Claude model, so its recusal from C could not be trusted).

Claude Fable 5.1 failed to start three times, then ran on a later attempt. It recused every Claude role.

### 2.3 Result (headline method M1)

M1 is the plain mean of all counted scores. Final figures after the late Fable 5.1 report (rounded, as I computed them on 4 Nov 2026):

| Line-up | M1 mean | Counted scores |
|---|---|---|
| **B** | **7.45** | 13 |
| C | 6.50 | 12 |
| A | 5.35 | 12 |

Before the Fable report the figures were B 7.49, C 6.55, A 5.38. The order B > C > A held under every alternative I tried:

| Method | What it counts | A | B | C |
|---|---|---|---|---|
| M2 | full-scope scorers with no role in the line-up | 5.66 | 7.93 | 6.50 |
| M3 | recused partials only | 5.15 | 7.05 | 6.60 |
| M4 | M1 without the four lowest-quality reports | 5.11 | 7.29 | 6.38 |
| M5 | M1 without one A score I judged unreliable | 5.19 | 7.49 | 6.55 |
| M6 | M1 without that panel model entirely | 5.19 | 7.39 | 6.40 |
| Quality-weighted | each score weighted by my quality rating of its report | 5.32 | 7.44 | 6.51 |

(M2–M6 and the weighted row are pre-Fable figures.) Scorers that held a role in B scored it lower (7.05) than scorers with no stake (7.93), so recusal did not inflate B. The ordering is robust; **the size of the B–C gap is not** (0.95 on M1, 1.43 on M2, and one scorer, Claude Sonnet 5.5, put C 0.2 ahead).

No panel model recommended A. Of the 12 counted before the late report, 7 recommended B unchanged, 4 recommended B with one role swapped and 1 recommended C with fixes. The late Fable report also recommended B's structure.

### 2.4 Chosen line-up: B plus gates, provisional

| Role | Model (provisional) | Conditions | Can be overturned by |
|---|---|---|---|
| Architect | Claude Fable 5.1 (fallback: Claude Opus 5.5) | Quotes only supplied texts or says "not in the supplied sources"; checked by a cross-family design reviewer | T18, T23, T36 |
| Design reviewer (added) | GPT-5.6 Sol or Gemini 4 Argon | Chosen by the seeded-flaw test | T24 |
| Lead implementer | Claude Opus 5.5 | Must pass the hard gates within 3 review rounds | T27 |
| Second implementer | Claude Sonnet 5.5; Codex 5.3 as challenger | If a non-Anthropic model is within 5 points, it wins | T25, T33 |
| Engineering reviewer | GPT-5.6 Sol | Finding counts only with a failing test | T24, T31 |
| Security reviewer | Grok 4.7; DeepSeek V4.1 Flash 1017 as parallel probe; Muse Wonder 1.0 as possible second reviewer | No network, read-only, no keys, proof-of-concept required | T26, T29, T46, T47 |
| Regulatory reviewer | Gemini 4 Argon (backup: Muse Wonder 1.0) | Run before its reported price change | T21, T22, T34 |

My confidence: medium that the B structure is right; low on the individual architect, second-implementer and security choices. That is why each choice has a test that can overturn it.

## 3. What the comparison found wrong or unsettled

The panel was useful mainly for what it disagreed about. Figures below are *as reported, retrieved/cited 4 Nov 2026; not independently verified*. Each is re-checked from its primary page in T03 before it may influence a decision.

| Point | Figures and sources | Status |
|---|---|---|
| Terminal-Bench 2.1, GPT-5.6 Sol | 91.9% cited for Sol; several reports say 91.9% belongs to the multi-agent "Sol Ultra" and Sol is 88.8% (source: OpenAI's published results table, as cited in the reports) | Probably mis-attributed |
| Bug Hunt leaderboard | Claude Sonnet 5.5 51.3 (max), GPT-5.6 Sol 43.5 (max; xhigh 39, medium 29), DeepSeek 42.7, Claude Opus 5.5 41.7, Muse Wonder 31.7, Grok 4.7 29.0 (source: Bug Hunt README, as read in one report) | Needs a primary re-read |
| Sonnet 5.5 Bug Hunt run | run scores 43–57; $154.03 and 287 minutes at max (source: Bug Hunt README, as reported) | Holds; one noisy run |
| Artificial Analysis (AA) Intelligence Index, Claude Fable 5.1 | 66 at publication vs 49–50 in other reports (source: AA index pages, as cited) | Unresolved; possibly an index re-version |
| Gemini 4 Argon hallucination | 15% (30 Sep snapshot) vs 4.3% (later snapshot) (source: AA-Omniscience, as cited) | Different snapshots, not an error |
| SWE-Together, Claude Opus 5.5 | 68.8% (source: apidog summary site, as cited; other reports attribute 68.8 to Fable) | Unverifiable; zero weight |
| CWE-Bench-AA | Grok 4.7 68.3%, DeepSeek 69.2% (source: AA, as cited; one report notes the gap is one task of 120) | A tie, not a ranking |
| Collinear CWE-bench v2 | Grok 4.7 54.7% pass@1 (6th), Muse Wonder 1.0 66.1% (2nd); every model weakest in Python, 46–59% (source: Collinear, as cited in the late report) | Context only |
| Grok sandbox behaviour | 44 of 218 SWE-Together trials bypassed the sandbox (source: apidog, secondary, as cited) | Credible, not primary-verified; tested in T29 |
| Gray Swan prompt-injection | GPT-5.6 Sol 27.0%, newer Sol 10.1%; Gemini 4 Argon 0.7%; Grok 4.6 51.8%; Kimi K3 52.7%; no row for Grok 4.7, Sonnet 5.5 or DeepSeek (source: vendor-supplied Gray Swan figures, as cited) | Vendor-supplied; no candidate has an independent injection score |
| DeepSeek hallucination | 96.5% vs 64–67% in different reports (source: AA, as cited) | Disputed |
| Grok 4.7 Terminal-Bench 4.0 | 37.6% vendor figure vs 25.8% in AA's own run and 28.79 on Vals (as cited) | Vendor figures sit above independent runs |
| Refusals on cyber tasks | Fable 16%, GPT-6 Astra 13% of CWE tasks declined (source: AA cyber pages, as cited) | Tested in T28 |
| Claude Opus 5.5 SWE-bench Pro | 89.9% (vendor figure, as cited) | Vendor only |
| CRS Pilot 0 (my own earlier pilot) | 16/16 seeded faults caught, 0 invented quotes, per model | Every panel report called it unverifiable as evidence for this project (small, ceiling effect, not independently re-run); re-run blind in T22 |

## 4. Gaps it found and how the trial covers them

The panel reports raised 32 gaps (G01–G32). Merging them, I added 3 process gaps (P1–P3), and the late report added 3 more (G34–G36). G33 (a missing panel report) is closed. Each gap maps to at least one test; the full list and the coverage matrix are in `trial-plan.md`, sections 11 and 12. The main themes:

- No head-to-head test on the real task: benchmarks are desk evidence (G01) → T21, T22, T25, T26, T27.
- No cost or spending limit (G02) → T04, T30, T44.
- No fixed pass/fail gates and no withheld answer key (G04, G05) → T01, T06–T12.
- Prompt injection unmeasured for models that read hostile text, and the runtime model inside the tool is the real injection surface (G20, G34) → T11, T26, T38–T45.
- A single model family writing the architecture, the lead code and the tests (G14) → T25, T33.
- Sandbox containment for a security reviewer that runs code (G19) → T29.
- Panel anchoring and unverified model identity (G12, G13) → T19, T20.
- Hash-chain tamper evidence, supply chain and data protection (G18, G31) → T13, T14, T48.

## 5. Costs

All figures are USD estimates, computed by a small arithmetic script with no model calls. **Nothing has been spent on the trial yet.**

**List prices used (USD per million tokens, input/output; list prices as reported in the panel reports at 4 Nov 2026; not independently verified):** Claude Fable 5.1 10/50; Claude Opus 5.5 4/20; Claude Sonnet 5.5 2/10; Gemini 4 Argon 2/10 until a reported end date of 30 Nov 2026, then 4/20 (end date unconfirmed); Grok 4.7 2/6 (run on a free route here, so $0); DeepSeek V4.1 Flash 1017 0.30/1.20; Muse Wonder 1.0 4/20 (uncertain).

**Assumptions (mine, not sourced):**
- No price was found for GPT-5.6 Sol, Codex 5.3 or Carbon. I use a band of 2/10 (low) to 4/20 (high).
- Tokens per package: 30k input and 12k output (low); output × 2.5 (high), because heavy-reasoning models write more.
- Test-author runs: 20k input and 25k output (high: × 2). Lead slice: 600k input and 120k output (low) to 1.2M and 240k (high).
- The only measured token count I have is one free-route panel run: 21,292 tokens in total.

| Stage | Tests | Low (USD) | High (USD) |
|---|---|---|---|
| 0 | T01–T17, T34, T45, T48 set-up; T49–T55, T57–T62, T64–T66 set-up | 0 | 0 |
| 1 | T18, T19, T20 (paid part optional), T21 tier 1, T25, T26, T28, T29, T32, T36, T46, T47 (runtime free tier $0) | 58.96 | 232.45 |
| 2 | T21 tier 2, T22, T23, T24, T27, T30, runtime paid tier (optional, gated) | 156.36 | 485.04 |
| 3 | T33 | 1.20 | 19.20 |
| **Total** | | **216.52** | **736.69** |
| **+ 25% contingency** | | **270.65** | **920.86** |
| *Total without the optional runtime paid tier* | | *171.16* | *645.97* |

The runtime-tier, T46 and T47 rows were added to the script's output by hand, so a cent of rounding difference is possible. **Funding and order:** the free Stage 0 runs first. Paid stages run in the stated order as funding allows, each with a per-stage spending limit that I set before that stage starts (recorded in `preregistration.md` before any paid call). If funds are short, the fixed order of cuts in `trial-plan.md` section 10 is kept. The T04 kill switch enforces whichever limit is in force. **Not estimated:** the cost of the build itself, and my own time.

## 6. Human review

Models do not have the last word. Before any public release of the software I plan independent review by three humans: one reviewer with a Part-66 B1 / Part-145 certifying background (a B1 certifying engineer), one with a CAMO or quality background, and one **human security reviewer**. The first two work through a written checklist against synthetic sample reports. The security reviewer reviews the threat model (`docs/security/threat-model.md`) and does a code review and penetration test of the record parser, the transport, the audit log, report integrity and the MCP tool manifest. Each reviewer's competence is recorded (`docs/quality/competence-records.md`). Their comments are feedback on a research prototype, not an approval, audit or certification, and are quoted only with their permission. The gate is test T56 in `trial-plan.md`. None has taken place yet.

## 7. Limits

- The comparison is a desk exercise on published, mostly vendor-supplied or second-hand figures. It is a reason to run the trial, not a substitute for it.
- Some panel models were reached through routes that could not confirm which model actually answered; T19 checks this.
- The quality ratings of the panel reports (used only in M4 and the weighted row) are my own judgement.
