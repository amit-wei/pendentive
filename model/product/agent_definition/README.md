# Agent Definition (`AD`)

Holds what states an agent, and changes it under control.

From `FUN-PL-10`, `FUN-PL-03`, `FUN-PL-06` and `FUN-PL-14`.

`DEC-037` divides what states an agent into three parts. The rules for work with
the platform are one statement for every agent. A position states what an agent
admits (`DEC-019`, `DEC-029`). An identity states what an agent is for, at two
levels (`DEC-038`). `MET-002` keeps the content of an identity outside this
repository; the system holds that each part exists and what each part must state.

Eleven functions, thirty-four requirements and ten risks. Three of the
requirements are safety requirements that answer those risks.

`OPN-054` reaches this system: `DEC-059` gives each declared resource one owner,
and the refusal of a second position that admits the acts on that resource is a
requirement here.

`agent_definition_tests.csv` holds the first `TST-` rows written anywhere in the
model. Thirty of the thirty-four requirements produced a criterion, and
`REQ-AD-039` has not been through the `TST-` pass. `REQ-AD-015` and `REQ-AD-034`
carry a `TBD` by design. `REQ-AD-001` does not, and the criterion
that it cannot produce is the defect.
