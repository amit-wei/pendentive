#!/usr/bin/env python3
"""
validate_model.py -- checks that the system model is internally consistent.

This is the traceability enforcement. Standard library only, so every check can be
read and changed without learning a framework.

Run:       python3 model/validate_model.py
Exit code: 0 if valid, 1 if any ERROR was found.

Levels are discovered, not hard-coded: any directory under model/ holding a file
named *_requirements.csv is treated as a decomposition level. Risks are
discovered the same way, from *_risks.csv. Adding model/system/ with either
in it needs no change here.
"""

import csv
import glob
import os
import re
import sys

MODEL = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(MODEL)
REGISTERS = os.path.join(MODEL, "registers")
PRODUCT = os.path.join(MODEL, "product")   # the root of the decomposition tree
DOCS = os.path.join(REPO, "docs")

# ---------------------------------------------------------------------------
# Conventions. Change these when the conventions change.
# ---------------------------------------------------------------------------

# One code per level, to a maximum of four levels: product, system, subsystem,
# component (MET-009). FUN-ST-CU-01, REQ-ST-CU-JN-001.
PATH_CODES = r"[A-Z]{2}(?:-[A-Z]{2}){0,2}"
FUNCTION_ID = re.compile(rf"^FUN-{PATH_CODES}-\d{{2}}$")
REQUIREMENT_ID = re.compile(rf"^REQ-{PATH_CODES}-\d{{3}}$")
RISK_ID = re.compile(rf"^RSK-{PATH_CODES}-\d{{3}}$")
CONSTRAINT_SOURCE = re.compile(r"^Constraint: .+$")    # Constraint: Amit

VERIFICATION = {"Inspection", "Analysis", "Demonstration", "Test"}
STATUS = {"draft", "agreed", "implemented", "verified", "dropped"}

# A decision is never deleted, so it needs a way to say it no longer governs.
# superseded: replaced by a fuller statement, the substance unchanged.
# reversed:   the condition in reverses_if fired and the substance changed.
DECISION_STATUS = {"proposed", "agreed", "superseded", "reversed"}
RETIRED = {"superseded", "reversed"}

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
REFERENCE = re.compile(
    rf"\b(?:FUN|REQ|RSK)-{PATH_CODES}-\d{{2,3}}\b|\b(?:OPN|DEC|MET)-\d{{3}}\b")


def compartment_of(identifier):
    """The compartment path in an identifier, which is everything between the
    prefix and the number: REQ-PL-001 -> PL, REQ-ST-CU-001 -> ST-CU."""
    parts = identifier.split("-")
    return "-".join(parts[1:-1]) if len(parts) >= 3 else None


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    errors, warnings = [], []

    # -- Discover the decomposition levels ------------------------------------
    # A risk is a failure mode of one compartment, so it lives with that
    # compartment rather than in a register spanning every level (MET-008).
    functions, requirements, risks = [], [], []
    by_directory = {}          # directory -> set of compartments found in it
    for kind, bucket in (("functions", functions),
                         ("requirements", requirements),
                         ("risks", risks)):
        for path in sorted(glob.glob(
                os.path.join(MODEL, "**", f"*_{kind}.csv"), recursive=True)):
            rows = load(path)
            bucket += rows
            seen = by_directory.setdefault(os.path.dirname(path), set())
            seen.update(c for c in (compartment_of(r["id"]) for r in rows) if c)

    if not requirements:
        print("ERROR    no *_requirements.csv found under model/")
        return 1

    questions = load(os.path.join(REGISTERS, "open_questions.csv"))
    compartments = load(os.path.join(REGISTERS, "compartments.csv"))
    declared = {row["path"]: row["compartment"] for row in compartments}
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

    risk_ids = set()
    for row in risks:
        kid = row["id"]
        if not RISK_ID.match(kid):
            errors.append(f"{kid}: malformed risk identifier (expected RSK-PL-nnn)")
        if kid in risk_ids:
            errors.append(f"{kid}: duplicate risk identifier")
        risk_ids.add(kid)

    question_ids = {q["id"] for q in questions}
    decision_ids = {d["id"] for d in decisions}

    # -- Decisions: a retired one must say what replaced it -------------------
    # A decision that no longer governs, with no pointer to what does, is worse
    # than no entry at all: it reads as current.
    for row in decisions:
        status = (row.get("status") or "").strip()
        replaced_by = (row.get("superseded_by") or "").strip()
        if status not in DECISION_STATUS:
            errors.append(
                f"{row['id']}: status '{status}' not allowed "
                f"(expected: {', '.join(sorted(DECISION_STATUS))})"
            )
        if status in RETIRED and not replaced_by:
            errors.append(f"{row['id']}: status is '{status}' but superseded_by is empty")
        if replaced_by and status not in RETIRED:
            errors.append(
                f"{row['id']}: superseded_by names {replaced_by}, but status is "
                f"'{status}'"
            )
        if replaced_by and replaced_by not in decision_ids:
            errors.append(
                f"{row['id']}: superseded_by names {replaced_by}, which does not exist"
            )

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

    # -- A function below product level names the function it decomposes ------
    for row in functions:
        parent = (row.get("parent_id") or "").strip()
        if parent and parent not in function_ids:
            errors.append(f"{row['id']}: parent_id '{parent}' does not exist")

    # -- A closed question says what closed it --------------------------------
    # A question marked closed with no pointer reads as answered, and the answer
    # cannot be found. Same failure as a superseded decision with no successor.
    QUESTION_STATUS = {"open", "closed"}
    for row in questions:
        status = (row.get("status") or "").strip()
        closed_by = (row.get("closed_by") or "").strip()
        if status not in QUESTION_STATUS:
            errors.append(
                f"{row['id']}: status '{status}' not allowed "
                f"(expected: {', '.join(sorted(QUESTION_STATUS))})"
            )
        if status == "closed" and not closed_by:
            errors.append(f"{row['id']}: closed, but closed_by is empty")
        if closed_by and status != "closed":
            errors.append(f"{row['id']}: closed_by is set, but status is '{status}'")
        if closed_by and closed_by not in decision_ids | requirement_ids:
            errors.append(
                f"{row['id']}: closed_by names {closed_by}, which is not a decision "
                f"or a requirement that exists"
            )

    # -- Requirements below product level must name a parent that exists ------
    # Product requirements have no parent within the model; their parent is the
    # function. Every level below traces upward, which is the other half of the V.
    for row in requirements:
        parent = (row.get("parent_id") or "").strip()
        if parent and parent not in requirement_ids:
            errors.append(f"{row['id']}: parent_id '{parent}' does not exist")

    # -- A safety requirement sits at the level of the risk it answers --------
    # A failure mode that is only visible inside one system is not answered by a
    # product "shall". If the mitigation has to be stated further up, the risk
    # was filed too low; if further down, too high. Level is the error made
    # repeatedly at product level, and this is the half of it that a machine
    # can see (MET-008).
    for row in requirements:
        source = row["generated_from"].strip()
        if source in risk_ids and compartment_of(source) != compartment_of(row["id"]):
            errors.append(
                f"{row['id']}: generated from {source}, a risk in compartment "
                f"{compartment_of(source)}, not {compartment_of(row['id'])}"
            )

    # -- The folder and the identifier must prove each other ------------------
    # A file dropped in the wrong directory is the mistake a nested layout makes
    # possible. Three things have to agree: one compartment per directory, one
    # directory per compartment, and a compartment as deep as the folder it is in.
    compartment_home = {}
    for directory, found in sorted(by_directory.items()):
        here = os.path.relpath(directory, PRODUCT)
        depth = 0 if here == os.curdir else len(here.split(os.sep))

        # Which compartment a directory holds is declared, not guessed. Without
        # this, a code that is unique and wrong passes every other check.
        key = os.path.relpath(directory, MODEL).replace(os.sep, "/")
        if key not in declared:
            errors.append(f"{key}: holds model files but is not in compartments.csv")
        else:
            for compartment in found:
                if compartment != declared[key]:
                    errors.append(
                        f"{key}: declared as {declared[key]}, but holds "
                        f"identifiers in {compartment}"
                    )

        if len(found) > 1:
            errors.append(
                f"{os.path.relpath(directory, REPO)}: holds more than one "
                f"compartment ({', '.join(sorted(found))})"
            )
        for compartment in found:
            if compartment in compartment_home:
                errors.append(
                    f"compartment {compartment} is used in two directories: "
                    f"{compartment_home[compartment]} and "
                    f"{os.path.relpath(directory, REPO)}"
                )
            else:
                compartment_home[compartment] = os.path.relpath(directory, REPO)
            # Product sits at the root and uses one code. Every level below it
            # adds one, so the count of codes is the depth of the folder.
            expected = 1 if depth == 0 else depth
            if len(compartment.split("-")) != expected:
                errors.append(
                    f"{os.path.relpath(directory, REPO)}: compartment "
                    f"{compartment} has {len(compartment.split('-'))} codes, but "
                    f"the directory is at depth {depth}"
                )

    for path, compartment in sorted(declared.items()):
        if not os.path.isdir(os.path.join(MODEL, path)):
            errors.append(
                f"compartments.csv: {compartment} names {path}, which is not a "
                f"directory"
            )

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
    # RPN is what decides where attention goes, so a mistyped factor misranks a
    # risk silently. Cheap to check, and the check is the arithmetic itself.
    for row in risks:
        try:
            s, l, d, rpn = (int(row[k]) for k in ("S", "L", "D", "RPN"))
        except (KeyError, ValueError):
            errors.append(f"{row['id']}: S, L, D and RPN must all be whole numbers")
        else:
            if s * l * d != rpn:
                errors.append(f"{row['id']}: RPN is {rpn}, but S x L x D is {s * l * d}")

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
    targets += sorted(glob.glob(
        os.path.join(MODEL, "**", "*_risks.csv"), recursive=True))
    targets.append(os.path.join(MODEL, "model_conventions.md"))
    targets.append(os.path.join(REPO, "README.md"))
    targets.append(os.path.join(REPO, "CLAUDE.md"))
    targets += sorted(glob.glob(os.path.join(MODEL, "**", "README.md"), recursive=True))
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
