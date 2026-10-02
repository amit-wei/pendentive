# Agent Runtime (`RN`)

Runs each agent.

For a turn of the user that Interaction gives and for a unit of work that Work and
Coordination sends, it starts the agent, gives its model what states that agent, makes
each call to the model through External Access, and carries each call to an act to
Actuation as that caller (`DEC-140`). Every call that generates from a model runs an
agent here (`DEC-141`, `DEC-153`). A run reads nothing that an earlier run left at the
provider (`REQ-RN-037`). It runs both runtimes of `DEC-142`. The acts that it gives an
agent at the start of a run, and what it keeps fixed during a run, are in `DEC-144`.

A run is of one unit or one exchange, and either can have several runs one after
another (`DEC-156`). A run does not wait for another agent; a note on a running unit
reaches the agent at its next turn, and nothing ends a working run from outside (`DEC-148`,
`DEC-150`). The run of an exchange ends when the user is idle or the platform restarts,
and the next turn starts a new run from the exchange so far (`DEC-156`). Each run is bounded (`DEC-145`), its context is discarded when it ends
(`DEC-146`), and its end is reported to Work and Coordination with the note that the
agent wrote (`DEC-147`).
