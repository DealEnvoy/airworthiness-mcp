# Release control

Date: 4 Nov 2026 (Europe/London). Owner: Isaac Adekunle. Test: T66 (gate), extends T35.

## 1. Rule

**Nothing is released until (a) the tests pass and (b) Isaac has signed off.** A release means a version tag, a published package or a published build of the software. Publishing planning documents, test plans or specifications is not a release of the software.

## 2. Preconditions for a release

1. Frozen hash list verified (`python3 verify_prereg.py` exits 0); any change since the freeze is a logged amendment.
2. Pass records for every **hard-fail test**: T06–T13, T50, T51, T53, T54, T57–T62, T64, T65. One open hard fail means no release and no waiver.
3. Pass records for every **gate**: T49, T52, T55, T56, T63.
4. T14: SBOM generated, dependencies pinned by hash, signature verified in a clean environment, data-protection checklist done.
5. T56: three review records (certifying engineer, CAMO or quality, security) complete with competence recorded; no open high or critical finding unless Isaac accepted the risk in writing with a reason; re-test after fixes done.
6. T66 script: record complete, hashes match the commit; CI workflows pin third-party actions to commit SHAs and use least-privilege token permissions; secret scan finds 0 secrets; the sealed key is not in the repository.
7. `CHANGELOG.md` entry written; if the tool manifest changed, the version was bumped (T64).
8. Open items in `corrective-action-log.md` are closed or explicitly accepted by Isaac.
9. `risk-register.md` reviewed on the release date.
10. Intended-purpose statement and disclaimer present (T58); regulatory documents re-read for overclaiming (T55).

## 3. Release record (template)

Copy this block into `docs/quality/releases/<version>.md` for each release.

```
Release: <version>            Date (Europe/London): <date and time>
Commit: <full hash>           Tag: <name>
Hard-fail tests (T06-T13, T50, T51, T53, T54, T57-T62, T64, T65): <pass record path / hash for each>
Gates (T49, T52, T55, T56, T63): <pass record path / hash for each>
T14 SBOM and signature result: <path / hash>
Review records (T56): certifying engineer <path>, CAMO or quality <path>, security <path>
Open findings and accepted risks: <list, each with reason and date>
Rule-set hash: <sha256>       Tool-manifest hash: <sha256>
Secret scan result: <tool, version, result>
Sign-off: Isaac Adekunle        Date: <date>        Signature or statement: <text>
```

## 4. Hotfix

A security fix goes through the same record, but the full hard-fail run may be limited to the tests the change could affect **plus** T50, T53, T54 and T64. The reasoning is written in the release record. No hard fail is waived.

## 5. Withdrawal

If a defect is found after release that could let a clean-looking result appear after an incomplete review, the release is withdrawn from distribution, a security advisory is published, and a corrective action is opened.

## 6. Status

No release has been made. Nothing has been built.
