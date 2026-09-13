#!/usr/bin/env python3
"""
validate.py -- checks that the requirements dataset is internally consistent.

Traceability enforcement. Standard library only, so every check here can be read
and changed without learning a framework.

Run:       python3 requirements/validate.py
Exit code: 0 if valid, 1 if any ERROR was found.
"""

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Conventions. Change these when the conventions change.
# ---------------------------------------------------------------------------

FUNCTION_ID = re.compile(r"^FUN-[A-Z]{2}-\d{2}$")      # FUN-PL-03
REQUIREMENT_ID = re.compile(r"^REQ-[A-Z]{2}-\d{3}$")   # REQ-PL-001
RISK_ID = re.compile(r"^RSK-\d{3}$")
CONSTRAINT_SOURCE = re.compile(r"^Constraint: .+$")    # Constraint: Amit

VERIFICATION = {"Inspection", "Analysis", "Demonstration", "Test"}
STATUS = {"draft", "agreed", "implemented", "verified", "dropped"}

# A requirement's type must match where it came from. This is the rule that
# keeps the three kinds of requirement from blurring into each other:
#   derived from a function   -> functional (or a performance/interface facet of one)
#   stated by a stakeholder   -> constraint
#   derived from a risk       -> safety
TYPE_BY_SOURCE = {
    "function":   {"functional", "performance", "interface"},
    "constraint": {"constraint"},
    "risk":       {"safety"},
}


def load(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def classify_source(value, function_ids, risk_ids, errors, rid):
    """Work out what kind of thing a requirement was generated from."""
    if value in function_ids:
        return "function"
    if value in risk_ids:
        return "risk"
    if CONSTRAINT_SOURCE.match(value):
        return "constraint"
    # Shaped like an ID but not found -> a dangling trace, which is the thing
    # traceability exists to prevent.
    if FUNCTION_ID.match(value) or RISK_ID.match(value):
        errors.append(f"{rid}: generated_from '{value}' does not exist")
    else:
        errors.append(
            f"{rid}: generated_from '{value}' is not a function, a risk, "
            f"or a stakeholder constraint"
        )
    return None


def main():
    errors, warnings = [], []

    functions = load("functions.csv")
    requirements = load("requirements.csv")
    risks = load("risks.csv")
    questions = load("open-questions.csv")

    # -- Functions: IDs unique and well formed --------------------------------
    function_ids = set()
    for row in functions:
        fid = row["id"]
        if not FUNCTION_ID.match(fid):
            errors.append(f"{fid}: malformed function ID (expected FUN-PL-nn)")
        if fid in function_ids:
            errors.append(f"{fid}: duplicate function ID")
        function_ids.add(fid)

    risk_ids = {r["id"] for r in risks}
    question_ids = {q["id"] for q in questions}

    # -- Requirements ---------------------------------------------------------
    seen = set()
    for row in requirements:
        rid = row["id"]

        if not REQUIREMENT_ID.match(rid):
            errors.append(f"{rid}: malformed requirement ID (expected REQ-PL-nnn)")
        if rid in seen:
            errors.append(f"{rid}: duplicate requirement ID")
        seen.add(rid)

        # Exactly one origin, and it must resolve.
        source = row["generated_from"].strip()
        kind = classify_source(source, function_ids, risk_ids, errors, rid)

        # Type must be consistent with that origin.
        rtype = row["type"].strip()
        if kind and rtype not in TYPE_BY_SOURCE[kind]:
            errors.append(
                f"{rid}: type '{rtype}' does not match a requirement generated "
                f"from a {kind} (expected: {', '.join(sorted(TYPE_BY_SOURCE[kind]))})"
            )

        # Controlled vocabulary.
        if row["verification"].strip() not in VERIFICATION:
            errors.append(
                f"{rid}: verification '{row['verification']}' not allowed "
                f"(expected: {', '.join(sorted(VERIFICATION))})"
            )
        if row["status"].strip() not in STATUS:
            errors.append(f"{rid}: status '{row['status']}' not allowed")

        # A requirement must say something, and must be a 'shall'.
        text = row["text"].strip()
        if not text:
            errors.append(f"{rid}: no requirement text")
        elif " shall " not in text and not text.startswith("No "):
            warnings.append(f"{rid}: text does not read as a 'shall' statement")

        # Any open question referenced in the text must actually exist, so that
        # a deferred decision cannot be quietly lost.
        for ref in re.findall(r"OPN-\d{3}", text):
            if ref not in question_ids:
                errors.append(f"{rid}: references {ref}, which does not exist")

    # -- Functions with nothing constraining them -----------------------------
    covered = {r["generated_from"].strip() for r in requirements}
    for row in functions:
        if row["id"] not in covered:
            warnings.append(f"{row['id']} ({row['name']}): no requirements generated from this function")

    # -- Risks must name mitigating requirements that exist -------------------
    # A risk is mitigated either by a safety requirement that exists only because
    # of it (generated_from = the risk), or by a requirement that exists for
    # functional reasons and happens to cover it. Both are legitimate, so the
    # check is on the mitigation column, not on where requirements came from.
    for r in risks:
        mitigation = r["mitigation"].strip()
        if not mitigation:
            errors.append(f"{r['id']}: no mitigation recorded")
        for ref in re.findall(r"REQ-[A-Z]{2}-\d{3}", mitigation):
            if ref not in seen:
                errors.append(f"{r['id']}: mitigation names {ref}, which does not exist")
        if not re.search(r"REQ-[A-Z]{2}-\d{3}", mitigation):
            warnings.append(f"{r['id']}: mitigation names no requirement")

    # -- Cross-references anywhere in the repository must resolve -------------
    # Requirement numbers shift when the set is consolidated. A reference left
    # behind in a decision or a diagram then points at the wrong thing, or at
    # nothing, and nobody notices. This catches it.
    known = function_ids | seen | risk_ids | question_ids
    targets = [os.path.join(HERE, "decisions.csv")]
    docs = os.path.join(os.path.dirname(HERE), "docs")
    if os.path.isdir(docs):
        targets += [os.path.join(docs, f) for f in sorted(os.listdir(docs)) if f.endswith(".md")]

    pattern = re.compile(r"\b(?:FUN|REQ)-[A-Z]{2}-\d{2,3}\b|\b(?:RSK|OPN)-\d{3}\b")
    for path in targets:
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                for ref in pattern.findall(line):
                    if ref not in known:
                        errors.append(
                            f"{os.path.basename(path)}:{lineno}: references {ref}, "
                            f"which does not exist"
                        )

    # -- Report ---------------------------------------------------------------
    for w in warnings:
        print(f"WARNING  {w}")
    for e in errors:
        print(f"ERROR    {e}")

    print()
    print(f"{len(functions)} functions, {len(requirements)} requirements, "
          f"{len(risks)} risks, {len(questions)} open questions, "
          f"{len(errors)} errors, {len(warnings)} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
