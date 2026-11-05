# Pre-registration

**Status: frozen at T01 (Freeze 1), 5 Nov 2026 (Europe/London). Stage 0 has not started. No test has been run and there are no results.**

## Why pre-register

A test is only meaningful if its pass mark was set before anyone saw the result. This project fixes its criteria in advance and fingerprints them, so that later readers can check the goalposts did not move. The approach follows CRS Pilot 0 (`DealEnvoy/crs-ai-agents`), which recorded file hashes before its runs.

## Two freezes

**Freeze 1 (T01), the product tests.** Frozen before Stage 0:

1. **Every pass/fail criterion and threshold** for the product tests in `docs/trial-plan.md`, including the hard-fail gates (T06–T13) and the security, fail-safe and design-rule tests (T49–T66, section 3a) with their fixed limits. Thresholds and spending limits that the plan marks **"set before that stage"** are not set yet; each is set and logged in `docs/amendments.md` before its stage starts.
2. **The synthetic data generator, its seed (20261104) and the generated data:** 394 packages in 8 sets (`data/packages/`) and the T06, T09 and T11 corpora (`data/corpora/`), each with a manifest of SHA-256 fingerprints.
3. **The fingerprints of the sealed seeded-fault key and of its secret salt.** The key (the answers) and the salt are kept outside the repository. Only their SHA-256 fingerprints are public until the results are published, when the key and the salt are published too so that anyone can regenerate the data and check it.
4. **The forbidden-wording lexicon, the required disclaimer and the two report status lines** (T12, T59).
5. **The documents that define security and design-rule tests:** the threat model, the planted-failure and fuzz-corpus specifications, the security policy and standards mapping, the release-control rules, the human-factors rules and the suspected-unapproved-parts specification, plus `tools/check_docs.py`, `tools/check_data.py` and `verify_prereg.py`. The risk register, corrective-action log, traceability, competence records, regulatory documents and other quality documents are living records. They stay editable and are not frozen.

**Freeze 2, the build-tool tests.** The build-tool tests (section 6a of the plan, T18–T20, T23–T25, T27–T30, T32–T34, T36, T46), T47, the role-selection rules, the named fallback models and the T21 candidate list stay open until Isaac approves the model line-up. They are then frozen in a second logged freeze, before any build-tool test runs. Freeze 2 records a new SHA-256 of the plan in `docs/amendments.md`; the text frozen at Freeze 1 stays recoverable from the tag.

Nothing is run before Freeze 1.

## How the record is made

1. The frozen files are listed in `PREREG_HASHES.txt` at the repository root, one line per file:

   ```
   <sha256>  <path>
   ```

   The salt and the sealed key are listed by fingerprint only (`../sealed/...`); their contents are not in the repository.
2. The commit that contains `PREREG_HASHES.txt` is marked with an **unsigned annotated git tag**, `stage0-t01-prereg`. It is not a signed tag.
3. An **OpenTimestamps proof** of `PREREG_HASHES.txt` is made with the free `ots` client (`PREREG_HASHES.txt.ots`). It anchors the hash list to the Bitcoin blockchain, which shows the list existed no later than the anchored time.
4. Isaac posts **one fingerprint** publicly: the SHA-256 of `PREREG_HASHES.txt` together with the commit hash. The date of that post is an independent timestamp.
5. `verify_prereg.py` recomputes every hash and reports any mismatch. Anyone can run it. The salt and key lines are checked only where the files are present.
6. When the key and salt are published with the results, readers can confirm both match the fingerprints recorded at the freeze, and can regenerate the data with `data/generate.py`.

## Limits of this record

The hash list and the tag are created by the author. The tag is unsigned, so it does not prove who made it. The OpenTimestamps proof and the public post show only that the hash list existed by those dates; they do not show that the criteria are good. The data are generated and deterministic only on Python 3.13.5 (the version used so far); other versions were not tested. The author drafted some of the test material with AI models used as build tools (see `docs/methods.md`); every threshold and decision is Isaac's. Human reviewers are not appointed yet; they are required before any public claim about results and are to be funded through grants. Stage 0 proceeds without them.

## Amendments

After a freeze, a criterion changes only through a dated entry in [`docs/amendments.md`](amendments.md) (a separate file, so this file stays unchanged): date (Europe/London), what changed, why, and whether any result had been seen. Results run under an amended criterion are reported next to the original, not instead of it.
