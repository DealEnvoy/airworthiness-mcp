# Suspected unapproved parts: awareness in the parts checks

Date: 4 Nov 2026 (Europe/London). Owner: Isaac Adekunle. Test: T63 (gate). Data set specification: `docs/security/fuzz-corpus-spec.md` section 6. AS9110-style counterfeit awareness; no claim of conformity.

## 1. Position

The tool's parts checks include **documentary indicators** that a part's paperwork may be inconsistent. They raise a flag for a human to review. They never say that a part is counterfeit, suspect-proven or unapproved. Deciding that is for qualified people following their organisation's procedures and the authority's guidance.

Wording used in reports: "Documentation indicator for review: possible suspect part."

## 2. Indicators (planned)

1. Release-certificate reference blank or missing on an installed part.
2. No traceability to the manufacturer or supplier.
3. Part-number format inconsistent with the recorded part type.
4. Serial-number format inconsistent with the recorded part type.
5. The same serial number on two installed parts.
6. Installation date earlier than the recorded receipt date.
7. Supplier on a user-supplied list for review.
8. The same certificate reference used for two different part numbers.

## 3. Limits

* The tool cannot see the part. It only reads what the record says.
* A forged document that is internally consistent will not be flagged.
* The indicator list is not exhaustive and is not an official list.
* Regulatory and industry references for suspected unapproved parts (for example authority guidance and bulletins) have **not** been collected yet. They are to be gathered under T02 and verified there. None is cited here, to avoid citing something unverified.
* The generated data set `t63_sup` (56 packages) and the sealed key carry this fault class from the T01 freeze, so T63 can run in Stage 0. The data are fictional and the faults are non-critical.

## 4. Review

The B1 reviewer (R1) is asked to review the indicator list and the wording (`competence-records.md`).
