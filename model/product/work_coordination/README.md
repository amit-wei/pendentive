# Work and Coordination (`WC`)

Holds work and directs it to agents.

From `FUN-PL-03` and `FUN-PL-04`. Work is one model (`DEC-005`). It holds the
work that `FUN-PL-13` raises, because that work is work (`DEC-015`). It holds work
that an agent does, and not work for the user (`DEC-041`).

Seven functions, twenty-nine requirements and ten risks. Ten of the requirements
are safety requirements that answer those risks.

`DEC-059` removes contention by ownership, so this system no longer detects it.
`FUN-WC-07`, `RSK-WC-002` and the five children of `REQ-PL-006` are redrafted or
dropped, and `OPN-054` carries that work. Until it is done the model holds both
`REQ-PL-006` and `DEC-059`.

`OPN-036`: `REQ-WC-036` refuses to give a unit of work by position, and nothing
refuses the raise of one, which `DEC-042` makes a write to the same body.
`OPN-048`: no requirement here gives Authorization the answer of the user that
`REQ-AU-003` and `REQ-AU-014` wait for. `OPN-049`: `FUN-WC-03` lets the agent
responsible state the result of a unit, which `REQ-PL-030` refuses for the answer
of the user.
