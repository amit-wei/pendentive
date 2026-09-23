# Interaction (`IA`)

Provides the surfaces between the user and the platform, by speech and by text.

From `FUN-PL-06`, `FUN-PL-05` and `FUN-PL-07`.

A client reaches the platform through this system, including a client that another
person wrote (`DEC-080`). The user chooses the agent of an exchange in text
(`DEC-088`). Every spoken exchange is with one declared agent (`DEC-089`), which
Agent Definition defines like any other (`DEC-083`). The agent that puts a
question may put it in its own words (`DEC-104`). An answer of the user reaches this system
from the user and not through an agent, which is what `REQ-PL-030` needs. Each
exchange is written to life state (`DEC-024`); what an agent draws from it afterwards
is the work of that agent.

The surface, the client and the architecture of speech are below this level.

`DEC-084` closes `OPN-049`: this system receives the answer of the user, and an
approval counts when the user confirms it in a separate step. `OPN-003` asks for the latency
budget of a spoken turn and waits for subsystem prototypes, and `REQ-IA-009` carries
it as `TBD`. `REQ-IA-005` is the part of `OPN-061` that this system holds.

`OPN-067` asks where the state of this system is held. `OPN-068` asks who raises
the work that draws from an exchange. `OPN-069` asks who declares the kind of an
exchange.

Work and Coordination accepts `INT-PL-29`, `INT-PL-30` and `INT-PL-33` and supplies
`INT-PL-10`. It gives this system the refusal of an answer to a unit that closed
(`INT-PL-35`), and what the user is then shown is `OPN-077`. A question for the user
is put by the agent whose position is flagged for it (`DEC-096`), and whether that is
the agent for speech is `OPN-071`. What a confirmation shows for a step that an
agent drives is `OPN-078`.
