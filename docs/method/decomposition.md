# Decomposing a system

The procedure for one system. It applies at every level: a product into systems, a
system into subsystems, a subsystem into components.

The builder decides. The drafting agent proposes, drafts and asks.

## Steps

1. **Crawl.** Before any drafting, search the whole model for the name of the system:
   the registers, every compartment, the interfaces, the docs. Rows written earlier
   state obligations against this system that nothing else will reach. Act on each one
   or raise an `OPN-` row.
2. **First principles.** Is the system needed at all, and what is it for? A system can
   be cut, or folded into another, at this step.
3. **Grill.** Questions to the builder in batches of about four. Each question
   states the issue, a recommendation and a confidence. A question that is skipped is
   asked again, briefly. Settle the questions before any row is written.
4. **Functions**, drafted and then red-lined by the builder.
5. **Requirements**, drafted and then red-lined. Each drafted row is classified:
   functional, safety (it goes to the FMEA), architecture (a decision only) or
   duplicate.
6. **Quality flow-down.** For each `quality` requirement of the parent, ask how the
   system's own work affects it. Each answer is an enabler: a requirement of the
   system whose parent is that quality row, with its criterion in its text, `TBD`
   where the value is not known. A system can have zero, one or several enablers for
   one quality row; there is no grid. An enabler states a property of the system,
   never the mechanism and never what an identity says. An existing row that already
   enables a quality keeps its parent and is named in the rationale of that quality
   row. An enabler that serves several quality rows takes one parent, chosen with all
   of them in view (`MET-035`).
7. **Close the open questions that the system answers.** Read
   `model/registers/open_questions.csv` end to end and close what this system settles.
   The session that decomposes a system is the one with the evidence to close them.
8. **Interface pass.** Read every interface row whose `from` or `to` names this
   system. For each one, name the requirement that accepts it or raise an `OPN-` row.
   The validator cannot see an accepting side left `TBD`, so this pass is manual.
9. **FMEA.** The risks are proposed in the session and go into the repository only
   after the builder has red-lined them (`MET-017`: from the failure of the
   compartment as seen from outside, not from the function list).
10. **Audit** with the `model-auditor` agent (`.claude/agents/`), also after every
   sweep. Brief it with what changed, the diff, the validator output and the builder's
   recent decisions. Never tell it not to re-litigate. Resume the same agent for each
   later pass. Passes continue until one finds only low, mechanical items, and every
   fix is audited before close. Check each claim against the registers, then apply
   each `MECHANICAL` finding, bring each `DECISION` finding and challenge to the
   builder, and reject a wrong finding with its reason. Bring the speculative items to
   the builder in one short list. The auditor ends each report with a change to its own
   brief; the builder decides, and an accepted change goes into the agent file.
11. **Close.** The validator is clean. Decisions taken along the way are `DEC-` or
    `MET-` rows; unanswered questions are `OPN-` rows. Commit when the builder says.

## How rows are drafted and changed

- **Draft through a script**, never by hand, so that every CSV stays well-formed.
- **Edit by identifier**, never by regenerating a shared file whole.
- **Validate** after every change. Fix the data.
- **Red-line**: the builder marks what is at the wrong level, bloated or missing.
  Level errors are the common failure.
- **Record**: what is decided becomes a `DEC-` or `MET-` row; what cannot be answered
  becomes an `OPN-` row.

## Naming a deferred system

A row that defers work to a system that is not yet written names that system in
words, in upper case, at the end of its text: `ACTUATION`, `INTERACTION`. A deferral
that says "the system that holds the acts" is invisible to the crawl.
