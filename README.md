# Pendentive

Infrastructure for a set of AI agents that manage the life of one person.

The agents are the tenants. Pendentive is what they stand on. It gives them one
body of life state, a hierarchy that sets their authority, a place where work stays
between conversations, and a way to reach the person that they work for.

The work is done in public. It uses systems engineering from end to end: product
functions, requirements under traceability, and verification by the V-model. The
method is as important as the system.

**Status:** the product functions and requirements are written. The product is
divided into ten systems. Ingestion has functions and requirements. The other
nine systems are empty.

## Layout

```
model/     structured data, machine-validated. The source of truth
docs/      prose and diagrams
```

The rule is mechanical: if `validate_model.py` reads it, it belongs in `model/`.

```
model/
├── model_conventions.md          the rules for the model
├── validate_model.py            traceability enforcement
├── product/                     the decomposition tree
│   ├── product_functions.csv    13 functions. Capabilities, not "shall" statements
│   ├── product_requirements.csv 25 requirements, one origin each
│   ├── product_risks.csv        FMEA over this level
│   └── <system>/                one directory for each of the nine systems
└── registers/
    ├── design_decisions.csv     what the system is
    ├── method_decisions.csv     how the model is written
    ├── open_questions.csv       questions held, not guessed at
    └── compartments.csv         the code and directory of each compartment
```

Each directory below `product/` is one compartment. The validator finds the levels.
It does not hold a list of them in its code.

A risk is a failure mode of one compartment. The model holds it with that
compartment, and its identifier carries the level: `RSK-PL-002`. `registers/` holds
only what spans every level.

Product requirements are few and broad by design — one or two per function. It is
acceptable that they are vague. Specificity arrives with their children.

## Checking it

```
python3 model/validate_model.py
```

Verifies that identifiers are well formed and unique, that every requirement has
exactly one origin which resolves, that its type matches that origin, that every
child names a parent that exists, that controlled vocabularies hold, that every risk
names a mitigation and an RPN equal to the product of its factors, that a safety
requirement sits at the level of the risk it answers, and that every cross-reference in the registers, the schema, the README and
the documentation points at something real.

Enable the pre-commit hook once:

```
git config core.hooksPath .githooks
```
