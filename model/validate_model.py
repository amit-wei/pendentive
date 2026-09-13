#!/usr/bin/env python3
"""
validate_model.py -- checks that the system model is internally consistent.

This is the traceability enforcement. Standard library only, so every check can be
read and changed without learning a framework.

Run:       python3 model/validate_model.py
Exit code: 0 if valid, 1 if any ERROR was found.

Levels are discovered, not hard-coded: any directory under model/ holding a file
named *_requirements.csv is treated as a decomposition level. Adding
model/system/system_requirements.csv needs no change here.
"""

import csv
import glob
import os
import re
import sys

MODEL = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(MODEL)
REGISTERS = os.path.join(MODEL, "registers")
DOCS = os.path.join(REPO, "docs")

# ---------------------------------------------------------------------------
# Conventions. Change these when the conventions change.
# ---------------------------------------------------------------------------

FUNCTION_ID = re.compile(r"^FUN-[A-Z]{2}-\d{2}$")      # FUN-PL-03
REQUIREMENT_ID = re.compile(r"^REQ-[A-Z]{2}-\d{3}$")   # REQ-PL-001
RISK_ID = re.compile(r"^RSK-\d{3}$")
CONSTRAINT_SOURCE = re.compile(r"^Constraint: .+$")    # Constraint: Amit

VERIFICATION = {"Inspection", "Analysis", "Demonstration", "Test"}
STATUS = {"draft", "agreed", "implemented", "verified", "dropped"}

# A requirement's type must match where it came from. This is what keeps the three
# kinds of requirement from blurring together:
#   from a function      -> functional (or a performance/interface facet of one)
#   from a stakeholder   -> constraint
#   from a risk          -> safety
TYPE_BY_SOURCE = {
    "function":   {"functional", "performance", "interface"},
    "constraint": {"constraint"},
    "risk":       {"safety"},
}

# Anything shaped like an identifier, wherever it appears in prose.
REFERENCE = re.compile(r"\b(?:FUN|REQ)-[A-Z]{2}-\d{2,3}\b|\b(?:RSK|OPN|DEC|MET)-\d{3}\b")


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    errors, warnings = [], []

    # -- Discover the decomposition levels ------------------------------------
    functions, requirements = [], []
    for path in sorted(glob.glob(os.path.join(MODEL, "*", "*_functions.csv"))):
        functions += load(path)
    for path in sorted(glob.glob(os.path.join(MODEL, "*", "*_requirements.csv"))):
        requirements += load(path)

    if not requirements:
        print("ERROR    no *_requirements.csv found under model/")
        return 1

    risks = load(os.path.join(REGISTERS, "risk_register.csv"))
    questions = load(os.path.join(REGISTERS, "open_questions.csv"))
    decisions = load(os.path.join(REGISTERS, "design_decisions.csv"))
    decisions += load(os.path.join(REGISTERS, "method_decisions.csv"))

    # -- Functions: identifiers unique and well formed ------------------------
    function_ids = set()
    for row in functions:
        fid = row["id"]
        if not FUNCTION_ID.match(fid):
            errors.append(f"{fid}: malformed function identifier (expected FUN-PL-nn)")
        if fid in function_ids:
            errors.append(f"{fid}: duplicate function identifier")
        function_ids.add(fid)

    risk_ids = {r["id"] for r in risks}
    question_ids = {q["id"] for q in questions}
    decision_ids = {d["id"] for d in decisions}

    # -- Requirements ---------------------------------------------------------
    requirement_ids = set()
    for row in requirements:
        rid = row["id"]

        if not REQUIREMENT_ID.match(rid):
            errors.append(f"{rid}: malformed requirement identifier (expected REQ-PL-nnn)")
        if rid in requirement_ids:
            errors.append(f"{rid}: duplicate requirement identifier")
        requirement_ids.add(rid)

        # Exactly one origin, and it must resolve.
        source = row["generated_from"].strip()
        if source in function_ids:
            kind = "function"
        elif source in risk_ids:
            kind = "risk"
        elif CONSTRAINT_SOURCE.match(source):
            kind = "constraint"
        else:
            kind = None
            errors.append(
                f"{rid}: generated_from '{source}' is not a function, a risk, "
                f"or a stakeholder constraint"
            )

        # Type must be consistent with that origin.
        rtype = row["type"].strip()
        if kind and rtype not in TYPE_BY_SOURCE[kind]:
            errors.append(
                f"{rid}: type '{rtype}' does not match a requirement generated from "
                f"a {kind} (expected: {', '.join(sorted(TYPE_BY_SOURCE[kind]))})"
            )

        if row["verification"].strip() not in VERIFICATION:
            errors.append(
                f"{rid}: verification '{row['verification']}' not allowed "
                f"(expected: {', '.join(sorted(VERIFICATION))})"
            )
        if row["status"].strip() not in STATUS:
            errors.append(f"{rid}: status '{row['status']}' not allowed")

        text = row["text"].strip()
        if not text:
            errors.append(f"{rid}: no requirement text")
        elif " shall " not in text and not text.startswith("No "):
            warnings.append(f"{rid}: text does not read as a 'shall' statement")

    # -- Requirements below product level must name a parent that exists ------
    # Product requirements have no parent within the model; their parent is the
    # function. Every level below traces upward, which is the other half of the V.
    for row in requirements:
        parent = (row.get("parent_id") or "").strip()
        if parent and parent not in requirement_ids:
            errors.append(f"{row['id']}: parent_id '{parent}' does not exist")

    # -- Functions with nothing constraining them -----------------------------
    covered = {r["generated_from"].strip() for r in requirements}
    for row in functions:
        if row["id"] not in covered:
            warnings.append(
                f"{row['id']} ({row['name']}): no requirements generated from this function"
            )

    # -- Risks must name mitigating requirements that exist -------------------
    # A risk is mitigated either by a safety requirement existing only because of
    # it, or by a requirement that exists for functional reasons and happens to
    # cover it. Both are legitimate, so the check is on the mitigation column.
    for row in risks:
        mitigation = row["mitigation"].strip()
        if not mitigation:
            errors.append(f"{row['id']}: no mitigation recorded")
        for ref in re.findall(r"REQ-[A-Z]{2}-\d{3}", mitigation):
            if ref not in requirement_ids:
                errors.append(f"{row['id']}: mitigation names {ref}, which does not exist")

    # -- Every cross-reference anywhere must resolve --------------------------
    # Identifiers shift when a set is consolidated or split. A reference left
    # behind in a decision, a diagram or the schema then points at nothing, and
    # nobody notices. This has happened twice; hence the check.
    known = function_ids | requirement_ids | risk_ids | question_ids | decision_ids
    targets = sorted(glob.glob(os.path.join(REGISTERS, "*.csv")))
    targets.append(os.path.join(MODEL, "model_schema.md"))
    targets.append(os.path.join(REPO, "README.md"))
    if os.path.isdir(DOCS):
        targets += sorted(glob.glob(os.path.join(DOCS, "*.md")))

    for path in targets:
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                for ref in REFERENCE.findall(line):
                    if ref not in known:
                        errors.append(
                            f"{os.path.relpath(path, REPO)}:{lineno}: references "
                            f"{ref}, which does not exist"
                        )

    # -- Report ---------------------------------------------------------------
    for w in warnings:
        print(f"WARNING  {w}")
    for e in errors:
        print(f"ERROR    {e}")

    print()
    print(f"{len(functions)} functions, {len(requirements)} requirements, "
          f"{len(risks)} risks, {len(decisions)} decisions, "
          f"{len(questions)} open questions, "
          f"{len(errors)} errors, {len(warnings)} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
