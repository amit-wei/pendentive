# Self-Observation (`SO`)

Watches the platform from outside each system, holds the facts about the platform, and
turns a condition over those facts into work.

From `FUN-PL-11`. Its body of data is separate from life state (`DEC-006`) and is not in
the copy away from the host (`DEC-167`).

**Why it is a system.** A system that stops cannot report that it stopped, so something
outside each system must watch it. The cost of the month comes from many systems and must
be seen before the invoice. One record of each fact lets a fault that spans systems be
found.

**What it does.**

- **Observation.** It finds whether each system answers and how fast, the storage and
  memory of the host, and the outcomes of the calls to each service.
- **Record.** It holds:
  - the record of each act on the outside world (`DEC-169`), which Actuation reads back;
  - the record of each call;
  - each fact that a system reports;
  - data about the quality of agents that agents write (`DEC-164`).
- **Cost.** It reports the metered sum and the limit that External Access gives
  (`DEC-165`). Each record of a call states the agent, so an agent finds the cost of
  each agent when asked.
- **Outcomes.** For each agent, it gives the share of its units that closed with no result,
  and the share of its requests that the user did not affirm. It measures and does not
  judge. Evaluations are the work of an agent (`OPN-103`).
- **Escalation** (`DEC-163`).
  - It raises a unit for each condition that a system reports (`DEC-162`, `MET-027`), and
    when a measure passes its threshold (`DEC-166`). Each measure starts with a
    threshold of the design, and an agent changes it.
  - When Work and Coordination does not take the unit, it notifies the user through
    Interaction.

**Waiting on other systems.**

- `OPN-098`: how Interaction shows the state and the notice with no agent between. Until
  it closes, `RSK-SO-002` (Self-Observation stops and nobody sees it) is open.
- `OPN-101`: the rating of the user.
- `OPN-103`: evaluations.
