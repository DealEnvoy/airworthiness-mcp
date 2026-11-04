# Human-factors note: how a tired reader might misread a report

Date: 4 Nov 2026 (Europe/London). Owner: Isaac Adekunle. Tests: T65 (hard fail for the zero-findings statement), T58, T59, T12. AS9110-style human-factors awareness; no claim of conformity.

## 1. Why this matters

The reader of a report is a certifying person who may be tired, interrupted, under time pressure at the end of a shift, or trusting a tool that has been right many times. The most dangerous failure of this tool is not a loud error. It is a quiet report that looks like an all-clear.

## 2. Misreadings to design against

| Misreading | Why it happens | Design response | Test |
|---|---|---|---|
| "No findings, so it is fine." | An empty list reads as approval | Fixed zero-findings statement: "No findings from the checks that ran. This is not an assurance that the records are complete or correct. A certifying human decides." plus a list of checks that ran and checks that did not | T65 |
| "Tool ran, so everything was checked." | The tool crashed or skipped a file and the output looks normal | Fail-safe: `NOT READY - review incomplete`, first line, exit code 3; no partial summary shown as complete | T50 |
| "Ready" read into "REVIEW COMPLETE". | "Complete" is read as "good" | The complete status always says "findings for human review"; no colour-only signal; no "ready", "pass", "OK", "clear" words | T59, T12 |
| Only the top of the report is read. | Fatigue; long lists | Status line first; critical findings first; counts of each severity at the top; the missing-data block is never collapsed | T65 |
| Finding fatigue. | Many low-value findings hide a critical one | Critical-first ordering; deduplicated findings; false-alarm rate measured (T31) | T65, T31 |
| Colour or icon as the only signal. | Colour-blindness; black-and-white printing; screen readers | Text first; no emoji or abbreviation as the only carrier of a status | T65 |
| "The tool says the sign-off is there." | The tool is read as confirming that a signature is valid | Reports say what is present in the record, cite the field, and never say a signature is valid or genuine | T59 |
| Quoted record text read as the tool's own words. | Hostile or confusing text inside a record | Record text appears only inside labelled, escaped citation fields | T11, T53 |
| A model's text read as a rule result. | Mixed output | Visible and machine-readable label on every language-model item; transparency note | T61 |
| Date and time confusion. | Mixed formats and zones | One format; Europe/London stated; dates in ISO form | T65 |
| Reading a report from an old run. | Several reports in a folder | Report carries the package id, run time, input hashes and fingerprint; a changed record changes the hash | T54 |
| Pressure to "just release it". | Schedule pressure | The tool has no release function and says a certifying human decides, in every report | T58 |

## 3. Rules for report content

1. First line: exactly one of the two status lines.
2. Intended-purpose statement and disclaimer in the header.
3. Critical findings first, then others by severity.
4. Missing data listed by exact field path, never collapsed.
5. List of checks that ran and checks that did not run.
6. Plain language; short sentences; no jargon that is not in the maintenance record.
7. No claim about the aircraft, only about the records.

## 4. Validation

T65 checks the rules by code on all 158 generated reports. A usability check with real certifying staff is **not done**; it is part of the optional human mini-study (T37) and the R1 reviewer's scope (`competence-records.md`).
