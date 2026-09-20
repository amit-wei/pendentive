# Authorization (`AU`)

Holds the declared classes of action that need the authorization of the user, and
states whether an action is in a class.

From `FUN-PL-07` and `FUN-PL-03`.

`DEC-052` keeps this system separate and small on purpose. A holder must not hold
acts that the classes gate, and each other candidate does: `AD` holds the act of
making an agent, `AC` the acts that leave the platform, `WC` the units of work that
carry the requests, and `IN` the widening of a source. `DEC-054` states this
system's own gate as a requirement and not as an entry in the register, so the
register does not classify the acts of the system that holds it. `DEC-058` states
that the declared classes are a declaration and not a fifth body under `DEC-024`.

`DEC-048` makes an answer of the user permit the action that the request states and
no other action. A permission that holds for later actions is a change to what a
position admits, which Agent Definition holds. `DEC-049` leaves this system holding
no record of a decision, and `DEC-051` gives the request to the boundary that needs
it. `DEC-057` makes the act exist before the request that asks about it.

Three functions, thirteen requirements and eight risks. Two of the requirements are
safety requirements that answer those risks, and one is a performance requirement
that carries a `TBD`.

Three risks carry a `TBD` mitigation and each names the question that holds it:
`RSK-AU-002` and `OPN-053`, `RSK-AU-003` and `OPN-052`, `RSK-AU-007` and `OPN-047`.
`INT-PL-19` has no supplying side, which `OPN-048` holds: the gate that protects the
class register has no path that carries the answer of the user to it.
