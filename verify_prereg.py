#!/usr/bin/env python3
"""Recompute SHA-256 for every file listed in PREREG_HASHES.txt and report mismatches.

Usage: python3 verify_prereg.py [hash_list]
Default list: PREREG_HASHES.txt.
Paths are relative to the repository root. The secret salt and the sealed key
(../sealed/seeded_fault_key.salt, ../sealed/seeded_fault_key.json) are checked
when present locally and reported as SEALED-ABSENT otherwise (not a failure).
Their contents are never in the repository; only the fingerprints are listed.
Exit 0 = all present files match; 1 = mismatch or missing repo file.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SEALED_MARK = "seeded_fault_key"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    lst = argv[1] if len(argv) > 1 else None
    if lst is None:
        for cand in ("PREREG_HASHES.txt",):
            if os.path.exists(os.path.join(ROOT, cand)):
                lst = cand
                break
    if lst is None:
        print("No PREREG_HASHES file found.")
        return 1
    bad = 0
    n = 0
    with open(os.path.join(ROOT, lst), encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            want, rel = line.split(None, 1)
            rel = rel.lstrip("*").strip()
            path = os.path.normpath(os.path.join(ROOT, rel))
            n += 1
            if not os.path.exists(path):
                if SEALED_MARK in rel:
                    print("SEALED-ABSENT  %s (not available locally; check after publication)" % rel)
                    continue
                print("MISSING        %s" % rel)
                bad += 1
                continue
            got = sha256(path)
            if got == want.lower():
                print("OK             %s" % rel)
            else:
                print("MISMATCH       %s\n  expected %s\n  actual   %s" % (rel, want, got))
                bad += 1
    print("%s: %d entries, %d problem(s)" % (lst, n, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
