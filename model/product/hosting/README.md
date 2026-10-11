# Hosting (`HO`)

Runs the parts of the platform on the host, starts them again when they stop, and holds
each part to its network, its storage and its memory.

From `FUN-PL-17`.

**Why it is a system** (`DEC-176`). A part cannot start itself again, and
Self-Observation stops with the parts that it watches. A fence that the fenced part
holds is a promise: a library inside a part can open a connection that the part does not
intend, so `REQ-PL-033` and `REQ-PL-024` hold only where something outside each part
refuses.

**A part** (`DEC-186`) is a unit that the host runs apart from the other parts. Each
part belongs to one system, a system can have more than one, and two systems share no
part and no store.

**What it does.**

- **Supervision.** It starts each part when the host starts, and starts again each part
  that stops. It reports each part that it starts again.
- **Isolation.** Only External Access reaches a destination outside the host. A
  connection from outside reaches only what the host routes to Interaction or External
  Access. No part reads the
  storage of another, and no part can change its own fence.
- **Resource bounds** (`DEC-179`). It holds each part within the memory and the storage
  allocated to it, and reserves storage so that the platform starts, makes its copy and
  starts on a new version when its data fills the rest. It gives Self-Observation the
  memory and the storage that each part uses.

**The host** (`DEC-177`). The platform states what it needs of a host and is verified on
one host. The host gives a runtime that runs the parts apart from each other, the routing
of encrypted traffic to the platform, the instant, and a share of memory and storage at
or above the budgets of `REQ-PL-039` and `REQ-PL-040`. The host can hold other work. Each
need except the instant is an interface from `HOST` (`MET-032`); each part reads the
instant from the host. A person who administers the host is outside the model
(`DEC-178`).

**Not here.** Installation, which does not run while the platform serves the user. The
time of the user, which Work and Coordination reads from life state (`DEC-181`). The
signal to a service away from the host, which Self-Observation gives (`DEC-182`).
