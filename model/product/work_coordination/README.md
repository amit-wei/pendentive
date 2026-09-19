# Work and Coordination (`WC`)

Holds work, directs it to agents, and detects contention.

From `FUN-PL-03` and `FUN-PL-04`. Work is one model (`DEC-005`). It holds the
work that `FUN-PL-13` raises, because that work is work (`DEC-015`). It holds work
that an agent does, and not work for the user (`DEC-041`).

Seven functions, twenty-eight requirements and ten risks. Ten of the requirements
are safety requirements that answer those risks.

`RSK-WC-002` is `TBD` on purpose, behind `OPN-027`. `OPN-036` is a known gap:
`REQ-WC-036` refuses to give a unit of work by position, and nothing refuses the
raise of one, which `DEC-042` makes a write to the same body.
