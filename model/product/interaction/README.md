# Interaction (`IA`)

Provides the surfaces between the user and the platform, by speech and by text.

From `FUN-PL-06`, `FUN-PL-05` and `FUN-PL-07`.

A client reaches the platform through this system, including a client that another
person wrote (`DEC-080`). The user chooses the agent of an exchange in text
(`DEC-088`). Every spoken exchange is with the agent that holds the position that speaks to the
user (`DEC-089`, `DEC-119`), which Agent Definition defines like any other (`DEC-083`). The agent that puts a
question may put it in its own words (`DEC-104`). An answer of the user reaches this system
from the user and not through an agent, which is what `REQ-PL-030` needs. Each
exchange is written to life state (`DEC-120`), in a kind that this system fixes by
design (`DEC-121`); what an agent draws from it afterwards
is the work of that agent.

The surface, the client and the architecture of speech are below this level.

`DEC-084` closes `OPN-049`: this system receives the answer of the user, and an
approval counts when the user confirms it in a separate step. `OPN-003` asks for the latency
budget of a spoken turn and waits for subsystem prototypes, and `REQ-IA-009` carries
it as `TBD`. `REQ-IA-005` is the part of `OPN-061` that this system holds.

This system holds the state that it needs for its own work and gives none of it to an
agent (`DEC-120`, `REQ-IA-031`). `OPN-068` asks who raises the work that draws from
an exchange.

Work and Coordination accepts `INT-PL-29`, `INT-PL-30` and `INT-PL-33` and supplies
`INT-PL-10`. It gives this system the refusal of an answer to a unit that closed
(`INT-PL-35`), which it shows in the exchange in which the user answered
(`REQ-IA-030`). A question for the user is put by the agent for speech (`DEC-119`). What a confirmation shows for a step that an
agent drives is `OPN-078`.
