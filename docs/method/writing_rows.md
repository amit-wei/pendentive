# Writing rows

How to write a row well. `model/model_conventions.md` holds the rules that make a row
valid, and this file does not repeat them. Read it first.

## Any row

- **No architecture in a row.** No product, protocol, tool or provider names. Write the
  property so that it holds whichever mechanism is chosen.
- **State a fact once.** A count written in words drifts from the rows it counts, and
  no check finds it. Cite the identifier instead.
- **Don't write "nothing else" into a list.** It locks the design. State what is in the
  list.
- **A reading rule over a word is applied to sentences nobody imagined.** Name the
  facts outright.

## Functions

- **Ask what the function is for** before naming capabilities.
- **No constraints in a definition.** "Loses none", "as the user gave it" and "no agent
  carries it" are requirements or risks, not capabilities.
- **"Give" and "receive" are interfaces, not functions.**
- **Each function describes the requirements generated from it.**
- **A hand-picked measure, breakdown or dashboard is usually overbuilding.** Ask whether
  the need is real, or whether an agent can answer it on request. A cost per agent was
  cut this way: an agent reads the records when asked.

## Requirements

- **Don't specify how an agent's message to the user looks.** State what crosses.
- **Don't watch for a fault that already fails visibly.** A fault that ends in a failure
  the platform already handles needs no detector of its own. A model that its provider
  retires fails each call, the run fails, and the stop of the work reaches an agent or
  the user (`DEC-191`). A row that watches for the notice of retirement is overbuilding.
  Detect early only what would otherwise pass unseen, such as a provider that runs
  another version than the call names.
- **Don't add a refusal that another bound already makes.** Ask which boundary already
  stops the threat, and whether the new refusal stops it at all. A refusal of each
  address that a connection does not state was cut (`DEC-199`): an agent that reaches the
  open web carries life state out there whatever another connection states, so the
  position of the agent is the bound.
- **A refusal holds only on what the boundary can see.** An HTTP method states only by
  convention whether a request changes state, and a service can break the convention.
- **Write the test before showing the row.** For each requirement, state the pass and
  the fail of a test that could run. A row with no such test is rewritten, not shown.
  Three causes recur:
  - **A bound with no condition of measurement.** Memory in use depends on the load, and
    storage depends on the data held. State the condition: "while it runs the most work
    that it runs at one time", "when it holds no data".
  - **A word of the model that the mechanism cannot see.** A fence sees a destination,
    not "an external service". Write the property in what the thing that verifies it
    can observe.
  - **A property outside the control of the system.** A system on a host that holds
    other work cannot keep the storage of the host free. Bound what the system holds.
- **State the behaviour, not the name of a mechanism, and leave its values to the level
  below.** "Has a back-off" passes any delay. "Waits longer before each start of a part
  that stopped soon after its last start, up to a wait of `TBD`" states what a test
  checks, and the level below sets the values.
- **A judgement is unverifiable.** "Refuse a request that commits funds" asks the
  system to judge. Refuse by a property that a declaration states, and gate the
  declaration where it weakens a gate.
- **"When the user asks" is not a testable gate.** Write "until the platform records an
  affirmative answer to a request that states …".
- **A child keeps every qualifier of its parent.** Dropping a word changes what the
  child refuses. A parent that refused "a call of a caller" became a child that refused
  "a call to an act", and the child then refused every write from Ingestion to State
  Custody.
- **A property that doing nothing satisfies is empty.** "The system lets the agent write
  a note" is met by a system that does nothing.
- **Check what a signal actually covers.** A rule that reads one outcome as covering
  more than it shows removes a judgement the agent needs. "Don't repeat a rejected
  contact" reads a rejection of the content or the timing as a rejection of the
  contact. Hold what happened, with enough of its context to tell what it covers.
- **A requirement with one `TBD` can still fix a policy.** "End the run at cost `TBD`"
  decides that the run ends. State where the value is held, not what is done with it.
- **Don't state the content of a payload.** State what each row gives.
- **A configuration statement is not a requirement.** The model states what the system
  does. Who holds an act is configuration.
- **Merge two acts into one row only where it is honest:** one act with two conditions,
  as in `REQ-IN-030`.
- **Two rows can contradict each other and pass the validator.** Read the compartment
  back after drafting.
- **Before proposing a new gate, check whether a decision already gates it.** A gate on
  bulk deletion would have loosened `DEC-021`, under which nothing is removed
  unless the user asks.
- **Check what a mechanism is for before generalising it.**
- **Size each row to its level and its job, in both directions.** Before showing a row,
  ask whether it is narrower than the job, and whether a test can still pass or fail it.
  A supply is general where the supplier does not care which instance crosses: State
  Custody gives a system a fact about the user, not the time zone alone. An acceptance
  is specific where a test must name what passes: Work and Coordination accepts the time
  zone. Each later reader adds its own acceptance to the same row.

## Risks

- **The failure mode is the failure, not the mechanism**: "double use", not "two agents
  act on one resource".
- **No configuration causes.** A declaration the user approved is not a failure of the
  system. What happens while the platform is off is not the platform's.
- **A mitigation states what it does**: prevents, detects or recovers. A mitigation that
  restates the function is not one.
- **An accepted risk that a safety row partly answers holds two failure modes.** Split
  it: `RSK-PL-010` (mitigated) and `RSK-PL-011` (accepted) were one risk.
- **Re-read the score anchors after a redraft.** A score carried across a change of
  scope is often wrong.
- **A mitigation in another compartment is not allowed.** Reword the risk to the
  compartment's own failure ("does not report").

## Decisions

- **A rationale claims only what its decision says.**
- **A decision is written only once the builder agrees.** Reasoning that ends in a
  register row sits for one exchange first.
- **A decision that restates another puts the change in its decision text**, not only in
  its reason. It copies no old reason: it says "The rest of the reason of `DEC-nnn`
  stands", after checking that the inherited reason is still true.
- **Scope a decision by what the rule is for.** A broad scope sentence can forbid what
  the model relies on.
- **A decision not yet carried by a commit may be edited in place.** After a commit,
  only supersession.

### A supersession

1. Write the new decision with the full decision text and the change in it.
2. Set the old one `superseded`, with `superseded_by`.
3. In each draft row that cites the old decision, change the identifier, then **read**
   each row where the substance changed.
4. In each agreed decision that cites it, add "(restated by `DEC-nnn`)" once. Never in
   `closed_by` or `superseded_by`.
5. Search for nested parentheses, `\(DEC-[0-9]+ \(restated`, and read those rows.
6. Search for the **concept**, not only the identifier. A row can reason from the same
   premise without citing it.
7. Stale wording in an agreed decision is fixed only by a later supersession, never in
   place.

## Interfaces

- **An interface records something that one side gives the other.** What every part
  reads from the host as it is, such as the instant, crosses no interface; it is a need
  of the host and stays in the register of parties outside (`MET-032`).
- **One row is one thing that crosses** (`MET-021`). A side may name several
  requirements.
- **An accepting side left `TBD` between two written systems is invisible to the
  validator.** The interface pass in `decomposition.md` finds it.

## The validator

- **A clean validator says nothing about meaning.** A clean report on the half that can
  be checked reads as clean on the whole. The audit covers the rest.
- **Prove each new check by breaking it** on a scratch copy.

## Scripting the CSVs

- Edit through a script, never by hand. The files use CRLF line endings.
- Take `fieldnames` from the `DictReader`, not from the first row: some files hold only
  a header.
- Open and close each file in a `with` block. An unclosed handle can truncate a file.
- Read the highest identifier; the next one is free (`MET-030`). Take it at the moment
  of writing.
