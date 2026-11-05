# Planted-failure set: specification (T50)

Status: **specification, frozen at T01 (Freeze 1, 5 Nov 2026). Nothing has been built or run.** Author: Isaac Adekunle. Written 4 Nov 2026 (Europe/London).

## 1. Purpose

T50 (fail-safe, HARD FAIL) requires that the tool never gives a clean-looking result after a failed or partial review. This set is the list of failures to plant. Rule: **any crash, timeout, unreadable or malformed record, missing data, bad signature or hash mismatch gives `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`, never a clean report.**

## 2. Expected output for every PF case

1. The status line is exactly `REVIEW INCOMPLETE - checks could not finish; do not rely on this report` and it is the first line of the report.
2. Exit code 3.
3. The failure class and the stage where it happened are named. Classes: INPUT_MISSING, INPUT_UNREADABLE, INPUT_MALFORMED, INTEGRITY, SIGNATURE, INTERNAL_ERROR, TIMEOUT, RESOURCE, AUDIT_WRITE, CONFIG, ENVIRONMENT, LIMIT_EXCEEDED. Stages: START, DISCOVER, MANIFEST, READ, PARSE, VALIDATE, RULES, AUDIT, REPORT, FINGERPRINT, OUTPUT.
4. The checks that did not complete are listed by name.
5. No finding list, count or summary appears in a form that could be read as a partial all-clear. A partial list of findings found before the failure may be shown only under a heading saying it is incomplete.
6. An audit-log entry is written with the failure class and stage. If the audit write is itself the failure (PF06, PF07, PF37), the message goes to standard error, the status is still `REVIEW INCOMPLETE` and the exit code is still 3.
7. If the report cannot be delivered (PF08, PF40), standard error carries the message and the exit code is 3.
8. Error text contains no record free text and no environment or path data beyond the package id.

## 3. Boundary note: missing data versus a finding (confirmed by Isaac, 5 Nov 2026, frozen at T01)

A **finding** is a gap in the maintenance record that the tool exists to detect (for example a task card whose sign-off field is present and empty). The tool reports findings and still finishes with `REVIEW COMPLETE - findings listed; a certifying engineer decides`.

A **not-run check** is a check that could not run because its input was absent, unreadable or not trustworthy. Any not-run check gives `REVIEW INCOMPLETE - checks could not finish; do not rely on this report`.

Where a package has withheld fields (the T08 set), the rule here treats a field a check depends on as a not-run check, so those packages give `REVIEW INCOMPLETE` with the exact missing field paths listed, in line with T08 (no guessed value). This boundary is confirmed and frozen at T01: **a gap in the record is a finding; a check that could not run gives `REVIEW INCOMPLETE`.** It decides what the T08 packages must output.

## 4. Planted failures (40)

The failure is injected from outside the production code path (a fault-injection harness: environment, file permissions, a patched module loaded by the test runner, signals), so the production code is the code under test. Each case starts from a known-good package from the generated set unless stated.

| ID | Stage | Failure planted | Expected class |
|---|---|---|---|
| PF01 | START | Rule-set file missing | CONFIG |
| PF02 | START | Rule-set file altered by one byte (hash differs from the pinned hash) | INTEGRITY |
| PF03 | START | Tool-manifest hash differs from the pinned hash | INTEGRITY |
| PF04 | START | Configuration file unreadable (permission denied) | CONFIG |
| PF05 | START | Configuration file invalid (unknown key, wrong type) | CONFIG |
| PF06 | START | Audit-log directory missing | AUDIT_WRITE |
| PF07 | START | Audit-log directory not writable | AUDIT_WRITE |
| PF08 | START | Report directory not writable | AUDIT_WRITE |
| PF09 | DISCOVER | Package directory does not exist | INPUT_MISSING |
| PF10 | DISCOVER | Package directory exists and is empty | INPUT_MISSING |
| PF11 | MANIFEST | Package MANIFEST file missing | INPUT_MISSING |
| PF12 | MANIFEST | One record file changed by one byte after the manifest was made (hash mismatch) | INTEGRITY |
| PF13 | MANIFEST | A file listed in the manifest is absent | INPUT_MISSING |
| PF14 | MANIFEST | A file present in the package is not in the manifest | INTEGRITY |
| PF15 | MANIFEST | Manifest unreadable (permission denied) | INPUT_UNREADABLE |
| PF16 | MANIFEST | Manifest malformed (bad line format) | INPUT_MALFORMED |
| PF17 | READ | Record file unreadable (permission denied) | INPUT_UNREADABLE |
| PF18 | PARSE | Record file truncated mid-value | INPUT_MALFORMED |
| PF19 | PARSE | Record file with invalid UTF-8 bytes | INPUT_MALFORMED |
| PF20 | PARSE | Record file of zero bytes | INPUT_MALFORMED |
| PF21 | VALIDATE | Required top-level section absent (for example the task cards) | INPUT_MISSING |
| PF22 | VALIDATE | A field that a check depends on is absent from a record, so that check cannot run (see the boundary note in section 3) | INPUT_MISSING |
| PF23 | VALIDATE | Unknown schema version | INPUT_MALFORMED |
| PF24 | PARSE | Duplicate key in an object | INPUT_MALFORMED |
| PF25 | VALIDATE | Wrong type in a key field (string where a list is required) | INPUT_MALFORMED |
| PF26 | VALIDATE | Declared record count differs from the number of records present | INPUT_MALFORMED |
| PF27 | PARSE | NaN literal in a number field | INPUT_MALFORMED |
| PF28 | PARSE | Exception injected inside the parser | INTERNAL_ERROR |
| PF29 | VALIDATE | Exception injected inside the validator | INTERNAL_ERROR |
| PF30 | RULES | Exception injected inside one rule (the other rules would run normally) | INTERNAL_ERROR |
| PF31 | REPORT | Exception injected inside the report builder | INTERNAL_ERROR |
| PF32 | FINGERPRINT | Exception injected inside the fingerprint step | INTERNAL_ERROR |
| PF33 | RULES | MemoryError injected during rules | RESOURCE |
| PF34 | PARSE | RecursionError injected during parsing | RESOURCE |
| PF35 | RULES | One rule sleeps beyond the 30 s watchdog | TIMEOUT |
| PF36 | RULES | Worker process (if the design uses one) killed with SIGKILL | INTERNAL_ERROR |
| PF37 | AUDIT | Audit write fails part-way through the run (no space left) | AUDIT_WRITE |
| PF38 | AUDIT | The existing audit log fails chain verification at start (an old entry was edited) | INTEGRITY |
| PF39 | START | Signature on the release bundle (rule set and manifest) is invalid | SIGNATURE |
| PF40 | OUTPUT | Standard output closed (broken pipe) when the report is written | ENVIRONMENT |

## 5. Controls (10)

Controls prove that the fail-safe is not simply always on. Each must give a normal report and no `REVIEW INCOMPLETE` banner.

| ID | Case | Expected |
|---|---|---|
| PC01 | A clean twin from the generated Tier-1 set | REVIEW COMPLETE - findings listed; a certifying engineer decides, with the T65 zero-findings statement |
| PC02 | A faulted package from the Tier-1 set | REVIEW COMPLETE - findings listed; a certifying engineer decides, the seeded critical fault flagged |
| PC03 | A Tier-2 package | REVIEW COMPLETE, findings as the oracle states |
| PC04 | A hard-set package | REVIEW COMPLETE, findings as the oracle states |
| PC05 | A forged-approval package (T41 set) | REVIEW COMPLETE, forged approval text treated as data, flagged, not accepted |
| PC06 | An injection package (T38 set) | REVIEW COMPLETE, injection text quoted only inside escaped citation fields |
| PC07 | A valid package just under the size limits (49 MiB, 499 files) | REVIEW COMPLETE within 30 s and 512 MiB |
| PC08 | A valid record nested exactly 32 deep | REVIEW COMPLETE |
| PC09 | A valid file name of exactly 255 bytes | REVIEW COMPLETE |
| PC10 | An audit log of 10,000 valid chained entries | Chain verifies; a normal report; the new entry appended |

## 6. Pass/fail

40 of 40 PF cases and 10 of 10 PC cases. A single PF case that yields `REVIEW COMPLETE - findings listed; a certifying engineer decides` fails T50 and is a hard fail for the whole project. Cases are run with the section 3a limits of `docs/trial-plan.md` enforced from outside the process.

## 7. Generation

No new data files are needed for most PF cases: they are produced at test time by copying a package from `data/packages/` and applying a scripted change, or by the fault-injection harness. The scripted changes and the harness are written and frozen with the rest of the test code at T01. `data/generate.py`, the sealed key and `data/packages/MANIFEST.sha256` are unchanged by this specification.
