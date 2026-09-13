# Requirements dataset — conventions

Structured data under git, validated by `model/validate_model.py`, which runs on
every commit via `.githooks/pre-commit`.

## Layout

```
model/
├── model_schema.md          this file
├── validate_model.py        traceability enforcement
├── product/                 one directory per decomposition level
│   ├── product_functions.csv
│   └── product_requirements.csv
└── registers/               span every level, so they are single files
    ├── design_decisions.csv     what the system is
    ├── method_decisions.csv     how the model is written
    ├── risk_register.csv
    └── open_questions.csv
```

`model/` holds structured data that is validated. `docs/` holds prose and diagrams.
The rule is mechanical: if `validate_model.py` reads it, it belongs in `model/`
(`MET-007`). Levels are discovered, so adding `model/system/` requires no change to
the validator. Filenames state what the file holds, lower case with underscores.

## Decisions are of two kinds

`design_decisions.csv` records what the system is — architecture, scope, behaviour.
`method_decisions.csv` records how the model itself is written — identifiers,
levels, what belongs where. Both are published; they answer different questions.
Decisions about how the work is done are neither, and are held outside this
repository.

## What is in scope

These requirements constrain **the platform**, stated as properties observable from
outside it (`MET-005`). A requirement that names a store, a register, a definition
file or any other internal part has assumed an architecture that has not been
decided, and belongs to a level that does not yet exist.

Two tests:

1. *Could this be written before knowing how the system is built?* If not, it is not
   a product requirement.
2. *Could this be verified entirely within one system?* If so, it belongs to that
   system, not here.

Product requirements are therefore few and broad — one or two per function (`MET-006`).
It is acceptable that they are vague. Specificity arrives with their children.

They do not constrain:

- **what an agent decides.** That the platform distinguishes actions needing consent
  is design. Which actions a given agent proposes is agent policy.
- **the user.** Obligations on a person are not requirements on a system.
- **how the system is built.** Held outside this repository.

`MET-002` and `MET-005` record the boundary. A requirement that fails it is moved or
deleted, not reworded.

## Identifier scheme

| Prefix | Meaning | Shape | Example |
|---|---|---|---|
| `FUN` | Function — a capability the system has. Never a "shall" | `FUN-<LVL>-<nn>` | `FUN-PL-03` |
| `REQ` | Requirement — a "shall" constraining the design | `REQ-<LVL>-<nnn>` | `REQ-PL-012` |
| `TST` | Verification case proving a requirement | `TST-<LVL>-<nnn>` | `TST-PL-012` |
| `DEC` | Decision, with reason and reversal condition | `DEC-<nnn>` | `MET-001` |
| `RSK` | Failure mode, FMEA-scored | `RSK-<nnn>` | `RSK-002` |
| `OPN` | Open question, held rather than guessed at | `OPN-<nnn>` | `OPN-003` |

`<LVL>` is `PL` at product level. Each system gets a two-letter code at the next
decomposition, each component one below that. An item's level is readable from its
ID alone.

Functions are flat at product level (`MET-003`). Decomposition happens at system level.

## Function versus requirement

A **function** is a capability, named as one:

> `FUN-PL-07` Authorization — gating declared classes of action behind an explicit
> affirmative answer from the user.

A **requirement** is a "shall" constraining the design:

> `REQ-PL-012` The platform shall distinguish actions requiring the user's
> authorization from those that do not, and shall not perform such an action without
> a recorded affirmative answer to a request stating that action.

## Where a requirement comes from

`generated_from` holds **exactly one** origin, and the origin determines the type:

| `generated_from` | `type` | Meaning |
|---|---|---|
| A `FUN-` ID | `functional`, `performance`, `interface` | Derived from a function |
| `Constraint: <name>` | `constraint` | Imposed by a stakeholder |
| An `RSK-` ID | `safety` | Exists only because of a failure mode |

`validate.py` enforces the pairing, so a constraint cannot be filed as a derived
requirement or the reverse.

A risk may also be mitigated by a requirement that exists for functional reasons.
That link lives in the `mitigation` column of `risks.csv`, not in `generated_from` —
a requirement has one origin, but a risk may be covered from several places.

## Columns — requirements.csv

| Column | Meaning |
|---|---|
| `id` | Unique identifier |
| `generated_from` | The single origin. Function, stakeholder constraint, or risk |
| `type` | functional · performance · interface · constraint · safety |
| `text` | The "shall" statement |
| `rationale` | Why it exists, and where it came from. Not a restatement |
| `verification` | Inspection · Analysis · Demonstration · Test |
| `status` | draft · agreed · implemented · verified · dropped |

The four verification methods are the ones `GOALS.md` uses for goals, so the method
is identical at both levels.

A requirement carries a verification **method**. Product requirements carry no
acceptance criteria, because they are broad by nature and the specificity belongs to
their children (`MET-004`). Criteria live in `TST-` entries at system and component
level.

A requirement may be verified only once all of its children and grandchildren have
been verified.

## Rules

1. One origin per requirement. If it has two, it is two requirements.
2. Every requirement names a verification method.
3. No requirement is deleted. It becomes `dropped`, with a `DEC-` entry saying why.
4. A question that cannot yet be answered becomes an `OPN-` entry. A requirement
   referencing an `OPN-` that does not exist is an error.
5. Vague and TBD are acceptable at this stage. Unverifiable is not.
