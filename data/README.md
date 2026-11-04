# Data

**Empty. No data has been generated yet.**

All data in this project will be **synthetic**: invented aircraft, registrations, operators, parts, defects, tasks, directives and records. No real aircraft, operator or maintenance organisation records will ever be stored here. Any resemblance to a real company, aircraft or person is unintended.

Planned contents (after T01):

- `generator/` — the synthetic record generator, run with a fixed random seed.
- `packages/` — generated work packages: packages with seeded faults, matching clean twins, packages with deliberately withheld fields, and packages with planted hostile text (prompt-injection test cases).
- The **seeded-fault key** (the answers) is kept out of the repository (`data/sealed/`, ignored by git) until results are published. Its SHA-256 fingerprint is recorded at the T01 freeze, so anyone can later check it was not changed.

Regulatory source texts used for quotation checks (T02) will be stored with their URL, retrieval date and SHA-256 fingerprint.
