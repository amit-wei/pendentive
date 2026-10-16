# Outside audit: brief

Temporary. Delete this file once the audit is done.

## What you are auditing

Pendentive is a personal-assistant platform for one user: agents that hold the user's
life state, coordinate work, act on the outside world with the user's authorization,
and run unattended on a small host. No code exists yet. What exists is a requirements
model, held as rows in CSV files (functions, requirements, risks, interfaces, decisions,
tests), and the method by which it is written. System level is now closed. The next
steps are the build setup, a v1 scope that is a thin vertical slice, acceptance tests,
and then the decomposition of the v1 systems into components.

Constraints that are design inputs: USD 50 a month for each running instance, apart
from the machine it runs on; a small VPS (2 vCPU, 3.7 GB); one builder working with
Claude Code; a first usable version in February 2027. The builder must be able to
understand and debug every part of what is built.

Start with `README.md` and `CLAUDE.md`, then `docs/method/`, `model/README.md`,
`model/model_conventions.md`, the product rows in `model/product/`, and the registers in
`model/registers/`. Read as much of the model as you need to judge it.

## How to approach it

From first principles. Ask what this platform must be, and whether the model describes
that thing, before you ask whether the model is well written. Everything is in scope:
the product, the scope, the architecture that the rows imply, the method, the
sequencing, and the decisions themselves. No decision is settled because it is recorded.

Take two perspectives, and keep them apart in your report:

1. **Programme.** Is this the right thing to build, for this user, at this size? Would
   the user use it every day, and for what? Does the plan reach something usable by
   February 2027 within the budget? Is the model paying for itself, or has the
   specification outgrown what it serves? What is overbuilt, what is missing, and what
   would you cut? Where is the programme's real risk?
2. **Lead engineer.** Can this be built as specified, on this host and budget, by this
   team? Which parts are hard, unknown or likely to fail at runtime? Is the security
   model sound, prompt injection included? Will it be debuggable? Which architecture do
   the rows imply, and is it the right one? What would you prototype first?

## What not to spend tokens on

Row-level mechanical checks: wording, identifiers, references between rows, validator
rules, style, and missing links. A separate audit agent does that. Cite a row only when
it shows a systemic point.

## Rules

- **Change nothing.** Do not edit, add, move or delete any file, apart from the one
  findings file below. Do not commit to `main`. If your environment needs a commit to
  return the file, commit only that file, on a new branch.
- Say how confident you are in each finding, and say where you are guessing.
- Put no personal information in the findings.

## Output

One file, `outside_audit_findings.md`, at the root of the repository:

1. **Verdict.** A few sentences: would you continue as planned, change course, or stop?
2. **Top findings.** At most ten, ranked by consequence. Each with the perspective, the
   finding, why it matters, what you would do, and your confidence.
3. **Programme.** Your findings from that perspective.
4. **Lead engineer.** Your findings from that perspective.
5. **Challenges to decisions.** Each with the decision, the challenge, and the cost to
   reverse it now and later.
6. **What to cut, and what is missing.**
7. **Questions for the builder.** What you could not judge without asking.
