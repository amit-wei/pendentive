# Work and Coordination (`WC`)

Holds work and directs it to agents.

From `FUN-PL-03` and `FUN-PL-04`. Work is one model (`DEC-005`). It holds the
work that `FUN-PL-13` raises, because that work is work (`DEC-015`). It holds work
that an agent does, and not work for the user (`DEC-041`).

Seven functions, thirty requirements and eleven risks. Ten of the requirements are
safety requirements that answer those risks.

`DEC-059` removes contention by ownership, and `OPN-054` worked that through.
`FUN-WC-07` is dropped and so are `REQ-WC-019`, `REQ-WC-020` and `REQ-WC-024`.
`FUN-WC-08` holds the owner of each declared resource as well as the resource, and
`REQ-WC-039` gives both to Agent Definition over `INT-PL-21`, where `REQ-AD-040`
refuses a second position. `DEC-060` supersedes `DEC-033` and `DEC-036`.

The severity did not vanish with the contention; it moved. `RSK-WC-002` is now the
double use of a resource that nobody declared, which is reversible by construction
and scores 36. `RSK-WC-011` is the resource that should have been declared and was
not, which is not reversible, scores 60 and has a `TBD` mitigation against
`OPN-055`. `RSK-WC-010` inverts: a class-level declaration now gives one position
every instance instead of matching units that do not collide.

`OPN-036`: `REQ-WC-036` refuses to give a unit of work by position, and nothing
refuses the raise of one, which `DEC-042` makes a write to the same body.
`OPN-048`: no requirement here gives Authorization the answer of the user that
`REQ-AU-003` and `REQ-AU-014` wait for. `OPN-049`: `FUN-WC-03` lets the agent
responsible state the result of a unit, which `REQ-PL-030` refuses for the answer
of the user.
