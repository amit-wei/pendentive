# Model conventions

The rules for the model. The reason for each rule is in
`model/registers/method_decisions.csv`.

## Layout

| Path | Holds |
|---|---|
| `model/product/` | the decomposition tree, one directory for each compartment |
| `model/registers/` | what spans every level |
| `model/validate_model.py` | the checks, run on every commit |
| `docs/` | prose and diagrams |

If `validate_model.py` reads it, it belongs in `model/` (`MET-007`). A filename
states what the file holds, in lower case with underscores (`MET-010`).

## Levels

The tree has four levels (`MET-009`). A system holds subsystems. A system does not
hold a system.

| Level | Codes | Identifier |
|---|---|---|
| Product | `PL` | `REQ-PL-nnn` |
| System | one | `REQ-<SYS>-nnn` |
| Subsystem | two | `REQ-<SYS>-<SUB>-nnn` |
| Component | three | `REQ-<SYS>-<SUB>-<CMP>-nnn` |

`registers/compartments.csv` declares the code that each directory holds
(`MET-015`).

A component is built and verified as one unit. A system is verified through its
children. If a component cannot be verified as one unit, the partition above it is
wrong.

## What anchors, and what spans

Functions, requirements and risks belong to one compartment. They are held with it
(`MET-008`). Decisions and open questions apply to more than one level. They are
held in `registers/`.

A risk has no parent (`MET-014`). RPN ranks risks inside one compartment only.

## Identifiers

| Prefix | Meaning | Shape |
|---|---|---|
| `FUN` | a capability. Never a "shall" | `FUN-<path>-nn` |
| `REQ` | a "shall" that constrains the design | `REQ-<path>-nnn` |
| `TST` | a case that verifies a requirement | `TST-<path>-nnn` |
| `RSK` | a failure mode, scored by FMEA | `RSK-<path>-nnn` |
| `DEC` | a decision about what the system is | `DEC-nnn` |
| `MET` | a decision about how the model is written | `MET-nnn` |
| `OPN` | a question that is held, not guessed at | `OPN-nnn` |

## Functions

A function is a capability. It is never a "shall". Size is not a criterion. A
function can be small or large, and that is not a reason to merge it or to divide
it. The criterion is one capability in one row (`MET-012`).

## Level

Two tests decide the level of a requirement:

1. Can you write it before you know how the system is built? If not, it is not a
   product requirement.
2. Can one system verify it? If yes, it belongs to that system.

A requirement that names a store, a register, a definition file or a latency budget
is at the wrong level. The rule recurses (`MET-005`). At product level, outside
means outside the platform. At system level, outside means outside that system, and
a requirement on a system does not name the parts inside it. Product requirements are few and broad (`MET-006`). They may
be vague. Their children carry the detail.

## Origin

`generated_from` holds one origin. The origin sets the type.

| `generated_from` | `type` |
|---|---|
| a `FUN-` identifier | `functional`, `performance` or `interface` |
| `Constraint: <name>` | `constraint` |
| an `RSK-` identifier | `safety`, in that risk's compartment |

A risk can also be mitigated by a requirement that exists for another reason. That
link is in the `mitigation` column of the risk, not in `generated_from`.

## Columns

**Requirements:** `id`, `parent_id`, `generated_from`, `type`, `text`, `rationale`,
`verification`, `status`.

**Functions:** `id`, `parent_id`, `name`, `definition`, `rationale`, `status`.

**Risks:** `id`, `failure_mode`, `cause`, `effect`, `detection`, `S`, `L`, `D`,
`RPN`, `mitigation`, `status`.

**Decisions:** `id`, `date`, `decision`, `reason`, `reverses_if`, `status`,
`superseded_by`.

`verification` is `Inspection`, `Analysis`, `Demonstration` or `Test`. These are the
four methods that `GOALS.md` uses, so the method is the same at every level.

`status` is `draft`, `agreed`, `implemented`, `verified` or `dropped` for a
requirement. For a decision it is `proposed`, `agreed`, `superseded` or `reversed`.

`RPN` is the product of `S`, `L` and `D`.

## Rules

1. One thing in a row. A row that states two things is two rows (`MET-012`).
2. One origin for a requirement. If it has two origins, it is two requirements.
3. A product requirement splits only if each half needs more than one system to
   verify it. A half that one system can verify is a child, not a sibling.
4. Every requirement names a verification method.
5. A product requirement carries no acceptance criterion (`MET-004`). Criteria are
   `TST-` entries at system level and below.
6. A requirement is verified only after all of its children are verified.
7. A safety requirement sits in the compartment of the risk that it answers.
8. A risk is mitigated by requirements in its compartment or below it, never above.
9. Nothing is deleted. A requirement becomes `dropped`. A decision becomes
   `superseded` or `reversed` and names what replaced it.
10. A question that you cannot answer becomes an `OPN-` row.
11. Vague is permitted. Unverifiable is not.
12. Text uses Simplified Technical English (`MET-013`).
13. A value that is not yet known is written as the word `TBD`, so that a search
    finds it. A requirement may carry a `TBD`. It may not carry a value that nobody
    can check.
