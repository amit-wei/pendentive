# Pendentive

Infrastructure for a tiered suite of AI agents that manage one person's life.

The agents are the tenants. Pendentive is what they stand on: one body of life
state, a hierarchy that scopes their authority, a place for work to live between
conversations, and a way for them to reach the person they work for.

Built in public. Systems-engineering method applied end to end — product functions,
requirements under traceability, V-model verification. The method is as much the
point as the system.

**Status:** product-level functions and requirements defined. Architecture not yet
decided.

## Layout

| Path | Contents |
|---|---|
| `requirements/` | The requirements dataset. Structured data, validated on commit |
| `requirements/SCHEMA.md` | Conventions: identifiers, columns, what belongs at this level |
| `docs/` | Design notes and diagrams |

## The dataset

| File | Holds |
|---|---|
| `functions.csv` | What the system does. Capabilities, not "shall" statements |
| `requirements.csv` | "Shall" statements constraining the design |
| `decisions.csv` | Choices made, with reasons and reversal conditions |
| `risks.csv` | FMEA over the design |
| `open-questions.csv` | Known unknowns, held rather than guessed at |

Twelve functions, twenty-three requirements. Product requirements are few and broad
by design; specificity arrives with their children at system and component level.

## Checking it

```
python3 requirements/validate.py
```

Verifies that identifiers are well-formed and unique, that every requirement has
exactly one origin which resolves, that its type matches that origin, that
controlled vocabularies hold, and that every cross-reference in the decisions and
the documentation points at something real.

Enable the pre-commit hook once:

```
git config core.hooksPath .githooks
```
