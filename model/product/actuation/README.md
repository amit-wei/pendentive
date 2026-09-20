# Actuation (`AC`)

Decides which operations change the outside world, asks `AU` whether an action is
in a declared class, and records each action that occurred.

From `FUN-PL-08`. `EX` carries the call. Every external change passes through here,
so that `REQ-PL-014` holds.

`DEC-051` makes the boundary that needs a decision raise the unit of work that asks
for it, and `DEC-057` makes the act exist before the request. `OPN-046` asks whether
the act that an answer names changes after the answer, and whether this system or
`WC` refuses that change. `REQ-PL-014` has no child.

The functions and requirements of this system are not yet written.
