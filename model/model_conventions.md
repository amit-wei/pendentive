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

## Risks

A failure mode is a failure of a compartment, as seen from outside that
compartment. The functions of the compartment check that the FMEA covers it. They
do not generate it (`MET-017`).

`S`, `L` and `D` are scored from 1 to 5 against these anchors, at every level
(`MET-016`). `RPN` is their product.

| | `S` severity | `L` likelihood | `D` detection |
|---|---|---|---|
| 1 | Nobody sees it | Needs two independent faults | The platform reports it |
| 2 | An answer is less useful | One time each year | A person sees it in a report that the person already reads |
| 3 | An agent is wrong and the user can see that it is wrong | One time each quarter | A person finds it if the person looks |
| 4 | An agent is wrong and the answer looks correct | One time each month | A person finds it only when the person traces a wrong answer back |
| 5 | The user stops the use of the system, or nobody can reverse the effect | Continuous, or by design | Nobody finds it |

## Identifiers

| Prefix | Meaning | Shape |
|---|---|---|
| `FUN` | a capability. Never a "shall" | `FUN-<path>-nn` |
| `REQ` | a "shall" that constrains the design | `REQ-<path>-nnn` |
| `TST` | a case that verifies a requirement | `TST-<path>-nnn` |
| `RSK` | a failure mode, scored by FMEA | `RSK-<path>-nnn` |
| `INT` | one thing that crosses between two compartments | `INT-<owner>-nn` |
| `DEC` | a decision about what the system is | `DEC-nnn` |
| `MET` | a decision about how the model is written | `MET-nnn` |
| `OPN` | a question that is held, not guessed at | `OPN-nnn` |

## Functions

A function is a capability. It is never a "shall". Size is not a criterion. A
function can be small or large, and that is not a reason to merge it or to divide
it. The criterion is one capability in one row (`MET-012`).

## Interfaces

An interface is held by the compartment that holds both of its sides
(`MET-018`). The product level holds the interfaces between systems, in
`product_interfaces.csv`. A system holds the interfaces between its subsystems.

One row names **one thing that crosses**, not one interface. The row holds what
states the supply on one side and what states the acceptance on the other. Each
side holds one or more requirements, separated by spaces or by commas, and each
one must exist in the compartment that the row names for that side (`MET-021`).
It does not hold the content of the contract, which stays in the requirement text.

A requirement of type `interface` must appear in a row. A side that is not
decomposed yet is written as `TBD`.

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

**Interfaces:** `id`, `from`, `to`, `item`, `supplied_by`, `accepted_by`,
`status`. `supplied_by` and `accepted_by` each hold one or more requirements
(`MET-021`), read the same way as `closed_by` and as the `mitigation` of a risk.

**Tests:** `id`, `requirement_id`, `criterion`, `status`. One row verifies one
requirement, and it is held in the compartment of that requirement. A product
requirement carries no criterion (`MET-004`), so no row names one.

**Decisions:** `id`, `date`, `decision`, `reason`, `reverses_if`, `status`,
`superseded_by`.

**Questions:** `id`, `question`, `resolves_at`, `raised`, `status`, `closed_by`.
`closed_by` holds one or more identifiers, separated by spaces or by commas, and
each one must be a decision or a requirement that exists (`MET-019`). It reads the
same way as the `mitigation` column of a risk.

`verification` is `Inspection`, `Analysis`, `Demonstration` or `Test`. These are the
four methods that `GOALS.md` uses, so the method is the same at every level.

Every row carries a `status`. The vocabulary is per kind of row and the validator
checks each one (`MET-023`, which restates `MET-020`).

| Kind | `status` |
|---|---|
| requirement, function, interface, test | `draft`, `agreed`, `implemented`, `verified`, `dropped` |
| risk | `open`, `mitigated`, `accepted`, `dropped` |
| decision | `proposed`, `agreed`, `superseded`, `reversed` |

A risk is `mitigated` when its mitigation names a requirement that stands. The
verification of that requirement is the status of the requirement and is not
repeated on the risk.

A risk is `accepted` when its failure mode stands and the answer to it is not a
requirement (`MET-023`). Its mitigation then names the decision that states the
answer, and names no requirement. `open` means nobody has answered it.

Nothing leaves `draft` until the decomposition is finished and a v1 scope exists
(`BLD-OPN-009`). At that point every row that v1 touches becomes `agreed`, which is
what `agreed` means: in scope and red-lined, not merely written.

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
9. A row that is `draft` and that no commit has carried may be deleted
   (`MET-024`). Once a commit carries a row, nothing is deleted: a requirement
   becomes `dropped`, and a decision becomes `superseded` or `reversed` and names
   what replaced it. An identifier is never reused.
10. A question that you cannot answer becomes an `OPN-` row.
11. Vague is permitted. Unverifiable is not.
12. Text uses Simplified Technical English (`MET-013`).
13. A value that is not yet known is written as the word `TBD`, so that a search
    finds it. A requirement may carry a `TBD`. It may not carry a value that nobody
    can check.
