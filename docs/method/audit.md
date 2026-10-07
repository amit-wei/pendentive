# The audit

Every system and every sweep is audited with fresh context before it closes. The
validator checks structure, not meaning: contradictions between rows, gates with no
supply path, a decision whose scope forbids what the model relies on, and stale prose
after a cascade all pass it. The audit is what finds them.

## How it runs

- One auditing agent, on a smaller model than the drafting session, with read-only
  tools. Each later pass resumes the same agent, so that it keeps the model loaded.
- Passes continue until a pass finds only low, mechanical items.
- **Every fix is audited before close.** Fixes made after one pass make new findings in
  the next.

## The prompt holds

- What the session changed, and the files to read: the diff and the validator output.
- **The checks:** level; one thing per row; verifiability; origin and type; that each
  mitigated risk names a requirement that answers its failure mode (`MET-025`);
  interfaces on both sides; cascades and stale prose; gaps against other systems.
- **A separate section on overbuilding and overspecifying:** gold-plating, implausible
  risks, duplicates, mitigations dressed as functions, mechanisms in rows, the wording
  of an agent's message in a row.
- **A separate section of challenges to the builder's decisions**, each with the
  reason and the cost to reverse. The prompt lists the recent decisions as context. It
  never says "do not re-litigate".
- **The output:** numbered findings, each with a severity and a label, `MECHANICAL` or
  `DECISION`.

## Close-out

- Apply each `MECHANICAL` finding.
- Bring each `DECISION` finding and each challenge to the builder.
- Reject a wrong finding, with the reason. Check each claim of the auditor against the
  registers before applying it.
