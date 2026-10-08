# Method

How the work on Pendentive is done, as it is done now (`MET-029`). Rules and
procedures in the present tense. This folder changes in place as the method changes,
and git holds its history. It holds no discussion, no history and no proposal. Why a
rule of method holds is its `MET-` row in `model/registers/method_decisions.csv`.

The rules for the model itself are in `model/model_conventions.md`. This folder holds
how the model and the platform are worked on.

| File | Holds |
|---|---|
| `decomposition.md` | the procedure for one system, from the crawl to the close |
| `writing_rows.md` | how to write a function, a requirement, a risk, a decision and an interface well |
| `parallel_sessions.md` | how two sessions work on the model at the same time |

A procedure that has a skill is held by the skill, in `.claude/skills/` or
`.claude/agents/`, and its file here is removed. A skill is written to work outside
this repository: it holds the general procedure, and this repository holds only what
is specific to it.

## Rules

- **The model constrains the platform only** (`MET-029`). Not what an agent decides,
  not the user, not how the work is done.
- **No personal information in the repository** (`MET-029`): not in rows, examples,
  fixtures, prompts or commit messages. A published commit cannot be withdrawn.
- **A question that cannot be answered now becomes an `OPN-` row**, not a guess.
- **No system is complete.** A later decomposition reaches back into an earlier system
  every time. A change that another system needs is an `OPN-` row against that system.
  A system is *written*, never *complete*.
- **Where alternatives are comparable, prefer the industry-standard mechanism** over the
  expedient one.
- **A comment records why, not what.**
- **Fix the data, never commit around the validator.** `model/validate_model.py` runs on
  every commit through the hook in `.githooks/`.
- **Nothing is claimed as verified unless it was run.**

## Verification

V-model, bottom-up. **A requirement is verified only once all of its children and
grandchildren are verified.** A component requirement has none, so it is verified
directly against the component. A system requirement waits for its components. A
product requirement waits for the whole tree beneath it.

A product requirement carries a verification method and no criterion (`MET-004`).
Criteria are `TST-` rows at system level and below.
