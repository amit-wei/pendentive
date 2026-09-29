# Agent Runtime (`RN`)

Runs each agent.

For a turn of the user that Interaction gives and for a unit of work that Work and
Coordination sends, it starts the agent, gives its model what states that agent, makes
each call to the model through External Access, and carries each call to an act to
Actuation as that caller (`DEC-140`). Every call that generates from a model runs an
agent here (`DEC-141`). It runs both runtimes of `DEC-142`. The acts that it gives an
agent at the start of a run, and what it keeps fixed during a run, are in `DEC-144`.

A run is of one unit or one exchange, and a unit can have several runs one after
another (`DEC-151`). A run does not wait for another agent; a note on a running unit
reaches the agent at its next turn, and nothing ends a run from outside (`DEC-148`,
`DEC-150`). Each run is bounded (`DEC-145`), its context is discarded when it ends
(`DEC-146`), and its end is reported to Work and Coordination with the note that the
agent wrote (`DEC-147`).
