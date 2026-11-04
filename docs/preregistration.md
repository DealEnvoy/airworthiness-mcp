# Pre-registration

**Status: draft. The freeze (T01) has not happened. No fingerprints have been recorded yet.**

## Why pre-register

A test is only meaningful if its pass mark was set before anyone saw the result. This project fixes its criteria in advance and fingerprints them, so that later readers can check the goalposts did not move. The approach follows CRS Pilot 0 (`DealEnvoy/crs-ai-agents`), which recorded file hashes before its runs.

## What is frozen at T01, before Stage 0

1. **Every pass/fail criterion and threshold** in `docs/trial-plan.md`, including the hard-fail gates (T06–T13).
2. **The runtime model candidate list** and the decision rule for choosing one (trial plan, section 7).
3. **The order of cuts** if funds are short, and the per-run limits. Each paid stage's spending limit is set by Isaac and recorded here before that stage starts.
4. **The synthetic data generator and its random seed.**
5. **The seeded-fault key** (the answers), which stays sealed and out of the repository until results are published.
6. **The forbidden-wording lexicon and the required disclaimer** (T12).

Nothing is run before the freeze.

## How fingerprints will be recorded

1. Isaac reviews and edits the criteria. Once final, the frozen files are listed in `PREREG_HASHES.txt` at the repository root, one line per file:

   ```
   <sha256>  <path>
   ```

   produced with `sha256sum <files> > PREREG_HASHES.txt` (or `shasum -a 256`).
2. The sealed key is hashed in the same list, so its fingerprint is public while its content is not.
3. The commit containing `PREREG_HASHES.txt` is tagged (`prereg-v1`), and the tag is signed by Isaac.
4. A small script, `verify_prereg.py`, will recompute every hash and report any mismatch. Anyone can run it.
5. When the key is published with the results, readers can confirm it matches the fingerprint recorded at the freeze.

## Limits of this record

The hash list and git tag are created by the author. Unless an external timestamp is added (for example a public post of the hash list, or a third-party timestamping service), they are a record of intent, not independent proof of timing. Any external timestamp used will be listed here.

## Amendments

After the freeze, a criterion can only change through a logged amendment in this file: date (Europe/London), what changed, why, and whether any result had been seen. Results run under an amended criterion are reported next to the original, not instead of it.

| Date | Change | Reason | Results seen before change? |
|---|---|---|---|
| — | none yet | — | — |
