# Actuation (`AC`)

The one interface through which a caller reaches every act that the platform can do.
It holds and does the acts on the outside world.

From `FUN-PL-08`, `FUN-PL-15`, `FUN-PL-14`, `FUN-PL-07` and `FUN-PL-03`.

`DEC-102` makes this system the interface for every act. It gives a caller the acts
that the position of the caller admits, takes each call, and gives each act on the outside
world with its arguments to Authorization. An act inside the platform is gated by the
system that holds it (`OPN-086`). An act that another system holds is carried to that
system, which refuses and does it. To show only the acts that a position admits is
not a refusal, so `REQ-AC-007` refuses separately. The acts of the other systems are
fixed by their design. The acts on the outside world are declared (`DEC-103`), and
the declaration states the external service and the form of the arguments, nothing
more. Authorization judges an act with its arguments, not the act alone.

`DEC-104` has this system refuse an act in a declared class and tell the caller, and
the caller raises the request and the gated unit. The act is done only when Work and
Coordination sends it released with its answer. `DEC-108` sends every released gated
unit here, so the answer is checked against the act at one point, and an act that
another system holds is carried to it from here. `DEC-105` gates only an act whose
arguments state its effect. A sequence that an agent drives, such as a page in a
browser, has no means to pay or to send in the name of the user, so it stops and
the agent reports it. `DEC-107` makes this system the only refuser, and External
Access checks no authority. `DEC-106` holds the record of each act in
Self-Observation, with the authority by reference.

Waiting on other systems: `OPN-080` and `OPN-081` in External Access, `OPN-082` in
Self-Observation, and `OPN-079` in Authorization. `OPN-066` asks whether `DEC-069` stands against the cost
of a cached prefix, and resolves at subsystem level. `DEC-110` sends an act on the outside world to the user when Authorization is silent.
`DEC-109` keeps Authorization as a system that this system asks at each call, and
gates a new act that no class names. A call that returns no result is not repeated (`REQ-AC-024`) and the caller is told
(`REQ-AC-031`). The record is given before the call (`REQ-AC-023`), Actuation reads it
back to avoid doing an act twice, and it fails closed when it cannot read it
(`REQ-AC-036`). An exemption names its acts, and a declared act that an exemption names
is not changed until the exemption is (`REQ-AC-035`). `OPN-085` asks whether each holder
accepts a call only from Actuation.
