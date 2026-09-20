# Agent Definition (`AD`)

Holds what states an agent, and changes it under control.

From `FUN-PL-10`, `FUN-PL-03`, `FUN-PL-06` and `FUN-PL-14`.

`DEC-037` divides what states an agent into three parts. The rules for work with
the platform are one statement for every agent. A position states what an agent
admits (`DEC-019`, `DEC-029`). An identity states what an agent is for, at two
levels (`DEC-038`). `MET-002` keeps the content of an identity outside this
repository; the system holds that each part exists and what each part must state.

Twelve functions, thirty-six requirements and ten risks. Three of the requirements
are safety requirements that answer those risks.

`OPN-054` reached this system. `FUN-AD-12` refuses a position that admits an act on
a declared resource which another position already admits, which is what makes
`DEC-059`'s ownership a property of the platform and not an arrangement of the
configuration. `REQ-AD-040` holds the refusal at declaration and `REQ-AD-041` at
conferral. `INT-PL-21` brings the declared resources and their owners from Work and
Coordination. Whether two agents may hold one owning position is `OPN-056`.

`agent_definition_tests.csv` holds the first `TST-` rows written anywhere in the
model. Every one of the thirty-four requirements now has a criterion, in
thirty-nine rows. `REQ-AD-015` and `REQ-AD-034` carry a `TBD` by design.
`REQ-AD-001` does not, and the criterion that it cannot produce is the defect.
`REQ-AD-039` has two acts and two outcomes, so it carries four rows.
