# Functional flow — product level

**Not an architecture.** No component, technology or deployment is implied here.
This shows the functions from `functions.csv`, the system boundary, and how work
moves between them. Architecture comes after the functional decomposition is agreed.

```mermaid
flowchart TB
    subgraph EXT_IN[" External sources "]
        SRC["Calendar · Mail · Brightspace<br/>Banking · Health · Drive"]
    end

    subgraph AMIT[" Amit "]
        USER["Voice on phone<br/>Text on laptop"]
    end

    subgraph SYS[" The platform "]
        direction TB
        F2["FUN-PL-02<br/>Ingestion"]
        F1[("FUN-PL-01<br/>Life State Custody")]
        F12["FUN-PL-12<br/>Behavioural Learning"]
        F5["FUN-PL-05<br/>Detection &amp; Initiation"]
        F6["FUN-PL-06<br/>Conversation &amp; Reach"]
        F3["FUN-PL-03<br/>Agent Coordination"]
        F4["FUN-PL-04<br/>Work Management"]
        F7{{"FUN-PL-07<br/>Authorization"}}
        F8["FUN-PL-08<br/>Actuation"]
        F9["FUN-PL-09<br/>Provenance"]
        F10["FUN-PL-10<br/>Agent Lifecycle"]
        F11["FUN-PL-11<br/>Self-Observation"]
        AGENTS["Agent population<br/><i>Personal Development · Study Command<br/>Finance · Career · Health · …</i>"]
    end

    SRC --> F2 --> F1
    F1 --> F12 --> F1
    USER <--> F6
    F6 --> F3
    F3 --> AGENTS
    AGENTS --> F3
    AGENTS <--> F1
    F3 --> F4
    F4 --> AGENTS
    F1 --> F5
    F5 -->|"evidence-bearing"| F6
    AGENTS --> F7
    F7 -->|"proposal"| F6
    F6 -->|"yes / no"| F7
    F7 -->|"authorised only"| F8
    F8 --> SRC
    F9 -.->|"marks inference,<br/>retains evidence"| F1
    F9 -.-> F6
    F10 -.->|"defines"| AGENTS
    F11 -.->|"cost · health · usage"| F6

    GOALS[/"GOALS.md<br/>owned by Personal Development Agent<br/>platform does not author it"/]
    GOALS -.-> AGENTS
    F5 -.->|"drift &amp; forewarning"| GOALS
```

## What the diagram asserts

**`FUN-PL-01` is the hub.** Every agent reads the same life state. This is the
single change that makes the suite harmonic, and `REQ-PL-001` states it.

**Actuation is reachable only through authorization.** There is no path from an
agent to the outside world that bypasses `FUN-PL-07`. That is `REQ-PL-014` drawn
as topology rather than trusted to behaviour.

**Detection reads state, never sources.** `FUN-PL-05` sits downstream of custody,
so a proactive message cannot be raised on data that has not been reconciled
against what is already known. This is what prevents the stated abandonment
behaviour — being reminded of something already overridden (`REQ-PL-001`).

**`GOALS.md` sits outside the platform.** The platform serves it and reports drift
against it; the Personal Development Agent owns it (`REQ-PL-019`).

**Provenance and lifecycle are dotted.** They act on everything rather than
sitting in the flow of work.

## What it does not yet settle

- Whether agents execute inside the platform or attach from outside (`DEC-002` proposes both, by runtime).
- Whether life state is one store or several.
- Where the master copy of `GOALS.md` lives (`OPN-006`).
- Who arbitrates cross-domain contention (`OPN-005`).
