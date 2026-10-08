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
