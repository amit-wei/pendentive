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

```
model/     structured data, machine-validated. The source of truth
docs/      prose and diagrams
```

The rule is mechanical: if `validate_model.py` reads it, it belongs in `model/`.

```
model/
├── model_schema.md              conventions: identifiers, columns, levels
├── validate_model.py            traceability enforcement
├── product/
│   ├── product_functions.csv    12 functions. Capabilities, not "shall" statements
│   └── product_requirements.csv 23 requirements, one origin each
└── registers/
    ├── design_decisions.csv     what the system is
    ├── method_decisions.csv     how the model is written
    ├── risk_register.csv        FMEA over the design
    └── open_questions.csv       unknowns held rather than guessed at
```

One directory per decomposition level. `system/` and `component/` arrive with the
decomposition; the validator discovers levels rather than hard-coding them.

Product requirements are few and broad by design — one or two per function. It is
acceptable that they are vague. Specificity arrives with their children.

## Checking it

```
python3 model/validate_model.py
```

Verifies that identifiers are well formed and unique, that every requirement has
exactly one origin which resolves, that its type matches that origin, that every
child names a parent that exists, that controlled vocabularies hold, that every risk
names a mitigation, and that every cross-reference in the registers, the schema, the
README and the documentation points at something real.

Enable the pre-commit hook once:

```
git config core.hooksPath .githooks
```
