# CLAUDE.md

Instructions for an agent working in this repository. Read `docs/method/README.md`
first: it holds how the work is done. The rules for the model are in
`model/model_conventions.md`, and `model/CLAUDE.md` loads when you work in `model/`.

## Hard boundaries

- **No personal information in the repository, ever** (`MET-029`). Not in rows,
  examples, fixtures, prompts or commit messages. A published commit cannot be
  withdrawn.
- **Never claim something is verified when it was not run.**
- **The validator runs on every commit.** Fix the data. Never commit around the hook.

## Constraints that bite

USD 50 a month for each running instance of the platform, excluding the machine it
runs on (`REQ-PL-020`). These are design inputs, not background facts.

## The builder's working agreement

Private, and absent from a public clone:

@workbench/CLAUDE.md
