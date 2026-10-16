# Outside audit: findings

Audit of the Pendentive requirements model as of commit `6d48d28` (2026-10-16). The
whole repository was read: the method, the conventions, the validator, every product
row, every system row, every register and every README. The validator was run and is
clean: 102 functions, 678 requirements, 156 risks, 181 interfaces, 44 tests, 235
decisions, 117 open questions.

Confidence is stated on each finding. "High" means the rows support it directly.
"Medium" means it rests on experience with systems of this kind and the rows are
consistent with it. "Low" means it is a guess that the builder can confirm or dismiss
in a sentence.

## 1. Verdict

Change course. Do not stop.

The thinking in this model is unusually careful. The decisions are reasoned, the
reversal conditions are stated, the security stance on prompt injection is the right
one, and the method caught real defects that a looser process would have shipped. The
product idea, a single body of life state that several bounded agents work from, is a
sound thing for this user to want.

But the specification has outgrown what it serves. Thirty-four days of work have
produced about 80,000 words of requirement and decision text, 662 live requirements
and eleven systems that the rows require to run as separately fenced parts with
separate stores, for one user on a 2 vCPU host, built by one person in the sixteen
weeks that remain before February 2027. The plan as sequenced, which is build setup,
then a v1 scope, then acceptance tests, then decomposition of the v1 systems into
components, cannot reach something usable by that date at the pace the history shows.
The architecture the rows imply does not admit a thin vertical slice: every act of
every agent crosses four systems, so the thinnest slice is still the full skeleton.

What I would do: freeze the model at system level and treat it as the design record it
already is. Pick a v1 that is four or five systems' worth of function running as one
process over one store, with two hard boundaries only, egress and the agent sandbox.
Build that skeleton in weeks. Let code answer the open questions. Write component rows
only where a verified property needs one. Fix two things before anything else: the
accepted exfiltration path through reads, and the personal information that is already
in the public repository.

## 2. Top findings

Ranked by consequence.

**1. The plan cannot reach February 2027.** Programme. The model took 34 days to reach
system level and is still entirely `draft`, with 68 live requirements that carry a
`TBD` value and 9 open questions that resolve at subsystem level. The method requires
decomposition to subsystem and component, acceptance criteria at every level, and
bottom-up verification before any requirement counts as verified. No code exists.
Sixteen weeks remain. Why it matters: a missed date on a personal project is not fatal,
but a project that spends its budget on specification and then rushes the build gets
the worst of both. What I would do: stop decomposing. Build v1 from the system rows.
Write rows below system level only for the parts whose verification demands it.
Confidence: high.

**2. The exfiltration path through reads is accepted at the highest score in the
model, and the user is not told what they accept.** Lead engineer. `RSK-PL-014`
(S5 L3 D5 = 75) and `DEC-199`: an agent that content steers can put life state into the
address of a request that only reads, on any connection that reaches the open web, and
the platform refuses nothing. The user "accepts that at the answer that lets an agent
reach it", but the request the user answers names an act and a connection, not the
consequence. Why it matters: this is the attack that is actually seen in deployed
agents today, it is silent (D5), and nobody can reverse it (S5). What I would do: the
model already has the mechanism to close most of it without a detector. Treat "reads
untrusted content broadly" and "reaches any address" as two capabilities that one
position may not hold together, refused at declaration and conferral in the shape of
`REQ-AD-040`. Keep search as an API act with a fixed destination and a bounded query.
Keep "fetch any address" and the browser session out of any position that also admits
a broad read of life state. Where a position must hold both, the request that widens it
states the consequence in words. Confidence: high on the gap, medium on the cost of the
fix.

**3. Personal information is in the public repository, by a convention the model
enforces.** Programme. The user's given name appears as the origin of every
`constraint` requirement in `product_requirements.csv`, in two open questions, and as a
label in the functional flow diagram. The diagram also names the user's institutional
data source and lists the agent population by life domain. `MET-029` and `CLAUDE.md`
call this a hard boundary and note that a published commit cannot be withdrawn. Why it
matters: the rule exists because the cost is irreversible, and the convention
`Constraint: <name>` makes the validator check a field that carries the name on every
commit. What I would do: change the origin to `Constraint: the user`, redraw the
diagram with generic labels, and add a validator check that refuses a known list of
strings. The history keeps the name; that is the cost of the convention and cannot be
undone, but it should not grow. Confidence: high.

**4. The architecture the rows imply is eleven isolated services on a two-core host,
and that is the wrong shape for one user and one builder.** Lead engineer. `DEC-186`:
two systems share no part and no store. `DEC-111` and `REQ-PL-032`: every call of an
agent to anything, a read of life state included, passes Agent Runtime, then Actuation,
then the holder, with a position confirmed from Agent Definition at each refusing
boundary. `REQ-HO-004` to `REQ-HO-007`: each part is fenced by the host for network and
storage. The result is a microservice mesh with eleven stores, four hops per tool call,
and distributed state machines for work, gates, releases, lapses, conditions and runs.
Why it matters: the builder must understand and debug every part. Eleven stores mean no
single query answers "what happened last night". `RSK-AC-006` and `RSK-AD-005` already
admit the latency tax. What I would do: keep two process boundaries, because they are
the ones that security needs and that the host must enforce anyway: External Access as
the only part with a route out and the only holder of credentials, and the agent's
model call and sandbox. Run everything else as one process over one database, with the
eleven systems as modules whose interfaces are the rows. The rows stay true; only
`DEC-186` and the "parts" language of Hosting change. Confidence: high on the diagnosis,
medium on the exact cut.

**5. Nothing in the model says what the user does with it on a Tuesday.** Programme.
The product functions are infrastructure capabilities. The quality rows
(`REQ-PL-042` to `REQ-PL-053`) measure correctness, usefulness and proportion at a
`TBD` rate against reference sets that do not exist. The platform ships with no agent
of the user (`DEC-175`), and its one agent starts with a position that admits nothing
(`DEC-198`), so the first hours of use are a sequence of approvals to widen a position
before any work is possible. Why it matters: "would the user use it every day, and for
what" cannot be answered from the model, and a platform whose value is entirely in
tenants that do not yet exist can be finished and still be unused. What I would do:
write three scenarios, one page each, before the v1 scope: a morning, a deadline, a
bill. Derive v1 from the sources, acts and agents those three need. Ship a starter set
of positions and agent identities as design content; `MET-029` permits content that
holds no personal information. Confidence: high that the gap exists, medium on its
consequence.

**6. The budget of USD 50 has no analysis behind it, and the design spends tokens
freely.** Programme and lead engineer. `REQ-PL-020` is verified by Analysis and no
analysis exists. The design sends every agent, on every call, three levels of identity,
the rules for every caller, the acts its identity names, the unit of work whole
(`REQ-RN-041`) and the exchange so far. Conditions start agents unattended. Derivations,
evaluations against reference cases, and the judgement of quality by a panel of models
are all agent runs. Speech, transcription and embeddings are metered calls. At current
frontier prices USD 50 buys in the order of five to fifteen million input tokens a
month, which is a few hundred agent turns of 50,000 tokens, which is a handful of turns
a day. The fallback (`DEC-165`) is that the platform refuses every metered call for the
rest of the month except the speaker agent, which means the unattended work that is the
point of the platform stops first. Why it matters: the budget is a design input and it
decides the model class, the context discipline and how many agents can run. What I
would do: measure one real agent turn in a prototype on the cheapest model that works,
multiply by the scenarios of finding 5, and let that number set `REQ-WC-034`, the
bounds of `DEC-145` and the metered limit. Confidence: medium; the arithmetic is
indicative and the builder may already have numbers outside the repository.

**7. The position predicate is a bespoke policy language that eight systems must
evaluate, and it is the most likely tarpit.** Lead engineer. `DEC-074`: a predicate
over kind, subject, writer, source, times and observed-or-inferred, with parameters
bound at conferral, plus acts, plus positions to confer and to retire, plus ownership
of declared resources, plus flags, plus the widening gate of `REQ-AD-059`. Subjects
form a declared hierarchy (`DEC-044`, `DEC-063`). Agents author these declarations and
the user approves widenings written by agents. Why it matters: every refusal in the
platform rests on it; agents must be able to write it; the user must be able to read a
widening and know what it grants; the builder must be able to debug a refusal at 2am.
No prototype exists. What I would do: prototype this first, on paper and then in code,
by writing the positions for the three agents of finding 5 by hand and checking that a
model can author one from a user's sentence. Cut subjects, parameters and resource
ownership from v1 if they do not earn their place in that exercise. Confidence: high
that it is the hardest unknown, medium that it fails.

**8. Browser-driven sessions, semantic query and speech are each a project of their
own and are not needed for v1.** Lead engineer. The browser session that "only reads"
(`REQ-EX-026`, `OPN-093` open, `RSK-EX-001` at 75, `RSK-EX-017` open) refuses by HTTP
method, which the rows themselves say a service can break, and it puts a rendering
engine inside the one part that holds every credential. The query by meaning is the
highest open risk in the model (`RSK-ST-001` at 80) with no mitigation and no
criterion, and it needs an embedding index that grows without bound on a 3.7 GB host.
Speech needs a client on a phone, streaming through the egress proxy, with a latency
budget that is `TBD`. Why it matters: each one is plausible in isolation and together
they are most of the engineering risk. What I would do: v1 is text through an existing
messaging client, exact queries, API connections only. Confidence: high.

**9. The exactly-once rules make the platform unable to retry, and a network blip
leaves an act in limbo for good.** Lead engineer. `REQ-EX-022` never repeats a call,
`REQ-RN-023` never sends a call to an act again, `REQ-AC-024` does not repeat an act
whose call returned no result while its record exists, and the record is removed only
by the user (`DEC-169`). A timeout on "create this calendar event" means the platform
can never create that event again by the same call. The caller "decides", but every
path it has is refused. Why it matters: on a home-grade network this is a weekly event,
and the failure is a confused user and an agent that rewords an act to get around a
safety rule. What I would do: give an act an idempotency key where the service offers
one, and a "read back and confirm" step where it does not, as the mechanism by which
`DEC-129`'s "a service that offers its own safe repeat does it itself" is met. State in
the rows that a call that returned no result may be confirmed, not only abandoned.
Confidence: medium-high.

**10. The verification programme is larger than the build.** Programme. Twelve quality
rows at product level, each verified once per release on a synthetic instance with
held-out sets, panels of model judges and human rubric review (`MET-034`, `DEC-187`);
two adversarial injection suites with adaptive attempts (`TST-PL-001`, `TST-PL-002`);
614 requirements verified by Test; a bottom-up rule under which a product requirement
is verified only after its whole tree is. For one builder this is a research programme
beside the product. Why it matters: a gate that cannot be run is a gate that is skipped
under pressure, and then the method's promise, nothing claimed verified that was not
run, is broken silently. What I would do: for v1, five end-to-end scenario tests, one
small injection suite of twenty cases run on each model change, and an evaluation set
whose trend is reported and is not a release gate. Confidence: high.

## 3. Programme

**Is this the right thing to build, for this user, at this size?** The need is real: a
person with several life domains, several data sources and a wish for agents that act,
not only advise, with one source of truth and a hard boundary on money, third parties
and access. The failure the user names, being reminded of something already overridden,
is a real failure of every assistant on the market. A platform that holds state with
provenance and supersession and bounds agents by position is a defensible answer. It
is, however, an answer to a platform problem, and the user's problem is a life problem.
The model never bridges the two. Its one concrete example of use, a single sentence in the
reason of `DEC-152`, does more to tell a reader what the platform is for than the 662
requirements around it.

**Would the user use it every day?** The honest answer from the model is: not at
first. Day one is a platform agent with an empty position, and every capability is
withheld until an agent exists to serve it (`DEC-175`). The user builds their agents by
conversation and approves each widening. That is a cold start that the user, who is
also the builder, will tolerate, and no other person would. Since the repository is
public and the method is "central", it is worth asking whether a second user is a goal.
If not, several decisions that protect generality (`DEC-177` on hosts, `MET-029` on
shipping no agent of the user, the portable definition of `REQ-PL-021`) cost more than
they return.

**Does the plan reach something usable by February 2027 within the budget?** No, as
sequenced. The evidence is the history: 34 days to write eleven systems at one level,
with each later system reaching back into the earlier ones. The remaining steps are a
v1 scope, acceptance tests at every level the v1 touches, and decomposition of the v1
systems to component level. If v1 touches the systems that the architecture forces it
to touch, which is at least Agent Runtime, External Access, Actuation, State Custody,
Work and Coordination, Agent Definition, Interaction and Hosting, then two more levels
for eight systems at the demonstrated pace is the rest of the year, before code. The
budget of money is less at risk than the budget of time, but see finding 6.

**Is the model paying for itself?** In parts, clearly. It found that the user's hard
boundary had almost no flowdown (`OPN-041`), that MCP servers attached to the model
bypass every gate (`RSK-PL-008`), that the writer of a record and the source of its
content are two facts (`DEC-061`), that a definition set existed in which five of six
declarations could not be removed (`FUN-PL-15`), and that ownership removes contention
where detection cannot (`DEC-059`). Each of those would have cost days in code. But the
ratio has turned. Forty-two of the 200 design decisions are restatements of an earlier
decision, each with a seven-step supersession procedure. About two dozen requirements
exist to give, carry and restore a copy of a body or a declaration. Eight rows say "only from
Actuation". A hundred rows are safety requirements answering risks scored by likelihood
and detection anchors that, with no code and no operation, are guesses. The validator
is 672 lines and the auditor agent brief is 136; both are maintained by the one person
who should be building. The rule "no system is complete" is honest and also means the
model has no natural stopping point.

**What is overbuilt?** The copy-and-restore machinery written separately for six
holders (`FUN-ST-08`, `FUN-AD-11`, `FUN-AU-04`, `FUN-AC-07`, `FUN-IN-07`, plus
External Access carriage), where one database backup would do once `DEC-186` falls.
Authorization as a system of 31 requirements whose job is one lookup; `DEC-109` kept it
separate partly because folding it in "supersedes about nine decisions", which is a
cost of the method, not of the design. Self-Observation as a system with its own body,
positions over its records, thresholds as declarations and a dead-man signal, where for
v1 a log table, a health endpoint and a free external ping service suffice. The
conditions over life state as stored structured queries run by State Custody under the
declarer's position at the time of the run (`DEC-171`), which implies a query language
over declared kinds; an agent on a time condition that runs the query itself gives the
same result with no new language. Resource ownership and the refusal of a second owning
position (`DEC-059`, `DEC-068`, `FUN-AD-12`, `FUN-WC-08`) for a population of agents
that does not yet exist. The portable definition and the one-form copy an agent can
read with no platform (`REQ-PL-021`, `DEC-043`, `DEC-159`, `REQ-ST-068`,
`REQ-AD-034`), which constrains the store format from day one for a degraded mode
nobody has needed yet.

**What is missing?** See section 6. The largest is a user scenario; the second is a
cost model; the third is the inbound edge, authentication, TLS and webhook
verification, which the model places with the host and which is the first thing an
attacker meets.

**Where is the programme's real risk?** Not in any one decision. It is that the
builder's attention is the only scarce resource, and the method consumes it at a rate
the history shows. The second risk is that the field moves under the model: prefix
caching (`DEC-144`), provider-side code execution (`DEC-152`), provider tools
(`DEC-160`), MCP (`DEC-161`), the instruction hierarchy (`OPN-106`) are all decisions
about the provider landscape of autumn 2026, and each one will be revisited by
February. A model that costs a supersession cascade per change will lag the ground.

## 4. Lead engineer

**Can this be built as specified, on this host and budget, by this team?** As
specified, no, within the time. As a design, most of it is buildable, and some of it is
good engineering that I would keep in any version. The parts I would keep without
change: one egress route that holds every credential and records every call
(`DEC-032`, `DEC-183`); credentials never pass through an agent (`DEC-125`,
`REQ-EX-016`); the platform states the writer and the time and takes neither from the
caller (`DEC-056`, `REQ-PL-029`); an act exists before the request that asks about it
and cannot change after the answer (`DEC-057`, `DEC-066`); the user's answer reaches
the platform from the user and is confirmed in a separate step that shows the act as
the platform holds it (`DEC-084`, `REQ-IA-017`, `REQ-IA-018`); the model is given no
tool on the host but the acts (`REQ-RN-022`); a run's context is discarded and reads
nothing an earlier run left at the provider (`REQ-RN-024`, `REQ-RN-037`); the client
does not prefetch an address an agent wrote (`REQ-IA-061`); no run waits on another
run (`DEC-148`); and supersession by observation time, not receipt time, with no
default for a missing observation time (`DEC-062`, `REQ-ST-007`).

**Which architecture do the rows imply?** A message-mediated service mesh. Agent
Runtime is the agent loop. Actuation is a single tool gateway through which every tool
call passes, including reads of state. Authorization is a classifier called per
outbound act. External Access is an egress proxy, a credential vault, a webhook
receiver, a backup carrier, an MCP host and a browser. Agent Definition is a policy
decision point that every other system calls to fetch a position. State Custody is an
append-only item store with kinds, subjects, provenance, supersession, exact and
semantic query, and a scheduler. Work and Coordination is a durable task state machine
with typed waits, gated units, releases, lapses, notes and a scheduler. Interaction is
the web and speech front end, the notification channel and two views. Self-Observation
is an audit log, a metrics store with thresholds, an escalator and a heartbeat. Hosting
is a container supervisor with per-part network and storage policy.

**Is it the right one?** The trust boundaries are right. The process boundaries are
not. The properties that must hold against a steered or careless agent are: it cannot
reach outside except through the proxy; it cannot read a credential; it cannot call a
tool the position does not admit; it cannot write a record's writer or time. The first
two need an OS or container boundary around the proxy and around the model call. The
last two are enforced in code wherever the code runs. Nothing else in the rows needs a
process boundary, and `DEC-186`'s reason, that a shared store is reached past the
boundary of the other, is true of a store two processes share and not of a store one
process owns with eleven modules in it. One process, one SQLite file in WAL mode, one
scheduler, one trace id: that is the shape that one person can hold in their head and
debug, and it meets every row except the ones that say "part".

**Which parts are hard, unknown or likely to fail at runtime?**

- The position predicate and its authoring by agents (finding 7).
- The form of a kind. Every writer, every refusal of `REQ-ST-060`, the copy, the
  restoration and the condition queries depend on a schema language for declared kinds
  that the model does not choose. It is below system level by the rules and it is the
  first thing the code must choose.
- The query by meaning (`RSK-ST-001`). Drop it from v1. An agent with exact queries over
  declared kinds and a good summary is most of its value.
- The browser session (`OPN-093`). Drop it from v1. When it returns, run it in its own
  part with a per-session credential injected by External Access, not inside the vault.
- Exactly-once without retry (finding 9).
- Catch-up semantics for conditions after a restart or a clock jump (`REQ-WC-108`,
  `REQ-WC-126`, `REQ-WC-127`, `REQ-ST-099`). Correct in the rows, fiddly in code, and
  the kind of thing that fires twenty units at 03:00 after a reboot. The "one open unit
  per condition" bound (`REQ-WC-109`) is the right safety net; keep it.
- The limit of the month (`DEC-165`): the exemptions for the speaker agent and the
  receiver of unnamed units are unbounded by design, and those two are the agents most
  exposed to steered content. A steered speaker agent in a loop after the limit is the
  cheapest way to spend the next month's budget. Give the exempt agents a daily bound.
- Memory on 3.7 GB with eleven processes, an embedding index, a browser and the
  per-part reserves of `REQ-HO-009`. Feasible without the browser and the index;
  marginal with them. A model on the host (`DEC-161`) is not feasible on this host for
  anything an agent would use.
- Agent-authored declarations in general. Kinds, subjects, positions, acts,
  connections, conditions, thresholds and resources are all written by agents from a
  user's sentence. The rows keep the content out of the model, which is right, and
  that content is where v1 succeeds or fails. The guidance for an act (`DEC-118`) is
  the only place it can live, and it is size-bounded by `REQ-AC-046`.

**Is the security model sound, prompt injection included?** The stance is sound and
better argued than most: bound what a steered agent can do, verify the bounds with
steered agents, count on no detector (`DEC-199`). The gaps, in order:

1. Exfiltration through reads (finding 2). The one place where the model knowingly
   leaves a S5 D5 path open, and a construction-level fix exists in its own vocabulary.
2. The inbound edge. `FUN-IA-01` "identifies the user" has no mechanism and no risk
   row beyond `RSK-IA-004`. Webhook authenticity (`REQ-EX-029`) depends on services
   that sign, and many do not. TLS, routing and rate limiting are needs of the host.
   This is correct placement by the rules and it is still the first attack surface. It
   belongs on the prototype list and in the acceptance tests.
3. The most privileged agent is the most exposed one. The platform agent speaks to the
   user, receives every unnamed unit, takes agent definitions from outside systems, and
   is exempt from the monthly limit. `DEC-198` starts it empty, which is right. Keep it
   empty of open-web acts for good, and let it delegate reading to agents that cannot
   reach outside.
4. The browser inside the credential vault (above).
5. The order of identity levels is not something a model honours (`OPN-106`, correctly
   researched), and the rows do not count on it. Good. But the rules for every caller
   and the identity of the platform are then advisory, and the confirmation step and
   the position are the whole defence. Make the confirmation step show the raw
   arguments, not a rendering an agent influences.
6. `DEC-178`, the administrator is unbounded, is right for one user and should be
   restated the day a second person touches the host.

**Will it be debuggable?** With eleven stores and typed waits across them, not by one
person at 2am, whatever the records say. With one store and one trace id per unit of
work carried on every hop, yes, and the work view of `DEC-200` becomes a query. The
rows already carry the unit of work of the run on each call (`REQ-AC-027`,
`REQ-RN-015`); make that the trace id and require it in every record that
Self-Observation holds. That is a property, not a mechanism, and it is missing.

**What would I prototype first?** In this order, each one a week or less:

1. The position predicate, on paper, for three agents, then in code as a function that
   refuses, with a model asked to author one from a sentence.
2. One agent turn end to end: Interaction receives a text turn, Agent Runtime
   assembles context from a definition, calls a model through an egress proxy that
   holds the key, the agent calls one read act and one gated write act, Actuation
   refuses the write, the agent raises a request, the user confirms, the act runs,
   every hop carries one trace id, and the whole thing is one process and one SQLite
   file. Measure tokens and latency. That number is the budget.
3. Ingestion of one real source into declared kinds with supersession by observation
   time, and a backup of the one file to the chosen location.
4. The injection suite, twenty cases, against the skeleton.

## 5. Challenges to decisions

Each with the decision, the challenge, and the cost to reverse now and later. "Now"
means before code; "later" means after a v1 is built on it.

- **`DEC-186` (two systems share no part and no store).** Challenge: the reason holds
  for two processes and a shared store, not for one process with module boundaries.
  One store is the single largest gain in debuggability and build time available.
  Keep the boundary around External Access and the model call. Cost now: a handful of
  rows in Hosting and a restatement. Later: very high; the store split is the
  architecture.

- **`DEC-111` (Actuation is the one interface for every act, reads of state
  included).** Challenge: the value of one interface is the classification and the
  record of acts on the outside world and the gate on declarations. A read of State
  Custody by an agent gains nothing from the hop and pays latency on every tool call.
  Let Agent Runtime call a holder directly with the caller it states, and let
  Actuation mediate acts on the outside world and declarations only. Cost now:
  moderate; eight "only from Actuation" rows and the `INT-PL-44` to `INT-PL-55`
  family. Later: high.

- **`DEC-199` (no address bound; the user accepts exfiltration at the widening).**
  Challenge: a position bounds which act, an address bound bounds where bytes go, and
  they are different bounds. The user's acceptance is not informed by the request as
  the rows state it. Refuse at declaration a position that admits both a broad read
  and an act that reaches any address, and name the consequence in the request where
  both are admitted. Cost now: low. Later: medium; it changes which agents can exist.

- **`DEC-143` (no client another person wrote; surfaces for text and speech built in
  Interaction).** Challenge: a messaging app the user already has, reached through its
  bot interface, is a surface of Interaction under `DEC-188`'s own definition, costs
  nothing to build, and is on the phone already. Speech can wait. Cost now: none; the
  rows admit it. Later: none.

- **`DEC-175` and `DEC-198` (ships with no agent of the user; the platform agent starts
  empty).** Challenge: the cold start is a wall of approvals. Ship a starter set of
  positions and identities as design content, written with no personal information,
  and let the user's first conversation be about their day and not about positions.
  Cost now: low. Later: low.

- **`DEC-171` (a condition over life state is a stored structured query that State
  Custody runs under the declarer's position at run time).** Challenge: it implies a
  query language over kinds and a scheduler in State Custody. A time condition that
  starts an agent which runs the query itself gives the same behaviour with no new
  language, at the cost of a model call per evaluation. For v1 that cost is right.
  Cost now: low; the rows stay and are not built. Later: medium.

- **`DEC-109` and `DEC-116` (Authorization stays a system, asked at each call).**
  Challenge: the reason for keeping it separate includes the cost of superseding nine
  decisions, which is a cost of the register and not of the design. The classification
  is one function. Cost now: low in design, moderate in rows. Later: low; a module is
  easy to move.

- **`DEC-159` and `REQ-ST-068` (the copy is one form an agent can read, and life state
  restores only from it).** Challenge: it fixes an export format before a store exists
  and forbids the fastest restoration. Keep the agent-readable export as a product of
  the store; let the restoration use whichever form is complete. Cost now: low. Later:
  medium.

- **`DEC-165` (the limit of the month exempts the speaker and the receiver of unnamed
  units without bound).** Challenge: the exempt agents are the most exposed ones; a
  loop there is unbounded spend. Give the exemption a daily bound. Cost now: low.
  Later: low.

- **`DEC-021` and `DEC-169` (nothing expires; the user removes records one selection
  at a time, with an affirmative answer each).** Challenge: the records of calls and
  of starts grow by the minute, and removing them needs a user answer. A retention
  period for operational records, declared like a threshold, is not the silent loss
  `DEC-021` guards against, because they are not life state. Cost now: low. Later:
  low.

- **`DEC-187`, `MET-033`, `MET-034`, `MET-035` (quality rows at product level, each
  verified per release on a synthetic instance, flowed down as enablers).** Challenge:
  the measures are right and the gate is unaffordable. Keep the rows as the definition
  of the evaluation set; make the per-release verification a reported trend, not a
  gate, until there is a second builder. Cost now: method only. Later: none.

- **`MET-009` and the sequencing to component level before build.** Challenge: a
  component is "approximately one file"; writing those rows before the files exist
  decides the code twice. Build v1 from system rows; write component rows from the
  code where a verified property needs a row. Cost now: method only. Later: none.

- **`MET-013` (Simplified Technical English, with a fixed internal vocabulary).**
  Challenge: the consistency is real and the cost is that "a released gated unit whose
  act another system holds, with its raiser, the answer and the request" is opaque to
  anyone who did not write it, the builder in six months included. A glossary of
  thirty terms in `docs/` would repay itself. Cost: an afternoon.

- **`DEC-177` and `DEC-178` (one host the owner controls; the administrator is
  unbounded).** No challenge; both are right for this user. Restate them the day a
  second person is involved.

## 6. What to cut, and what is missing

**Cut from v1** (keep the rows, mark them out of scope):

- Speech, and the phone client that it implies (`FUN-IA-03` speech, `REQ-IA-009`,
  `REQ-RN-005`, `REQ-IA-049`, `DEC-089`, `DEC-119` speech half).
- Browser-driven sessions (`DEC-127`, `REQ-EX-017`, `REQ-EX-026`, `OPN-093`).
- Query by meaning and the embedding calls (`FUN-ST-06`, `REQ-ST-016`, `REQ-ST-062`,
  `REQ-ST-066`, `REQ-ST-067`, `REQ-ST-096`, `RSK-ST-001`).
- Subjects and their hierarchy (`FUN-ST-11`, `DEC-044`, `DEC-063`); kinds alone, with
  a writer and a source, bound enough for three agents.
- Parameters bound at conferral (`DEC-074` second sentence, `REQ-AD-031`).
- Resource ownership (`FUN-WC-08`, `FUN-AD-12`, `DEC-059`, `DEC-068`).
- Conditions over life state as stored queries (`FUN-ST-12`); keep conditions over
  time.
- Separate copy and restoration for each declaration holder; one backup of one store.
- The portable definition and the degraded mode without the platform (`REQ-PL-021`,
  `FUN-AD-09`, `REQ-AD-026`, `REQ-AD-034`); keep a readable export.
- Provider-side tools and code execution (`DEC-152`, `DEC-160`, `REQ-EX-041`,
  `REQ-EX-042`); refuse all tools at the provider in v1.
- Thresholds as declarations with a starting value per measure (`DEC-166`,
  `REQ-SO-024`, `REQ-SO-026`, `REQ-SO-036`); a fixed handful of alarms.
- Hierarchy change rules (`DEC-040`, `REQ-AD-017`) and retirement bounds (`DEC-064`,
  `REQ-AD-042`) until there are agents to arrange.
- The per-release quality verification programme as a gate.
- Self-Observation and Authorization as separate processes.

**Missing:**

- Three written scenarios of use, and the first three agents' jobs. Everything in v1
  should trace to one of them.
- A cost model: tokens per turn, turns per day, model class per agent, against
  `REQ-PL-020`.
- The inbound edge as a first-class concern: how the user authenticates to Interaction,
  how a webhook is verified when the service does not sign, rate limits, TLS. The
  rows place these with the host; the build cannot.
- One trace identifier carried on every hop and held in every record.
- A retry and confirmation story for acts whose call returned no result.
- The schema language for the form of a kind, and the data model it implies. The rows
  name items, kinds, values before, writers, sources, two times, derived inputs,
  relations and exchanges; they do not choose how a kind states a form.
- A choice of model class and the cheap-model fallback; `REQ-AD-043` holds a version
  per agent and nothing says which.
- The operational story: how a new version is deployed on the one host, how a
  migration keeps `REQ-PL-041` true, and how the builder inspects state when an agent
  cannot answer. `DEC-178` says the administrator passes everything; the build needs
  the tool.
- The identity of the platform and of the platform agent, as text. `DEC-172` and
  `DEC-175` make them design content and `MET-029` permits them. They are the crux of
  the cold start and of learning (`OPN-105`), and they are zero lines.
- A glossary.
- A daily bound on the agents the monthly limit exempts.
- The reader-and-actor separation for untrusted content, as a position rule.

## 7. Questions for the builder

What I could not judge without asking.

1. What are the three things you want done for you every week that nothing does today?
   Which sources and which acts do they need?
2. Have you measured one agent turn anywhere, in tokens and in seconds, and on which
   model? Does USD 50 a month hold against it?
3. How many hours a week do you have until February, and is February a hard date or a
   hope?
4. What does "usable" mean in February: text with calendar and mail, or speech on the
   phone?
5. Would a messaging app you already use, through its bot interface, be an acceptable
   client for v1? If not, why not?
6. Is the method itself a deliverable, for a portfolio, a thesis or a later team? If it
   is, the ratio of specification to code is a choice and not a defect, and the verdict
   softens to "sequence differently".
7. Can you write, by hand today, the positions for three agents in the predicate of
   `DEC-074`? What does a request to widen one of them say to you as the user?
8. Would you accept one process over one SQLite file, with the egress proxy and the
   model call as the only hard boundaries, as v1? If not, which property do you believe
   you lose?
9. Which outside runtime did you have in mind for `REQ-PL-021`, and have you ever used
   an agent that way?
10. Who else will read this model in the next year?
11. When the monthly limit refuses calls, what do you expect the platform to still do
    for you, concretely, for the rest of that month?
12. Did the private workbench already answer any of the above? If so, the public model
    should point at the fact that an answer exists, without its content.
