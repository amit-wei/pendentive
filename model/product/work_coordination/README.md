# Work and Coordination (`WC`)

Holds work and directs it to agents.

From `FUN-PL-03` and `FUN-PL-04`. Work is one model (`DEC-005`). It holds the
work that `FUN-PL-13` raises, because that work is work (`DEC-100`). It holds work
that an agent does, and not work for the user (`DEC-041`).

`DEC-059` removes contention by ownership, and `OPN-054` worked that through.
`FUN-WC-07` is dropped and so are `REQ-WC-019`, `REQ-WC-020` and `REQ-WC-024`.
`FUN-WC-08` holds the owner of each declared resource as well as the resource, and
`REQ-WC-039` gives both to Agent Definition over `INT-PL-21`, where `REQ-AD-040`
refuses a second position. `DEC-070` supersedes `DEC-060`, which superseded
`DEC-033` and `DEC-036`.

The severity did not vanish with the contention; it moved. `RSK-WC-002` is now the
double use of a resource that nobody declared, which is reversible by construction
and scores 36. `RSK-WC-011` is the resource that should have been declared and was
not, which is not reversible and scores 60. `DEC-070` states its answer, and the
requirement waits for `ACTUATION`. `RSK-WC-010` inverts: a class-level declaration now gives one position
every instance instead of matching units that do not collide.

`REQ-WC-036` refuses to give a unit of work by position, and `REQ-WC-040` refuses
the raise of one, which `DEC-042` makes a write to the same body (`OPN-036`).

Session 10 wrote the path of the answer of the user through this system.
`DEC-092` holds the answer with the unit that asked, supplied only by Interaction,
and used as a gate (`REQ-WC-055`) or read by the raiser (`REQ-WC-021`). `DEC-093`
makes one waiting state: a unit states the kind of event it waits on, and the design
fixes one reporter for each kind (`FUN-WC-09`, `REQ-WC-051`). `DEC-095` makes a
question and a message one shape. `DEC-096` sends a question to the flagged position,
and `DEC-094` lets only the raiser withdraw: before the event, or for a gated
unit until it is sent. `DEC-101` lets only an agent raise a message; this system
raises work that names no agent when the user must be told. `DEC-099` sends a
gated unit only when its raiser releases it, at a time that the request may state,
and closes it when the approval lapses; the released unit goes to the system that
does the action (`REQ-WC-069`). `OPN-048`, `OPN-063`,
`OPN-064`, `OPN-065`, `OPN-072` and `OPN-073` are closed.

Still open here: `OPN-075`, the items of the contract for a unit, which
`REQ-WC-064` holds as `TBD`. `OPN-076`, the kinds of event that no interface row
carries yet. `INT-PL-34` waits on `OPN-071` in Agent Definition, and `INT-PL-35` on
`OPN-077` in Interaction. `INT-PL-36`, `INT-PL-37` and `INT-PL-38` wait on
`OPN-079` in Actuation and Authorization, and `OPN-078` asks how a step of a
sequence that an agent drives is gated.
