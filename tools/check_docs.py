#!/usr/bin/env python3
"""Document checks for trial tests T49 and T55 (and spec sanity for T50, T53, and the T12 lexicon strings).

Usage:
    python3 tools/check_docs.py threat-model   # T49
    python3 tools/check_docs.py security-docs  # T55 (script part; manual item stays with Isaac)
    python3 tools/check_docs.py specs          # T50 / T53 specification sanity
    python3 tools/check_docs.py lexicon        # T12: frozen tool strings vs the lexicon; document hits (information only)
    python3 tools/check_docs.py all

Standard library only. Reads files, writes nothing, makes no network call.
Exit code 0 = all checks pass, 1 = at least one check failed, 2 = usage error.
"""
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "docs", "trial-plan.md")
TM = os.path.join(ROOT, "docs", "security", "threat-model.md")

# Hard-fail tests that every threat model must cite (T49 criterion 7).
HARD_FAIL = (["T%02d" % n for n in range(6, 14)]
             + ["T50", "T51", "T53", "T54"]
             + ["T%d" % n for n in range(57, 63)]
             + ["T64", "T65"])
LLM_TAGS = ["LLM%02d" % n for n in range(1, 11)]
MCP_TAGS = ["MCP-TP", "MCP-TDI", "MCP-RP", "MCP-CD", "MCP-EA"]
STRIDE = ["S", "T", "R", "I", "D", "E"]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def plan_test_ids():
    text = read(PLAN)
    ids = set(re.findall(r"^### (T\d{2})\b", text, re.M))
    ids |= set(re.findall(r"^#### (T\d{2})\b", text, re.M))
    ids |= set(re.findall(r"^\| (T\d{2}) \|", text, re.M))
    return ids


def table_rows(text, first_cell_re):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(first_cell_re, cells[0]):
            rows.append(cells)
    return rows


def check_threat_model():
    errs = []
    if not os.path.exists(TM):
        return ["docs/security/threat-model.md is missing"]
    text = read(TM)
    known = plan_test_ids()
    comps = {r[0]: r[1] for r in table_rows(text, r"C\d+") if len(r) == 2}
    if len(comps) != 10:
        errs.append("expected 10 components, found %d" % len(comps))
    threats = [r for r in table_rows(text, r"TM-\d+") if len(r) == 7]
    if not threats:
        errs.append("no threat rows found")
    cited = set()
    tags = set()
    by_comp = {c: [] for c in comps}
    letters_of = {}
    for tid, comp, stride, tag, threat, mitig, tests in threats:
        if comp not in comps:
            errs.append("%s: unknown component %s" % (tid, comp))
        else:
            by_comp[comp].append(tid)
        ls = [x.strip() for x in stride.split(",") if x.strip()]
        letters_of[tid] = set(ls)
        if not ls or any(x not in STRIDE for x in ls):
            errs.append("%s: bad STRIDE letters %r" % (tid, stride))
        if not mitig.strip() or mitig.strip() in ("-", "–"):
            errs.append("%s: empty mitigation" % tid)
        tid_tests = [t.strip() for t in tests.split(",") if t.strip()]
        if not tid_tests:
            errs.append("%s: no test ID" % tid)
        for t in tid_tests:
            if not re.fullmatch(r"T\d{2}", t):
                errs.append("%s: bad test ID %r" % (tid, t))
            elif t not in known:
                errs.append("%s: test %s does not exist in trial-plan.md" % (tid, t))
            else:
                cited.add(t)
        if tag.strip() not in ("", "-", "–"):
            tags.add(tag.strip())
    for c, ids in by_comp.items():
        if not ids:
            errs.append("component %s has no threat row" % c)
    # STRIDE matrix
    matrix = [r for r in table_rows(text, r"C\d+ .*") if len(r) == 7]
    seen_matrix = set()
    for r in matrix:
        cid = r[0].split(" ")[0]
        seen_matrix.add(cid)
        for letter, cell in zip(STRIDE, r[1:]):
            if cell.startswith("N/A:"):
                if len(cell) < 12:
                    errs.append("matrix %s %s: N/A without a reason" % (cid, letter))
            else:
                ids = [x.strip() for x in cell.split(",") if x.strip()]
                if not ids:
                    errs.append("matrix %s %s: empty cell" % (cid, letter))
                for i in ids:
                    if i not in letters_of:
                        errs.append("matrix %s %s: unknown threat %s" % (cid, letter, i))
                    elif letter not in letters_of[i]:
                        errs.append("matrix %s %s: %s does not carry letter %s" % (cid, letter, i, letter))
    if set(comps) - seen_matrix:
        errs.append("matrix missing components: %s" % ", ".join(sorted(set(comps) - seen_matrix)))
    for t in LLM_TAGS + MCP_TAGS:
        if t not in tags:
            errs.append("no threat row tagged %s" % t)
    for t in HARD_FAIL:
        if t not in cited:
            errs.append("hard-fail test %s is not cited by any threat row" % t)
    print("threat-model: %d threats, %d components, %d tests cited" % (len(threats), len(comps), len(cited)))
    return errs


NEG = re.compile(r"\b(not|no|never|nor|neither|without|cannot|can't|isn't|doesn't|don't|unless|if|may|might|would|could|"
                 r"future|aim|aims|whether|any|nothing|none|until|before|toward|towards|target|planned|plan|"
                 r"to be|should|must not|would be|claim|claims|claimed)\b", re.I)
OVERCLAIM = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+(fully\s+|already\s+|now\s+)?(compliant|certified|approved|accredited|conformant)\b"
    r"|\bcompl(y|ies) with\b|\bin compliance with\b|\bcertified (to|against|under)\b|\bapproved (under|by)\b"
    r"|\baccredited (against|to)\b|\bconforms? to\b|\bmeets? (the )?(requirements|all|every)\b", re.I)
PLACE = [
    "SECURITY.md", "README.md", "docs/regulatory-path.md", "docs/ai-act-self-assessment.md",
]


def overclaim_files():
    files = list(PLACE)
    for d in ("docs/security", "docs/quality"):
        full = os.path.join(ROOT, d)
        if os.path.isdir(full):
            for name in sorted(os.listdir(full)):
                if name.endswith(".md"):
                    files.append(d + "/" + name)
    return files


def sentences(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    for block in re.split(r"\n\s*\n", text):
        flat = " ".join(block.split())
        for s in re.split(r"(?<=[.!?;])\s+|\s\|\s", flat):
            yield s


def check_security_docs():
    errs = []
    root_sec = os.path.join(ROOT, "SECURITY.md")
    doc_sec = os.path.join(ROOT, "docs", "security", "SECURITY.md")
    std = os.path.join(ROOT, "docs", "security", "standards-mapping.md")
    for p in (root_sec, doc_sec, std):
        if not os.path.exists(p):
            errs.append("missing %s" % os.path.relpath(p, ROOT))
    if errs:
        return errs
    if "docs/security/SECURITY.md" not in read(root_sec):
        errs.append("root SECURITY.md does not point to docs/security/SECURITY.md")
    for p in (root_sec, doc_sec):
        t = read(p)
        if not re.search(r"private security advisor", t, re.I):
            errs.append("%s does not name GitHub private security advisories" % os.path.relpath(p, ROOT))
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", t):
            errs.append("%s contains an e-mail address" % os.path.relpath(p, ROOT))
    t = read(std)
    sections = re.split(r"^## ", t, flags=re.M)[1:]
    wanted = {
        "OWASP Top 10 for LLM Applications": False,
        "NIST SP 800-218": False,
        "SLSA": False,
        "ISO/IEC 27001:2022": False,
        "EASA Part-IS": False,
    }
    for sec in sections:
        head = sec.splitlines()[0]
        for k in wanted:
            if k in head:
                wanted[k] = True
                if not re.search(r"alignment, not compliance", sec, re.I):
                    errs.append("standards-mapping section '%s' is not marked 'alignment, not compliance'" % head)
    for k, ok in wanted.items():
        if not ok:
            errs.append("standards-mapping has no section for %s" % k)
    n = 0
    for rel in overclaim_files():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        for s in sentences(read(p)):
            if OVERCLAIM.search(s) and not NEG.search(s):
                errs.append("possible overclaim in %s: %s" % (rel, s[:160]))
            n += 1
    print("security-docs: scanned %d sentences in %d files" % (n, len(overclaim_files())))
    print("security-docs: MANUAL item not checked by script: private vulnerability reporting switched on in repository settings")
    return errs


def check_specs():
    errs = []
    pf = os.path.join(ROOT, "docs", "security", "planted-failure-set-spec.md")
    fz = os.path.join(ROOT, "docs", "security", "fuzz-corpus-spec.md")
    if not os.path.exists(pf) or not os.path.exists(fz):
        return ["planted-failure or fuzz spec missing"]
    t = read(pf)
    for i in range(1, 41):
        if not re.search(r"^\| PF%02d \|" % i, t, re.M):
            errs.append("PF%02d missing" % i)
    for i in range(1, 11):
        if not re.search(r"^\| PC%02d \|" % i, t, re.M):
            errs.append("PC%02d missing" % i)
    f = read(fz)
    total = 0
    for cls in "ABCDEFGHI":
        m = re.search(r"^\| FZ-%s \| [^|]+\| (\d+) \|" % cls, f, re.M)
        if not m:
            errs.append("class FZ-%s missing" % cls)
        else:
            total += int(m.group(1))
    if total < 200:
        errs.append("only %d targeted fuzz cases; need at least 200" % total)
    print("specs: 40 PF, 10 PC checked; %d targeted fuzz cases" % total)
    return errs


def lexicon_patterns():
    with open(os.path.join(ROOT, "data", "t12_lexicon.json"), encoding="utf-8") as fh:
        lex = json.load(fh)
    return lex, [(p["id"], re.compile(p["regex"], re.I)) for p in lex["forbidden_patterns"]]


def norm(text):
    return unicodedata.normalize("NFKC", " ".join(text.split()))


def check_lexicon():
    """T12 script part. Fails if a frozen tool string matches a forbidden pattern, if the two status
    lines differ between the lexicon and the trial plan, or if the old status wording is still present.
    Document hits are printed for information only: documents quote the phrases to forbid them."""
    errs = []
    lex, pats = lexicon_patterns()
    strings = lex.get("frozen_tool_strings", {})
    need = ("status_review_complete", "status_review_incomplete", "disclaimer", "intended_purpose",
            "zero_findings_statement")
    for k in need:
        if k not in strings:
            errs.append("lexicon has no frozen string %s" % k)
    for k, v in strings.items():
        for pid, rx in pats:
            if rx.search(norm(v)):
                errs.append("frozen tool string %s matches %s" % (k, pid))
    plan = read(PLAN)
    for k in ("status_review_complete", "status_review_incomplete"):
        if k in strings and ("`%s`" % strings[k]) not in plan:
            errs.append("trial-plan.md does not contain the frozen line %s verbatim" % k)
    if lex.get("required_disclaimer") != strings.get("disclaimer"):
        errs.append("required_disclaimer differs from the frozen disclaimer string")
    stale = []
    for r, _, files in os.walk(ROOT):
        if os.sep + ".git" in r or os.sep + "packages" in r or os.sep + "corpora" in r:
            continue
        for name in files:
            if name.endswith((".md", ".py", ".json", ".txt")) and name != "check_docs.py":
                p = os.path.join(r, name)
                if "NOT READY" in read(p):
                    stale.append(os.path.relpath(p, ROOT))
    for p in stale:
        errs.append("old status wording 'NOT READY' still present in %s" % p)
    # information only
    doc_hits = {}
    for r, _, files in os.walk(ROOT):
        if os.sep + ".git" in r or os.sep + "packages" in r or os.sep + "corpora" in r:
            continue
        for name in files:
            if name.endswith(".md"):
                p = os.path.join(r, name)
                t = norm(read(p))
                n = sum(1 for _, rx in pats if rx.search(t))
                if n:
                    doc_hits[os.path.relpath(p, ROOT)] = n
    print("lexicon: %d patterns; %d frozen tool strings checked" % (len(pats), len(strings)))
    print("lexicon: document hits (information only, documents are out of scope): %d file(s) %s"
          % (len(doc_hits), json.dumps(doc_hits, sort_keys=True)))
    return errs


def main(argv):
    cmds = {"threat-model": check_threat_model, "security-docs": check_security_docs, "specs": check_specs,
            "lexicon": check_lexicon}
    if len(argv) != 2 or (argv[1] != "all" and argv[1] not in cmds):
        print(__doc__)
        return 2
    run = list(cmds) if argv[1] == "all" else [argv[1]]
    failed = False
    for name in run:
        errs = cmds[name]()
        if errs:
            failed = True
            print("FAIL %s" % name)
            for e in errs:
                print("  - " + e)
        else:
            print("PASS %s" % name)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
